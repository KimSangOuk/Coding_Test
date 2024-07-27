import java.util.*;
import java.lang.*;
import java.io.*;

// The main method must be in a class named "Main".
class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st=new StringTokenizer(br.readLine());
        int n=Integer.parseInt(st.nextToken());
        int m=Integer.parseInt(st.nextToken());
        List<PriorityQueue<Long>> classes = new LinkedList<PriorityQueue<Long>>();
        for(int i=0;i<n;i++){
            PriorityQueue<Long> pq=new PriorityQueue<>();
            st=new StringTokenizer(br.readLine());
            for(int j=0;j<m;j++){
                pq.add(Long.parseLong(st.nextToken()));
            }
            classes.add(pq);
        }
        long answer=Long.MAX_VALUE;
        long max_value=-1;
        PriorityQueue<long[]> pq=new PriorityQueue<>((a,b)->Long.compare(a[0],b[0]));
        for(int i=0;i<n;i++){
            long cgp=classes.get(i).remove();
            long[] arr=new long[2];
            arr[0]=cgp;
            arr[1]=i;
            pq.add(arr);
            if(max_value<cgp){
                max_value=cgp;
            }
        }        
        while(true){
            long[] now=pq.remove();
            if(answer>Math.abs(now[0]-max_value)){
                answer=Math.abs(now[0]-max_value);
            }
            if(classes.get((int)now[1]).isEmpty()){
                break;
            }
            long tmp=classes.get((int)now[1]).remove();
            if(tmp>max_value){
                max_value=tmp;
            }
            pq.add(new long[]{tmp,now[1]});

        }
        System.out.println(answer);
    }

}
