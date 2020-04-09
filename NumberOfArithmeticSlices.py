def numberOfArithmeticSlices(A : List[int]) -> int:
    n = len(A)
    if n <= 2:
        return 0
    else:
        result = 0
        pre = 0
        for i in range(n - 2):
            if A[i + 2] - A[i + 1] == A[i + 1] - A[i]:
                pre += 1
                result += pre 
            else:
                pre = 0
        return result
    
    