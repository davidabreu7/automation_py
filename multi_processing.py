from concurrent import futures
import time

def factorize_naive(n):
    """ A naive factorization method. Take integer 'n', return list of
        factors.
    """
    if n < 2:
        return []
    factors = []
    p = 2

    while True:
        if n == 1:
            return factors

        r = n % p
        if r == 0:
            factors.append(p)
            n = n // p
        elif p * p >= n:
            factors.append(n)
            return factors
        elif p > 2:
            # Advance in steps of 2 over odd numbers
            p += 2
        else:
            # If p == 2, get to 3
            p += 1
    assert False, "unreachable"


def pool_factorizer_map(nums, nprocs):
    executor = futures.ProcessPoolExecutor
    # Let the executor divide the work among processes by using 'map'.
    with executor(max_workers=nprocs) as executor:
        return {num:factors for num, factors in
                                zip(nums,
                                    executor.map(factorize_naive, nums))}



t1 = time.perf_counter()
print(pool_factorizer_map(range(1000), 2))
t2 = time.perf_counter()

print(t2-t1)