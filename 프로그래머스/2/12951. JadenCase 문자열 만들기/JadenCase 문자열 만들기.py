def solution(s):
    # 입력값을 공백으로 나눔
    # 각 단어의 첫글자를 대문자로 첫글자 제외하고는 다 소문자로
    # 공백인 경우 ''(빈문자열) 반환
    
    words = s.split(" ")
    answer = [word[0].upper()+word[1:].lower() if word else "" for word in words]
    # 위의 list comprehension을 풀어쓴 버전
    # for str in words:
    #     if word:   빈 문자열인지 체크
    #         answer.append(word[0].upper() + word[1:].lower())
    #     else:
    #         ""   빈문자열
    return " ".join(answer)