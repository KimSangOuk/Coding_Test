import java.util.*;

class Solution {
    public static List<String[]> generatePermutations(String[] strArray){
        List<String[]> permutations = new ArrayList<>();
        generatePermutations(new ArrayList<>(),List.of(strArray),permutations);
        return permutations;
    }
    private static void generatePermutations(List<String> prefix, List<String> strList, List<String[]> permutations){
        int n=strList.size();
        if(n==0){
            permutations.add(prefix.toArray(new String[0]));
        }else{
            for(int i=0;i<n;i++){
                List<String> newPrefix = new ArrayList<>(prefix);
                newPrefix.add(strList.get(i));
                List<String> remaining = new ArrayList<>(strList.subList(0,i));
                remaining.addAll(strList.subList(i+1,n));
                generatePermutations(newPrefix,remaining,permutations);
            }
        }
    }
    public long solution(String expression) {
        long answer = 0;

        String[] opers=new String[]{"+","-","*"};
        List<String[]> oper_prior_list=generatePermutations(opers);
        String[] exp_list=expression.split("");

        StringBuilder num_str=new StringBuilder();
        List<String> exp_main=new ArrayList<>();
        for(int i=0;i<exp_list.length;i++){
            if(Arrays.asList(opers).contains(exp_list[i])){
                exp_main.add(num_str.toString());
                exp_main.add(exp_list[i]);
                num_str=new StringBuilder();
            }else{
                num_str.append(exp_list[i]);
            }
        }
        if(num_str.length()!=0){
            exp_main.add(num_str.toString());
        }
        long max_value=0;
        for(String[] prior:oper_prior_list){
            List<String> exp=new ArrayList<>(exp_main);
            for(String op:prior){
                List<String> new_arr=new ArrayList<>();
                int k=0;
                while(k<exp.size()){
                    if(exp.get(k).equals(op)){
                        long first=Long.parseLong(new_arr.get(new_arr.size()-1));
                        String oper_this=exp.get(k);
                        long second=Long.parseLong(exp.get(k+1));
                        long mid=0;
                        if(oper_this.equals("+")){
                            mid=first+second;
                        }else if(oper_this.equals("*")){
                            mid=first*second;
                        }else{
                            mid=first-second;
                        }
                        new_arr.set(new_arr.size()-1,Long.toString(mid));
                        k+=2;
                    }else{
                        new_arr.add(exp.get(k));
                        k+=1;
                    }
                }
                exp=new_arr;
            }
            max_value=Math.max(max_value,Math.abs(Long.parseLong(exp.get(0))));
        }
        answer=max_value;
        return answer;
    }
}