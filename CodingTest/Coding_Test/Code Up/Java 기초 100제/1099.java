import java.util.*;
import java.lang.*;
import java.io.*;

class Main {
    public static void main(String[] args) {
        Scanner scanner=new Scanner(System.in);
        int [][]board=new int[10][10];
        int start_x=1;
        int start_y=1;
        int target_x=0;
        int target_y=0;
        for(int i=0;i<10;i++){
            for(int j=0;j<10;j++){
                int now=scanner.nextInt();
                if(now==2){
                    target_x=i;
                    target_y=j;
                }
                board[i][j]=now;
            }
        }
        while(true){
            if(board[start_x][start_y]==2){
                board[start_x][start_y]=9;
                break;
            }
            board[start_x][start_y]=9;

            int nx_right=start_x;
            int ny_right=start_y+1;
            int nx_down=start_x+1;
            int ny_down=start_y;
            if(board[nx_right][ny_right]!=1){
                start_x=nx_right;
                start_y=ny_right;
                if(board[start_x][start_y]==2){
                    board[start_x][start_y]=9;
                    break;
                }
                continue;
            }else if(board[nx_down][ny_down]!=1){
                start_x=nx_down;
                start_y=ny_down;
                if(board[start_x][start_y]==2){
                    board[start_x][start_y]=9;
                    break;
                }
                continue;
            }else{
                break;
            }
        }

        for(int i=0;i<10;i++){
            for(int j=0;j<10;j++){
                System.out.printf("%d ",board[i][j]);
            }
            System.out.println();
        }
    }
}