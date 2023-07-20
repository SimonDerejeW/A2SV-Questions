def wrap(string, max_width):
    txtwrap = ""
    for i in range(0,len(string),max_width):
        txtwrap+=string[i:i+max_width]
        txtwrap+='\n'
    return txtwrap
