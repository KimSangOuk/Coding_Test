import java.util.*;
import java.lang.*;
import java.io.*;

class Main {
    public static void main(String[] args) {
        Scanner scanner=new Scanner(System.in);
        int n=scanner.nextInt();
        int[]arr=new int[n];
        for(int i=0;i<n;i++){
            int k=scanner.nextInt();
            arr[i]=k;
        }
        for(int i=n-1;i>=0;i--){
            System.out.printf("%d ",arr[i]);
        }

    }
}