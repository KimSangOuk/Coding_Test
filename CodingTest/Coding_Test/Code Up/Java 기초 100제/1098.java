import java.util.*;
import java.lang.*;
import java.io.*;

class Main {
    public static void main(String[] args) {
        Scanner scanner=new Scanner(System.in);
        int n=scanner.nextInt();
        int m=scanner.nextInt();
        int [][]board=new int[n][m];
        int cnt=scanner.nextInt();
        for(int i=0;i<cnt;i++){
            int l=scanner.nextInt();
            int d=scanner.nextInt();
            int x=scanner.nextInt();
            int y=scanner.nextInt();
            if(d==0){
                for(int k=y-1;k<y-1+l;k++){
                    board[x-1][k]=1;        
                }
            }else{
                for(int j=x-1;j<x-1+l;j++){
                    board[j][y-1]=1;
                }
            }
        }

        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                System.out.printf("%d ",board[i][j]);
            }
            System.out.println();
        }
    }
}