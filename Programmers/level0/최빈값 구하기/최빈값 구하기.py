from collections import Counter

def solution(array):
    # 각 숫자별 등장 횟수를 셉니다 (예: {3: 3, 1: 1, 2: 1})
    counts = Counter(array).most_common()
    
    # 1. 만약 데이터가 하나뿐이라면 바로 그 값이 최빈값
    if len(counts) == 1:
        return counts[0][0]
    
    # 2. 가장 많이 등장한 횟수(counts[0][1])와 
    # 두 번째로 많이 등장한 횟수(counts[1][1])를 비교합니다.
    if counts[0][1] == counts[1][1]:
        return -1
    
    return counts[0][0]