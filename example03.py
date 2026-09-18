a = 100
b = 123.45
c = "string"
d = True
print(type(a))
print(type(b))
print(type(c))
print(type(d))


price = 100
discount = 0.8
total = f"原价：{price}，折后：{price * discount}"
print(total)

pi = 3.141526
print(f"圆周率保留两位小数：{pi:.2f}")
print(f"数字右对齐：{123:>10}")

name = "张三"
age = 25
message1 = f"我是{name}，今年{age}岁"
message2 = "我是{}，今年{}岁".format(name, age)
print(message1)
print(message2)
