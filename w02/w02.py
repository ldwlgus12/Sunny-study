# 입출력

# 정수 입력 - 정수 입력받아 계산
a = int(input())
print(a*2+3)

# 실수 입력 - 실수 입력받아 계산 2
n = float(input())
print(f'{n+1.5:.2f}')

# 공백을 사이에 두고 입력 - 입력받은 값과 합 출력
a,b = map(int, input().split())
print(a, b, a+b)

# 2개의 줄에 걸쳐 입력 - 정수 세 개 입력받아 출력
a,b = map(int, input().split())
c = int(input())
print(a, b, c)

# 문자, 문자열 입력 - 문자열 순서 바꾸기
a = input()
b = input()
print(b)
print(a)

# 특정 문자를 사이에 두고 입력 - 전화번호 바꾸기
a,b,c = input().split('-')
print(f'{a}-{c}-{b}')

