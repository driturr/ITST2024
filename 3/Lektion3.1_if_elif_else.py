for i in range(100):
    if i % 3 == 0 and i % 5 == 0:
        print(i, ": FizzBuzz")
        continue
    elif i % 3 == 0:
        print(i, ": Fizz")
        continue
    elif i % 5 == 0:
        print(i, ": Buzz")
        continue
    
    else: print(i, "No divisible")