import java.util.*;
import java.lang.*;
import java.io.*;

// The main method must be in a class named "Main".
class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader bf=new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st=new StringTokenizer(bf.readLine());
        int n=Integer.parseInt(st.nextToken());
        int l=Integer.parseInt(st.nextToken());
        int[] fruits=new int[n];
        st=new StringTokenizer(bf.readLine());
        for(int i=0;i<n;i++){
            fruits[i]=Integer.parseInt(st.nextToken());
        }

        Arrays.sort(fruits);

        for(int i=0;i<n;i++){
            if(fruits[i]<=l){
                l++;
            }
        }
        System.out.println(l);
    }
}