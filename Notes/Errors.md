# Syntax Errors

> Syntax <=> Rules

# Semantic Errors

Semantic errors are much more challenging to squash

Semantic errors are where you code doesn't "mean" what you actually mean

# Format strings
we can use string methods to help solve [[]]

# .lower()


# upper ()

# .strip (chars)
the `.strip()` method **removes** characters from both beginning and end of the string

```python
user_feeling = input ("how are you feeling today?")

# "good!" "good." "Good"
if user_feeling.lower().strip("!.,") == "good":
	print("That's great!")
```

## `.split(str)`  ->
the `.split()` method splits a string into a [[List]], separating the string based on the character you give it.

```python
grocery_str = "eggs milk cheese hotwheels"

grocery_list = grocery_str.split(" ")
```



