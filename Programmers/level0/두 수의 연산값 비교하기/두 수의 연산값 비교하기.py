def solution(a, b):
    # 1. a ⊕ b 계산 (문자열로 붙인 뒤 정수로 변환)
    # f-string을 사용하면 str(a) + str(b)보다 간결합니다.
    ab = int(f"{a}{b}")
    
    # 2. 2 * a * b 계산
    two_ab = 2 * a * b
    
    # 3. 두 값을 비교하여 큰 값을 반환
    # 문제에서 두 값이 같으면 ab를 반환하라고 했으므로 >=를 사용합니다.
    if ab >= two_ab:
        return ab
    else:
        return two_ab