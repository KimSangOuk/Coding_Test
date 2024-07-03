import java.util.*;
import java.lang.*;
import java.io.*;

class Solution {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int tc=sc.nextInt();
        for(int i=1;i<=tc;i++){
            int answer=0;
            for(int j=0;j<10;j++){
                int k=sc.nextInt();
                if(k%2==1){
                    answer+=k;
                }
            }
            System.out.printf("#%d %d\n",i,answer);
        }
    }
}