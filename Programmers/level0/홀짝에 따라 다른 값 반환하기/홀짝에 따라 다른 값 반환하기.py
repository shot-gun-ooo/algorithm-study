def solution(n):
    answer = 0
    
    if n % 2 != 0:  # n이 홀수일 때
        # 1부터 n까지 2씩 건너뛰며 반복 (1, 3, 5, ...)
        for i in range(1, n + 1, 2):
            answer += i
            
    else:  # n이 짝수일 때
        # 2부터 n까지 2씩 건너뛰며 반복 (2, 4, 6, ...)
        for i in range(2, n + 1, 2):
            answer += (i ** 2)  # 제곱을 더함
            
    return answer