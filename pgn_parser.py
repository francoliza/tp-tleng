import ply.lex as lex
import ply.yacc as yacc
import sys
from lexer import tokens


def p_start(p):
    '''
    start   : partida start
            | partida
    '''


def p_partida(p):
    '''
    partida     : metadata rondas RESULTADO
    '''


def p_metadata(p):
    '''
    metadata    : DESCRIPTOR metadata
                | DESCRIPTOR
    '''


def p_rondas(p):
    '''
    rondas  : comentario rondas
            | lambda
    '''
    # Si es un comentario se traslada el valor de la ronda por si ocurre antes de la primera jugada
    if len(p) > 2:
        p[0] = p[2]


def p_rondas_numero(p):
    '''
    rondas  : NUMERO_RONDA rondas
    '''
    # Si es la primera ronda se cuenta el valor de la jugada
    if p[1].strip() == '1.':
        global primeras_jugadas
        primeras_jugadas[p[2]] = primeras_jugadas.get(p[2], 0) + 1


def p_rondas_jugada(p):
    '''
    rondas  : JUGADA rondas
    '''
    # p[1][1] guarda el nivel de anidamiento de la jugada, si es mayor al maximo se actualiza
    global max_level
    if p[1][1] > max_level:
        max_level = p[1][1]
    # se guarda la jugada en la ronda
    p[0] = p[1][0]


def p_comentario(p):
    '''
    comentario  : PARENTESIS_IZQ rondas PARENTESIS_DER
                | LLAVES_IZQ rondas LLAVES_DER
    '''


def p_lambda(p):
    '''
    lambda :
    '''
    pass


def p_error(p):
    if p.type == 'DESCRIPTOR':
        print('No se encontro un resultado para la partida!')
    else:
        print("Error de analisis!")

# Variables globales

# Maximo nivel de anidamiento para comentario con jugada
max_level = 0

# Contador de las primeras jugadas, guarda <string, int>
primeras_jugadas = {}

if __name__ == '__main__':
    s = ''
    for line in sys.stdin:
        s += line

    parser = yacc.yacc()
    parser.parse(s)

    if len(primeras_jugadas) > 0:
        print('Primera jugada mas repetida:', max(primeras_jugadas, key=primeras_jugadas.get))
    print('Maximo nivel de anidamiento de comentario con jugada:', max_level)
