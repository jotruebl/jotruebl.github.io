---
title: Quick Tips to Write Better Python Code
tags: 
- tricks
- tips
- review
- best practices
- built-in functions
---
This post is a summary of some useful tips and tricks I recently saw [in a video by Corey Schafer](https://www.youtube.com/watch?v=C-gEQdGVXbk&t). The video itself is a quick 10 minutes and I definitely think it's useful even for experienced Pythonistas as it cant act as a reminder of some basic shortcuts. But unless you're a beginner, it's probably faster and just as effective to read the tips rather than watching a video explaining everything step by step. Hence this post. Let's get started.

## Ternary Operators 
Imagine an if/else conditional statement:

```python
if condition:
    x = 1
else:
    x = 0
```

This can be written as a one-liner:

```python
x = 1 if condition else 0
```

However, don't sacrifice clarity for the sake of brevity.

## Keep Track of Digits with Underscores 
WHen we write numbers (in English speaking countries), we add a comma every 3 digits to make it more readable. For example, one million is written as 1,000,000. Commas can't be used in programming in this way. This can get frustrating when trying to determine the size of a number:

```python
x = 10000000000
```

One way to fix this is to use scientific notation, but if all the digits are significant or if you're writing something like a serial number, then it's not a good idea to drop any digits. In this case, you can use the underscore to separate digits: 

```python
num1 = 10_000_000_000
print(num1)
```
```
>> 10000000000
```

## Formatting with f-strings  
Very similar to the previous tip. Simply, you can add commas when printing a variable using f-string formatting:

```python
num1 = 10_000_000_000
print(f'{num1:,}')
```
```
>> 10,000,000,000
```

Cool.

## Context Managers
Imagine you want to open a file, save the contents to a variable, and then close the file:
```python
f = open('test.txt', 'r')
file_contents = f.read()
f.close()
```
A context manager can help with this. Context managers aid in the handling of resources. For example, in this instance we can use [with/as](https://docs.python.org/3/reference/compound_stmts.html#the-with-statement), which allows us to do two related operations as a pair with some other code in between. In this example, the two related operations are opening and closing the file and the code in between is saving the content to a variable.

```python
with open('test.txt', 'r') as f:
    file_contents = f.read()
```
The benefit here is we dont need to manually close the file ourselves and the code is much ceaner.

## Use Enumerate()
It's likely you already know about this method, but it serves as a good reminder anyways. Imagine you want to loop over an iterable while also keeping track of the index. You'd probably write something like this:

```python
names = ['Shannon' ,'Mark', 'Jim']

index = 0
for name in names:
    print(index, name)
    index += 1
```
```
>> 0 Shannon
>> 1 Mark
>> 2 Jim
```

The enumerate function removes the need for manually creating an index counter:

```python
for index, name in enumerate(names):
    print(index, name)
```
```
>> 0 Shannon
>> 1 Mark
>> 2 Jim
```
enumerate() also accepts optional arguments to start counting at a value other than zero.

## Use Zip() 
Like enumerate(), most of us probably already know about the zip function. Imagine you need to loop over two lists at once:

```python
names = ['Clark Kent', 'Bruce Wayne', 'Tony Stark']
heroes = ['Superman', 'Batman', 'Iron Man']

for index, name in enumerate(names):
    hero = heroes[index]
    print(f'{name} is actually {hero}')
```
```
>> Clark Kent is actually Superman
>> Bruce Wayne is actually Batman
>> Tony Stark is actually Iron Man
```

The zip function does this for us:
```python
for name, hero in zip(names, heroes):
    print(f'{name} is actually {hero}')
```
```
>> Clark Kent is actually Superman
>> Bruce Wayne is actually Batman
>> Tony Stark is actually Iron Man  
```
[zip()](https://docs.python.org/3.3/library/functions.html#zip) can be used on any kind of iterable and accepts any number of objects. 

[Click here to see the rest of Python's built-in functions.](https://docs.python.org/3/library/functions.html)

## Unpacking and the *-operator
Let's say we have a tuple and want to unpack it. We can do the following:
```python
items = (1,2)
a, b = (1,2)
print(a, b)
```
```
>> 1 2
```

If we dont plan to use the second variable, we can set it as an underscore. It still saves _ as 2, but
other developers (or your future self) will recognize it as a variable you don't need.
```python
a, _ = (1,2)
```

But what if we don't have the same number of variables as items we're trying to unpack? The solution is to use the [*-operator](https://docs.python.org/3/tutorial/controlflow.html#unpacking-argument-lists).

If we put an * in front of b, then remaining values will be set to b as a list.

```python
a, *b = (1,2,3)
print(a)
print(b)
```
```
>> 1
>> [2, 3]
```

We can also just use the first two values and ignore the rest:
```python
a, b, *_ = (1,2,3,4,5)
print(a)
print(b)
```
```
>> 1
>> 2
```
Note this how [argument unpacking works](https://docs.python.org/3/tutorial/controlflow.html#unpacking-argument-lists). Also see [keyword arguments and the **-operator](https://docs.python.org/3/tutorial/controlflow.html#keyword-arguments).
## Getting and Setting Attributes
Dynamically setting an instance attribute is easy:
```python
class Person():
    pass

person = Person()
person.first_name = 'Jon'
```
But what if you wanted to create an attribute name based on the value of one variable with a corresponding attribute value based on another variable? For example, say you have a set of keyword variables that you'd like to set as an object's attributes. If the name of the attribute you are trying to set is held in a variable, then x.variable_name = "some value" won't work, but instead it will set the attribute name to literally "variable_name."  

Here's a concrete example:
```python
first_key = 'first_name'
first_val = 'Jon'

person.first_key = first_val
```
The problem with this is that the attribute is now named 'first_key' instead of 'first_name'
Essentially, [setattr()](https://docs.python.org/3.3/library/functions.html#setattr) can be used when the name of the attribute you wish to set is contained in a variable. This is because setattr() takes 3 arguements: the object, a string, and a value.
```python
first_key = 'first_name'
first_val = 'Jon'

setattr(person, first_key, first_val)
print(person.first_name)
```
```
>> Jon
```

Note: setattr() should not be confused with \__setattr__() [which is an entirely different, although extremely useful, method.](https://docs.python.org/3/reference/datamodel.html#object.__setattr__)

Similarly, [getattr()](https://docs.python.org/3.3/library/functions.html#getattr) can be used when the attribute you want to access is saved somewhere as a variable. You can also set a default return in the instances where the attribute does not exist.

That's it for now. As I said in the intro, unless you're a complete beginner to Python you likely already knew about these tips. But it's good to periodically remind yourself of the best practices to ensure you're not ingraining bad habits or making overly-complicated code.