def solution(my_string):
    answer = ''
    for i in my_string:
        if i in ['a', 'e', 'i', 'o', 'u']:
          my_string = my_string.replace(i, '')
    
    answer = my_string
    return answer

# return "".join([i for i in my_string if not(i in "aeiou")])