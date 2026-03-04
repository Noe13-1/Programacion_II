package ejercicio1;

import java.util.Scanner;

public class Estadistica {

    private double[] datos;

    public Estadistica(double[] datos) {
        this.datos = datos;
    }

    public double promedio() {
        double suma = 0;
        for (double d : datos) {
            suma += d;
        }
        return suma / datos.length;
    }

    public double desviacion() {
        double prom = promedio();
        double sumaCuadrados = 0;
        for (double d : datos) {
            sumaCuadrados += Math.pow(d - prom, 2);
        }
        return Math.sqrt(sumaCuadrados / (datos.length - 1));
    }

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        double[] valores = new double[10];
        System.out.print("Ingrese 10 números: ");
        for (int i = 0; i < 10; i++) {
            valores[i] = input.nextDouble();
        }

        Estadistica est = new Estadistica(valores);

        System.out.println("El promedio es " + String.format("%.2f", est.promedio()));
        System.out.println("La desviación standard es " + String.format("%.5f", est.desviacion()));
        
        input.close();
    }
}

