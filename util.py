def go(xs, per_part):
    begin = 0
    end = per_part
    result = list()
    while True:
        result.append(xs[begin:end])
        begin = end
        end = end + per_part
        if end >= len(xs):
            end = len(xs)
        if begin >= end:
            return result

