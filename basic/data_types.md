## Numbers, Variables, and Strings


`\t`: Tab

`\\` or `//`: Allowed Slash

`\'`: Allowed Single Quote

`\"`: Allowed Double quote

`{{` or `}}`: Allowed single curly bracket in formatted strings

`"your single-line text"`: Wrap a single quote (`'`) or double quote (`"`) around text / numbers to make it a string.

`\`: A `slash` in front of a `return`/`enter` will escape that. Allowing for multi-line strings without the triple quotes. Such as:
```python
"this is my string example\
when I close it here"
```


`""" your multi-line text"""`: Wrap 3x single quotes (```) or 3x double quotes (`"`) around a lot of text to allow for multi-line strings. Such as:
```python
"""this is my string example
when I close it here"""
```


#### The `.format()` method


#### The `%` method


#### `f` Strings (aka `f-string`)

## Lists, Tuples & Dictionaiers

### Lists
```python
>>> my_cart = [12.99, 312, 32, 142]
>>> sum(my_cart)
498.99
>>> my_cart.append(39.99)
>>> print(my_cart)
[12.99, 312, 32, 142, 39.99]
>>> len(my_cart)
5
>>> my_cart
[12.99, 312, 32, 142, 39.99]
>>> my_cart[3]
142
```

### Tuples
Tuples are a lot like lists, but they're immutable so they can't be changed in-place. We create them like lists, but with () instead of [].

```python
>>> thing = (1, 2, 3)
>>> thing
(1, 2, 3)
```

### Dictionaries
```python
>>> my_data = {"name": "Justin Mitchel"}
>>> my_data["name"]
'Justin Mitchel'
>>> my_data = {"name": "Justin Mitchel", "location": "California"}
>>> my_data[0]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 0
>>> my_data.keys()
dict_keys(['name', 'location'])
>>> list(my_data.keys())
['name', 'location']
>>> list(my_data.keys())[0]
'name'
>>> my_data.append({"occ": "coder"})
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'dict' object has no attribute 'append'
>>> my_data["occ"] = "Coder"
>>> my_data
{'name': 'Justin Mitchel', 'location': 'California', 'occ': 'Coder'}
>>> user_1 = {"name": "James bond"}
>>> user_2 = {"name": "Ned Stark"}
>>> my_users = [user_1, user_2]
>>> my_users
[{'name': 'James bond'}, {'name': 'Ned Stark'}]
```

## Sets

Sometimes we just want to store a bunch of things. We don't need to have the same thing twice and we don't care about the order. This is when sets come in. They are like lists without order or duplicates, or keys of dictionaries without the values. 

We can create a set just like a dictionary, but without :.

```python

>>> names = {'wub_wub', 'theelous3', 'RubyPinch', 'go|dfish', 'Nitori'}
>>> names
{'RubyPinch', 'theelous3', 'go|dfish', 'wub_wub', 'Nitori'}
>>> type(names)
<class 'set'>

```


## Iterables, iterators and Generators


