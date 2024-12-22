def solution(number):
    answer = 0
    # 숫자 3개로 조합할 수 있는 모든 경우의 수를 찾기 위해 3중 for문
    for i in range(len(number) - 2):
        for j in range(i + 1, len(number) - 1):
            for k in range(j + 1, len(number)):
                if number[i] + number[j] + number[k] == 0:
                    answer += 1
    
    return answer