import re


def phone(string, num):
    book = {}
    for entry in string.split('\n'):
        if entry:
            number = re.search(r'\+(.*?)[^\-\d]', entry).group(1)
            if number in book.keys() and number == num:
                return 'Error => Too many people: {}'.format(number)
            name = re.search(r'\<(.*)\>', entry).group(1)
            entry = entry.replace(number, '').replace('<{}>'.format(name), '').strip()
            garbage = set(re.findall(r'([^a-zA-Z0-9\s\-\.]|\!)', entry))
            if garbage:
                for g in garbage:
                    entry = entry.replace(g, ' ')
            address = re.sub(r' +', ' ', entry).strip()
            book[number] = [name, address]
    if num not in book.keys():
        return 'Error => Not found: {}'.format(num)
    return 'Phone => {p}, Name => {n}, Address => {a}'.format(p=num, n=book[num][0], a=book[num][1])
