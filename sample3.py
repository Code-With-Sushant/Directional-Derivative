import sympy as smp # type: ignore
import math as math

x,y,z = smp.symbols('x y z',real=True)
f = x*y**2 + y*z**3 + z*x**2

a = int(input("Enter i: "))
b = int(input("Enter j: "))
c = int(input("Enter k: "))

a1 = 1
b1 = 1
c1 = 1

dfdx=smp.diff(f,x) #first derivative wrt x
dfdy=smp.diff(f,y) #first derivative wrt y
dfdz=smp.diff(f,z) #first derivative wrt z
 

dfdx = dfdx.subs([(x,a),(y,b),(z,c)]).evalf()
dfdy = dfdy.subs([(x,a),(y,b),(z,c)]).evalf()
dfdz = dfdz.subs([(x,a),(y,b),(z,c)]).evalf()

f2d = math.sqrt(a1*a1 + b1*b1 + c1*c1)
print(f2d)
dd1 = dfdx * a1
dd2 = dfdy * b1
dd3 = dfdz * c1
print(dd1+dd2+dd3)
dd = (dd1 + dd2 + dd3)/f2d
print (dd)
