def swap_case(s):
    st = ""
    for i in s:
        if i.isupper():
            i = i.lower()
        else:
            i = i.upper()
        st += "".join(i)
    return st
