def solution(n):
    # range(1, n + 1, 2)
    # 1부터 n까지(n+1 미만), 2씩 건너뛰며(1, 3, 5...) 생성
    answer = list(range(1, n + 1, 2))
    return answer