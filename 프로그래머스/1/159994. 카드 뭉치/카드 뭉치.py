from collections import deque

def solution(cards1, cards2, goal):
    # 카드 뭉치를 deque로 만들기, deque로 만드는 이유는 첫번째 요소를 빼서 삭제하는것이 편하기 때문
    cards1 = deque(cards1)
    cards2 = deque(cards2)
    
    # goal에 단어가 있을때까지 반복
    for word in goal:
        # 첫번째 카드 뭉치의 첫번째 요소와 단어가 같다면 첫번째 카드 뭉치의 첫번째 요소 삭제
        if cards1 and word == cards1[0]:
            cards1.popleft()
        # 두번째 카드 뭉치의 첫번째 요소와 단어가 같다면 두번째 카드 뭉치의 첫번째 요소 삭제
        elif cards2 and word == cards2[0]:
            cards2.popleft()
        # 같지 않다면
        else:
            return 'No'
    
    # goal의 요소를 다 클리어하면
    return 'Yes'
