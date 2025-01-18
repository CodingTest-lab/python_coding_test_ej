def solution(array, commands):
    # i번째부터 j번째까지 자른거에 k번째 원소들만 모아서 배열 만들기
    answer = []
    for i,j,k in commands:
        temp_arr = array[i-1:j]
        temp_arr.sort()
        answer.append(temp_arr[k-1])
    return answer