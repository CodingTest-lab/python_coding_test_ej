def solution(phone_number):
    answer = ''
    star = '*' * (len(phone_number) - 4)
    str = phone_number[-4 : ]
    return star + str

# return "*"*(len(s)-4)+s[-4:]