# This will break upon entry of "your name".
while True:
    print("Please type 'your name'.")
    name = input()
    if name == "your name":
        break

print("Thank you!")