def solution(num, total):
    # 등차는 1로 고정
    # 연속된 수의 합 공식 n(n+1)/2을 이용해 중간값 계산
#     mid = total // num
    
#     # 첫번째 숫자
#     start = mid - (num//2)
    
    
#     # range()는 0부터 num-1까지
#     return [start + i for i in range(num)]

    d=0
    for i in range(1, num):
        d += i
    start=(total-d)//num
    answer = [i for i in range(start, start+num)]
    return answer