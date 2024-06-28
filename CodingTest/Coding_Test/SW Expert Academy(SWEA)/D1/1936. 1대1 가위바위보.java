import java.util.Scanner;
import java.io.FileInputStream;


class Solution
{
  public static void main(String args[]) throws Exception
  {
    Scanner s=new Scanner(System.in);
        int a=s.nextInt();
        int b=s.nextInt();
        if((a==1 && b==3)||(!(a==1&&b==3)&&(a>b))){
            System.out.println('A');
        }else{
            System.out.println('B');
        }
  }
}