def solution(s):
    result = []
    # 각 단어를 공백기준으로 분리
    str = s.split(' ')
    # s 는 각 단어
    for i in str:
        answer = ''
        # j는 각 단어의 단어길이만큼 반복
        for j in range(len(i)):
            if j % 2 == 0:  # 각 단어 인덱스가 짝수면
                answer += i[j].upper()
            else:  # 각 단어 인덱스가 홀수면
                answer += i[j].lower()
        result.append(answer)  
    return ' '.join(result)  # 공백 한칸 주고 합치기