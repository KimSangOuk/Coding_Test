import java.util.*;
import java.lang.*;
import java.io.*;

class Main {
    public static void main(String[] args) {
        Scanner scanner=new Scanner(System.in);

        while(true){
             int k=scanner.nextInt();
            if(k==0){
                break;
            }else{
                System.out.printf("%d\n",k);
            }
        }
    }
}