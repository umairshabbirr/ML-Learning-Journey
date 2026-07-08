// Add Two Numbers By lambda fuction 
add = lambda a, b: a + b

print(add(10, 20))

// Maximum Number by lamba functions
maximum = lambda x, y: x if x > y else y

print(maximum(15, 30))

// Even or Odd
even = lambda x: x % 2 == 0

print(even(10))
print(even(7))

// Square Every Number by map
numbers = [1, 2, 3, 4, 5]

squares = list(map(lambda x: x ** 2, numbers))

print(squares)
