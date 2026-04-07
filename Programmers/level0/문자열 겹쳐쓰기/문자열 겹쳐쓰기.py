
def solution(my_string, overwrite_string, s):
    # s 전까지의 문자열 + 덮어쓸 문자열 + 덮어쓴 뒤에 남은 나머지 문자열
    answer = my_string[:s] + overwrite_string + my_string[s + len(overwrite_string):]
    return answer