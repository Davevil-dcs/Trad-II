# base_parser.py
class BaseParser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def token_actual(self):
        """Devuelve el token actual sin avanzar."""
        if self.pos < len(self.tokens):
            return self.tokens[self.pos]
        return ("$", 23)  # Indicador de fin de entrada

    def avanzar(self):
        """Avanza al siguiente token."""
        if self.pos < len(self.tokens):
            self.pos += 1

    def match(self, esperado):
        """
        Compara el token actual con el tipo esperado.
        Si coincide, avanza; si no, lanza error.
        """
        lexema, tipo = self.token_actual()
        if tipo == esperado:
            print(f"[OK] Match: {lexema}")
            self.avanzar()
        else:
            self.error(f"Se esperaba token tipo {esperado}, pero se encontró '{lexema}'")

    def coincide(self, tipo):
        """Devuelve True si el token actual coincide con el tipo dado."""
        _, tipo_actual = self.token_actual()
        return tipo_actual == tipo

    def fin(self):
        """Indica si ya se llegó al final de la lista de tokens."""
        return self.pos >= len(self.tokens)

    def error(self, mensaje):
        """Lanza un error sintáctico con contexto."""
        lexema, tipo = self.token_actual()
        raise SyntaxError(f"Error en posición {self.pos} (token '{lexema}', tipo {tipo}): {mensaje}")
