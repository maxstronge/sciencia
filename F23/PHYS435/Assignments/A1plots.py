import sympy as sym
from sympy import pi

x =  sym.symbols('x')

y = sym.Piecewise((0, -pi<= x < 0), (sym.sin(x), 0 < x <= pi))

# plot y as a function of x

sym.plot(y, (x, -pi, pi), xlabel = '$x$', ylabel = '$y$', title = 'Plot of $y = f(x)$')

