def solution(arr):
    answer = []
    answer.append(arr[0])  # 첫번째 글자 넣기
    now = arr[0]  
    # for 문 돌면서 now랑 i가 같지 않다면 리스트에 추가
    for i in arr:
        if i != now:
            answer.append(i)
            now = i
    return answer

    # a[-1:]는 리스트 a의 마지막 요소를 포함하는 리스트를 반환
    # [i]는 현재 반복 중인 문자를 단일 요소로 가진 리스트
    # a[-1:] == [i] 는 리스트 a의 마지막 문자가 현재 문자와 같은지 비교
    # a = []
    # for i in s:
    #     if a[-1:] == [i]: continue
    #     a.append(i)
    # return a