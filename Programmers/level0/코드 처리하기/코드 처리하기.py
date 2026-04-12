def solution(code):
    ret = ''
    mode = 0
    
    # code의 각 문자를 인덱스와 함께 하나씩 확인합니다.
    for idx in range(len(code)):
        if mode == 0:
            # mode가 0일 때
            if code[idx] == "1":
                mode = 1  # mode 전환
            else:
                # 1이 아니고 idx가 짝수일 때만 추가
                if idx % 2 == 0:
                    ret += code[idx]
        else:
            # mode가 1일 때
            if code[idx] == "1":
                mode = 0  # mode 전환
            else:
                # 1이 아니고 idx가 홀수일 때만 추가
                if idx % 2 != 0:
                    ret += code[idx]
    
    # 결과가 빈 문자열이면 "EMPTY", 아니면 ret 반환
    return ret if ret != "" else "EMPTY"