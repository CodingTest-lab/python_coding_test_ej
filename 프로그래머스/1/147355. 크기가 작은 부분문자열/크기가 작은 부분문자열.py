def solution(t, p):
    # p 길이와 같은 부분 문자열 생성(p 길이만큼 자를수있는 경우의 수를 len(t) - len(p) + 1로 계산 후 배열에 추가)
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