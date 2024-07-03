import java.util.*;
import java.lang.*;
import java.io.*;

class Main {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int tc=sc.nextInt();
        for(int i=1;i<=tc;i++){
            int answer=0;
            for(int j=0;j<10;j++){
                int k=sc.nextInt();
                answer+=k;
            }
            System.out.printf("#%d %d\n",i,Math.round((float)answer/10));
        }
    }
}