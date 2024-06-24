import java.util.*;
import java.lang.*;
import java.io.*;

class Main {
    public static void main(String[] args) {
        Scanner scanner=new Scanner(System.in);
        int n=scanner.nextInt();
        int[]cnt=new int[24];
        for(int i=0;i<n;i++){
            int k=scanner.nextInt();
            cnt[k]+=1;
        }
        for(int i=1;i<=23;i++){
            System.out.printf("%d ",cnt[i]);
        }
    }
}