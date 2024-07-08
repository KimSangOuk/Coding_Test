import java.util.*;
import java.lang.*;
import java.io.*;
import java.math.*;

// The main method must be in a class named "Main".
class Main {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        Map<Integer,Integer> map_x=new HashMap<Integer,Integer>();
        Map<Integer,Integer> map_y=new HashMap<Integer,Integer>();
        for(int i=0;i<3;i++){
            int x=sc.nextInt();
            int y=sc.nextInt();
            if(map_x.containsKey(x)){
                map_x.put(x,2);
            }else{
                map_x.put(x,1);
            }
            if(map_y.containsKey(y)){
                map_y.put(y,2);
            }else{
                map_y.put(y,1);
            }
        }
        int answer_x=0;
        int answer_y=0;
        for(int x : map_x.keySet()){
            if(map_x.get(x)==1){
                answer_x=x;
            }
        }
        for(int y : map_y.keySet()){
            if(map_y.get(y)==1){
                answer_y=y;
            }
        }
        System.out.printf("%d %d",answer_x,answer_y);
    }
}