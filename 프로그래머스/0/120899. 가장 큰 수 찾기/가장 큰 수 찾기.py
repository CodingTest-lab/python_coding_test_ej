def solution(array):
    result = []
    answer = sorted(array)
    max = answer[-1]
    index = array.index(max)
    result.append(max)
    result.append(index)
    return result

# 가장 큰 값 찾기, array.index() 는 해당 값의 인덱스 찾기
# val = max(array)
# return [val, array.index(val)]