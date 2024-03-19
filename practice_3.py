import sympy

def least_squares_method(x, y, function) -> list:
    pass

x, y, a, b = sympy.symbols('x y a b', real=True)
f = ((a*x)+b-y)**2
print(sympy.diff(f, a))


f = (a*sympy.cos(2*x)+b*sympy.sin(x)-y)**2
print(sympy.diff(f, a))



x, y, z = sympy.symbols('x y z', real=True)
f = 4*x*y + x*sympy.sin(z) + x**3 + z**8*y
print(sympy.diff(f, x))









