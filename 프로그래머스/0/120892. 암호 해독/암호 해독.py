def solution(cipher, code):
    answer = ''
    cipher_arr = list(cipher)
    # 0부터 배열길이 - 1 까지 반복
    for i in range(len(cipher_arr)):
        if (i + 1) % code == 0:
            answer += cipher_arr[i]
    
    return answer