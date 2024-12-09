# 배열의 길이가 홀수로 정해져있으므로 배열의 길이를 2로 나눈 몫으로 계산
# 배열의 길이가 짝수라면 (배열 길이) // 2 -1 과 (배열 길이) // 2 의 중간값
def solution(array):
    sorted_arr = sorted(array)
    n = len(sorted_arr)
    return sorted_arr[n//2]

# return sorted(array)[len(array) // 2]
