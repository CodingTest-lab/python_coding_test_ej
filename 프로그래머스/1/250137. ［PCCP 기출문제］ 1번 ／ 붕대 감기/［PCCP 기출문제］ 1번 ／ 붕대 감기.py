def solution(bandage, health, attacks):
    # 시간은 attacks의 최대 공격 시간동안 실행, attacks는 공격시간 기준 오름차순이므로 마지막 리스트의 공격시간
    max_time = attacks[-1][0]
    # 현재 체력 = 최대 체력
    max_health = health
    
    # 딕셔너리 자료형을 사용해 attacks안의 내용을 키(공격시간):값(피해량) 형태로 만듦
    attack_dic = {}
    for i in attacks:
        attack_dic[i[0]] = i[1]
    
    # 현재 시간
    t = 0
    # 연속 성공 횟수
    con = 0
    
    # 현재 시간이 마지막 공격시간보다 작거나 같을때까지 반복
    while t <= max_time:
        # 1. 공격 받을 때 공격량만큼 체력 감소, 연속 성공 횟수 초기화
        if t in attack_dic:
            health -= attack_dic[t]
            con = 0
            
            # 공격 받는 중 체력이 0 이하면 죽음
            if health <= 0:
                return -1
            
        # 2. 공격받지 않을때
        else:
            # 연속 성공 횟수 1씩 증가
            con += 1
            # 연속 성공 횟수가 시전 시간보다 작으면
            if con < bandage[0]:
                # 현재 체력에 초당 회복량 추가
                health += bandage[1]
                # 현재 체력이 최대 체력보다 크면
                if health > max_health:
                    # 현재 체력이 최대 체력이 됨
                    health = max_health
                    
            # 연속 성공 횟수가 시전 시간보다 크거나 같으면
            else:
                # 현재 체력에 초당 회복량과 추가 회복량이 추가됨
                health = health + bandage[1] + bandage[2]
                # 현재 체력이 최대 체력보다 크면
                if health > max_health:
                    # 현재 체력이 최대 체력이 됨
                    health = max_health
                # 연속 성공 횟수 초기화
                con = 0
                
        # 현재 시간이 1씩 증가
        t += 1          
    
    return health