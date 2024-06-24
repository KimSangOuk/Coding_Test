import java.util.*;
import java.lang.*;
import java.io.*;

class Main {
    public static void main(String[] args) {
        Scanner scanner=new Scanner(System.in);
        int a=scanner.nextInt();
        int d=scanner.nextInt();
        int n=scanner.nextInt();

        for(int i=0;i<n-1;i++){
            a+=d;           
        }
        System.out.println(a);
    }
}