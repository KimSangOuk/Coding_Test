import java.util.*;
import java.lang.*;
import java.io.*;

// The main method must be in a class named "Main".
class Main {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int h=sc.nextInt();
        int w=sc.nextInt();
        int[] block=new int[w];
        int[][] board=new int[h][w];
        for(int i=0;i<w;i++){
            block[i]=sc.nextInt();
        }
        for(int i=0;i<h;i++){
            for(int j=0;j<w;j++){
                if(i>=h-block[j]){
                    board[i][j]=1;
                }
            }
        }
        int answer=0;
        for(int i=h-1;i>-1;i--){
            for(int j=w-1;j>-1;j--){
                if(board[i][j]==1){
                    continue;
                }else{
                    boolean left_have_wall=false;
                    boolean right_have_wall=false;
                    int ny=j;
                    while(!left_have_wall && 0<=ny && ny<w){
                        if(board[i][ny]==1){
                            left_have_wall=true;
                            break;
                        }
                        ny--;
                    }
                    ny=j;
                    while(!right_have_wall&&0<=ny&&ny<w){
                        if(board[i][ny]==1){
                            right_have_wall=true;
                            break;
                        }
                        ny++;
                    }
                    if(left_have_wall&&right_have_wall){
                        answer++;
                    }
                }
            }
        }
        System.out.println(answer);
    }
}