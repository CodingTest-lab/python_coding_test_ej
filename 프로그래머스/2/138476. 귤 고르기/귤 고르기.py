from collections import Counter
def solution(k, tangerine):
    # 종류 개수
    answer = 0
    
    # Counter 객체를 사용해 요소의 빈도 수 세기
    counter = Counter(tangerine)
    
    # counter 는 '2': 3 이런식으로 값이 반복, i는 요소, cnt는 반복 개수, 빈도수가 높은 요소부터 추출
    for i, cnt in counter.most_common():
        # 전체 귤 개수 k에서 반복 개수만큼 빼주기
        k -= cnt
        # 종류 개수에 1 추가
        answer += 1
        # 전체 귤 개수가 0이하면 반복 종료
        if k <= 0: break
    
    return answer