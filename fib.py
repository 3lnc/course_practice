a, b, n = 1, 1, 2

while n < 10**6:
    a, b, n = b, a + b, n + 1

print(len(str(b)))


# # First fibonacci number that is greater than 10 millions
# a, b = 1, 1

# while b < 10 ** 7:
#     a, b = b, a + b

# print(b)

# # First fibonacci number than is longer than 1000 symbols in decimal view
# a, b = 1, 1

# while len(str(b)) < 1000:  # same as b < 10**999, but latter is faster
#     a, b = b, a + b

# print(b)

