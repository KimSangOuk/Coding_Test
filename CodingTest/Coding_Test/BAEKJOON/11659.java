import java.util.*;
import java.lang.*;
import java.io.*;

// The main method must be in a class named "Main".
class Main {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        int m=sc.nextInt();
        int[] arr=new int[n+1];
        int[] cumerative_sum=new int[n+1];
        for(int i=1;i<n+1;i++){
            arr[i]=sc.nextInt();
            cumerative_sum[i]=cumerative_sum[i-1]+arr[i];
        }
        StringBuilder sb=new StringBuilder();
        for(int k=0;k<m;k++){
            int i=sc.nextInt();
            int j=sc.nextInt();
            sb.append(cumerative_sum[j]-cumerative_sum[i-1]);
            sb.append("\n");
        }
        System.out.println(sb);
    }
}