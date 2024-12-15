def solution(cipher, code):
    answer = ''
    cipher_arr = list(cipher)
    # 0부터 배열길이 - 1 까지 반복
    for i in range(len(cipher_arr)):
        if (i + 1) % code == 0:
            answer += cipher_arr[i]
    
    return answer

# code - 1 부터 시작해서 끝까지 code 간격으로 새 문자열 생성
# return cipher[code-1::code]