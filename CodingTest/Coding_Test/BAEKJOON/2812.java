import java.util.*;
import java.lang.*;
import java.io.*;

// The main method must be in a class named "Main".
class Main {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        int k=sc.nextInt();
        String[] num=sc.next().split("");
        Stack<String> stack=new Stack<>();
        int lastL=num.length;
        int curL=0;
        for(int i=0;i<num.length;i++){
            if(stack.isEmpty()){
                stack.push(num[i]);
                lastL--;
                curL++;
                continue;
            }
            if(lastL+curL<=n-k||Integer.parseInt(stack.peek())>=Integer.parseInt(num[i])){
                if(curL<n-k){
                    stack.push(num[i]);
                    curL++;
                    lastL--;
                }
            }else{
                while(!stack.isEmpty()&&lastL+curL>n-k&&Integer.parseInt(stack.peek())<Integer.parseInt(num[i])){
                    stack.pop();
                    curL--;
                }
                stack.push(num[i]);
                curL++;
                lastL--;
            }
        }
        // System.out.println(stack.toString());
        StringBuilder sb=new StringBuilder();
        for(int i=0;i<stack.size();i++){
            sb.append(stack.get(i));
            // System.out.println(stack.get(i));
        }
        System.out.println(sb.toString());
    }
}