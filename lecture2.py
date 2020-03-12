def prosta_iterace(fce,x0,number,tol):

    #from scipy import linalg
    import numpy
    iter = 0
    x = x0
    chyba = 1.e10
    while (iter<number) and (chyba > tol):
        x_new = fce(x)
        chyba = numpy.abs(x_new - x)
        x=x_new
        iter = iter + 1
        print(iter,x,chyba)
    return x, chyba

def Newtonova_metoda(fce,fce_der,x0,number,tol):

    #from scipy import linalg
    import numpy
    iter = 0
    x = x0
    chyba = 1.e10
    while (iter<number) and (chyba > tol):
        x_new = x - fce(x)/fce_der(x)
        chyba = numpy.abs(x_new - x)
        x=x_new
        iter = iter + 1
        print(iter,x,chyba)
    return x, chyba


def fce1(x):
    
    return (x + 2./x)/2.

def fce2(x):
    
    import numpy
    return numpy.sin(x)

def fce3(x):
    
    import numpy
    return numpy.sin(x)

def fce4(x):
    
    return (9. * x ** 2. - 7. * x - 5.)**(1./3.)

def fce5(x):
    
    return x ** 3 - 9. * x ** 2. + 7. * x + 5.

def fce5_der(x):
    
    return 3. * x ** 2. - 18. * x + 7.
