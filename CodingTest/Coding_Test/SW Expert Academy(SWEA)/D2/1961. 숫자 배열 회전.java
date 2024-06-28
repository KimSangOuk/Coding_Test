import java.util.*;
import java.io.FileInputStream;

class Solution
{
  public static void main(String args[]) throws Exception
  {
    Scanner s=new Scanner(System.in);
        int tc=s.nextInt();
        for(int i=1;i<=tc;i++){
            System.out.println("#"+i);
            int n=s.nextInt();
            int[][] board=new int[n][n];
            for(int j=0;j<n;j++){
                for(int t=0;t<n;t++){
                    board[j][t]=s.nextInt();
                }
            }
            String[] strs=new String[n];
            for(int j=0;j<n;j++){
                strs[j]="";
            }
            for(int j=0;j<3;j++){
                board=rotate(board,n);

                for(int k=0;k<n;k++){
                    for(int t=0;t<n;t++){
                        strs[k]+=Integer.toString(board[k][t]);
                    }
                    strs[k]+=" ";
                }
            }
            for(int j=0;j<n;j++){
                System.out.println(strs[j]);
            }
        }
  }
    public static int[][] rotate(int[][] arr,int n){
        int[][] new_board=new int[n][n];
        for(int i=0;i<n;i++){
            for(int j=0;j<n;j++){
                new_board[j][n-i-1]=arr[i][j];
            }
        }
        return new_board;
    }
}