import java.util.*;
import java.lang.*;
import java.io.*;

class Main {
    static int answer;
    public static void dfs(int total, int now, int[] arr, int b){
        if(total>=b){
            answer=Math.min(total-b,answer);
        }else{
            for(int i=now+1;i<arr.length;i++){
                dfs(total+arr[i],i,arr,b);
            }
        }
    }
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int tc=sc.nextInt();
        for(int i=1;i<=tc;i++){
            answer=Integer.MAX_VALUE;
            int n=sc.nextInt();
            int b=sc.nextInt();
            int[] arr=new int[n];
            for(int j=0;j<n;j++){
                arr[j]=sc.nextInt();
            }
            Arrays.sort(arr);
            for(int j=0;j<n;j++){
                int total=arr[j];
                dfs(total,j,arr,b);
            }
            System.out.printf("#%d %d\n",i,answer);
        }
    }
}