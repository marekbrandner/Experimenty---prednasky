import numpy
import matplotlib.pyplot as plt
import lecture1

def pokus():
#    lecture1.residuum(10)
    t = numpy.arange(0., 10., 0.2)
    plt.plot(t, 1./numpy.tanh(t) - 1./t , 'r--')
    plt.show()
if __name__ == "__main__":
    pokus()