#Ejercicio 1
import random
class Juego:
    def __init__(self, vidas):
        self.vidasIniciales = vidas
        self.numeroDeVidas = vidas
        self.record = 0

    def reiniciaPartida(self):
        self.numeroDeVidas = self.vidasIniciales
        print("Partida reiniciada. Vidas:", self.numeroDeVidas)

    def actualizaRecord(self):
        self.record += 1
        print("Record actualizado:", self.record)

    def quitaVida(self):
        self.numeroDeVidas -= 1
        print("Te quedan", self.numeroDeVidas, "vidas")
        return self.numeroDeVidas > 0


class JuegoAdivinaNumero(Juego):
    def __init__(self, vidas):
        super().__init__(vidas)
        self.numeroAAdivinar = 0

    def juega(self):
        self.reiniciaPartida()
        self.numeroAAdivinar = random.randint(0, 10)
        print("Adivina un numero entre 0 y 10")

        while True:
            try:
                num = int(input("Ingresa un numero: "))
            except:
                print("Error: ingresa un numero valido")
                continue

            if num == self.numeroAAdivinar:
                print("Acertaste!")
                self.actualizaRecord()
                break
            else:
                if self.quitaVida():
                    if num < self.numeroAAdivinar:
                        print("El numero es mayor")
                    else:
                        print("El numero es menor")
                else:
                    print("Te quedaste sin vidas")
                    print("El numero era:", self.numeroAAdivinar)
                    break

class Aplicacion:
    @staticmethod
    def main():
        juego = JuegoAdivinaNumero(3)
        juego.juega()

if __name__ == "__main__":
    Aplicacion.main()