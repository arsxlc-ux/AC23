#Циклический сдвиг
def min_shift(S, T):
    if len(S) != len(T):
        return -1
    
    double_S = S + S  
    idx = double_S.find(T)
    if idx == -1:
        return -1
    else:
        return idx % len(S)  
S = "abcdz"
T = "zabcd"
shift = min_shift(S, T)

print(shift)  
