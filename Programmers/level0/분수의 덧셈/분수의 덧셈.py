import math

def solution(numer1, denom1, numer2, denom2):
    # 1. 두 분수를 더한 분자와 분모 구하기
    new_numer = numer1 * denom2 + numer2 * denom1
    new_denom = denom1 * denom2
    
    # 2. 최대공약수(GCD) 구하기
    gcd_value = math.gcd(new_numer, new_denom)
    
    # 3. 최대공약수로 나누어 기약분수 만들기
    # 나눗셈 결과는 정수여야 하므로 // 연산자를 사용합니다.
    answer = [new_numer // gcd_value, new_denom // gcd_value]
    
    return answer