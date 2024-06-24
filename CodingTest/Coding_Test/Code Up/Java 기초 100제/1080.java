import java.util.*;
import java.lang.*;
import java.io.*;

class Main {
    public static void main(String[] args) {
        Scanner scanner=new Scanner(System.in);
        int k=scanner.nextInt();

        int i=1;
        int sum=0;
        while(true){
            sum+=i;
            if(sum>=k){
                break;
            }
            i++;
        }
        System.out.println(i);
    }
}