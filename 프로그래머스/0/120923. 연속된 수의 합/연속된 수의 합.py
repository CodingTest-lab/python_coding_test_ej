def solution(num, total):
    # 기본 합계 구하기
    d=0
    for i in range(1, num):
        d += i
        
    # 목표 합계에서 기본 합계를 빼서 시작 숫자 계산
    start=(total-d)//num
    
    # 시작숫자부터 연속된 num개의 숫자 생성
    return [i for i in range(start, start+num)]
  