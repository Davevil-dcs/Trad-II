from ..base_parser import BaseParser
from defvar import DefVar

class Programa(BaseParser):
    def parse(self):
        """
        <programa> ::= <DefVar> | ε
        (Versión inicial — luego podrá incluir <DefFunc> y otras reglas)
        """
        if self.current_token is None:
            print("✅ Programa vacío reconocido (ε)")
            return True

        # Si el token actual es un tipo → iniciar DefVar
        if self.current_token[0] in ["int", "float", "char", "void"]:
            print("Analizando definición de variable global...")
            def_var = DefVar(self.tokens, self.pos)
            success, new_pos = def_var.parse()
            if success:
                self.pos = new_pos
                self.advance()
                print("✅ Regla <Programa> reconocida correctamente\n")
                return True
            else:
                print("❌ Error al reconocer <DefVar> dentro de <Programa>")
                return False

        # Si no hay tokens reconocibles, se acepta vacío (ε)
        print("✅ Programa vacío reconocido (ε)")
        return True
