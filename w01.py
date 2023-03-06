# 01 출력

# 기본 출력
# 다양하게 출력
print('Total days in Year')
print(365)
print('Circumference rate')
print('3.1415926535')

# 변수와 자료형
# 정수 선언하고 곱 출력
a, b = 26, 5
print(a, '*', b, '=', a*b)

# 출력 형식
# 변수 출력하기 3
a,b,c = 1,2,'C'
print(f'{a}->{b}->{c}')

# 소수점 맞춰 출력
# 두 실수의 곱
a, b = 5.26 , 8.27
print(f'{a*b:.3f}')

# 변수 값 변경
# 문자 변경하기
a = 'C'
a = 'T'
print(a)

# 다른 변수로부터 값 변경
# 정수 복사
a = 3
b = 4
b = a
print(a, b)
print(a*b)

# 두 변수 값을 교환
# 데이터 교환
a, b, c = 5,6,7
a,b,c = c,a,b
print(a)
print(b)
print(c)

# 변수 값 동시에 복사
# 합을 복사하기
a,b,c, = 1,2,3
a = b = c = a+b+c
print(a,b,c)

