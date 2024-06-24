import java.util.*;
import java.lang.*;
import java.io.*;

class Main {
    public static void main(String[] args) {
        Scanner scanner=new Scanner(System.in);
        int h=scanner.nextInt();
        int b=scanner.nextInt();
        int c=scanner.nextInt();
        int s=scanner.nextInt();

        System.out.printf("%.1f MB",(float)h*b*c*s/8/1024/1024);
    }
}