#import scipy
#from scipy import linalg
#import numpy
 

def residuum(n):

    from scipy import linalg
    import numpy
    A = linalg.hilbert(n)
    xexact = numpy.ones((n, 1))
    b = A.dot(xexact)
    xcomp = linalg.solve(A, b)
    residuum = b - A.dot(xcomp)
    print("x computed")
    print(xcomp)
    print("residuum")
    print(residuum)
    error = xcomp - xexact
    print("error")
    print(error)
    print("condition number")
    condition_number = numpy.linalg.cond(A)
    print(condition_number)
    print("eigenvalues")
    eigenvalues, eigenvectors = numpy.linalg.eig(A)
    print(eigenvalues)
    output = 0
    return output

def J_integral(n):

    import numpy
    J = numpy.log(6./5.)
    for i in range(1, n+1, 1):
        J = -5 * J + 1. / i
        print("i = % 3d, J = % 5.10f" % (i, J))
    return J

def J_integral_mod(n):

    J = 0.
    for i in range(1000, n, -1):
        J = -1./5. * J + 1. / 5./i
        print("i = % 3d, J = % 5.10f" % (i-1, J))
    return J
