import ply.lex as lex
import ply.yacc as yacc
import sys

# mi lista de tockens
tokens = [
	'INT',
	'FLOAT',
	'NOMBRE',
	'SUMA',
	'RESTA',
	'DIVISION',
	'MULTIPLICACION',
	'IGUAL'
]

t_SUMA = r'\+'
t_RESTA = r'\-'
t_MULTIPLICACION = r'\*'
t_DIVISION = r'\/'
t_IGUAL = r'\='

t_ignore = r' '

## por ejemplo cadenas del tipo 1.1, 2.4, etc
def t_FLOAT(t):
	r'\d+\.\d+'
	t.value = float(t.value)
	return t

def t_INT(t):
	r'\d+'
	t.value = int(t.value)
	return t

def t_NOMBRE(t):
	r'[a-zA-Z_][a-zA-Z_0-9]*'
	t.type = 'NOMBRE'
	return t

def t_error(t):
	print("caracteres ilegales")
	t.lexer.skip(1)


lexer = lex.lex()

def p_calculadora(p):
	'''
	calculadora : expresion
				| lamda 	
	'''

	print(p[1])


def p_expresion(p):
	'''
	expresion 	: expresion MULTIPLICACION expresion
				| expresion DIVISION expresion
				| expresion SUMA expresion
				| expresion RESTA expresion
	'''
	p[0] = (p[2], p[1], p[3])

def p_expresion_int_float(p):
	'''
	expresion 	: INT
				| FLOAT
	'''
	p[0] = p[1]

#no hace nada
def p_lamda(p):
	'''
	lamda :
	'''
	p[0] = None

parser = yacc.yacc()

while True:
	try:
		s = input('')
	except EOFError:
		break
	parser.parse(s)
