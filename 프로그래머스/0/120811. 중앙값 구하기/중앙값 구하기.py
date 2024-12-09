def solution(array):
    sorted_arr = sorted(array)
    n = len(sorted_arr)
    return sorted_arr[n//2]

# return sorted(array)[len(array) // 2]