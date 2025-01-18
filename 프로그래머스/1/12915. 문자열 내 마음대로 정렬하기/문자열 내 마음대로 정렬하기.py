def solution(strings, n):
    # strings 안의 모든 원소들의 n번째 글자 추출
    # 추출한 배열을 오름차순 정렬
    return sorted(strings, key = lambda x:(x[n], x))