import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.HashMap;
import java.util.Collections;
import java.util.Arrays;

class Solution {
    public static List<String[]> makeCombinations(String[] arr,int n, int r){
        List<String[]> combinations=new ArrayList<String[]>();
        String[] combination=new String[r];
        makeCombination(arr,combination,0,0,r,combinations);

        return combinations;
    }
    public static void makeCombination(String[] arr,String[] combination,int start,int index,int r,List<String[]> combinations){
        if(index==r){
            combinations.add(combination.clone());
            return;
        }
        for(int i=start;i<=arr.length-r+index;i++){
            combination[index]=arr[i];
            makeCombination(arr,combination,i+1,index+1,r,combinations);
        }
    }
    public String[] solution(String[] orders, int[] course) {
        ArrayList<String> answer = new ArrayList<>();
        Map<Integer,Map<String,Integer>> map=new HashMap<>();

        for(int how_many : course){
            map.put(how_many,new HashMap<String,Integer>());
        }

        for(String order : orders){
            String[] order_list=order.split("");
            for(int how_many : course){
                List<String[]> combinations=makeCombinations(order_list,order_list.length,how_many);
                for(String[] combination : combinations){
                    Arrays.sort(combination);
                    StringBuilder sb=new StringBuilder();
                    for(String k : combination){
                        sb.append(k);
                    }
                    String s=sb.toString();
                    if(map.get(how_many).containsKey(s)){
                        map.get(how_many).put(s,map.get(how_many).get(s)+1);
                    }else{
                        map.get(how_many).put(s,1);
                    }
                }
            }
        }
        for(int k:course){
            int largest_value=2;
            ArrayList<String> largest_list=new ArrayList<>();
            for(String key : map.get(k).keySet()){
                if(largest_value<map.get(k).get(key).intValue()){
                    largest_value=map.get(k).get(key).intValue();
                    largest_list=new ArrayList<>();
                    largest_list.add(key);
                }else if(largest_value==map.get(k).get(key).intValue()){
                    largest_list.add(key);
                }
            }
            for(String s:largest_list){
                answer.add(s);
            }
        }
        Collections.sort(answer);
        String[] real_answer=answer.toArray(new String[0]);
        return real_answer;
    }
}