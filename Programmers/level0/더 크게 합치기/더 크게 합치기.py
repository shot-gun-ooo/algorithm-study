def solution(a, b):
    # 두 조합 중 더 큰 값을 골라냅니다.
    return max(int(f"{a}{b}"), int(f"{b}{a}"))