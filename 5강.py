import math

# 반지름, 높이 값 할당
rad = int(input('반지름의 값을 입력하세요. : '))
hei = int(input('높이의 값을 입력하세요. : '))
pi_value = math.pi

# 모선의 높이(l) 계산
slant_height = math.sqrt(rad ** 2 + hei ** 2)

# 부피 출력
print('원뿔의 부피입니다.')
print(1/3 * pi_value * rad ** 2 * hei)
# 겉넓이 출력
print('원뿔의 겉넓이입니다.')
print(pi_value * rad ** 2 + pi_value * rad * slant_height)
