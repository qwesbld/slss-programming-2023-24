A list in Python is a collection of items We can store *different* values in a list **Order matters** in a list
# Creating A List
To make a list we use brackets [ ] to surround our list we separate out the items using , 

```python
some_list = ["John", "Tim", "Sara"]
```

# Access Elements in a List
We can grab things from lists using the bracket notation
In our example above, if i wanted to access "Tim", I would do the following

```python
some_list [1] #"Tim"
some_list [2] #"Sara"
some_list [-1] #"Sara"
some_list [-2] #"Tim"
```

Inside the brackets, we say the index of the *value* we want 
Python uses 0-index counting, which means we start counting at 0

# Modules
Modules are bits of code that we can use in Python 
These bits of code aren't automatically included, so 
we need to import them into our code

# The time module
Time allows us to play around with anything related to time We can pause our code using time
```python
import time
```