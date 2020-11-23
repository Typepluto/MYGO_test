def reverseDict(input):
    rt=None
    
    while isinstance(input,dict) and input:
        key, input = input.popitem()
        if rt:
            rt = {key:rt}
        else:
            rt = key

    if rt:
        return {input:rt}
    return input