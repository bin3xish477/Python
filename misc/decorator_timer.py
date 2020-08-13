#!/usr/bin/env python3

# decorator
def timed(fn):
    from time import perf_counter
    from functools import wraps

    # closure
    @wraps(fn)
    def inner(*args, **kwargs):
        start = perf_counter()
        result = fn(*args, **kwargs)
        end = perf_counter()
        elapsed = end - start

        args_ = [str(a) for a in args]
        kwargs_ = [f'{k}={v}' for (k,v) in kwargs.items()]
        all_args = args_ + kwargs_
        args_str = ','.join(all_args)

        print(f'{fn.__name__}({args_str}) took {elapsed:.6f}s to run')

        return result
    return inner

# generating fibonacci sequence using recursion
def recur_fibo(n: int) -> int:
    if n <= 2:
        return 1
    else:
        return recur_fibo(n-2) + recur_fibo(n-1)

@timed
def recur_fib_call(n):
    return recur_fibo(n)

recur_fib_call(20)


# generating fibonacci sequence with a loop
@timed
def loop_fibo(n: int) -> int:
    fib_1, fib_2 = 1, 1
    for i in range(3, n + 1):
        fib_1, fib_2 = fib_2, fib_1 + fib_2
    return fib_2

loop_fibo(20)


# generating fibonacci sequence using reduce
@timed
def reduce_fibo(n: int):
    from functools import reduce
    initial = (1, 0)
    dummy = range(n)
    fib_n = reduce(lambda prev, n: (prev[0] + prev[1], prev[0]), dummy, initial)

    return fib_n[0]

reduce_fibo(20)