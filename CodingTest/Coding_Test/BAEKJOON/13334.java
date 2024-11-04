import java.util.*;
import java.lang.*;
import java.io.*;

// The main method must be in a class named "Main".
class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st= new StringTokenizer(br.readLine());
        int n= Integer.parseInt(st.nextToken());

        PriorityQueue<int[]> pq=new PriorityQueue<>((a,b)->Integer.compare(a[1],b[1]));

        for(int i=0;i<n;i++){
            st=new StringTokenizer(br.readLine());
            int h=Integer.parseInt(st.nextToken());
            int o=Integer.parseInt(st.nextToken());
            if(h<o){
                pq.offer(new int[]{h,o});
            }else{
                pq.offer(new int[]{o,h});
            }
        }

        st=new StringTokenizer(br.readLine());
        int d=Integer.parseInt(st.nextToken());

        int max=0;
        PriorityQueue<Integer> pq2=new PriorityQueue<>();
        while(!pq.isEmpty()){
            int[] now=pq.poll();
            int start=now[1]-d;
            pq2.offer(now[0]);
            while(!pq2.isEmpty()&&pq2.peek()<start){
                pq2.poll();
            }
            max=Math.max(max,pq2.size());
        }
        System.out.println(max);
    }
}