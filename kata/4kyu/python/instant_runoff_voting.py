from operator import itemgetter


def runoff(voters):
    if voters:
        first_choices = [v[0] for v in voters]
        cd = {k: first_choices.count(k) for k in set(first_choices)}
        voters = [[c for c in v if c in first_choices] for v in voters]

        if len(set(cd.values())) == 1 and len(set(cd.keys())) > 1:
            return None

        if max(cd.values()) > sum(cd.values()) // 2:
            return max(cd.items(), key=itemgetter(1))[0]

        to_remove = [k for k in cd.keys() if cd[k] == min(cd.values())]
        voters = [[c for c in v if c not in to_remove] for v in voters]
        return runoff(voters)
