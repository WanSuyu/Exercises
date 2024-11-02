import numpy as np
import matplotlib.pyplot as plt

def f(x,y,z):
    return z
def g(x,y,z,n):
    return -y**n-(2/x)*z
def RK4(x0,y0,z0,n):
    h=0.05 # length of step
    x_result = [x0]
    y_result = [y0]
    if n==0 or n==2:
        while y0>=-0.25:
            K0=f(x0,y0,z0)
            L0 = g(x0,y0,z0,n)
            K1 = f(x0+h/2,y0+h*K0/2,z0+h*L0/2)
            L1 = g(x0+h/2,y0+h*K0/2,z0+h*L0/2,n)
            K2 = f(x0+h/2,y0+h*K1/2,z0+h*L1/2)
            L2 = g(x0+h/2,y0+h*K1/2,z0+h*L1/2,n)
            K3 = f(x0+h,y0+h*K2,z0+h*L2)
            L3 = g(x0+h,y0+h*K2,z0+h*L2,n)
            x0+=h
            y0+=(K0+2*K1+2*K2+K3)*h/6
            z0+=(L0+2*L1+2*L2+L3)*h/6
            x_result.append(x0)
            y_result.append(y0)
    else:
        while x0<20:
            K0=f(x0,y0,z0)
            L0 = g(x0,y0,z0,n)
            K1 = f(x0+h/2,y0+h*K0/2,z0+h*L0/2)
            L1 = g(x0+h/2,y0+h*K0/2,z0+h*L0/2,n)
            K2 = f(x0+h/2,y0+h*K1/2,z0+h*L1/2)
            L2 = g(x0+h/2,y0+h*K1/2,z0+h*L1/2,n)
            K3 = f(x0+h,y0+h*K2,z0+h*L2)
            L3 = g(x0+h,y0+h*K2,z0+h*L2,n)
            x0+=h
            y0+=(K0+2*K1+2*K2+K3)*h/6
            z0+=(L0+2*L1+2*L2+L3)*h/6
            x_result.append(x0)
            y_result.append(y0)
    return x_result,y_result

plt.figure()
for i in np.arange(0,6,1):
    x,y = RK4(1e-10,1,0,i)
    plt.title('Numerical Solutions(Runge-Kutta)')
    plt.plot(x,y,label = 'n=%s'%i)
    plt.xlabel(r'$\xi$')
    plt.ylabel(r'$\theta$')
    plt.xlim(0,20)
    plt.legend()
plt.show()
