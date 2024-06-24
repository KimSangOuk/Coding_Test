import java.util.*;

class Solution {
    public int[] solution(int[] answers) {
        ArrayList<Integer> answer = new ArrayList<>();
        int[] a_input={1,2,3,4,5};
        int[] b_input={2,1,2,3,2,4,2,5};
        int[] c_input={3,3,1,1,2,2,4,4,5,5};
        int[] score={0,0,0};

        for(int i=0;i<answers.length;i++){
            if(a_input[i%a_input.length]==answers[i]){
                score[0]++;
            }
            if(b_input[i%b_input.length]==answers[i]){
                score[1]++;
            }
            if(c_input[i%c_input.length]==answers[i]){
                score[2]++;
            }
        }

        // int max_value=0;
        // for(int i=0;i<3;i++){
        //     if(max_value<score[i]){
        //         answer=new ArrayList<>();
        //         max_value=score[i];
        //         answer.add(i+1);
        //     }else if(max_value==score[i]){
        //         answer.add(i+1);
        //     }
        // }
        int max_value=Arrays.stream(score).max().getAsInt();
        for(int i=0;i<3;i++){
            if(max_value==score[i]){
                answer.add(i+1);
            }
        }

        return answer.stream().mapToInt(Integer::intValue).toArray();
    }
}