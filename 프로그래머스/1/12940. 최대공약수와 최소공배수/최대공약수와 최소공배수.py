def solution(n, m):
    x, y = n, m
    
    while y != 0:
        x, y = y, x % y
    
    # 최대공약수
    gcd = x
    # 최소공배수
    lcm = (n * m) // gcd
    
    return [gcd, lcm]

    # 위 코드랑 같은 내용이지만 좀 더 깔끔한 버전
    # c,d = max(n, m), min(n, m)
    # t = 1
    # while t>0:
    #     t = c%d
    #     c, d = d, t
    # answer = [ c, int (n*m/c)]
    # return answer