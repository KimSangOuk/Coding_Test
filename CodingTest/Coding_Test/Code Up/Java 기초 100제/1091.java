import java.util.*;
import java.lang.*;
import java.io.*;

class Main {
    public static void main(String[] args) {
        Scanner scanner=new Scanner(System.in);
        long a=scanner.nextInt();
        int d1=scanner.nextInt();
        int d2=scanner.nextInt();
        int n=scanner.nextInt();

        for(int i=0;i<n-1;i++){
            a=a*d1+d2;           
        }
        System.out.println(a);
    }
}