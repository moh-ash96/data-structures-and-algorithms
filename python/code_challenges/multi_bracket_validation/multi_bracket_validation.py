def multi_bracket_validation(input):
    open = tuple('({[')
    close = tuple(')}]')
    pairs = dict(zip(open, close))
    list1 = []
    for i in input:
        if i in open:
            list1.append(pairs[i])
        elif i in close:
            if not list1 or i != list1.pop():
                return False
    if not list1:
        return True
    else:
        return False
