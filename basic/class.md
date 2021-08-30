## Classes and Inheritance

We can define attributes and functions inside a class. In Python, there's a "magic" method that runs when we create a new instance by calling theclass. It's called __init__ and it does nothing by default. If our __init__ method takes other arguments than self we can call the class with arguments and they will be given to __init__.

```python

class Animal:
    noise = "Rrrr"
    color = "Red"
    def __init__(self, noise, color):
        self.noise = noise
    def make_noise(self): # this
        print(f"{self.noise}")
    def set_noise(self, new_noise):
        self.noise = new_noise
    def get_noise(self):
        return self.noise
    def set_noise(self, new_noise):
        self.noise = new_noise
        return self.noise
    def get_color(self):
        return self.color
    def set_color(self, new_color):
        self.color = new_color
        return self.color
    

class Wolf(Animal):
    noise = "grrrr"


class BabyWolf(Wolf):
    color = "yellow"
```

Use CapsWords for class names and lowercase_words_with_underscores for other names. This makes it easy to see which objects are classes and which objects are instances.

## Magic methods

Methods that have a name __like_this__ and a special meaning are called magic methods or special methods.

Some magic methods have a default implementation that is used if the class doesn't define anything else. For example, if we don't define an __init__ then our class will take no arguments and it won't have any attributes by default.

```python

>>> class Thing:
...     def __len__(self):
...         return 5
...
>>> t = Thing()
>>> t
<__main__.Thing object at 0x7f05e4597198>
>>> t.__len__()
5
>>> len(t)
5
>>>

```

### Item 22: Prefer Helper Classes Over Bookkeeping with Dictionaries and Tuples

### Item 23: Accept Functions for Simple Interfaces Instead of Classes

The __call__ special method enables instances of a class to be called like plain Python functions.

When you need a function to maintain state, consider defining a class that provides the __call__ method instead of defining a stateful closure

A class object with __call__ method can be used as a acting method with ability to have internal state. 

### Item 27: Prefer Public Attributes Over Private Ones

Item 28: Inherit from collections.abc for Custom Container Types

in python new data structure(container) can inherit from build in containers like list, dict,..

in PHP we cann't do that

### Item 29: Use Plain Attributes Instead of Get and Set Methods

use @property instead

### Item 30: Consider @property Instead of Refactoring Attributes

The built-in @property decorator makes it easy for simple accesses of an instance’s attributes to act smarter

### Item 31: Use Descriptors for Reusable @property Methods

### Item 32: Use __getattr__, __getattribute__, and __setattr__ for Lazy Attributes

If your class defines __getattr__, that method is called every time an attribute can’t be found in an object’s instance dictionary. If the attribute already exits, this method will not be called again.

__getattribute__ is a special method which is called every time an attribute is accessed on an object, even in cases where it does exist in the attribute dictionary

Avoid infinite recursion in __getattribute__ and __setattr__ by using methods from super()

## Metaclasses

### Item 33: Validate Subclasses with **Metaclasses**

Often a class’s validation code runs in the __init__ method, when an object of the class’s type is constructed. Using metaclasses for validation can raise errors much earlier.

Validate subclass right at the time it is declared. The __new__ method of metaclasses is run after the class statement’s entire body has been processed.

**Metaclasses** have slightly different syntax in Python 2 vs. Python 3.

### Item 34: Register Class Existence with **Metaclasses**

Put a register into metaclass

## Concurrency  and Parallelism

Item 36: Use subprocess  to  Manage  Child   Processes
 - Class registration is a helpful pattern for building modular Python programs.
 - Metaclasses let you run registration code automatically each time your base class is subclassed in a program.
 - Using metaclasses for class registration avoids errors by ensuring that you never miss a registration call.

### Item 35: Annotate Class Attributes with Metaclasses


