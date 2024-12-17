
# Method 1: output the first N numbers of the Fibonacci sequence in Python
# key concepts #
'''
[iterable]:
1. An object that can be looped over (like a book you know you can read page by page)
2. It must have an __iter__() method that returns an iterator.

[iterator]:
1. An object that does the actual "giving" of items one by one.
2. It must have a __next__() method that gives the next item or raises StopIteration when there are no more items.

The for loop does the following:
Calls __iter__() to get an iterator (in this case, the object itself).
Calls __next__() repeatedly to get the next value.
When there are no more values (when StopIteration is raised), the loop stops.
'''  
class Fab(object): 
 
    def __init__(self, max): 
        self.max = max 
        self.n, self.a, self.b = 0, 0, 1 

    # The __iter__() method makes the class iterable.
    def __iter__(self): 
        return self 
    
    # the __next__() method was used to define the behavior of an iterator.
    def __next__(self):  
        if self.n < self.max: 
            r = self.b 
            self.a, self.b = self.b, self.a + self.b 
            self.n = self.n + 1 
            return r 
        raise StopIteration()
 
for n in Fab(5): 
    print(n)

# You can check if an object is iterable by using the iter() function:
# This will work because the class has __iter__(); If an object doesn’t have __iter__(), Python will raise an error.
print(iter(Fab(2)))




# Method 2: output the first N numbers of the Fibonacci sequence in Python
# key concepts #
'''
1. A function with yield becomes a generator function(a generator function is a special type of function in Python that produces an iterator). 
2. Calling it doesn't execute the function immediately; instead, it returns a generator object.
3. for loops or the next() function can be used to get values from a generator function
'''
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b  # Update to the next Fibonacci numbers

# Using the generator with for loop 
print('print with loop')
for num in fibonacci(10):
    print(num, end=" ")

# Using the generator with next()
print('print with next')
gen = fibonacci(5)
print(next(gen)) 
print(next(gen)) 
print(next(gen)) 
print(next(gen)) 
print(next(gen)) 