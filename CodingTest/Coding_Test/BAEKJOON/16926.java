import java.util.*;
import java.lang.*;
import java.io.*;

// The main method must be in a class named "Main".
class Main {

    static int[] dx={0,1,0,-1};
    static int[] dy={1,0,-1,0};
    public static void main(String[] args) throws IOException {
        BufferedReader bf=new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st=new StringTokenizer(bf.readLine());
        int n=Integer.parseInt(st.nextToken());
        int m=Integer.parseInt(st.nextToken());
        int r=Integer.parseInt(st.nextToken());

        int[][] arr=new int[n][m];
        for(int i=0;i<n;i++){
            st=new StringTokenizer(bf.readLine());
            for(int j=0;j<m;j++){
                arr[i][j]=Integer.parseInt(st.nextToken());
            }
        }

        int std_value=Math.min(n,m)/2;
        int[][] visited=new int[n][m];
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                visited[i][j]=-1;
            }
        }

            for(int s=0;s<std_value;s++){
                int x=s;
                int y =s;
                int d=0;
                int stack=0;
                Deque<Integer> q=new ArrayDeque<>();
                q.addLast(arr[x][y]);
                visited[x][y]=s;
                while(true){
                    if(stack>=4){
                        break;
                    }
                    int nx=x+dx[d];
                    int ny=y+dy[d];
                    if(nx<0 || ny<0 ||nx>=n||ny>=m||visited[nx][ny]!=-1){
                        d=(d+1)%4;
                        stack++;
                        continue;
                    }
                    q.addLast(arr[nx][ny]);
                    x=nx;
                    y=ny;
                    visited[nx][ny]=s;
                }
                // while(!q.isEmpty()){
                //     System.out.printf("%d ",q.removeFirst());
                // }
                // System.out.println();
                for(int k=0;k<r;k++){
                    q.addLast(q.removeFirst());
                }

                x=y=s;
                d=0;
                stack=0;
                arr[x][y]=q.removeFirst();
                while(!q.isEmpty()){
                    if(stack>=4){
                        break;
                    }
                    int nx=x+dx[d];
                    int ny=y+dy[d];
                    if(nx<0 || ny<0 ||nx>=n||ny>=m||visited[nx][ny]!=s){
                        d=(d+1)%4;
                        stack++;
                        continue;
                    }
                    arr[nx][ny]=q.removeFirst();
                    x=nx;
                    y=ny;
                }

            }
            for(int i=0;i<n;i++){
                for(int j=0;j<m;j++){
                    System.out.printf("%d ",arr[i][j]);
                }
                System.out.println();
            }

    }
}