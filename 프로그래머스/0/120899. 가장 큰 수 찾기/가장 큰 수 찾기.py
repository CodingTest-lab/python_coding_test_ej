def solution(array):
    result = []
    answer = sorted(array)
    max = answer[-1]
    index = array.index(max)
    result.append(max)
    result.append(index)
    return result