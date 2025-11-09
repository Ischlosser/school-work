def recfn(N):
    if N <= 0:
        return 0
    else:
        if N%2 == 0:
            result = recfn(N-1) - N
        else:
            result = recfn(N-1) + N
    return result
input = int(input())
print(recfn(input))
