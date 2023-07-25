def addSpaces(self, s: str, spaces: List[int]) -> str:
    lis =[]
    x = 0
    for i in spaces :
        lis.append(s[x:i])
        x = i
    lis.append(s[x:])
    return " ".join(lis)
