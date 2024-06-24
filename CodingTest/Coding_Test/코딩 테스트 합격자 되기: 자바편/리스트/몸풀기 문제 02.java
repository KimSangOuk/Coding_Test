import java.util.*;
import java.lang.*;
import java.io.*;

class Main {
    public static void main(String[] args) {
        int[] arr=new int[]{4 ,2 ,2 ,4 ,5 ,1 ,2};
        System.out.println(Arrays.toString(solution(arr)));
    }

    static int[] solution(int[] arr){
        // Integer[] result=Arrays.stream(arr).boxed().distinct().toArray(Integer[]::new);
        // Arrays.sort(result,Collections.reverseOrder());
        // return Arrays.stream(result).mapToInt(Integer::intValue).toArray();
        TreeSet<Integer> set=new TreeSet<>(Collections.reverseOrder());
        for(int num:arr){
            set.add(num);
        }
        int[] result=new int[set.size()];
        for(int i=0;i<result.length;i++){
            result[i]=set.pollFirst();    
        }
        return result;
    }
}