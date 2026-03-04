package ejercicio1;

import java.util.Scanner;

public class EcuacionCuadratica {
	
    private double a;
    private double b;
    private double c;

    public EcuacionCuadratica(double a, double b, double c) {
        this.a = a;
        this.b = b;
        this.c = c;
    }

    public double getDiscriminante() {
        return Math.pow(this.b, 2) - (4 * this.a * this.c);
    }

    public double getRaiz1() {
        double discriminante = getDiscriminante();
        if (discriminante < 0) {
            return 0;
        }
        return (-this.b + Math.sqrt(discriminante)) / (2 * this.a);
    }

    public double getRaiz2() {
        double discriminante = getDiscriminante();
        if (discriminante < 0) {
            return 0;
        }
        return (-this.b - Math.sqrt(discriminante)) / (2 * this.a);
    }

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.print("Ingrese a, b, c: ");
        double a = input.nextDouble();
        double b = input.nextDouble();
        double c = input.nextDouble();

        EcuacionCuadratica ecuacion = new EcuacionCuadratica(a, b, c);
        double disc = ecuacion.getDiscriminante();

        if (disc > 0) {
            System.out.println("La ecuación tiene dos raíces " + 
                               ecuacion.getRaiz1() + " y " + ecuacion.getRaiz2());
        } else if (disc == 0) {
            System.out.println("La ecuación tiene una raíz " + ecuacion.getRaiz1());
        } else {
            System.out.println("La ecuación no tiene raíces reales");
        }

        input.close();
    }
}

