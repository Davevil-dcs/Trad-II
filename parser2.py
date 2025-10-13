
from lexer import lexer
from base_parser import BaseParser


# Importaciones futuras:
# from clases.Programa import Programa
# from clases.Definiciones import Definiciones
# ... (y así hasta las 52 clases)

class Parser(BaseParser):
    def __init__(self, tokens):
        super().__init__(tokens)

    def parse(self):
        """
        Punto de entrada principal del parser.
        Aquí iniciarás el análisis invocando la primera producción.
        """
        print("Iniciando análisis sintáctico...")

        # Ejemplo (cuando tengas las clases):
        # programa = Programa(self)
        # programa.parse()

        print("Análisis sintáctico finalizado correctamente.")


if __name__ == "__main__":
    cadena = 'int num = 10;'
    tokens = lexer(cadena)
    print("Tokens generados:", tokens)

    parser = Parser(tokens)
    parser.parse()
