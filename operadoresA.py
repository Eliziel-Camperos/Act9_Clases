print("Actividad 9 clases v3")
print("Eliziel Camperos 22308051281159")

# zona de clases
class Operadores1159:
    def suma1159(self, E, C):
        s1159 = E + C
        print(f"La suma de {E} + {C} = {s1159}")

    def re1159(self, E, C):
        r1159 = E - C
        print(f"La resta de {E} - {C} = {r1159}")

    def mu1159(self, E, C):
        m1159 = E * C
        print(f"La multiplicación de {E} x {C} = {m1159}")

    def di1159(self, E, C):
        if C != 0:
            d1159 = E / C
            print(f"La división de {E} / {C} = {d1159}")
        else:
            print("Error: División por cero.")

    def mo1159(self, E, C):
        mo1159 = E % C
        print(f"El módulo de {E} % {C} = {mo1159}")

    def ex1159(self, E, C):
        ex1159 = E ** C
        print(f"{E} elevado a {C} = {ex1159}")

    def co1159(self, E, C):
        if C != 0:
            co1159 = E // C
            print(f"El cociente de {E} // {C} = {co1159}")
        else:
            print("Error: División por cero.")

# Zona de creación del objeto
operadorEli = Operadores1159()

# zona de objetos
print("Funciones de operaciones")
print("Suma")
operadorEli.suma1159(5, 4)
print("resta")
operadorEli.re1159(5, 4)
print("multiplicación")
operadorEli.mu1159(5, 4)
print("división")
operadorEli.di1159(5, 4)
print("Módulo")
operadorEli.mo1159(5, 4)
print("Exponente")
operadorEli.ex1159(5, 4)
print("cociente")
operadorEli.co1159(5, 4)
