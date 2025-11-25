def find_substring_indexes(S, T):
    indexes = []
    start_pos = 0
    while True:
        pos = S.find(T, start_pos)
        if pos == -1:
            break
        indexes.append(pos)
        start_pos = pos + 1 
    return indexes
S = "ababbababa"
T = "aba"
indexes = find_substring_indexes(S, T)
print(' '.join(map(str, indexes)))  # Вывод: 0 5 7