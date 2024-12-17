def solution(emergency):
    # 입력 배열을 내림차순으로 정렬
    # .index(e) : 각 원소의 정렬된 배열에서의 인덱스
    # 순위는 인덱스 + 1
    return [sorted(emergency, reverse=True).index(e) + 1 for e in emergency]

    # 바깥 for문 : 각 원소 순회
    # 안쪽 for문 : 해당 원소와 다른 모든 원소 비교
    # lt는 자신보다 큰 원소의 개수 + 1
    # arr = []
    # for i in emergency:
    #     idx = 1
    #     for j in emergency:
    #         if i < j:
    #             idx += 1
    #     arr.append(idx)
    # return arr