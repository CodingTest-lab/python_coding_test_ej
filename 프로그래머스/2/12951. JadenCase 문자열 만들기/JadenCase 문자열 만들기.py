def solution(s):
    # 입력값을 공백으로 나눔
    # 각 단어 중간에 대문자가 나올 수 있으므로 다 소문자로 바꿈
    # 각 단어 첫글자가 알파벳이 아니면 이어지는 알파벳은 소문자로
    # answer = []
    # words = s.split(" ")
    # for str in words:
    #     if str != " ":
    #         answer.append(str[0].upper() + str[1:].lower())
    #     else:
    #         answer.append(" ")
    # return " ".join(answer)
    words = s.split(" ")
    answer = [word[0].upper()+word[1:].lower() if word else "" for word in words]
    return " ".join(answer)