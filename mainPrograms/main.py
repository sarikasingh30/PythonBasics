# --------------------------------------------------------------------------------------------------------
# Print value upto to 2 decimal places.
import textwrap
t = 40
print('{:.2f}'.format(t))
# --------------------------------------------------------------------------------------------------------
# to initialize empty set,string,dictionary,tuple
a = set()
b = tuple()
d = dict()
s = str()
print(a, b, d, s)
# --------------------------------------------------------------------------------------------------------
# Wrap the string into a paragraph of width .


def wrap(string, max_width):
    y = textwrap.fill(string, max_width)
    return y


string = "ABCDEFGHIJKLIMNOQRSTUVWXYZ"
max_width = 4
x = wrap(string, max_width)
print(x)
# --------------------------------------------------------------------------------------------------------
