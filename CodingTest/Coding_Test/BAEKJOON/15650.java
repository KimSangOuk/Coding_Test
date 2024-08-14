import java.util.*;
import java.lang.*;
import java.io.*;

// The main method must be in a class named "Main".
class Main {
    public static List<int[]> generateCombinations(int[] arr,int m){
        List<int[]> combinations=new ArrayList<>();
        int[] combination=new int[m];
        generateCombination(combinations,0,0,m,arr,combination);

        return combinations;
    }
    public static void generateCombination(List<int[]> combinations,int index,int start,int m,int[] arr,int[] combination){
        if(index==m){
            combinations.add(combination.clone());
            return;
        }
        for(int i=start;i<arr.length;i++){
            combination[index]=arr[i];
            generateCombination(combinations,index+1,i+1,m,arr,combination);
        }
    }

    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        int m=sc.nextInt();
        int[] arr=new int[n];
        for(int i=0;i<n;i++){
            arr[i]=i+1;
        }
        List<int[]> combinations=generateCombinations(arr,m);
        StringBuilder sb=new StringBuilder();
        for(int[] combination :combinations){
            for(int k:combination){
                sb.append(k);
                sb.append(" ");
            }
            sb.append('\n');
        }
        System.out.println(sb.toString());
    }
}