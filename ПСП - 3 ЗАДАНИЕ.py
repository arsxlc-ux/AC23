# получение ПСП
def PSP (s):
    midle = 0  
    delite = 0  
    for ch in s:
        if ch == '(':
            midle += 1
        elif ch == ')':
            if midle > 0:
                midle -= 1
            else:
                delite += 1 
    delite += midle
    return delite
s1 = "())(() "
print(PSP(s1))  
