import java.util.*;
import java.lang.*;
import java.io.*;

// The main method must be in a class named "Main".
class Main {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        long answer=0;
        int n=sc.nextInt();
        int k=sc.nextInt();
        int[] bags=new int[k];
        PriorityQueue<int[]> jewels=new PriorityQueue<>(Comparator.comparingInt(pair->pair[0])); 
        for(int i=0;i<n;i++){
            int m=sc.nextInt();
            int v=sc.nextInt();
            jewels.add(new int[]{m,v});
        }
        for(int i=0;i<k;i++){
            bags[i]=sc.nextInt();
        }
        Arrays.sort(bags);

        PriorityQueue<Integer> tmpPriorityQueue=new PriorityQueue<>(Collections.reverseOrder());
        for(int bag:bags){
            while(!jewels.isEmpty()&&bag>=jewels.peek()[0]){
                tmpPriorityQueue.add(jewels.poll()[1]);
            }
            if(!tmpPriorityQueue.isEmpty()){
                answer+=tmpPriorityQueue.poll();
            }
        }
        System.out.println(answer);
    }
}