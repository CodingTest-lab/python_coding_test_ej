# # 각 로봇의 두 포인트 간 이동 경로를 각 로봇 경로 리스트에 추가하는 함수 
# def get_path(start_r, start_c, end_r, end_c, robot_move):
#     # 현재 좌표를 시작 좌표로 초기화
#     now_r = start_r
#     now_c = start_c
    
#     # 현재 좌표가 목표 좌표와 같을때까지 경로 탐색(현재 좌표가 목표 좌표와 다른 동안 계속 반복, 현재 좌표가 목표 좌표에 도달하면 반복 종료)
#     while not (now_r == end_r and now_c == end_c):
#         # r축부터 이동
#         # 현재 r이 목표 r보다 작으면 +1만큼 이동 
#         if now_r < end_r:
#             now_r += 1
#             robot_move.append([now_r, now_c])
#             continue
#         # 현재 r이 목표 r보다 크면 -1만큼 이동 
#         if now_r > end_r:
#             now_r -= 1
#             robot_move.append([now_r, now_c])
#             continue
            
#         # c축 이동
#         # 현재 c가 목표 c보다 작으면 +1만큼 이동
#         if now_c < end_c:
#             now_c += 1
#             robot_move.append([now_r, now_c])
#             continue
#         # 현재 c가 목표 c보다 크면 -1만큼 이동
#         if now_c > end_c:
#             now_c -= 1
#             robot_move.append([now_r, now_c])

# def solution(points, routes):
#     answer = 0
    
#     # 각 포인트의 좌표를 저장하는 딕셔너리(ex. {1:[3,2],...})
#     point_dic = {}
#     # 포인트 저장 딕셔너리 생성
#     for i in range(len(points)):
#         r,c = points[i]
#         point_dic[i+1] = [r,c]
        
#     # 모든 로봇의 경로 리스트
#     robots_routes = []
    
#     # 모든 로봇의 경로 리스트에 값을 넣기 위한 과정
#     # 로봇 대수만큼 반복(routes 배열 길이 = 로봇 대수)
#     for i in range(len(routes)):
#         # routes 내 각 경로 추출
#         route = routes[i]
#         # 시작 포인트
#         start_point = route[0]
#         # 시작 포인트 좌표 -> 포인트 저장 딕셔너리에서 추출
#         start_r, start_c = point_dic[start_point]
#         # 각 로봇 경로 리스트에 시작 포인트 좌표 추가
#         robot_move = [[start_r, start_c]]

#         # 각 로봇의 이동 횟수만큼 반복(포인트 간 이동) -> 포인트가 2개면 1번 이동
#         for j in range(1, len(route)):
#             # 시작 포인트에서 다음 포인트로 이동
#             end_point = route[j]
#             # 도착 포인트 좌표
#             end_r, end_c = point_dic[end_point]
#             # 경로 탐색 함수
#             get_path(start_r, start_c, end_r, end_c, robot_move)
#             # 시작 포인트를 다음 포인트에 대입해 끝 포인트가 될때까지 반복(ex.route가 [4,2,1,3]이면 (4->2),(2->1),(1->3) 이런식으로 포인트 이동을 하기때문에)
#             start_point = end_point
        
#         # 각 로봇의 경로를 모든 로봇의 경로 리스트에 추가
#         robots_routes.append(robot_move)
    
#     # 시간 순회(각 로봇들 중 가장 좌표 이동을 많이 한 로봇 기준, 시작 좌표에서 목표 좌표까지 가기 위해 거쳐간 좌표가 가장 많은 로봇)
#     max_time = max([len(i) for i in robots_routes])
    
#     # 중복 경로 있는지 확인
#     # 가장 큰 좌표 이동 횟수만큼 반복(시간 순회)
#     for i in range(max_time):
#         # 방문한 좌표
#         visit = set()
#         # 중복된 좌표
#         count = set()

#         # 로봇 대수만큼 반복
#         for j in range(len(robots_routes)):
#             # 해당 로봇의 경로가 없으면 다음 로봇으로 넘어감
#             if len(robots_routes[j]) < (i+1):
#                 continue
                
#             # 각 로봇의 각 좌표
#             r, c = robots_routes[j][i]
            
#             # r,c가 이미 중복된 좌표 넣는 곳에 있으면 다음 반복문 실행
#             if (r,c) in count:
#                 continue
                
#             # r,c가 방문한 좌표 넣는 곳에 있으면 중복된 좌표 넣는 곳에 추가
#             if (r,c) in visit:
#                 count.add((r,c))
#                 continue
            
#             # 최초라면 방문한 좌표 넣는 곳에 넣어줌
#             visit.add((r,c))
        
#         # 시간대 별로 중복된 좌표 넣는 곳의 길이를 추가
#         answer += len(count)
#     return answer

# 시작, 끝에 대한 정보를 받으면, 경로 정보를 list형태로 이어서 반환.
def get_path(start_r, start_c, end_r, end_c, out_list):

    now_r = start_r
    now_c = start_c

    while not (now_r == end_r and now_c == end_c):

        # r축부터 이동
        if now_r > end_r:
            now_r -= 1
            out_list.append([now_r, now_c])
            continue

        if now_r < end_r:
            now_r += 1
            out_list.append([now_r, now_c])
            continue

        # c축 이동
        if now_c > end_c:
            now_c -= 1
            out_list.append([now_r, now_c])
            continue

        if now_c < end_c:
            now_c += 1
            out_list.append([now_r, now_c])


def solution(points, routes):
    answer = 0

    # 포인트에 대한 위치를 사전 연산
    point_map = {}

    for i in range(len(points)):
        r, c = points[i]
        point_map[i + 1] = [r, c]

    # 각 로봇당 경로를 모조리 끌어옴.
    robot_paths = []

    for i in range(len(routes)):

        route = routes[i]
        start_point = route[0]
        start_r, start_c = point_map[start_point]
        out_list = [[start_r, start_c]] # 경로를 담아둘 리스트

        for j in range(1, len(route)):
            end_point = route[j]

            start_r, start_c = point_map[start_point]
            end_r, end_c = point_map[end_point]

            get_path(start_r, start_c, end_r, end_c, out_list)

            start_point = end_point

        robot_paths.append(out_list)


    # 시간 순회.
    max_time = max([len(i) for i in robot_paths])

    for i in range(max_time):
        coord_set = set()
        counted_coord_set = set()
        for j in range(len(robot_paths)):

            # 이미 경로가 종료된 경우.
            if len(robot_paths[j]) < (i+1):
                continue

            r, c = robot_paths[j][i]

            # 이미 해당 좌표가 게산되었다면.
            if (r, c) in counted_coord_set:
                continue

            # 이미 해당 좌표가 있다면.
            if (r, c) in coord_set:
                counted_coord_set.add((r, c))
                continue

            # 최초라면, 그냥 넣어줌.
            coord_set.add((r, c))

        # 정답에 현재 시간대에, 여러 좌표에서 충돌된 횟수를 더해줌.
        answer += len(counted_coord_set)

    return answer