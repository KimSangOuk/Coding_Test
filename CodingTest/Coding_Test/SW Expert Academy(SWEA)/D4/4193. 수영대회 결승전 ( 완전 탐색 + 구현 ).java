import java.util.*;
import java.lang.*;
import java.io.*;

class Pos implements Comparable<Pos>{
    int time;
    int nextX;
    int nextY;

    public Pos(int time,int nextX,int nextY){
        this.time=time;
        this.nextX=nextX;
        this.nextY=nextY;
    }

    @Override
    public int compareTo(Pos other){
        if(this.time!=other.time){
            return Integer.compare(this.time,other.time);
        }else if(this.nextX!=other.nextX){
            return Integer.compare(this.nextX,other.nextX);
        }
        return Integer.compare(this.nextY,other.nextY);
    }
    @Override
    public String toString(){
        return "("+time+", "+nextX+", "+nextY+")";
    }
}

class Solution {
    public static void main(String[] args) {
        int[] dx={-1,1,0,0};
        int[] dy={0,0,-1,1};

        Scanner s=new Scanner(System.in);
        int tc=s.nextInt();
        for(int i=1;i<=tc;i++){
            int n=s.nextInt();
            int[][] board=new int[n][n];
            int[][] visited=new int[n][n];
            for(int j=0;j<n;j++){
                for(int k=0;k<n;k++){
                    board[j][k]=s.nextInt();
                }
            }
            int sx=s.nextInt();
            int sy=s.nextInt();
            int tx=s.nextInt();
            int ty=s.nextInt();
            PriorityQueue<Pos> q=new PriorityQueue<>();
            q.add(new Pos(0,sx,sy));
            while(!q.isEmpty()){
                Pos p=q.poll();
                if(p.nextX==tx && p.nextY==ty){
                    System.out.printf("#%d %d\n",i,p.time);
                    break;
                }
                for(int j=0;j<4;j++){
                    int nx=p.nextX+dx[j];
                    int ny=p.nextY+dy[j];
                    int nt=0;
                    if(nx<0 || ny<0 || nx>=n || ny>=n){
                        continue;
                    }
                    if(board[nx][ny]==1){
                        continue;
                    }
                    if(visited[nx][ny]==1){
                        continue;
                    }
                    visited[nx][ny]=1;
                    if(board[nx][ny]==2){
                        nt=p.time+3-p.time%3;
                    }else{
                        nt=p.time+1;
                    }
                    q.add(new Pos(nt,nx,ny));
                }
            }
            if(visited[tx][ty]==0){
                System.out.printf("#%d %d\n",i,-1);
            }
        }
    }
}