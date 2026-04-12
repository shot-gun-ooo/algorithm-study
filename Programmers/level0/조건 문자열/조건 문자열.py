def solution(ineq, eq, n, m):
    cond = ineq + eq
    
    if cond == ">=":
        return 1 if n >= m else 0
    elif cond == "<=":
        return 1 if n <= m else 0
    elif cond == ">!":
        return 1 if n > m else 0
    elif cond == "<!":
        return 1 if n < m else 0