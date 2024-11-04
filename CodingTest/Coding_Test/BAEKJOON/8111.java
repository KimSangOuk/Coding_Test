import java.util.*;
import java.lang.*;
import java.io.*;

// The main method must be in a class named "Main".
class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st= new StringTokenizer(br.readLine());
        int T= Integer.parseInt(st.nextToken());

        StringBuilder sb=new StringBuilder();
        for(int i=0;i<T;i++){
            st=new StringTokenizer(br.readLine());
            int N=Integer.parseInt(st.nextToken());
            sb.append(bfs(N));
            sb.append("\n");
        }
        System.out.println(sb.toString());
    }

    static class Pair{
        String str;
        int num;
        public Pair(String str,int num){
            this.str=str;
            this.num=num;
        }
    }

    public static String bfs(int num){
        Deque<Pair> q=new ArrayDeque<>();
        boolean[] visited=new boolean[20001];
        q.add(new Pair("1",1));
        while(!q.isEmpty()){
            Pair cur=q.poll();
            int curNum=cur.num;
            String curStr=cur.str;
            if(curNum==0){
                return curStr;
            }
            if(curStr.length()>100){
                return "BRAK";
            }
            int plusZero=(curNum*10)%num;
            if(!visited[plusZero]){
                visited[plusZero]=true;
                q.add(new Pair(curStr+"0",plusZero));
            }
            int plusOne=(curNum*10+1)%num;
            if(!visited[plusOne]){
                visited[plusOne]=true;
                q.add(new Pair(curStr+"1",plusOne));
            }
        }
        return "BRAK";
    }
}