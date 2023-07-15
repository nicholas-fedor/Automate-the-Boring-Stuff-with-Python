def spam(divideBy):
    return 42 / divideBy

try:
    print(spam(2))
    print(spam(12))
    print(spam(0))
    print(spam(1))
except ZeroDivisionError:
    print('Error: Invalid Argument.')

# 21.0
# 3.5
# Error: Invalid Argument.

# Program doesn't run 'print(spam(1))' because there is no return after the except clause.