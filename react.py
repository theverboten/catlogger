from rx import create, of, operators as op
import random

test = of("Hello", "World")
sub = test.pipe(
    op.map(lambda a: a+" 2")
)

print("From test:")
subscriber = sub.subscribe(lambda i: print("String is {0}".format(i)))

# "Hello", "World"
