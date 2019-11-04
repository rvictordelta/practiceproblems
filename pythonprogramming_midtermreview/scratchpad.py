# print(10/3)
# print(10//3)
# print(10 % 3)
# print(divmod(10, 3))
#
# s = "testing"
# l = ['a', 'b']
# t = ('a', 'b')
# l[1] = 'B'
#
# print("s\tp\na\0m")
# print(r"""a\na""")
#
# S = 'abcedfg'
# print(S[4:1:-1])
# S = 'xxxxSPAMxxxxSPAMxxxxx'
# S = S.replace('xx', 'mm')
# print(S[::-1])
#
# d = {1: 'a', 2: 'b'}
# print(list(d.items()))
#
#
# x, y = [1, 2]
# print(x)
# print(y)
# print(x, y)
# z = [1, 2]
# # print(z[0::-1])
# a, *b = 'spam'
# print(a)
# print(b)
# x = 10
# y = x
# x += 20
# print(y)

# x = [1,2,3]
# y = x
# x = 100
# print(y)

# def square(x):
#     return x * x
# def count_calls(func):
#     count = 0
#     def inner(*args, **kwargs):
#         nonlocal count
#         count += 1
#         print(f'Called {count} times')
#         return func(*args, **kwargs)
#     return inner
#
# call_func = count_calls(square)
# print(call_func(2)) # What gets printed?
# print(call_func(3)) # What gets printed?

# history = []
# def remember():
#     def f(*args):
#         history.append(args)
#         return history
#     return f
#
# test = remember()
# test('a')
# test('b')
# print(history)
#
# print(sum(list(map(lambda x, y: x*y, [1, 2], [2, 3]))))

print((lambda arg1: arg1 + 2)(2))

