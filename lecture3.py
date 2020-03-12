def gem(A, b):
    from scipy import linalg
    import numpy
    xcomp = linalg.solve(A, b)
    print("reseni")
    print(xcomp)
    residuum = b - A.dot(xcomp)
    print("residuum")
    print(residuum)
    print("condition number")
    condition_number = numpy.linalg.cond(A)
    print(condition_number)

def lu_rozklad(A, b):
    from scipy import linalg
    import numpy
    P, L, U = linalg.lu(A)
    print("L")
    print(L)
    print("U")
    print(U)
    print("P")
    print(P)
    ycomp = linalg.solve(L, P.conj().T @ b)
    xcomp = linalg.solve(U, ycomp)
    print("reseni")
    print(xcomp)
    residuum = b - A.dot(xcomp)
    print("residuum")
    print(residuum)
    print("condition number")
    condition_number = numpy.linalg.cond(A)
    print(condition_number)
    
def qr_rozklad(A, b):
    from scipy import linalg
    import numpy
    Q, R = linalg.qr(A)
    print("Q")
    print(Q)
    print("R")
    print(R)
    ycomp = Q.conj().T @ b
    xcomp = linalg.solve(R, ycomp)
    print("reseni")
    print(xcomp)
    residuum = b - A.dot(xcomp)
    print("residuum")
    print(residuum)
    print("condition number")
    condition_number = numpy.linalg.cond(A)
    print(condition_number)

def jacobi(A, b, x, eps, max_pocet_iteraci):

    import numpy
    err = 1.
    pocet_iteraci = 1
    n = numpy.size(A, 1)
    x_new = x.copy()
    while (err > eps) and (pocet_iteraci < max_pocet_iteraci):
        for i in range(0, n, 1):
            x_new[i] = 1 / A[i][i] \
                * (b[i] - A[i][0:i:1] @ x[0:i:1]
                    - A[i][i+1:n:1] @ x[i+1:n:1])
        err = numpy.linalg.norm(x_new - x)
        print(pocet_iteraci, err)
        pocet_iteraci = pocet_iteraci + 1
        x = x_new.copy()
    return x, pocet_iteraci, err

def gauss_seidel(A, b, x, eps, max_pocet_iteraci):

    import numpy
    err = 1.
    pocet_iteraci = 1
    n = numpy.size(A, 1)
    x_new = x.copy()
    while (err > eps) and (pocet_iteraci < max_pocet_iteraci):
        for i in range(0, n, 1):
            x_new[i] = 1 / A[i][i] \
                * (b[i] - A[i][0:i:1] @ x_new[0:i:1]
                    - A[i][i+1:n:1] @ x[i+1:n:1])
        err = numpy.linalg.norm(x_new - x)
        print(pocet_iteraci, err)
        pocet_iteraci = pocet_iteraci + 1
        x = x_new.copy()
    return x, pocet_iteraci, err

def sor(A, b, x, eps, max_pocet_iteraci,omega):

    import numpy
    err = 1.
    pocet_iteraci = 1
    n = numpy.size(A, 1)
    x_new = x.copy()
    while (err > eps) and (pocet_iteraci < max_pocet_iteraci):
        for i in range(0, n, 1):
            x_pom = 1 / A[i][i] \
                * (b[i] - A[i][0:i:1] @ x_new[0:i:1]
                    - A[i][i+1:n:1] @ x[i+1:n:1])
            x_new[i] = (1 - omega) * x[i] + omega * x_pom
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