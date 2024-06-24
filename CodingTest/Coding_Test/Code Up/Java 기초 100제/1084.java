import java.util.Scanner;
import java.io.BufferedWriter;
import java.io.OutputStreamWriter;
import java.io.IOException;

class Main {
    public static void main(String[] args) throws IOException {
        Scanner scanner = new Scanner(System.in);
        int r = scanner.nextInt();
        int g = scanner.nextInt();
        int b = scanner.nextInt();
        int total = 0;

        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        for (int i = 0; i < r; i++) {
            for (int j = 0; j < g; j++) {
                for (int t = 0; t < b; t++) {
                    bw.write(i + " " + j + " " + t + "\n");
                    total++;
                }
            }
        }
        bw.write(String.valueOf(total));
        bw.flush();
        bw.close();
    }
}