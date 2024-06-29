import java.util.*;
import java.lang.*;
import java.io.*;

class Tuple{
    private int first;
    private int second;

    public Tuple(int first,int second){
        this.first=first;
        this.second=second;
    }

    public int getFirst(){
        return this.first;
    }

    public int getSecond(){
        return this.second;
    }
}

// The main method must be in a class named "Main".
class Main {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int tc=sc.nextInt();
        int[] dx={0,0,-1,1,-1,-1,1,1};
        int[] dy={-1,1,0,0,1,-1,1,-1};

        for(int i=1;i<=tc;i++){
            int answer=0;
            int n=sc.nextInt();
            String[][] board=new String[n][n];
            int[][] bomb_checker=new int[n][n];
            boolean[][] visited=new boolean[n][n];
            for(int j=0;j<n;j++){
                String s=sc.next();
                for(int k=0;k<n;k++){
                    board[j][k]=Character.toString(s.charAt(k));
                }    
            }
            for(int j=0;j<n;j++){
                for(int k=0;k<n;k++){
                    if(board[j][k].equals("*")){
                        bomb_checker[j][k]=-1;
                    }else{
                        int cnt=0;
                        for(int m=0;m<8;m++){
                            int nx=j+dx[m];
                            int ny=k+dy[m];
                            if(nx<0 || ny<0 || nx>=n || ny>=n){
                                continue;
                            }
                            if(board[nx][ny].equals("*")){
                                cnt++;
                            }
                        }
                        bomb_checker[j][k]=cnt;
                    }
                }
            }

            for(int j=0;j<n;j++){
                for(int k=0;k<n;k++){
                    if(bomb_checker[j][k]==0 && !visited[j][k]){
                        answer++;
                        visited[j][k]=true;
                        Queue<Tuple> q=new LinkedList<>();
                        q.offer(new Tuple(j,k));
                        while(!q.isEmpty()){
                            Tuple tuple=q.poll();
                            int x=tuple.getFirst();
                            int y=tuple.getSecond();
                            if(bomb_checker[x][y]>0){
                                continue;
                            }
                            for(int m=0;m<8;m++){
                                int nx=x+dx[m];
                                int ny=y+dy[m];
                                if(nx<0||ny<0||nx>=n||ny>=n){
                                    continue;
                                }
                                if(visited[nx][ny]){
                                    continue;
                                }
                                if(bomb_checker[nx][ny]==-1){
                                    continue;
                                }
                                if(m>=4){
                                    if(!visited[nx][y] || !visited[x][ny]){
                                        continue;
                                    }
                                }
                                visited[nx][ny]=true;
                                q.offer(new Tuple(nx,ny));
                            }
                        }
                    }
                }
            }
            for(int j=0;j<n;j++){
                for(int k=0;k<n;k++){
                    if(!visited[j][k] && bomb_checker[j][k]>0){
                        answer++;
                    }
                }
            }
            System.out.printf("#%d %d\n",i,answer);
        }

    }
}