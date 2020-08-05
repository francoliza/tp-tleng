import ply.lex as lex
import ply.yacc as yacc
import sys

# mi lista de tockens
tokens = [
	'CORCHETE_IZQ',
	'CORCHETE_DER',
	'PARENTESIS_IZQ',
	'PARENTESIS_DER',
	'LLAVES_IZQ',
	'LLAVES_DER',
	'COMILLAS',
	'ESPACIO',
	'RONDA',
	'JUGADA',
	'RESULTADO',
	'CHAR'
]

t_CORCHETE_IZQ = r'\['
t_CORCHETE_DER = r'\]'
t_PARENTESIS_IZQ = r'\('
t_PARENTESIS_DER = r'\)'
t_LLAVES_IZQ = r'\{'
t_LLAVES_DER = r'\}'
t_COMILLAS = r'\"'
t_ESPACIO = r'\s'

#t_ignore = r' '

count = 0

def t_JUGADA(t):
	r'[PNBRQK]?[a-h]?[1-8]?x?[a-h][1-8](\+|\#)?|O-O|O-O-O'					#no sé muy bien a que se refiere
	
	return t

def t_RONDA(t):
	r'\d+(\.|\.\.\.)'
	return t

def t_RESULTADO(t):
	r'1-0|0-1|1/2-1/2'
	return t

def t_CHAR(t):
	r'[\S\s]'
	t.type = 'CHAR'
	return t

def t_error(t):
	print("caracteres ilegales")
	t.lexer.skip(1)


lexer = lex.lex()

def p_start(p):
	'''
	start 	: partida start 
			| partida 	
	'''

	print(p[1])


def p_partida(p):
	'''
	partida 	: metadata B

	'''
	p[0] = (p[2], p[1], p[3])

def p_metadata(p):
	'''
	metadata 	: A1 metadata 
				| A1

	'''

def p_A1(p):
	'''
	A1 		: CORCHETE_IZQ A2 ESPACIO COMILLAS A2 COMILLAS CORCHETE_DER

	'''

def p_A2(p):
	'''
	A2 		: CHAR A2
			| CHAR

	'''

def p_B(p):
	'''
	B 		: B1 RESULTADO

	'''

def p_B1(p):
	'''
	B1 		: RONDA JUGADA comentario JUGADA comentario B1	
			| RONDA JUGADA comentario  
			| lamda

	''' 		

def p_comentario(p):
	'''
	comentario 	: PARENTESIS_IZQ B5 PARENTESIS_DER
				| LLAVES_IZQ B5 LLAVES_DER
				| lamda

	'''

def p_B5(p):
	'''
	B5 		: texto comentario JUGADA B5
			| texto comentario B5
			| lamda 

	'''	

def p_texto(p):
	'''
	texto 	: CHAR texto
			| lamda

	'''

def p_lamda(p):
	'''
	lamda :
	'''
	pass

def p_error(p):
     print("Syntax error in input!")


parser = yacc.yacc()

s = """[Event "Renova Group Grand Prix 2013"] 
1. d4 d5 2. c4 c6 3. Nc3 1-0"""

#while True:
#	try:
#	except EOFError:
#		break

lexer.input(s)
 
 # Tokenize
while True:
	tok = lexer.token()
	if not tok:
		break			# No more input
	print(tok)


#parser.parse(s)
