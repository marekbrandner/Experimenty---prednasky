def nejvetsi_spad(A, b, x, eps, max_pocet_iteraci):

    import numpy
    err = 1.
    pocet_iteraci = 1
    n = numpy.size(A, 1)
    x_new = x.copy()
    while (err > eps) and (pocet_iteraci < max_pocet_iteraci):
        r = b - A @ x
        t = (r.conj().T @ r) / (r.conj().T @ A @ r)
        x_new = x + t * r
        err = numpy.linalg.norm(x_new - x)
        print(pocet_iteraci, err)
        pocet_iteraci = pocet_iteraci + 1
        x = x_new.copy()
    return x, pocet_iteraci, err

def sdruzene_gradienty(A, b, x, eps, max_pocet_iteraci):

    import numpy
    err = 1.
    pocet_iteraci = 1
    n = numpy.size(A, 1)
    x_new = x.copy()
    r = b - A @ x
    s = r.copy()
    while (err > eps) and (pocet_iteraci < max_pocet_iteraci):
        t = (s.conj().T @ r) / (s.conj().T @ A @ s)
        x_new = x + t * s
        r = r - t * A @ s
        Beta = (s.conj().T @ A @ r) / (s.conj().T @ A @ s)
        s = r - Beta * s
        err = numpy.linalg.norm(x_new - x)
        print(pocet_iteraci, err)
        pocet_iteraci = pocet_iteraci + 1
        x = x_new.copy()
    return x, pocet_iteraci, err

def uloha1(n):
    from scipy import linalg
    import numpy
    A = linalg.hilbert(n)
    xexact = numpy.ones((n, 1))
    b = A.dot(xexact)
    return A, b
    

def uloha2():
    from scipy import linalg
    import numpy
    A = numpy.array([[2.,-1.], [-1.,2.]])
    xexact = numpy.ones((2, 1))
    b = A.dot(xexact)
    x=numpy.array([[0.],[0.]])
    return A, b, x

def uloha3(n):
    from scipy import linalg
    import numpy
    xexact = numpy.ones((n, 1))
    pom = numpy.ones((n-1, 1))
    A = 2. * numpy.eye(n) - numpy.diagflat(pom,-1) - numpy.diagflat(pom,1)
    b = A.dot(xexact)
    x=numpy.zeros((n,1))
    return A, b, x