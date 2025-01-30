# maybe make this a python package?
import sympy
import eqbuilder
t = eqbuilder.SingleTerm(eqbuilder.Variable('x'), coefficient=2)
ex = eqbuilder.Expression([t])
eqbuilder.Function.Sine(ex)
ex = eqbuilder.SingleTerm(ex, degree=2)
t2 = eqbuilder.SingleTerm(eqbuilder.Variable('x'), degree=3)
ex2 = eqbuilder.Expression([t2])
eqbuilder.Function.Cosine(ex2)
ex2 = eqbuilder.SingleTerm(ex2, degree=2)

m = eqbuilder.Expression([t*t2])
eqbuilder.Function.Sine(m)
eqbuilder.Function.Cosine(m)
ms = m.simplify()
pms = eqbuilder.sympy.poly(ms)
print(eqbuilder.sympy_to_eqbuilder(pms))
print('simple docomposition')
print(eqbuilder.decompose_simple_poly(pms))
e = eqbuilder.Expression([t])
eqbuilder.Function.Sine(e)
e = eqbuilder.Expression([e, t2])
eqbuilder.Function.Cosine(e)
pe = eqbuilder.sympy.poly(e.simplify())
print(eqbuilder.sympy_to_eqbuilder(pe))
# print(help(ms))
# print(ms.args[0].args)
# c = ms.args[0].args
# a = eqbuilder.sympy.Poly(ms)
# print(eqbuilder.sympy.Poly(c[0]).degree())
# print(eqbuilder.sympy.Poly(c[0]).coeffs())
# # print(a.functions())
# b = eqbuilder.sympy.Add.make_args(a)
# print(b)

# https://docs.sympy.org/latest/modules/functions/elementary.html#trigonometric