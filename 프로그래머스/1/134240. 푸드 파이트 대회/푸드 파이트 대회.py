def solution(food):
    # 음식은 각 개수를 2로 나눈 몫만큼 개수가 들어감(대신 각 음식의 개수가 1 이하면 들어가지 않음)
    # 결과에는 각 음식의 인덱스가 들어감
    answer = ''
    for i, value in enumerate(food):
        answer += str(i) * (value//2) 
    
    return answer + '0' + answer[::-1]