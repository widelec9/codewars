import re
from collections import defaultdict
from datetime import datetime


class Inspector:
    def __init__(self):
        self.countries = ['Arstotzka', 'Antegria', 'Impor', 'Kolechia', 'Obristan', 'Republia', 'United Federation']
        self.cts_allow = ['Arstotzka']
        self.req_doc = {c: ['passport'] for c in self.countries}
        self.req_vaccs = {c: [] for c in self.countries}
        self.wanted = []
        self.docs = ['passport', 'ID_card', 'access_permit', 'work_pass', 'grant_of_asylum', 'certificate_of_vaccination', 'diplomatic_authorization']

    def __rcv_bul_allow_deny_citizens(self, string):
        for s in string.split('\n'):
            allow_deny_cts = re.search(r'(Allow|Deny) citizens of (.*)', s)
            if allow_deny_cts is not None:
                action = allow_deny_cts.group(1)
                cts_list = allow_deny_cts.group(2).split(', ')
                self.cts_allow += [c.lstrip() for c in cts_list if action == 'Allow' and c not in self.cts_allow]
                self.cts_allow = list(set(self.cts_allow) - set([c for c in cts_list if action == 'Deny' and c in self.cts_allow]))

    def __rcv_bul_update_documents(self, string):
        for s in string.split('\n'):
            req_doc = re.search(r'(.*) require (.*)', s)
            if req_doc is not None:
                who = req_doc.group(1).split(',')[0]
                doc = req_doc.group(2).split(',')[0].replace(' ', '_')
                doc = 'certificate_of_vaccination' if 'vaccination' in doc else doc
                who = [c for c in self.countries if c != 'Arstotzka'] if who in ['Foreigners', 'Workers'] else [c for c in self.countries] if who == 'Entrants' else who
                for k in self.req_doc.keys():
                    if k in who and doc not in self.req_doc[k]:
                        self.req_doc[k] += [doc]

    def __rcv_bul_update_vaccs(self, string):
        for s in string.split('\n'):
            req_vaccs = re.search(r'(.*) no longer require (.*) vaccination', s)
            if req_vaccs is not None:
                who = req_vaccs.group(1).split(',')[0]
                vaccs = req_vaccs.group(2).split(',')
                who = [c for c in self.countries if c != 'Arstotzka'] if who == 'Foreigners' else [c for c in self.countries] if who == 'Entrants' else who.lstrip('Citizens of ').split(',')
                for k in who:
                    for v in vaccs:
                        if v in self.req_vaccs[k]:
                            self.req_vaccs[k].remove(v)
                            if len(self.req_vaccs[k]) == 0 and len(self.req_doc[k]) > 0:
                                self.req_doc[k].remove('certificate_of_vaccination')
            if 'no longer' not in s:
                req_vaccs = re.search(r'(.*) require (.*) vaccination', s)
                if req_vaccs is not None:
                    who = req_vaccs.group(1).split(',')[0]
                    vaccs = req_vaccs.group(2).split(',')
                    who = [c for c in self.countries if c != 'Arstotzka'] if who == 'Foreigners' else [c for c in self.countries] if who == 'Entrants' else who.lstrip('Citizens of ').split(',')
                    for k in who:
                        self.req_vaccs[k] += vaccs

    def __rcv_bul_update_wanted(self, string):
        wanted = re.search(r'Wanted by the State: (.*)', string)
        if wanted is not None:
            self.wanted.append(wanted.group(1))

    def receive_bulletin(self, string):
        self.__rcv_bul_allow_deny_citizens(string)
        self.__rcv_bul_update_documents(string)
        self.__rcv_bul_update_vaccs(string)
        self.__rcv_bul_update_wanted(string)

    def __get_vals_dict(self, docs_parsed):
        vals = defaultdict(list)
        for doc in list(docs_parsed.keys()):
            for key in docs_parsed[doc].keys():
                vals[key] += [docs_parsed[doc][key]]
        if 'ID_card' in docs_parsed.keys():
            vals['NATION'] = ['Arstotzka']
        return {k: set(vals[k]) if len(set(vals[k])) > 1 else list(set(vals[k]))[0] for k in vals.keys()}

    def inspect(self, entrant):
        if entrant == {}:
            return 'Entry denied: missing required passport.'
        else:
            docs_parsed = {doc: {entry.split(': ')[0]: entry.split(': ')[1] for entry in entrant[doc].split('\n')} for doc in entrant.keys()}
            vals = self.__get_vals_dict(docs_parsed)

            if type(vals['NAME']) == str and ' '.join(vals['NAME'].split(', ')[::-1]) in self.wanted:
                return 'Detainment: Entrant is a wanted criminal.'

            if len(docs_parsed.keys()) > 1:
                check = {'ID#': 'ID number', 'NATION': 'nationality', 'NAME': 'name', 'DOB': 'date of birth', 'SEX': 'sex', 'HEIGHT': 'height', 'WEIGHT': 'weight'}
                for k in set(check.keys()).intersection(vals.keys()):
                    if type(vals[k]) == set:
                        return 'Detainment: {} mismatch.'.format(check[k])

            if vals['NATION'] not in self.cts_allow:
                return 'Entry denied: citizen of banned nation.'

            docs_required = self.req_doc[vals['NATION']].copy()
            if 'PURPOSE' in vals and vals['PURPOSE'] != 'WORK' and 'work_pass' in docs_required:
                docs_required.remove('work_pass')

            if len(set(docs_required).difference(set(docs_parsed.keys()))) > 0:
                if 'diplomatic_authorization' in docs_parsed.keys():
                    if 'Arstotzka' not in vals['ACCESS']:
                        return 'Entry denied: invalid diplomatic authorization.'
                else:
                    if not (vals['NATION'] == 'Arstotzka' and 'ID_card' in docs_parsed.keys() and 'passport' not in docs_required) and \
                            not (vals['NATION'] != 'Arstotzka' and 'passport' in docs_parsed.keys() and 'grant_of_asylum' in docs_parsed.keys()):
                        missing_docs = sorted(list(set(docs_required).difference(set(docs_parsed.keys()))), key=lambda x: (x != 'passport', x))
                        return 'Entry denied: missing required {}.'.format(missing_docs[0].replace('_', ' '))

            for d in docs_parsed:
                if 'EXP' in docs_parsed[d].keys() and datetime.strptime(docs_parsed[d]['EXP'], '%Y.%m.%d') < datetime.strptime('1982.11.22', '%Y.%m.%d'):
                    return 'Entry denied: {} expired.'.format(d.replace('_', ' '))

            if 'certificate_of_vaccination' in docs_required and 'certificate_of_vaccination' in docs_parsed and not all(x in vals['VACCINES'].split(', ') for x in self.req_vaccs[vals['NATION']]):
                return 'Entry denied: missing required vaccination.'

            return 'Glory to Arstotzka.' if vals['NATION'] == 'Arstotzka' else 'Cause no trouble.'