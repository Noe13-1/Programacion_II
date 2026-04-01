import math

class AlgebraVectorial:
    
    def __init__(self, a1, a2, a3):
        self.a1 = a1
        self.a2 = a2
        self.a3 = a3

    def magnitud(self):
        return math.sqrt(self.a1**2 + self.a2**2 + self.a3**2)

    def suma(self, v):
        return AlgebraVectorial(self.a1 + v.a1,
                                self.a2 + v.a2,
                                self.a3 + v.a3)

    def resta(self, v):
        return AlgebraVectorial(self.a1 - v.a1,
                                self.a2 - v.a2,
                                self.a3 - v.a3)

    def producto_escalar(self, v):
        return self.a1*v.a1 + self.a2*v.a2 + self.a3*v.a3

    def producto_cruz(self, v):
        return AlgebraVectorial(
            self.a2*v.a3 - self.a3*v.a2,
            self.a3*v.a1 - self.a1*v.a3,
            self.a1*v.a2 - self.a2*v.a1
        )
    # (a) |a+b| = |a−b|
    def perpendicular_a(self, v):
        suma = self.suma(v).magnitud()
        resta = self.resta(v).magnitud()
        return suma == resta

    # (b) |a−b| = |b−a|
    def perpendicular_b(self, v):
        resta1 = self.resta(v).magnitud()
        resta2 = v.resta(self).magnitud()
        return resta1 == resta2

    # (c) a · b = 0
    def perpendicular_c(self, v):
        return self.producto_escalar(v) == 0

    # (d) |a+b|^2 = |a|^2 + |b|^2
    def perpendicular_d(self, v):
        suma2 = self.suma(v).magnitud()**2
        return suma2 == self.magnitud()**2 + v.magnitud()**2

    # (e) a = r·b
    def paralela_e(self, v):
        ratios = []
        if v.a1 != 0:
            ratios.append(self.a1 / v.a1)
        if v.a2 != 0:
            ratios.append(self.a2 / v.a2)
        if v.a3 != 0:
            ratios.append(self.a3 / v.a3)
        if len(ratios) == 0:
            return True  
        for r in ratios:
            if r != ratios[0]:
                return False
        return True

    # (f) a × b = 0
    def paralela_f(self, v):
        cruz = self.producto_cruz(v)
        return cruz.a1 == 0 and cruz.a2 == 0 and cruz.a3 == 0

    # (g) Proyección ortogonal de a sobre b
    def proyeccion(self, v):
        factor = self.producto_escalar(v) / (v.magnitud()**2)
        return AlgebraVectorial(v.a1*factor, v.a2*factor, v.a3*factor)

    # (h) Componente de a sobre b (solo magnitud)
    def componente(self, v):
        return self.producto_escalar(v) / v.magnitud()


v1 = AlgebraVectorial(1, 2, 3)
v2 = AlgebraVectorial(2, 4, 6)

print("Producto escalar =", v1.producto_escalar(v2))
print("Magnitud v1 =", v1.magnitud())
print("Perpendicular a) |a+b| = |a-b| :", v1.perpendicular_a(v2))
print("Perpendicular b) |a-b| = |b-a| :", v1.perpendicular_b(v2))
print("Perpendicular c) a·b = 0 :", v1.perpendicular_c(v2))
print("Perpendicular d) |a+b|^2 = |a|^2 + |b|^2 :", v1.perpendicular_d(v2))
print("Paralela e) a = r·b :", v1.paralela_e(v2))
print("Paralela f) a × b = 0 :", v1.paralela_f(v2))
print("Proyección de a sobre b =", v1.proyeccion(v2).a1, v1.proyeccion(v2).a2, v1.proyeccion(v2).a3)
print("Componente de a en b =", v1.componente(v2))