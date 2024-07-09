import java.util.LinkedList;
import java.util.Queue;

class Solution {
    public int solution(int[] queue1, int[] queue2) {
        int answer = 0;

        Queue<Integer> q1=new LinkedList<Integer>();
        Queue<Integer> q2=new LinkedList<Integer>();
        for(int i : queue1){
            q1.offer(i);
        }
        for(int i : queue2){
            q2.offer(i);
        }
        long sum_value_q1=0;
        long sum_value_q2=0;
        for(int i : q1){
            sum_value_q1+=i;
        }
        for(int i : q2){
            sum_value_q2+=i;
        }

        if((sum_value_q1+sum_value_q2)%2!=0){

            return -1;
        }
        if(sum_value_q1==sum_value_q2){
            return 0;
        }
        boolean canMake=false;
        while(true){
            if(answer>1000000){
                break;
            }
            if(sum_value_q1>sum_value_q2){
                int k=q1.poll();
                q2.offer(k);
                answer+=1;
                sum_value_q1-=k;
                sum_value_q2+=k;
            }else if(sum_value_q1==sum_value_q2){
                return answer;
            }else{
                int k=q2.poll();
                q1.offer(k);
                answer+=1;
                sum_value_q2-=k;
                sum_value_q1+=k;
            }
        }

        if(!canMake){
            return -1;
        }

        return answer;
    }
}