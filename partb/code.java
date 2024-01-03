import java.util.Arrays;

public class UndoomDice {
    public static void main(String[] args) {
        int[] initialDieFaces = {1, 2, 3, 4, 5, 6};
        int[] dieA = initialDieFaces.clone();
        int[] dieB = initialDieFaces.clone();
        int[] newDieA = undoomDice(dieA, dieB)[0];
        int[] newDieB = undoomDice(dieA, dieB)[1];
        System.out.print("New Die A: ");
        for (int value : newDieA) {
            System.out.print(value + " ");
        }
        System.out.println();

        System.out.print("New Die B: ");
        for (int value : newDieB) {
            System.out.print(value + " ");
        }
    }

    public static int[][] undoomDice(int[] dieA, int[] dieB) {
        int total1 = Arrays.stream(dieA).sum();
        int total2 = Arrays.stream(dieB).sum();
        double factor = (double) total1 / total2;
        int[] a = new int[dieA.length];
        int[] b = new int[dieB.length];
        for (int i = 0; i < dieA.length; i++) {
            a[i] = Math.min(4, dieA[i]);
        }
        for (int i = 0; i < dieB.length; i++) {
            int adjustedValue = (int) Math.round(dieB[i] * factor);
            b[i] = Math.max(adjustedValue, 1);  
        }
        return new int[][]{a, b};
    }
}