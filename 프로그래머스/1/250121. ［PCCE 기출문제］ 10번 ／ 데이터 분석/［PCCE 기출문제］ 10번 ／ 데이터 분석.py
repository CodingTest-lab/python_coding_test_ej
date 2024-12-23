def solution(data, ext, val_ext, sort_by):
    # data에서 ext값이 val_ext보다 작은 데이터만 뽑은 후 sort_by에 해당하는 값 기준으로 오름차순 정렬
    criteria = {
        'code':0, 'date':1, 'maximum':2, 'remain':3
    }   # 딕셔너리로 기준을 만들어 놓기, 처음엔 조건문으로 할까 생각도 했는데 효율성을 위해 이렇게 저장해놓는게 나은듯
    answer = []
    for i in data:   # 2차원 배열 내 배열들을 돌면서
        # criteria[ext] 는 criteria['code'] = 0 이런식으로 만들어짐, 딕셔너리의 key를 문자열로 해놓은 이유 -> 인덱스로 사용하기 위함
        if i[criteria[ext]] < val_ext:
            answer.append(i)
    return sorted(answer, key=lambda x: x[criteria[sort_by]])  # 람다식 내의 x변수는 answer 2차원배열 내 각각의 배열
