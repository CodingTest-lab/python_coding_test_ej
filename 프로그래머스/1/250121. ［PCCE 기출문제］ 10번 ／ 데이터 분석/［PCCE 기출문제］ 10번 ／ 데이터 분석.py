def solution(data, ext, val_ext, sort_by):
    # data에서 ext값이 val_ext보다 작은 데이터만 뽑은 후 sort_by에 해당하는 값 기준으로 오름차순 정렬
    criteria = {
        'code':0, 'date':1, 'maximum':2, 'remain':3
    }
    answer = []
    for i in data:
        if i[criteria[ext]] < val_ext:
            answer.append(i)
    return sorted(answer, key=lambda x: x[criteria[sort_by]])