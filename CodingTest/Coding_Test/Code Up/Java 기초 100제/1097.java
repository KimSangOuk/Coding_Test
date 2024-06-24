import java.util.*;
import java.lang.*;
import java.io.*;

class Main {
    public static void main(String[] args) {
        Scanner scanner=new Scanner(System.in);
        int [][]board=new int[19][19];
        for(int i=0;i<19;i++){
            for(int j=0;j<19;j++){
                board[i][j]=scanner.nextInt();
            }
        }
        int k=scanner.nextInt();
        for(int i=0;i<k;i++){
            int n=scanner.nextInt();
            int m=scanner.nextInt();
            for(int j=0;j<19;j++){
                for(int t=0;t<19;t++){
                    if(j==n-1 || t==m-1){
                        if(j==n-1 && t==m-1){
                            continue;
                        }else if(board[j][t]==1){
                            board[j][t]=0;
                        }else{
                            board[j][t]=1;
                        }

                    }
                }
            }
        }

        for(int i=0;i<19;i++){
            for(int j=0;j<19;j++){
                System.out.printf("%d ",board[i][j]);
            }
            System.out.println();
        }
    }
}