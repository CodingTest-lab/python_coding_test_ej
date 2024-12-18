def solution(numbers, k):
    # k 는 몇번째로 공을 던지는지 나타냄, -1은 인덱스가 0부터 시작하기 때문
    # 매번 한명을 건너뛰므로 2씩 이동
    # 배열의 길이를 초과하면 다시 처음으로 돌아가게 하는 나머지 연산
    return numbers[(k - 1) * 2 % len(numbers)]