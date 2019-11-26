def same_structure_as(original, other):
    if type(original) != type(other):
        return False
    if type(original) != list and type(other) != list:
        return True
    while len(original) and len(other):
        if len(original) != len(other):
            return False
        original_types, other_types = [type(o) for o in original], [type(o) for o in other]
        original_lists, other_lists = [i for i, ot in enumerate(original_types) if ot == list], [i for i, ot in enumerate(other_types) if ot == list]
        if original_lists != other_lists:
            return False
        if not original_lists:
            break
        while original_lists:
            if not same_structure_as(original[0], other[0]):
                return False
            original.pop(0)
            other.pop(0)
            original_lists.pop(0)
    return True
