def spam():
    print(eggs) # ERROR
    eggs = 'spam local'

eggs = 'global'
spam()

# Output: UnboundLocalError: local variable 'eggs' referenced before assignment