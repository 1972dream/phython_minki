"""
리스트
-열거형 변수를 나타내는 지료구조 중 하나-
# 열거형변수=기차
-리스트는 대괄호를 이용함
-리스트안의 값들은 쉼표로 구분함
<특1>
리스트 안의 요소는 대괄호로 접근할수있음(indexing)
왼쪽부터 0번째임
오른쪽부터 -1번쨰임
<특2>
빈 리스트 만들수있음요
ex) a=[]
<특3>
요소를 추가할 때는 append 메소드 이용함
단 맨 뒤에만 추가한다고 한다
<특4>
요소를 뺼 때는 pop메소드를 이용함
단 맨 마지막 요소만 제거됨
<특5>
요소 값을 이용해서 제거할때는 remove 메소드를 사용함
<특6>
오름차순 정멸할 때는 sort 메소드를 사용

정멸 오름차순=1234
     내림차순=4321
[2,4,1,3]
<특7>
내림차순 정렬할 때는 reverse 메소드 사용 
"""
# a = 10
# b = "민기"
# c = ["사과", "귤", "바나나"]
# d = [1, 2, 3, 4]
# e = ["사과", 2, "귤", 4]
# print(a)
# print(b)
# print(c)
# print(d)
# print(e)
# print(c[0])
# print(c[1])
# print(c[2])
# print(c[-1])
# print(c[-2])
# print(c[-3])
# print(d[1] ** d[2])
# print(d[-1] % d[1])
# 민기 = []
# print(민기)
# 민기.append("윤성이 보다 잘생김 하지만 팩트")
# print(민기)
# 민기.append("공부 윤성이보다 잘함 팩트")
# print(민기)
# 민기.pop()
# print(민기)
# 민기.pop()
# print(민기)
# 민기.pop()
# print(민기)
# 진우 = ["뺀질", "블랙", "모자"]
# print(진우)
# 진우.pop()
# print(진우)
# 진우.remove("뺀질")
# print(진우)
num = [2, 4, 1, 3]
print(num)
num.sort()
# print(num)
fruit = ["watermelon", "orange", "apple", "banana"]
print(fruit)
fruit.sort()
# print(fruit)
num.reverse()
print(num)
fruit.reverse()
print(fruit)
