def split_workload(workload):
    if not workload:
        return None, None
    diff = [abs(sum(workload[:i]) - sum(workload[i:])) for i, w in enumerate(workload)]
    return diff.index(min(diff)), min(diff)
