TABLA_TOKENS = {
    'int':4, # Tipo
    'float':4,
    'char':4,
    'void':4,
    '+':5, # Operador suma
    '-':5,
    '*':6, # Operador multiplicacion
    '/':6, 
    '<':7, # Operador relacional
    '<=':7,
    '>=':7,
    '>':7,
    'opOR':8, # Operador OR
    '&&':9, # Operador AND
    '!':10, # Operador NOT
    '==':11, # Operador Igualdad
    '!=':11, 
    ';':12, # Punto y coma
    ',':13, # Coma
    '(':14, # Parentesis (apertura)
    ')':15, # Parentesis (cierre)
    '{':16, # Corchete (apertura)
    '}':17, # Corchete (cierre)
    '=':18, # Operador asignacion
    'if':19, # if
    'while':20, #while
    'return':21, #return
    'else':22, #else
    #'$':23,#Solo se incluye al final de las cadenas para indicar el final
    'error':-1 # Error
}

def lexer(cadena):
    tokens = []
    i = 0
    while i < len(cadena):
        c = cadena[i]

        # Ignorar espacios
        if c.isspace():
            i += 1
            continue

        #Identicadores/palabras reservadas/tipos
        if c.isalpha() or c == '_':
            lexema = c
            i += 1
            while i < len(cadena) and (cadena[i].isalnum() or cadena[i] == '_'):
                lexema += cadena[i]
                i += 1

            if lexema in TABLA_TOKENS:
                tokens.append((lexema, TABLA_TOKENS[lexema]))
            else:
                tokens.append((lexema, 0))  # Identificador
            continue

        #Números (enteros / reales)
        if c.isdigit():
            lexema = c
            i += 1
            es_real = False
            while i < len(cadena) and (cadena[i].isdigit() or cadena[i] == '.'):
                if cadena[i] == '.':
                    if es_real:  # segundo punto = error
                        break
                    es_real = True
                lexema += cadena[i]
                i += 1

            tokens.append((lexema, 2 if es_real else 1))
            continue

        # --- Cadenas ---
        if c == '"':
            lexema = c
            i += 1
            while i < len(cadena) and cadena[i] != '"':
                lexema += cadena[i]
                i += 1
            if i < len(cadena):
                lexema += '"'  # cerrar comillas
                i += 1
            tokens.append((lexema, 3))
            continue

        # --- Operadores y símbolos ---
        # Intentar leer de 2 caracteres primero (ej: <=, >=, ==, !=, &&, ||)
        if i + 1 < len(cadena) and cadena[i:i+2] in TABLA_TOKENS:
            lexema = cadena[i:i+2]
            tokens.append((lexema, TABLA_TOKENS[lexema]))
            i += 2
            continue

        # De 1 carácter
        if c in TABLA_TOKENS:
            tokens.append((c, TABLA_TOKENS[c]))
            i += 1
            continue

        # Si nada coincidió → error
        tokens.append((c, -1))
        i += 1

    return tokens

print(lexer("void wacamole = 10; $"))
