from lexer import analizador_lexico

# PARSER RECURSIVO DESCENDENTE

def parser(resultado_lexer):
    lineas = [linea.strip() for linea in resultado_lexer.split("\n") if linea.strip()]
    tokens = []
    for linea in lineas:
        if "->" in linea and "," in linea:
            try:
                numero = int(linea.split("->")[1].split(",")[0].strip())
                tokens.append(numero)
            except:
                pass

    pos = 0

    def actual():
        if pos < len(tokens):
            return tokens[pos]
        return None

    def avanzar():
        nonlocal pos
        pos += 1

    def coincidir(token):
        nonlocal pos
        if actual() == token:
            print("PILA:", pila())
            avanzar()
        else:
            print("ERROR SINTACTICO, se esperaba", token, "y se encontró", actual())
            raise SystemExit

    def pila():
        return f"[{', '.join(map(str, tokens[pos:]))}]"

    def programa():
        print("PILA:", pila())
        definiciones()
        # Si ya consumimos todos los tokens (EOF implícito) o estamos en un token EOF explícito (23) -> ACEPTACION
        if pos >= len(tokens) or actual() == 23:
            print("ACEPTACION")
        else:
            print("ERROR: no se alcanzó EOF")

    def definiciones():
        print("PILA:", pila())
        if actual() in [4]:  # tipo
            definicion()
            definiciones()
        else:
            pass

    def definicion():
        print("PILA:", pila())
        if actual() == 4:
            temp = tokens[pos + 2] if pos + 2 < len(tokens) else None
            if temp == 14:
                defFunc()
            else:
                defVar()

    def defVar():
        print("PILA:", pila())
        coincidir(4)       # tipo
        coincidir(0)       # identificador
        # Inicialización opcional
        if actual() == 18: # =
            coincidir(18)
            expresion()
        listaVar()
        coincidir(12)      # ;

    def listaVar():
        print("PILA:", pila())
        if actual() == 13:
            coincidir(13)
            coincidir(0)
            listaVar()
        else:
            pass

    def defFunc():
        print("PILA:", pila())
        coincidir(4)
        coincidir(0)
        coincidir(14)
        parametros()
        coincidir(15)
        bloqFunc()

    def parametros():
        print("PILA:", pila())
        if actual() == 4:
            coincidir(4)
            coincidir(0)
            listaParam()
        else:
            pass

    def listaParam():
        print("PILA:", pila())
        if actual() == 13:
            coincidir(13)
            coincidir(4)
            coincidir(0)
            listaParam()
        else:
            pass

    def bloqFunc():
        print("PILA:", pila())
        coincidir(16)
        defLocales()
        coincidir(17)

    def defLocales():
        print("PILA:", pila())
        if actual() in [4, 0, 19, 20, 21]:
            defLocal()
            defLocales()
        else:
            pass

    def defLocal():
        print("PILA:", pila())
        if actual() == 4:
            defVar()
        else:
            sentencia()

    def sentencias():
        print("PILA:", pila())
        if actual() in [0, 19, 20, 21]:
            sentencia()
            sentencias()
        else:
            pass

    def sentencia():
        print("PILA:", pila())
        if actual() == 0:
            coincidir(0)
            coincidir(18)
            expresion()
            coincidir(12)
        elif actual() == 19:
            coincidir(19)
            coincidir(14)
            expresion()
            coincidir(15)
            sentenciaBloque()
            otro()
        elif actual() == 20:
            coincidir(20)
            coincidir(14)
            expresion()
            coincidir(15)
            bloque()
        elif actual() == 21:
            coincidir(21)
            valorRegresa()
            coincidir(12)
        else:
            llamadaFunc()
            coincidir(12)

    def otro():
        print("PILA:", pila())
        if actual() == 22:
            coincidir(22)
            sentenciaBloque()
        else:
            pass

    def bloque():
        print("PILA:", pila())
        coincidir(16)
        sentencias()
        coincidir(17)

    def valorRegresa():
        print("PILA:", pila())
        if actual() in [0, 1, 2, 3, 5, 7, 9, 10, 14]:
            expresion()
        else:
            pass

    def argumentos():
        print("PILA:", pila())
        if actual() in [0, 1, 2, 3, 5, 7, 9, 10, 14]:
            expresion()
            listaArgumentos()
        else:
            pass

    def listaArgumentos():
        print("PILA:", pila())
        if actual() == 13:
            coincidir(13)
            expresion()
            listaArgumentos()
        else:
            pass

    def termino():
        print("PILA:", pila())
        if actual() == 0:
            temp = tokens[pos + 1] if pos + 1 < len(tokens) else None
            if temp == 14:
                llamadaFunc()
            else:
                coincidir(0)
        elif actual() in [1, 2, 3]:
            coincidir(actual())
        else:
            print("ERROR en termino, encontrado:", actual())
            raise SystemExit

    def llamadaFunc():
        print("PILA:", pila())
        coincidir(0)
        coincidir(14)
        argumentos()
        coincidir(15)

    def sentenciaBloque():
        print("PILA:", pila())
        if actual() == 16:
            bloque()
        else:
            sentencia()

    def expresion():
        print("PILA:", pila())
        if actual() == 14:
            coincidir(14)
            expresion()
            coincidir(15)
        elif actual() == 5:
            coincidir(5)
            expresion()
        elif actual() == 10:
            coincidir(10)
            expresion()
        elif actual() in [0, 1, 2, 3]:
            termino()
            if actual() in [6, 5, 7, 11, 9, 8]:
                op = actual()
                coincidir(op)
                expresion()
        else:
            print("ERROR en expresion, encontrado:", actual())
            raise SystemExit

    programa()

codigo = 'int elote = 12;'

resultado, analisis_correcto = analizador_lexico(codigo)

if analisis_correcto:
    parser(resultado)
else:
    print("Error léxico")

