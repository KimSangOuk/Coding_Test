import java.util.*;
import java.lang.*;
import java.io.*;

// The main method must be in a class named "Main".
class Main {
    static int N;
    static int S;
    static int[] arr;
    public static void main(String[] args) throws IOException {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st=new StringTokenizer(br.readLine());

        N=Integer.parseInt(st.nextToken());
        S=Integer.parseInt(st.nextToken());
        st=new StringTokenizer(br.readLine());

        arr=new int[N];
        for(int i=0;i<N;i++){
            arr[i]=Integer.parseInt(st.nextToken());
        }

        long sum=arr[0];
        int startIdx=0;
        int endIdx=0;
        int answer=100001;
        while(true){
            int size=endIdx-startIdx+1;
            if(sum>=S){
                if(size<answer){
                    answer=size;
                }
                sum-=arr[startIdx++];
                if(startIdx>=N){
                    break;
                }
            }else{
                if(endIdx>=N-1){
                    break;
                }
                sum+=arr[++endIdx];
            }
        }
        if(answer==100001)
            System.out.println(0);
        else
            System.out.println(answer);
    }
}