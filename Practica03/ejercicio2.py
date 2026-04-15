import random

class Juego:
    def __init__(self, vidas):
        self.vidasIniciales = vidas
        self.numeroDeVidas = vidas
        self.record = 0

    def reiniciaPartida(self):
        self.numeroDeVidas = self.vidasIniciales
        print(f"Partida reiniciada. Vidas: {self.numeroDeVidas}")

    def actualizaRecord(self):
        self.record += 1
        print(f"Record actualizado: {self.record}")

    def quitaVida(self):
        self.numeroDeVidas -= 1
        print(f"Te quedan {self.numeroDeVidas} vidas")
        return self.numeroDeVidas > 0

class JuegoAdivinaNumero(Juego):
    def __init__(self, vidas):
        super().__init__(vidas)
        self.numeroAAdivinar = random.randint(0, 10)

    def validaNumero(self, num):
        return 0 <= num <= 10

    def juega(self):
        self.reiniciaPartida()
        print("Adivina el numero entre 0 y 10")

        while True:
            try:
                num = int(input("Ingresa un numero: "))
            except ValueError:
                print("Error: Ingresa un numero entero")
                continue

            if not self.validaNumero(num):
                continue

            if num == self.numeroAAdivinar:
                print("Acertaste!")
                self.actualizaRecord()
                break
            else:
                if self.quitaVida():
                    print("El numero es mayor" if num < self.numeroAAdivinar else "El numero es menor")
                else:
                    print(f"Fin del juego. El numero era: {self.numeroAAdivinar}")
                    break

class JuegoAdivinaPar(JuegoAdivinaNumero):
    def __init__(self, vidas):
        super().__init__(vidas)
        self.numeroAAdivinar = random.randrange(0, 11, 2)

    def validaNumero(self, num):
        if 0 <= num <= 10 and num % 2 == 0:
            return True
        print("Error: debe ser un numero PAR entre 0 y 10")
        return False

class JuegoAdivinaImpar(JuegoAdivinaNumero):
    def __init__(self, vidas):
        super().__init__(vidas)
        self.numeroAAdivinar = random.choice([1, 3, 5, 7, 9])

    def validaNumero(self, num):
        if 0 <= num <= 10 and num % 2 != 0:
            return True
        print("Error: debe ser un numero IMPAR entre 0 y 10")
        return False

class Aplicacion:
    @staticmethod
    def main():
        print("\n--- JUEGO ADIVINA NÚMERO ---")
        juego1 = JuegoAdivinaNumero(3)
        juego1.juega()

        print("\n--- JUEGO ADIVINA NÚMERO PAR ---")
        juego2 = JuegoAdivinaPar(3)
        juego2.juega()

        print("\n--- JUEGO ADIVINA NÚMERO IMPAR ---")
        juego3 = JuegoAdivinaImpar(3)
        juego3.juega()

if __name__ == "__main__":
    Aplicacion.main()

