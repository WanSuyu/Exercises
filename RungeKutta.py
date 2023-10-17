# using RK4 for the solution of Lane-Emden
# 2023/5/11  By Wan
def f(x,y,z):
    return z

def g(x,y,z,n):
    return -y**n-(2/x)*z

def RK_solve(x0,y0,z0,n,h):
    k1 = f(x0,y0,z0)
    l1 = g(x0,y0,z0,n)
    k2 = f(x0+h/2,y0+(h*k1)/2,z0+(h*l1)/2)
    l2 = g(x0+h/2,y0+(h*k1)/2,z0+(h*l1)/2,n)
    k3 = f(x0+h/2,y0+(h*k2)/2,z0+(h*l2)/2)
    l3 = g(x0+h/2,y0+(h*k2)/2,z0+(h*l2)/2,n)
    k4 = f(x0+h/2,y0+(h*k3)/2,z0+(h*l3)/2)
    l4 = g(x0+h/2,y0+(h*k1)/2,z0+(h*l3)/2,n)
    x1 = x0+h
    y1 = y0+(h/6)*(k1+2*k2+2*k3+k4)
    z1 = z0+(h/6)*(l1+2*l2+2*l3+l4)
    return x1, y1, z1

