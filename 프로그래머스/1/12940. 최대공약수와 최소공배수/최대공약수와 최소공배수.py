def solution(n, m):
    x, y = n, m
    
    while y != 0:
        x, y = y, x % y
    
    # 최대공약수
    gcd = x
    # 최소공배수
    lcm = (n * m) // gcd
    
    return [gcd, lcm]