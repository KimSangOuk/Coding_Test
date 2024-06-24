import java.util.*;
import java.lang.*;
import java.io.*;

class Main {
    public static void main(String[] args) {
        Scanner scanner=new Scanner(System.in);
        int k=scanner.nextInt();

        for(int i=1;i<=k;i++){
            if(i%3!=0){
                System.out.printf("%d ",i);
            }
        }
    }
}