import java.util.*;
import java.lang.*;
import java.io.*;

// The main method must be in a class named "Main".
class Main {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int s=sc.nextInt();
        int p=sc.nextInt();
        String dna_s=sc.next();
        int a=sc.nextInt();
        int c=sc.nextInt();
        int g=sc.nextInt();
        int t=sc.nextInt();
        int answer=0;
        int length=0;

        int a_cnt=0;
        int c_cnt=0;
        int g_cnt=0;
        int t_cnt=0;
        int start=-1;
        for(int i=0;i<s;i++){
            char now=dna_s.charAt(i);
            if(length<p){
                length++;
                if(now=='A')
                    a_cnt++;
                if(now=='C')
                    c_cnt++;
                if(now=='G')
                    g_cnt++;
                if(now=='T')
                    t_cnt++;   
            }else{
                if(now=='A')
                    a_cnt++;
                if(now=='C')
                    c_cnt++;
                if(now=='G')
                    g_cnt++;
                if(now=='T')
                    t_cnt++;   
            }
            if(length==p){
                if(start>=0){
                    char end=dna_s.charAt(start);
                    if(end=='A')
                        a_cnt--;
                    if(end=='C')
                        c_cnt--;
                    if(end=='G')
                        g_cnt--;
                    if(end=='T')
                        t_cnt--; 
                }
                start++;
                if(a<=a_cnt&&c<=c_cnt&&g<=g_cnt&&t<=t_cnt)
                    answer++;
            }
        }
        System.out.println(answer);
    }
}