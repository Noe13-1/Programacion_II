package ejercicio1;

import java.util.Random;

public class Cronometro {
    private long inicia;
    private long finaliza;

    public Cronometro() {
        this.inicia = System.currentTimeMillis();
    }

    public void inicia() {
        this.inicia = System.currentTimeMillis();
    }

    public void detener() {
        this.finaliza = System.currentTimeMillis();
    }

    public long lapsoDeTiempo() {
        return this.finaliza - this.inicia;
    }

    public long getInicia() { return inicia; }
    public long getFinaliza() { return finaliza; }

    public static void main(String[] args) {
        int tamaño = 100000;
        int[] numeros = new int[tamaño];
        Random rnd = new Random();

        for (int i = 0; i < tamaño; i++) {
            numeros[i] = rnd.nextInt(100000);
        }

        Cronometro reloj = new Cronometro();
        
        reloj.inicia();
        ordenacionSeleccion(numeros);
        reloj.detener();

        System.out.println("Tiempo de ejecución para 100,000 números: " + reloj.lapsoDeTiempo() + " ms.");
    }

    public static void ordenacionSeleccion(int[] arr) {
        for (int i = 0; i < arr.length - 1; i++) {
            int indiceMin = i;
            for (int j = i + 1; j < arr.length; j++) {
                if (arr[j] < arr[indiceMin]) {
                    indiceMin = j;
                }
            }
            int temporal = arr[indiceMin];
            arr[indiceMin] = arr[i];
            arr[i] = temporal;
        }
    }
}

