import java.util.*;
import java.lang.*;
import java.io.*;

class Main {
    public static void main(String[] args) {
        Scanner scanner=new Scanner(System.in);
        int a=scanner.nextInt();
        int b=scanner.nextInt();
        System.out.printf("%d\n",a+b);
        System.out.printf("%d\n",a-b);
        System.out.printf("%d\n",a*b);
        System.out.printf("%d\n",a/b);
        System.out.printf("%d\n",a%b);

        System.out.printf("%.2f",(float)a/b);
    }
}