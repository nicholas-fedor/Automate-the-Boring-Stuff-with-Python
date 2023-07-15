def spam(divideBy):
    return 42 / divideBy

print(spam(2)) # 21.0
print(spam(12)) # 3.5
print(spam(0)) # ZeroDivisionError: division by zero
print(spam(1)) # doesn't run due to unhandled error above.