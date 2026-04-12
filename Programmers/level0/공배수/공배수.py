def solution(number, n, m):
    # number가 n으로 나누어 떨어지고(배수), 
    # 동시에 m으로도 나누어 떨어지는지 확인합니다.
    if number % n == 0 and number % m == 0:
        return 1
    else:
        return 0