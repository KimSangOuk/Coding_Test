import java.util.*;
import java.lang.*;
import java.io.*;

class Main {
    public static void main(String[] args) {
        Scanner scanner=new Scanner(System.in);
        int a=scanner.nextInt();
        int b=scanner.nextInt();
        int c=scanner.nextInt();

        int t=1;
        while(true){
            if(t%a==0&&t%b==0&&t%c==0){
                System.out.printf("%d",t);
                break;
            }
            t++;
        }
    }
}