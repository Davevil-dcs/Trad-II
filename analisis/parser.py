import re
from lexer import analizador_lexico
from lista import lis



no_terminales = ["programa","Definiciones","Definicion","DefVar","ListaVar","DefFunc","Parametros","ListaParam","BloqFunc","DefLocales","DefLocal","Sentencias","Sentencia","Otro","Bloque","ValorRegresa","Argumentos","ListaArgumentos","Termino","LlamadaFunc","SentenciaBloque","Expresion"]

arbol =[]

codigo = 'int main(int a){}'

resultado, analisis_correcto = analizador_lexico(codigo)
patron = r'-> (\d+),'
valores_numericos_str = re.findall(patron, resultado)


cadena = [int(val) for val in valores_numericos_str]
cadena.append(23) #24 tokens y 22 no terminales

print(resultado)
print(cadena)

pila = [0]
apregla = 0

while True:
    accion = lis[pila[-1]][cadena[0]]
    apregla = accion
    #print(pila)
    if accion>0:
        
        pila.append(cadena[0])
        pila.append(accion)
    
    if accion == 0:
        print("Error de sintaxis")
        break
    #Tenemos del -2 al -53 para 52 reglas
    #programa inicia en 24
    elif accion < 0:
        #print("Realizando reduccion")
        if accion==-53:
            pila.pop()
            pila.pop()
            pila.append(45)
        elif accion==-52:
            for _ in range(6):
                pila.pop()
            pila.append(45)
        elif accion==-51:
            for _ in range(6):
                pila.pop()
            pila.append(45)
        elif accion==-50:
            for _ in range(6):
                pila.pop()
            pila.append(45)
        elif accion==-49:
            for _ in range(6):
                pila.pop()
            pila.append(45)
        elif accion==-48:
            for _ in range(6):
                pila.pop()
            pila.append(45)
        elif accion==-47:
            for _ in range(6):
                pila.pop()
            pila.append(45)
        elif accion==-46:
            for _ in range(4):
                pila.pop()
            pila.append(45)
        elif accion==-45:
            for _ in range(4):
                pila.pop()
            pila.append(45)
        elif accion==-44:
            for _ in range(6):
                pila.pop()
            pila.append(45)
        elif accion==-43:
            pila.pop()
            pila.pop()
            pila.append(44)
        elif accion==-42:
            pila.pop()
            pila.pop()
            pila.append(44)
        elif accion==-41:
            for _ in range(8):
                pila.pop()
            pila.append(43)
        elif accion==-40:
            pila.pop()
            pila.pop()
            pila.append(42)
        elif accion==-39:
            pila.pop()
            pila.pop()
            pila.append(42)
        elif accion==-38:
            pila.pop()
            pila.pop()
            pila.append(42)
        elif accion==-37:
            pila.pop()
            pila.pop()
            pila.append(42)
        elif accion==-36:
            pila.pop()
            pila.pop()
            pila.append(42)
        elif accion==-35:
            for _ in range(6):
                pila.pop()
            pila.append(41)
        elif accion==-34:
            pila.append(41)
        elif accion==-33:
            for _ in range(4):
                pila.pop()
            pila.append(40)
        elif accion==-32:
            pila.append(40)
        elif accion==-31:
            pila.pop()
            pila.pop()
            pila.append(39)
        elif accion==-30:
            pila.append(39)
        elif accion==-29:
            for _ in range(6):
                pila.pop()
            pila.append(38)
        elif accion==-28:
            for _ in range(4):
                pila.pop()
            pila.append(37)
        elif accion==-27:
            pila.append(37)
        elif accion==-26:
            for _ in range(4):
                pila.pop()
            pila.append(36)
        elif accion==-25:
            for _ in range(6):
                pila.pop()
            pila.append(36)
        elif accion==-24:
            for _ in range(10):
                pila.pop()
            pila.append(36)
        elif accion==-23:
            for _ in range(12):
                pila.pop()
            pila.append(36)
        elif accion==-22:
            for _ in range(8):
                pila.pop()
            pila.append(36)
        elif accion==-21:
            for _ in range(4):
                pila.pop()
            pila.append(35)
        elif accion==-20:
            pila.append(35)
        elif accion==-19:
            pila.pop()
            pila.pop()
            pila.append(34)
        elif accion==-18:
            pila.pop()
            pila.pop()
            pila.append(34)
        elif accion==-17:
            for _ in range(4):
                pila.pop()
            pila.append(33)
        elif accion==-16:
            pila.append(33)
        elif accion==-15:
            for _ in range(6):
                pila.pop()
            pila.append(32)
        elif accion==-14:
            for _ in range(8):
                pila.pop()
            pila.append(31)
        elif accion==-13:
            pila.append(31)
        elif accion==-12:
            for _ in range(6):
                pila.pop()
            pila.append(30)
        elif accion==-11:
            pila.append(30)
        elif accion==-10:
            for _ in range(12):
                pila.pop()
            pila.append(29)
        elif accion==-9:
            for _ in range(6):
                pila.pop()
            pila.append(28)
        elif accion==-8:
            pila.append(28)
        elif accion==-7:
            for _ in range(8):
                pila.pop()
            pila.append(27)
        elif accion==-6:
            pila.pop()
            pila.pop()
            pila.append(26)
        elif accion==-5:
            pila.pop()
            pila.pop()
            pila.append(26)
        elif accion==-4:
            for _ in range(4):
                pila.pop()
            pila.append(25)
        elif accion==-3:
            pila.append(25)
        elif accion==-2:
            pila.pop()
            pila.pop()
            pila.append(24)
        elif accion==-1:
            arbol.reverse()
            print("\n".join(arbol))
            print("Cadena aceptada")
            break
        #print(no_terminales[pila[-1]-24])
        arbol.append(no_terminales[pila[-1]-24])
        accion = lis[pila[-2]][pila[-1]]
        pila.append(accion)
        accion = lis[pila[-1]][cadena[0]]
        
        if accion==0:
            print("Error")
            break
    if cadena[0]!=23 and apregla >0:
        cadena.pop(0)