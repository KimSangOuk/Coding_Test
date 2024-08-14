import java.util.*;
import java.lang.*;
import java.io.*;

// The main method must be in a class named "Main".
class Main {

    public static List<int[]> generateCombinations(int[] arr,int m){
        List<int[]> combinations=new ArrayList<int[]>();
        int[] combination=new int[m];
        generateCombination(combinations,0,0,m,arr,combination);

        return combinations;
    }

    public static void generateCombination(List<int[]> combinations,int start,int index,int m,int[] arr,int[] combination){
        if(index==m){
            combinations.add(combination.clone());
            return;
        }
        for(int i=start;i<arr.length;i++){
            combination[index]=arr[i];
            generateCombination(combinations,i+1,index+1,m,arr,combination);
        }
    }

    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        int[] arr=new int[n];
        for(int i=0;i<n;i++){
            arr[i]=i;
        }

        int[][] food=new int[n][2];
        for(int i=0;i<n;i++){
            food[i][0]=sc.nextInt();
            food[i][1]=sc.nextInt();
        }

        double answer=1000000000;
        for(int i=1;i<n+1;i++){
            List<int[]> combinations=generateCombinations(arr,i);
            for(int[] combination : combinations){
                double s=1;
                double b=0;
                for(int k : combination){
                    s*=food[k][0];
                    b+=food[k][1];
                }
                answer=Math.min(answer,Math.abs(s-b));
            }
        }
        System.out.println((int)answer);

    }
}