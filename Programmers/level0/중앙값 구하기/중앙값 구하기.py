def solution(array):
    # 1. 먼저 배열을 크기 순으로 정렬합니다.
    array.sort()
    
    # 2. 길이를 구하고 2로 나눈 몫을 인덱스로 사용합니다.
    # (길이가 홀수이므로 2로 나눈 몫이 정확히 가운데 인덱스가 됩니다.)
    index = len(array) // 2
    
    answer = array[index]
    return answer