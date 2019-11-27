def ensure_same_length(*lists_under_inspection: list) -> bool:
    if not len({len(item) for item in lists_under_inspection}) == 1:
        raise ValueError
    else:
        return True


def add(*lists: list) -> list:
    result = []
    ensure_same_length(*lists)
    for list_item in zip(*lists):
        ensure_same_length(*list_item)
        sublist = []
        for item in zip(*list_item):
            sublist.append(sum(item))
        result.append(sublist)
    return result
