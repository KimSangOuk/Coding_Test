import java.util.*;
import java.lang.*;
import java.io.*;

class Main {
    public static void main(String[] args) {
        Scanner scanner=new Scanner(System.in);
        int k=scanner.nextInt();

        int sum=0;
        int i=1;
        while(true){
            sum+=i;
            if(sum>=k){
                System.out.printf("%d",sum);
                break;
            }
            i++;
        }
    }
}