# 文字列型

fruit = 'apple'
print(fruit)
print(type(fruit))

print(fruit * 10)
fruit_10 = fruit * 10
print(fruit_10)

new_fruit = fruit + ' banana'
print(new_fruit)

fruits = """apple
banana
grape
"""
print(fruits)

fruit = 'banana'
print(fruit[2])
print(fruit[-1])

# encode, decode => bytes[]
byte_fruit = fruit.encode('utf-8')
print(byte_fruit)
print(type(byte_fruit))

str_fruit = byte_fruit.decode('utf-8')
print(type(str_fruit))

# count

msg = 'ABCDRABC'
print(msg.count('ABC'))

# startswith, endswith

print(msg.startswith('ABCD'))
print(msg.endswith('DC'))

# strip, rstrip, lstrip

msg = ' ABC '
print(msg)
print(msg.strip())
msg = 'AABAABAA'
print(msg.strip('A'))
msg = 'AABCAACBAA'
print(msg.strip('BA'))
print(msg.lstrip('BA'))
print(msg.rstrip('BA'))

# upper, lower, swapcase, replace, capitalize

msg = 'abcABC'
msg_u = msg.upper()
msg_l = msg.lower()
msg_s = msg.swapcase()
print(msg_u, msg_l, msg_s)

msg = 'ABCDEABC'
msg_r = msg.replace('ABC', 'FFF')
print(msg_r)
msg_r = msg.replace('ABC', 'FFF', 1)
print(msg_r)

msg = 'helLo wOrld'
print(msg.capitalize())
