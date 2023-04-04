"""
    [ 심화 정렬 의 종류 ]     
        [1] 퀵정렬 
        [2] 힙정렬 
        [3] 합병정렬 
        [4] 팀정렬 (합병정렬과 삽입정렬을 조합해서 만든 정렬)
"""

"""
    # https://docs.python.org/ko/3.7/howto/sorting.html
    [파이썬에서 제공하는 내부 정렬 함수]
"""
a = [1,24,545,76,5,35]
a.sort() # 정렬 
print(a)
a.reverse() # 뒤집기
print(a)


"""
    [두가지 조건으로 정렬]
"""
b = [
    [10, "김종식"] , 
    [90, "이만수"] , 
    [39, "조만수"] , 
    [90, "김민지"]
]
# [1] 점수순으로 내림차순 정렬 단, 점수가 같으면 이름순으로 오름차순 정렬
# [[90, '김민지'], [90, '이만수'], [39, '조만수'], [10, '김종식']]
b = sorted(b , key=lambda x : (-x[0] , x[1] ))
print(b)

# [1] 점수순으로 내림차순 정렬 단, 점수가 같으면 이름순으로 내림차순 정렬
# [[90, '이만수'], [90, '김민지'], [39, '조만수'], [10, '김종식']]
#  reverse=True 는 전체가 뒤집히기때문에 식도 반대로써야한다.
b = sorted(b , key=lambda x : (x[0] , x[1] ), reverse=True) 
print(b)


