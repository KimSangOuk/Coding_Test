import java.util.*;
import java.lang.*;
import java.io.*;

class Main {
    public static void main(String[] args) {
        Scanner scanner=new Scanner(System.in);
        int w=scanner.nextInt();
        int h=scanner.nextInt();
        int b=scanner.nextInt();
        // int s=scanner.nextInt();

        System.out.printf("%.2f MB",(float)w*h*b/8/1024/1024);
    }
}