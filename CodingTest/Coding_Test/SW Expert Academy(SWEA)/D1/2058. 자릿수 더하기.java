import java.util.*;
import java.io.FileInputStream;

class Solution
{
    public static void main(String args[]) throws Exception
    {
        Scanner s=new Scanner(System.in);
        String str=s.next();
        int answer=0;
        for(int i=0;i<str.length();i++){
            answer+=str.charAt(i)-'0';
        }
        System.out.println(answer);
    }
}