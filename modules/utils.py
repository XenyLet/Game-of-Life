def group_list(l, chunks_num):
    l = list(l)
    input_size = len(l)
    slice_size = input_size // chunks_num
    remain = input_size % chunks_num
    result = []
    iterator = iter(l)
    for i in range(chunks_num):
        result.append([])
        for j in range(slice_size):
            result[i].append(next(iterator))
        if remain:
            result[i].append(next(iterator))
            remain -= 1
    return result

def one_level_flatten(l):
    r = []
    for el in l:
        r.extend(el)
    return r