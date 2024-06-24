import java.util.*;
import java.lang.*;
import java.io.*;

class Main {
    public static void main(String[] args) {
        Scanner scanner=new Scanner(System.in);
        int a=scanner.nextInt();

        switch (a) {
            case 12:
            case 1:
            case 2:
                System.out.printf("winter\n");
                break;
            case 3:
            case 4:
            case 5:
                System.out.printf("spring\n");
                break;
            case 6:
            case 7:
            case 8:
                System.out.printf("summer\n");
                break;
            case 9:
            case 10:
            case 11:
                System.out.printf("fall\n");
                break;
        }
    }
}