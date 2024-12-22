def solution(sizes):
    # 2차원 배열 내 각 배열들 중 큰값은 큰값리스트에, 작은값은 작은값리스트에 넣고 각 리스트 중 제일 큰값을 곱하자 
    # ex) [60,50] -> w에 60, h에 50 넣기 / [30,70] -> w에 70, h에 30 넣기
    w = []
    h = []
    for i in sizes:
        w.append(max(i))
        h.append(min(i))
    return max(w) * max(h)

    # 처음부터 오름차순으로 각 배열을 정리하면 0번 인덱스에는 작은값, 1번 인덱스에는 큰값이 들어감 -> 0번 인덱스와 1번 인덱스 값들 중 가장 큰 두값을 곱하자
    # sizes = [sorted(s) for s in sizes]
    # return max([x[0] for x in sizes]) * max([x[1] for x in sizes])