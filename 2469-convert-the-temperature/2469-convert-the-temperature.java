class Solution {
     public static double[] convertTemperature(double celsius) {
        double kelvin = celsius + 273.15;
        double fahrenheit = (celsius * 9 / 5) + 32;
        return new double[]{kelvin, fahrenheit};
    }

    public static void main(String[] args) {
        double celsius = 25.0;
        double[] ans = convertTemperature(celsius);

        System.out.println("Celsius: " + celsius);
        System.out.println("Kelvin: " + ans[0]);
        System.out.println("Fahrenheit: " + ans[1]);
    }
}