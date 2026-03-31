def solution(num_list):
    # 1. 마지막 원소와 그 전 원소를 변수에 담아두면 편해요.
    last = num_list[-1]
    prev = num_list[-2]
    
    # 2. 문제의 조건대로 비교하기
    if last > prev:
        # 마지막 원소가 더 크면: (마지막 - 그전) 값을 추가
        num_list.append(last - prev)
    else:
        # 크지 않다면 (작거나 같다면): (마지막 * 2) 값을 추가
        num_list.append(last * 2)
        
    return num_list

print(solution([2, 1, 6]))