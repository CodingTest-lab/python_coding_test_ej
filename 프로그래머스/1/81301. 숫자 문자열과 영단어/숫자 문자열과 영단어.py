def solution(s):
    eng_num = {
        "zero": 0,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }
    
    # 각 단어를 숫자로 대체
    for eng in eng_num:
        s = s.replace(eng, str(eng_num[eng]))
    
    return int(s)
# 딕셔너리 .items() 메서드 : 딕셔너리의 키-값 쌍을 튜플 형태로 반환
    # eng_num은 key에만 접근 가능
    # eng_num.items()를 사용해야 key/value 둘다 접근 가능