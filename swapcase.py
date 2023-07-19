def swap_case(s):
    string = ""
    for i in s:
        if i.islower():
            string+=i.upper()
        else:
            string+=i.lower()
    return string
