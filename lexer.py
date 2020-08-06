import ply.lex as lex
import sys

tokens = [
    'DESCRIPTOR',
    'PARENTESIS_IZQ',
    'PARENTESIS_DER',
    'LLAVES_IZQ',
    'LLAVES_DER',
    'NUMERO_RONDA',
    'JUGADA',
    'RESULTADO',
]


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Un descriptor es lo que esta entre corchetes antes de cada partida, forma parte de la metadata
def t_DESCRIPTOR(t):
    r'\[\S+\s+\"[^\]]*\"\]'
    # Se inicializa el nivel de anidamiento en 0 antes de comenzar la partida
    t.lexer.level = 0
    return t


def t_PARENTESIS_IZQ(t):
    r'\('
    increase_level(t)
    t.value = t.lexer.level
    return t


def t_PARENTESIS_DER(t):
    r'\)'
    decrease_level(t)
    t.value = t.lexer.level
    return t


def t_LLAVES_IZQ(t):
    r'\{'
    increase_level(t)
    t.value = t.lexer.level
    return t


def t_LLAVES_DER(t):
    r'\}'
    decrease_level(t)
    t.value = t.lexer.level
    return t

# Reconoce cualquier jugada valida
def t_JUGADA(t):
    r'[PNBRQK]?[a-h]?[1-8]?x?[a-h][1-8](\+|\#)?|O-O|O-O-O'
    # En el valor del token se guarda la jugada junto a su nivel de anidamiento
    t.value = (t.value, t.lexer.level if hasattr(t.lexer, 'level') else 0)
    return t

# El numero de ronda terminado en . o...
def t_NUMERO_RONDA(t):
    r'\d+(\.|\.\.\.)\s'
    return t

# El resultado se debe encontrar al final del archivo o seguido de dos saltos de linea
def t_RESULTADO(t):
    r'(1-0|0-1|1/2-1/2)(\n\n|$)'
    # Para referenciar mas precisamente, se cuentan los saltos de linea (si llego al final del archivo ya no importa)
    t.lexer.lineno += 2
    # Si el nivel de anidamiento es mayor a cero, quedo algun comentario abierto
    if t.lexer.level > 0:
        print('Falta cerrar un comentario!')
    return t

# Todos los demas caracteres se ignoran
def t_error(t):
    t.lexer.skip(1)


def increase_level(t):
    if not hasattr(t.lexer, 'level'):
        t.lexer.level = 1
        return t
    t.lexer.level += 1
    return t


def decrease_level(t):
    if not hasattr(t.lexer, 'level'):
        print('Empieza cerrando comentario!')
        return t
    t.lexer.level -= 1
    if t.lexer.level < 0:
        print('Falta abrir un comentario!')
    return t

lexer = lex.lex()

# Se puede ejecutar esto para obtener info de debug mas detallada
if __name__ == '__main__':
    s = ''
    for line in sys.stdin:
        s += line
    
    lexer = lex.lex(debug=1)
    lexer.input(s)
    while True:
        tok = lexer.token()
        if not tok:
            break
        print(tok)