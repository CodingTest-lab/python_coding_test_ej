def solution(people, limit):
    answer = 0
    # 무게를 오름차순 정렬 후 두 포인터를 지정
    people.sort()
    left, right = 0, len(people) - 1
    
    # 최저(left) + 최고(right) 가 limit보다 크다면 최고만 보트에 태워보냄(right를 왼쪽으로 한칸 이동)
    while left <= right:
        # left번째 + right번째 가 limit 이하라면 left를 오른쪽으로 이동(최저와 최고를 보트에 태울 수 있다면 태워보내고 그 다음 점을 찾아감)
        if people[left] + people[right] <= limit:
            left += 1
        right -= 1
        answer += 1
    return answer