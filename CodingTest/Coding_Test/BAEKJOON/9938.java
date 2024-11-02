import java.util.*;
import java.lang.*;
import java.io.*;

// The main method must be in a class named "Main".
class Main {
    public static int findParent(int[] parent, int x){
        if(parent[x]!=x){
            parent[x]=findParent(parent,parent[x]);
        }
        return parent[x];
    }

    public static void unionParent(int[] parent,int a,int b){
        a=findParent(parent,a);
        b=findParent(parent,b);
        if(a>b){
            parent[b]=a;
        }else{
            parent[a]=b;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st=new StringTokenizer(br.readLine());
        int N=Integer.parseInt(st.nextToken());
        int L=Integer.parseInt(st.nextToken());

        int[] parent=new int[L+2];
        for(int i=1;i<L+2;i++){
            parent[i]=i;
        }

        StringBuilder sb=new StringBuilder();

        for(int i=0;i<N;i++){
            st=new StringTokenizer(br.readLine());
            int a=Integer.parseInt(st.nextToken());
            int b=Integer.parseInt(st.nextToken());
            int parentA=findParent(parent,a);
            int parentB=findParent(parent,b);
            int emptyL=findParent(parent,1);
            if(parentA==a){
                unionParent(parent,a,a+1);
                sb.append("LADICA\n");
            }else if(parentB==b){
                unionParent(parent,b,b+1);
                sb.append("LADICA\n");
            }else if(emptyL!=L+1){
                unionParent(parent,emptyL,emptyL+1);
                sb.append("LADICA\n");
            }else{
                sb.append("SMECE\n");
            }
        }

        System.out.println(sb.toString());
    }
}