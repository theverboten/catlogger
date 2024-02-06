from rx import Observable


def print_value(value):
    print("{} is the value. ".format(value))


Observable(["abc", "def", "ghi"])\
    .subscribe(print_value)

Observable.interval(1) \
    .sample(3) \
    .subscribe(print_value)
