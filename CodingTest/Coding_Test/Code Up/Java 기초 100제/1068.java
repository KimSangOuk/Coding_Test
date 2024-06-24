import java.util.*;
import java.lang.*;
import java.io.*;

class Main {
    public static void main(String[] args) {
        Scanner scanner=new Scanner(System.in);
        int a=scanner.nextInt();

        if(a>=90){
            System.out.printf("A\n");
        }else if(a>=70){
            System.out.printf("B\n");
        }else if(a>=40){
            System.out.printf("C\n");
        }else{
            System.out.printf("D\n");
        }
    }
}