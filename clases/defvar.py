from ..base_parser import BaseParser

class DefVar(BaseParser):
    def parse(self):
        """
        <DefVar> ::= tipo identificador <ListaVar> ;
        <ListaVar> ::= ε | , identificador <ListaVar>
        (Versión extendida: permite inicializaciones)
        """

        # 1️⃣ Verificar tipo
        if self.current_token is None or self.current_token[0] not in ["int", "float", "char", "void"]:
            print("❌ Error: se esperaba un tipo de dato en <DefVar>")
            return False, self.pos

        tipo = self.current_token[0]
        self.advance()

        # 2️⃣ Verificar primer identificador
        if self.current_token is None or self.current_token[1] != 0:
            print("❌ Error: se esperaba identificador después del tipo en <DefVar>")
            return False, self.pos

        variables = []
        ident = self.current_token[0]
        self.advance()

        # 3️⃣ Verificar si hay inicialización (= expresión)
        valor = None
        if self.current_token and self.current_token[0] == "=":
            self.advance()
            if self.current_token and self.current_token[1] in [0, 1, 2, 3]:  # id, entero, real, cadena
                valor = self.current_token[0]
                self.advance()
            else:
                print("❌ Error: se esperaba una expresión después de '=' en <DefVar>")
                return False, self.pos
        variables.append((ident, valor))

        # 4️⃣ Leer posibles más variables (, id [= expr])
        while self.current_token and self.current_token[0] == ",":
            self.advance()
            if self.current_token is None or self.current_token[1] != 0:
                print("❌ Error: se esperaba identificador después de ',' en <ListaVar>")
                return False, self.pos

            ident = self.current_token[0]
            self.advance()
            valor = None
            if self.current_token and self.current_token[0] == "=":
                self.advance()
                if self.current_token and self.current_token[1] in [0, 1, 2, 3]:
                    valor = self.current_token[0]
                    self.advance()
                else:
                    print("❌ Error: se esperaba expresión después de '=' en <ListaVar>")
                    return False, self.pos

            variables.append((ident, valor))

        # 5️⃣ Verificar punto y coma
        if self.current_token is None or self.current_token[0] != ";":
            print("❌ Error: se esperaba ';' al final de <DefVar>")
            return False, self.pos

        print(f"✅ Declaración reconocida correctamente:")
        for v, val in variables:
            if val is not None:
                print(f"   - {tipo} {v} = {val}")
            else:
                print(f"   - {tipo} {v}")

        return True, self.pos
