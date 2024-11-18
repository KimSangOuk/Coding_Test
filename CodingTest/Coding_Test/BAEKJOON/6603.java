import java.util.*;
import java.lang.*;
import java.io.*;

// The main method must be in a class named "Main".
class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb=new StringBuilder();
        while(true){
            StringTokenizer st=new StringTokenizer(br.readLine());
            int k=Integer.parseInt(st.nextToken());
            if(k==0)break;
            int[] arr=new int[k];
            for(int i=0;i<k;i++){
                arr[i]=Integer.parseInt(st.nextToken());
            }
            printCombinations(arr,k,sb);
            sb.append("\n");
        }
        System.out.println(sb.toString());
    }

    public static void printCombinations(int[] arr, int k, StringBuilder sb){
        int[] combination=new int[k];
        makeCombination(arr,combination,0,0,sb);
    }

    public static void makeCombination(int[] arr, int[] combination, int start, int index, StringBuilder sb){
        if(index==6){
            for(int i=0;i<6;i++){
                sb.append(Integer.toString(combination[i])+" ");
            }
            sb.append("\n");
            return;
        }
        for(int i=start;i<=arr.length-6+index;i++){
            combination[index]=arr[i];
            makeCombination(arr,combination,i+1,index+1,sb);
        }
    }
}