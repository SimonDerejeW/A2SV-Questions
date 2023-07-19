class Solution:
    def reverse(self, x: int) -> int:
        
        lis = list(str(x))
        for i in range(len(lis)):
            if lis[i] == '-':
                y = lis.pop(i)
                lis.append(y)
                break

        rev = lis[::-1]
        
        intlis2 = rev[:]
        for i in rev:
            if i == '0':
                intlis2.remove(i)
            elif i!='0':
                break
        x = ''.join(intlis2)
        if len(intlis2) == 0:
            return 0
        y = int(x)
        if -2**31 <= y and y <= 2**31 - 1:
            return y
        else:
            return 0
