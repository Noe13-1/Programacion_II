import math

class Vector3D:
    def __init__(self, a1, a2, a3):
        self.a1 = a1
        self.a2 = a2
        self.a3 = a3

    # Magnitud
    def magnitud(self):
        return math.sqrt(self.a1**2 + self.a2**2 + self.a3**2)

    def normal(self):
        mag = self.magnitud()
        if mag == 0:
            return Vector3D(0,0,0)
        return Vector3D(self.a1/mag, self.a2/mag, self.a3/mag)

    def producto_escalar(self, v):
        return self.a1*v.a1 + self.a2*v.a2 + self.a3*v.a3

    def producto_cruz(self, v):
        return Vector3D(
            self.a2*v.a3 - self.a3*v.a2,
            self.a3*v.a1 - self.a1*v.a3,
            self.a1*v.a2 - self.a2*v.a1
        )

    def __add__(self, v):
        return Vector3D(self.a1+v.a1, self.a2+v.a2, self.a3+v.a3)

    def __rmul__(self, r):
        return Vector3D(r*self.a1, r*self.a2, r*self.a3)

    def __str__(self):
        return f"({self.a1}, {self.a2}, {self.a3})"

v1 = Vector3D(1, 2, 3)
v2 = Vector3D(4, 5, 6)
r = 3

print("v1 =", v1)
print("v2 =", v2)
print("v1 + v2 =", v1 + v2)
print("r * v1 =", r * v1)
print("|v1| =", v1.magnitud())
print("Normalizado v1 =", v1.normal())
print("v1 · v2 =", v1.producto_escalar(v2))
print("v1 × v2 =", v1.producto_cruz(v2))