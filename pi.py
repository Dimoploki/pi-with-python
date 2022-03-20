actual_pi = 3.141592653589793


def pi1(n: int):
    """Find pi by using the Gregory-Leibniz Series."""
    piover4 = 0
    sign = 1
    for i in range(n):
        piover4 += sign*(1/(2*i + 1))
        sign *= -1
    print(4 * piover4)


def pi2(n: int):
    """Find pi using the Nilakantha Series."""
    pi = 3
    sign = 1
    for i in range(2, n + 2):
        top = 2*i
        pi += 4/(sign*(top-2)*(top-1)*top)
        print(pi)
        sign *= -1


pi2(int(input("How many iterations? >>> ")))
