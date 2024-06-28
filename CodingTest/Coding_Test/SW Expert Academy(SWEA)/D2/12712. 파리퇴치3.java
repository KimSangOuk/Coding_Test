import java.util.*;
import java.io.FileInputStream;

class Solution
{
  public static void main(String args[]) throws Exception
  {
    Scanner s=new Scanner(System.in);
        int tc=s.nextInt();
        int[] dx1={0,0,-1,1};
        int[] dy1={-1,1,0,0};
        int[] dx2={-1,1,-1,1};
        int[] dy2={1,1,-1,-1};
        for(int i=1;i<=tc;i++){
            int n=s.nextInt();
            int m=s.nextInt();
            int answer=0;
            int[][] board=new int[n][n];
            for(int j=0;j<n;j++){
                for(int k=0;k<n;k++){
                    board[j][k]=s.nextInt();
                }
            }
            for(int j=0;j<n;j++){
                for(int k=0;k<n;k++){
                    int x=j;
                    int y=k;
                    int sum=board[x][y];
                    for(int t=1;t<m;t++){
                        for(int q=0;q<4;q++){
                            int nx=x+dx1[q]*t;
                            int ny=y+dy1[q]*t;
                            if(nx<0||ny<0||nx>=n||ny>=n){
                                continue;
                            }
                            sum+=board[nx][ny];
                        }
                    }
                    if(sum>answer){
                        answer=sum;
                    }

                    sum=board[x][y];
                    for(int t=1;t<m;t++){
                        for(int q=0;q<4;q++){
                            int nx=x+dx2[q]*t;
                            int ny=y+dy2[q]*t;
                            if(nx<0||ny<0||nx>=n||ny>=n){
                                continue;
                            }
                            sum+=board[nx][ny];
                        }
                    }
                    if(sum>answer){
                        answer=sum;
                    }
                }
            }
            System.out.printf("#%d %d\n",i,answer);
        }
  }
}