from functools import partial

def deprecated(f=None, *, since=None, will_be_removed=None):
    if f is None:
        return partial(deprecated, since=since, will_be_removed=will_be_removed)
    
    def inner(*args, **kwargs):
        print(f'Warning: function {f.__name__} is deprecated{f" since version {since}" if since else ""}. \
It will be removed in {f"version {will_be_removed}" if will_be_removed else "future versions"}. ')
        ret = f(*args, **kwargs)
        return ret
    return inner

@deprecated
def foo():
    print('Hello from foo')
# Warning: function foo is deprecated. It will be removed
# in future versions.
# Hello from foo

@deprecated(since="4.2.0", will_be_removed="5.0.1")
def bar():
    print('Hello form bar')
# Warning: function bar is deprecated since version 4.2.0.
# It will be removed in version 5.0.1.
# Hello from bar

foo()
bar()