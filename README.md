# tp-tleng

## Instalar ply para python

https://www.dabeaz.com/ply/ la versión 3.11
Pararse donde se descargo el archivo y en una terminal tipear
```sh
$ tar -xzvf ply-3.11.tar.xz
$ cd ply-3.11/ply
$ sudo python3 install setup.py
```

## Ejecutar

Hay que correr el ejecutable **python3 pgn_parser.py** que lee de la entrada estandar. En la salida indica cual es la primera jugada mas repetida y el maximo nivel de anidamiento de comentario con jugada, de la siguiente manera:
```
Primera jugada mas repetida: d4 ( 31 veces )
Maximo nivel de anidamiento de comentario con jugada: 4
```

En caso de detectar algun error durante el analisis se indica antes con un comentario.

Para obtener info mas detallada del lexer se puede ejecutar con **python3 lexer.py**.
