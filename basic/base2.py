# 変数の応用

animal = 'dog'
動物 = 'cat'
print(動物)

# 定数

LEGAL_AGE = 20
age = 18

if age < LEGAL_AGE:
    print('未成年')
else:
    print('成人')

# format文
print(f'age = {age}')  # 3.6
print(f'{age=}')  # 3.8 変数の中身確認とかにつかえる
