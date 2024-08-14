import java.util.*;
import java.lang.*;
import java.io.*;

// The main method must be in a class named "Main".
class Main {
    public static List<int[]> generatePermutations(int[] arr,int m){
        List<int[]> permuations=new ArrayList<>();
        int[] permuation=new int[m];
        boolean[] visited=new boolean[arr.length];
        generatePermutation(permuations,0,m,arr,visited,permuation);

        return permuations;
    }
    public static void generatePermutation(List<int[]> permuations,int index,int m,int[] arr,boolean[] visited,int[] permuation){
        if(index==m){
            permuations.add(permuation.clone());
            return;
        }
        for(int i=0;i<arr.length;i++){
            if(!visited[i]){
                visited[i]=true;
                permuation[index]=arr[i];
                generatePermutation(permuations,index+1,m,arr,visited,permuation);
                visited[i]=false;
            } 
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
        List<int[]> permuations=generatePermutations(arr,m);
        StringBuilder sb=new StringBuilder();
        for(int[] permuation :permuations){
            for(int k:permuation){
                sb.append(k);
                sb.append(" ");
            }
            sb.append('\n');
        }
        System.out.println(sb.toString());
    }
}