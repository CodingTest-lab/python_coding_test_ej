def solution(s):
    # 공백을 기준으로 나누어 리스트로 변환
    # int 함수를 사용하여 문자열 리스트의 각 요소를 정수로 변환
    # 배열에서 최솟값과 최댓값을 찾고 문자열로 반환
    arr = list(map(int, s.split(' ')))
    return str(min(arr)) + " " + str(max(arr))
