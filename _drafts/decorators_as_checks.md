we can add decorators to ensure the correct values are being passed when calculating raw data in pyce tools.

resources:
https://gist.github.com/Zearin/2f40b7b9cfc51132851a

https://dbader.org/blog/python-decorators#:~:text=Python's%20decorators%20allow%20you%20to,great%20use%20case%20for%20decoration.

https://medium.com/swlh/python-function-decorators-a-brief-tutorial-78377046c253

Python objects are first-class.
When passed around in C++, functions are done so via pointers. This means when you defer the pointer, you invoke the code it points to.
Python hwoever treats functions as values that are assigned to variables. We can then pass them around without immediately calling them.

Function closures
A closure is an inner function that has access to the variables of its enclosing function.
Such a variable is free because...

```python
def outer(text):
    word_list = text.split()

    def inner(word):
        return word in word_list

return inner

>> text = 'some random sentence'
>> f = outer(text)
>> f('random')
True
```

Even though word_list is not in the scope of the inner function, since it's a closure, it has acess to the variables of its enclosing scope. The word_list is a free variable.

Now we can discuss decorators.
A decorator is a function that takes another function as an argument. This other function is said to be 'decorated'. The original function then returns a new function.

```python
def my_decorator(func):
    def wrapper():
        print('wrapper function doing some decoration')
        func()

    return wrapper
```

Next, define a function to be decorated.

```python
def some_func():
    print('Please decorater me')
```

Here, the decorator returns the inner function. It also takes another function as an argument. Because of free variables and first class functions, the function passed to my_decorator is available to wrapper().
Thus, wrapper() can intercept and augment the func().

When we return wrapper, we are essentially returning an augmented function that can be called.

https://medium.com/swlh/python-function-decorators-a-brief-tutorial-78377046c253