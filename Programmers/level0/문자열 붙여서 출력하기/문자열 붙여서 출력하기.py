str1, str2 = input().strip().split(' ')

print(f"{str1}{str2}")

# input(): 사용자로부터 한 줄을 입력받습니다. (예: "apple pen")

# .strip(): 앞뒤에 혹시 있을지 모를 불필요한 공백을 제거합니다.

# .split(' '): 공백(' ')을 기준으로 문자열을 자릅니다. 결과적으로 ['apple', 'pen']이라는 **리스트(묶음)**가 만들어집니다.