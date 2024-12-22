def solution(t, p):
    # p 길이와 같은 부분 문자열 생성
    # 위에서 생성한 부분문자열들과 p를 비교
    # 해당 값보다 작으면 answer에 1씩 추가
    answer = 0
    number = []

    for i in range(len(t) - len(p) + 1):
        number.append(t[i : i + len(p)])
        
    for i in number:
        if int(i) <= int(p):
            answer += 1
    
    return answer