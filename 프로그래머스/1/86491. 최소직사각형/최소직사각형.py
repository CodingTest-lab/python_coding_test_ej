def solution(sizes):
    # 2차원 배열 내 각 배열들 중 큰값은 큰값리스트에, 작은값은 작은값리스트에 넣고 각 리스트 중 제일 큰값을 곱하자
    w = []
    h = []
    for i in sizes:
        w.append(max(i))
        h.append(min(i))
    return max(w) * max(h)