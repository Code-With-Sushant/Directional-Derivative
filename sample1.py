import sympy as smp # type: ignore
import math as math

x,y,z = smp.symbols('x y z',real=True)
f = y**2 - x*y*z

a = int(input("Enter i: "))
b = int(input("Enter j: "))
c = int(input("Enter k: "))

a1 = int(input("Enter i1: "))
b1 = int(input("Enter j1: "))
c1 = int(input("Enter k1: "))


dfdx=smp.diff(f,x) #first derivative wrt x
dfdy=smp.diff(f,y) #first derivative wrt y
dfdz=smp.diff(f,z) #first derivative wrt z

# f1 = dfdx * "i" + dfdy * "j" + dfdz * "k"
# f2 = a * "i" + b * "j" + c * "k"
dfdx = dfdx.subs([(x,a1),(y,b1),(z,c1)]).evalf()
dfdy = dfdy.subs([(x,a1),(y,b1),(z,c1)]).evalf()
dfdz = dfdz.subs([(x,a1),(y,b1),(z,c1)]).evalf()

print(dfdx,dfdy,dfdz)

f2d = math.sqrt(a*a + b*b + c*c)
print(f2d)
dd1 = dfdx * a
dd2 = dfdy * b
dd3 = dfdz * c
print("dd1+dd2+dd3: ",dd1+dd2+dd3)
dd = (dd1 + dd2 + dd3)/f2d
print ("DD :",dd)