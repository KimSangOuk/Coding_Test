import java.util.*;
import java.lang.*;
import java.io.*;

class Main {
    public static void main(String[] args) {
        Scanner scanner=new Scanner(System.in);
        int n=scanner.nextInt();
        int small_num=100;
        for(int i=0;i<n;i++){
            int k=scanner.nextInt();
            if(small_num>k){
                small_num=k;
            }
        }
        System.out.printf("%d",small_num);
    }
}