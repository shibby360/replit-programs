import sympy
import math
from sympy.parsing.sympy_parser import parse_expr
class Variable:
  def __init__(self, name):
    self.name = name
    self.sympy_symbol = sympy.Symbol(name)
  def __str__(self):
    return str(self.name)
    
class FunctionList:
  def __init__(self, funcs=[]):
    self.funcs = funcs
  def add_func(self, func):
    self.funcs.append(func)

class Function:
  class Sine:
    def __init__(self, arg):
      self.arg = arg
      self.arg.add_func(self)
    def __str__(self):
      return 'sin'
  class Cosine:
    def __init__(self, arg):
      self.arg = arg
      self.arg.add_func(self)
    def __str__(self):
      return 'cos'
  class Logarithm:
    def __init__(self, base, arg):
      self.arg = arg
      self.base = base
      self.arg.add_func(self)
    def __str__(self):
      return 'log_'+str(self.base)
  class NaturalLogarithm:
    def __init__(self, arg):
      self.arg = arg
      self.arg.add_func(self)
    def __str__(self):
      return 'ln'
  func_dict = {
    'sin':Sine,
    'cos':Cosine,
    'log':Logarithm,
    'ln':NaturalLogarithm
  }
      
class Constants:
  class PI:
    def __init__(self):
      pass
    def numerical(self):
      return math.pi
    def symbol(self):
      return 'π'
    def __str__(self):
      return 'PI'
  class E:
      def __init__(self):
        pass
      def numerical(self):
        return math.e
      def __str__(self):
        return 'E'
  
class SingleTerm:
  def __init__(self, term, coefficient=1, degree=1):
    self.degree = degree
    self.coefficient = coefficient
    self.term = term
  def __str__(self):
    return f'{str(self.coefficient)+"*" if self.coefficient != 1 else ""}{self.term}{"^"+str(self.degree) if self.degree != 1 else ""}'
  def __mul__(self, other):
    return MultipleTerms([self, other], mode='*')
  __rmul__ = __mul__

class MultipleTerms:
  def __init__(self, terms, coefficient=1, degree=1, mode='+'):
    self.degree = degree
    self.coefficient = coefficient
    self.terms = terms
    self.mode = mode
  def __str__(self):
    return f'{str(self.coefficient)+"*" if self.coefficient != 1 else ""}({self.mode.join([str(x) for x in self.terms])}){"^"+str(self.degree) if self.degree != 1 else ""}'

class Expression:
  def __init__(self, terms=[]):
    self.terms = terms
    self.functions = FunctionList([])
  def add_func(self, func):
    self.functions.add_func(func)
  def __str__(self):
    base_expr =  ' + '.join([str(x) for x in self.terms])
    newterm = base_expr
    for func in self.functions.funcs:
      newterm = str(func) + '(' + newterm + ')'
    return '(' + newterm + ')'
  def simplify(self):
    return sympy.simplify(parse_expr(sympy_str(self)))

class Equation:
  def __init__(self, lhexpr, rhexpr):
    self.sympy_eq = sympy.Eq(sympy.parsing.sympy_parser.parse_expr(sympy_str(lhexpr)), sympy.parsing.sympy_parser.parse_expr(sympy_str(rhexpr)))
  def solve(self):
    return sympy.solve(self.sympy_eq)

class Inequality:
  def __init__(self, lhexpr, ineq, rhexpr):
    pass

def sympy_str(obj):
  return str(obj).replace('^','**')

def decompose_simple_poly(sympy_poly):
  poly = sympy_poly.args[0]
  run = 1
  funclist = []
  while run:
    if poly.func.is_Function:
      funclist.append(poly.func)
      poly = poly.args[0]
    else:
      run = 0
  end = SingleTerm('x', sympy.poly(poly).coeffs()[0], sympy.poly(poly).degree())
  endexpr = Expression([end])
  for i in funclist[::-1]:
    Function.func_dict[str(i)](endexpr)
  return endexpr
  
def sympy_to_eqbuilder(sympy_poly):
  poly = sympy_poly.args[0]
  run = 1
  print('Poly: ' + str(poly))
  nargs = poly.args
  while run:
    print(poly.func)
    if poly.func.is_Function:
      if len(poly.args) > 0:
        nargs = []
        for i in poly.args:
          print("poly.args of i: " + str(i))
          nargs.append(
            decompose_simple_poly(sympy.poly(i)))
          print("nargs" + str(nargs))
          break
      poly = poly.args[0]
    else:
      run = 0
    print(poly)
    print()
  print(nargs)