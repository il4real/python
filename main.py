def chunked(symbols, n):
    result = []
    end = [[]]
    for i in range(n):
        for j in range(n):
            result = symbols[j: i + j + 1]
            if len(result) == i + 1:
                end.append(result)
    return end


symbols = input().split()
n = len(symbols)

print(chunked(symbols, n))