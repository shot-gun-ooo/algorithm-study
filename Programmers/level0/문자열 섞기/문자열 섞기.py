def solution(str1, str2):
    answer = ''
    # 문자열의 길이만큼 반복문 실행
    for i in range(len(str1)):
        answer += str1[i] # str1의 i번째 글자 추가
        answer += str2[i] # str2의 i번째 글자 추가
    return answer