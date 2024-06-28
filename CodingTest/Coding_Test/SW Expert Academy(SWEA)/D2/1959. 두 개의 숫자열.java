import java.util.Scanner;
import java.io.FileInputStream;

class Solution
{
  public static void main(String args[]) throws Exception
  {
    Scanner s=new Scanner(System.in);
        int tc=s.nextInt();
        for(int i=1;i<=tc;i++){
            int n=s.nextInt();
            int m=s.nextInt();
            int[] arr1=new int[n];
            int[] arr2=new int[m];
            for(int j=0;j<n;j++){
                arr1[j]=s.nextInt();
            }
            for(int j=0;j<m;j++){
                arr2[j]=s.nextInt();
            }
            int answer=0;
            if(n<m){
                for(int j=0;j<m-n+1;j++){
                    int sum=0;
                    for(int k=0;k<n;k++){
                        sum+=arr1[k]*arr2[j+k];
                    }
                    if(answer<sum){
                        answer=sum;
                    }
                }
            }else{
                for(int j=0;j<n-m+1;j++){
                    int sum=0;
                    for(int k=0;k<m;k++){
                        sum+=arr2[k]*arr1[j+k];
                    }
                    if(answer<sum){
                        answer=sum;
                    }
                }
            }
            System.out.printf("#%d %d\n",i,answer);
        }
  }
}