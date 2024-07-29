import java.util.*;
import java.lang.*;
import java.io.*;

// The main method must be in a class named "Main".
class Main {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        char[] exp=sc.next().toCharArray();
        StringBuilder ans=new StringBuilder();
        Deque<Character> stack = new LinkedList<>();
        for(char c:exp){
            if(Character.isLetter(c)){
                ans.append(c);
            }else if(c=='('){
                stack.addLast(c);
            }else if(c==')'){
                while(!stack.isEmpty()&&stack.getLast()!='('){
                    ans.append(stack.removeLast());
                }
                stack.removeLast();
            }else if(c=='+'||c=='-'){
                while(!stack.isEmpty()&&stack.getLast()!='('){
                    ans.append(stack.removeLast());
                }
                stack.addLast(c);
            }else if(c=='*'||c=='/'){
                while(!stack.isEmpty()&&stack.getLast()!='('&&stack.getLast()!='+'&&stack.getLast()!='-'){
                    ans.append(stack.removeLast());
                }
                stack.addLast(c);
            }
        }
        while(!stack.isEmpty()){
            ans.append(stack.removeLast());
        }
        System.out.println(ans.toString());
    }
}