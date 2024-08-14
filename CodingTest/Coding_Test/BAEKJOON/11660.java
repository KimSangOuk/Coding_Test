import java.util.*;
import java.lang.*;
import java.io.*;

// The main method must be in a class named "Main".
class Main {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        int m=sc.nextInt();
        int[][] arr=new int[n][n];
        int[][] dp=new int[n][n];
        for(int i=0;i<n;i++){
            for(int j=0;j<n;j++){
                arr[i][j]=sc.nextInt();
                dp[i][j]=arr[i][j];
            }
        }
        for(int i=0;i<n;i++){
            for(int j=0;j<n;j++){
                int left=0;
                if(j>0)
                    left=dp[i][j-1];
                int up=0;
                if(i>0)
                    up=dp[i-1][j];
                int left_up=0;
                if(j>0&&i>0)
                    left_up=dp[i-1][j-1];
                dp[i][j]+=left+up-left_up;
            }
        }
        StringBuilder sb=new StringBuilder();
        for(int i=0;i<m;i++){
            int x1=sc.nextInt()-1;
            int y1=sc.nextInt()-1;
            int x2=sc.nextInt()-1;
            int y2=sc.nextInt()-1;
            int x1y2=0;
            if(x1-1>=0)
                x1y2=dp[x1-1][y2];
            int x2y1=0;
            if(y1-1>=0)
                x2y1=dp[x2][y1-1];
            int x1y1=0;
            if(x1-1>=0&&y1-1>=0)
                x1y1=dp[x1-1][y1-1];
            sb.append(dp[x2][y2]-x1y2-x2y1+x1y1);
            sb.append('\n');
        }
        System.out.println(sb.toString());
    }
}