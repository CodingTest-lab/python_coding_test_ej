# 입력받은 시간을 초로 나타내는 함수
def time_to_sec(time):
    mm, ss = map(int, time.split(':'))
    return 60 * mm + ss

def solution(video_len, pos, op_start, op_end, commands):
    
    len_sec = time_to_sec(video_len)
    pos_sec = time_to_sec(pos)
    op_s_sec = time_to_sec(op_start)
    op_e_sec = time_to_sec(op_end)
    
    # op_start <= pos <= op_end 라면 pos는 op_end로 이동
    if op_s_sec <= pos_sec <= op_e_sec:
        pos_sec = op_e_sec
        
    # 명령어에 따라 구간 이동
    for command in commands:
        # 10초 전 이동 -> video_len과 10초 전 중 큰거
        if command == 'prev':
            pos_sec = max(0, pos_sec - 10)
        # 10초 후 이동 -> video_len과 10초 후 중 작은거
        else:
            pos_sec = min(len_sec, pos_sec + 10)
            
        # op_start <= pos <= op_end 라면 pos는 op_end로 이동
        if op_s_sec <= pos_sec <= op_e_sec:
            pos_sec = op_e_sec
        
    # 결과를 mm:ss 형태로 나타내야하므로 분은 60으로 나눈 몫, 초는 60으로 나눈 나머지
    result = [pos_sec//60, pos_sec%60]
    
    # 분과 초가 10 미만이면 앞에 0을 붙임
    return ':'.join(map(lambda x:str(x) if x >= 10 else '0'+str(x), result))