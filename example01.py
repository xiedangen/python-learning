import math

print("hello world")
print("goodbye world")

# 单行注释
# aaa

"""
这是一个多行注释
第二行
"""

is_student = True
is_teacher = False

print("auto save")


print("Python 中以下值转换为 False")
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(0.0))
print(bool(0j))
print(bool(""))
print(bool([]))
print(bool({}))
print(bool(set()))
print(bool(()))

print()

print("Python 中以下值转换为 True")
print(bool(True))
print(bool(1))
print(bool(-1))
print(bool(0.1))
print(bool("0.1"))
print(bool("0"))
print(bool(" "))
print(bool([1, 2]))
print(bool({"a": 1}))

print()

print("Python 的 NaN 是真值")
print(bool(float("nan")))
print(bool(math.nan))

name: str = "张三"
age: int = 15

print(type(100))
print(isinstance(100, int))

print(int("123"))
print(type(int("123")))
print(float("123.45"))
print(type(float("1123.45")))
print(str(100))
print(type(str(100)))
print(bool(100))
print(type(bool(100)))

print()

name = ""
if name:
    print("有名字")
else:
    print("没有名字")

item = []
if item:
    print("有物品")
else:
    print("没有物品")


def greet(name=None):
    if name:
        return f"Hello, {name}"

    return "Hello, Guest"


print(greet())
print(greet(None))
print(greet(False))
print(greet("Tom"))
