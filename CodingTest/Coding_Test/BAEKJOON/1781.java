import java.util.*;
import java.lang.*;
import java.io.*;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st=new StringTokenizer(br.readLine());
        int N=Integer.parseInt(st.nextToken());
        PriorityQueue<int[]> pq=new PriorityQueue<>((a,b)->Integer.compare(a[0],b[0]));
        for(int i=0;i<N;i++){
            st=new StringTokenizer(br.readLine());
            int deadline=Integer.parseInt(st.nextToken());
            int cup=Integer.parseInt(st.nextToken());
            pq.offer(new int[]{deadline,cup});
        }
        int answer=0;
        PriorityQueue<Integer> pqV=new PriorityQueue<>();
        while(!pq.isEmpty()){
            int[] now=pq.poll();
            int deadline=now[0];
            int cup=now[1];
            answer+=cup;
            pqV.offer(cup);
            if(pqV.size()>deadline){
                answer-=pqV.poll();
            }
        }
        System.out.println(answer);
    }
}