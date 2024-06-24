import java.util.*;
import java.lang.*;
import java.io.*;

class Main {
    public static void main(String[] args) {
        Scanner scanner=new Scanner(System.in);
        int [][]board=new int[19][19];
        int t=scanner.nextInt();
        for(int i=0;i<t;i++){
            int n=scanner.nextInt();
            int m=scanner.nextInt();
            board[n-1][m-1]=1;
        }
        for(int i=0;i<19;i++){
            for(int j=0;j<19;j++){
                System.out.printf("%d ",board[i][j]);
            }
            System.out.println();
        }
    }
}