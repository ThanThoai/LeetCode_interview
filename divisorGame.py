def divisorGame(N : int) -> bool:
    if N == 1:
        return False
    else:
        result = [0] * (N + 1)
        result[2] = 1
        for i in range(3, N + 1):
            for j in range(1, int(i / 2) + 1):
                if i % j == 0 and result[i - j] == 0:
                    result[i] = 1
        return bool(result[N])
    