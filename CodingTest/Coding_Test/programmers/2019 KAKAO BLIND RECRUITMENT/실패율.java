import java.util.*;

class Solution {
    public int[] solution(int N, int[] stages) {
        int[] answer = new int[N];
        HashMap<Integer,Float> map=new HashMap<>();
        int total_users=stages.length;
        int[] try_stage_num=new int[N+2];
        for(int i=0;i<total_users;i++){
            try_stage_num[stages[i]]++;
        }
        for(int i=1;i<=N;i++){
            if(try_stage_num[i]!=0){
                map.put(i,(float)try_stage_num[i]/total_users);
            }else{
                map.put(i,0.0f);
            }
            total_users-=try_stage_num[i];
        }

        List<Map.Entry<Integer,Float>> list=new ArrayList<>(map.entrySet());
        list.sort(Collections.reverseOrder(Map.Entry.comparingByValue()));
        for(int i=0;i<list.size();i++){
            answer[i]=list.get(i).getKey();
        }

        // return map.entrySet().stream().sorted((o1,o2)->Float.compare(o2.getValue(),o1.getValue())).mapToInt(HashMap,Entry::getKey).toArray()

        return answer;
    }
}