import java.util.*;
import java.lang.*;
import java.io.*;

class Main {
    public static void main(String[] args) {
        Scanner scanner=new Scanner(System.in);
        int a=scanner.nextInt();

        if(a<0){
            System.out.printf("minus\n");
            if(a%2==0){
                System.out.printf("even\n");
            }else{
                System.out.printf("odd\n");
            }
        }else{
            System.out.printf("plus\n");
            if(a%2==0){
                System.out.printf("even\n");
            }else{
                System.out.printf("odd\n");
            }
        }
    }
}