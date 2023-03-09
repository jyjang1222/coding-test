'''
04 COS PRO 2급 Python 4차
[4차][구현] 문제9) 위험한 지역 몇개인지 알려주기 - Python3

□ 문제설명

4 x 4 크기 격자 모양 지형에 위험 지역이 몇 개인지 알고 싶습니다. 위험지역이란 동, 서, 남, 북 인접한 지역이 모두 해당 지역보다 높은 지역입니다. 예를 들어 지역 높이가 아래와 같다면

빨간 영역은 인접한 지역이 모두 해당 지역보다 높은 위험지역입니다.
지역별 높이가 담긴 2차원 배열 height, height의 길이 height_len이 solution 함수의 매개변수로 주어질 때, 위험 지역이 몇 개인지 return 하도록 solution 함수를 완성해주세요.

□ 매개변수 설명

지역별 높이가 담긴 2차원 배열 height, height의 길이 height_len이 solution 함수의 매개변수로 주어집니다.
각 지역의 높이는 1 이상 50 이하인 자연수입니다.
height_len은 항상 4입니다.

□ return 값 설명

위험지역이 몇 개인지 return 해주세요.

예시

height : [[3, 6, 2, 8], [7, 3, 4, 2], [8, 6, 7, 3], [5, 3, 2, 9]]
height_len : 4
return : 5
'''

def solution(height):
	count = 0
	for i in range(len(height)):
		for j in range(len(height[i])):
			if i-1 < 0:
				north = 10
			else:
				north = height[i-1][j]
			if i+1 > len(height[i])-1:
				south = 10
			else:
				south = height[i+1][j]
			if j-1 < 0:
				west = 10
			else:
				west = height[i][j-1]
			if j+1 > len(height[i])-1:
				east = 10
			else:
				east = height[i][j+1]
			
			# if height[i][j] < north and height[i][j] < south and height[i][j] < west and height[i][j] < east:
			# 	count +=1
			
			arr = [north, south, west, east]
			
			chk = True
			for direction in arr:
				if height[i][j] > direction:
					chk = False
					
			if chk:
				count +=1
				
	return count


height = [[3, 6, 2, 8], [7, 3, 4, 2], [8, 6, 7, 3], [5, 3, 2, 9]]
ret = solution(height)
print("solution 함수의 반환 값은", ret, "입니다.")