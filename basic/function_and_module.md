## Function

### Multiple return values

Function can take multiple arguments, but they can only return one value. But sometimes it makes sense to return multiple values as well. The best solution is to return a tuple of values, and just unpack that wherever the function is called:

```python

def login():
    username = input("Username: ")
    password = input("Password: ")

def login():
    ...
    return (username, password)


username, password = login()
```

### *args, **kwargs

*args just magically gets whatever positional arguments the function is given and turns them into a tuple, and never raises errors.

```python

>>> def thing(*args):
...     print("now args is", args)
...
>>> thing()
now args is ()
>>> thing(1, 2, 3)
now args is (1, 2, 3)
>>>

```

**kwargs is the same thing as *args, but with keyword arguments instead of positional arguments.

```python

>>> def thing(**kwargs):
...     print('now kwargs is', kwargs)
...
>>> thing(a=1, b=2)
now kwargs is {'b': 2, 'a': 1}
```

## Main function


The last function in a program like this is usually called `main` and it runs the program using other functions. 

```python

import sys
import requests
from datetime import datetime

from formatting import format_msg

def send(name, website=None, verbose=False):
    if website != None:
        msg = format_msg(my_name=name, my_website=website)
    else:
        msg = format_msg(my_name=name)
    if verbose:
        print(name, website)
    # send the message
    r = requests.get("http://httpbin.org/json")
    if r.status_code == 200:
        return r.json()
    else:
        return "There was an error"

if __name__ == "__main__":
    print(sys.argv)
    name = "Unknown"
    if len(sys.argv) > 1:
        name = sys.argv[1]
    response = send(name, verbose=True)
    print(response)

```

The __name__ variable is set differently depending on how we run the file, and it's '__main__' when we run the file directly instead of importing. So if we run the file normally it asks us the words, and if we import it instead we can still run the functions one by one. If you want to know more about __name__ just make a file that prints it and run it in different ways.

## Modules and standard python libraries

```python

import random

print("A random number between 1 and 3:", random.randint(1, 3))
```

All the modules come from the same path where python library (standard libraries) is defined and from the same directory where the running file is located

There's a module called sys that contains various things built into Python. Actually the whole module is built-in, so there's no sys.py anywhere. The sys module has a list that contains all places that modules are searched from:

```python

>>> import sys
>>> sys
<module 'sys' (built-in)>
>>> sys.path
['',
 '/usr/lib/python37.zip',
 '/usr/lib/python3.7',
 '/usr/lib/python3.7/lib-dynload',
 '/home/akuli/.local/lib/python3.7/site-packages',
 '/usr/local/lib/python3.7/dist-packages',
 '/usr/lib/python3/dist-packages']
>>>

```

