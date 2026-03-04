package ejercicio1;

import java.util.Scanner;


public class EstadisticaEstructurada {
    public static void main(String[] args) {
        Scanner leer = new Scanner(System.in);

        double[] numeros = new double[10];
        
        System.out.print("Ingrese 10 números: ");
        for (int i = 0; i < 10; i++) {
            numeros[i] = leer.nextDouble();
        }

        double sumaTotal = 0;
        for (int i = 0; i < 10; i++) {
            sumaTotal += numeros[i];
        }
        double promedio = sumaTotal / 10;

        double sumaDiferenciasCuadrado = 0;
        for (int i = 0; i < 10; i++) {
            double diferencia = numeros[i] - promedio;
            sumaDiferenciasCuadrado += (diferencia * diferencia);
        }
        
        double resultadoDesviacion = Math.sqrt(sumaDiferenciasCuadrado / 9);
        
        System.out.println("El promedio es " + promedio);
        System.out.println("La desviación standard es " + resultadoDesviacion);
        
        leer.close();
    }
}

