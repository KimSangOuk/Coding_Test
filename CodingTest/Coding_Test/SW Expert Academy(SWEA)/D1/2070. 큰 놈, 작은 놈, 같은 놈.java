import java.util.*;
import java.lang.*;
import java.io.*;

class Solution {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int tc=sc.nextInt();
        for(int i=1;i<=tc;i++){
            int a=sc.nextInt();
            int b=sc.nextInt();
            if(a>b){
                System.out.printf("#%d >\n",i);
            }else if(a<b){
                System.out.printf("#%d <\n",i);
            }else{
                System.out.printf("#%d =\n",i);
            }
        }
    }
}