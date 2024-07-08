import java.util.*;
import java.lang.*;
import java.io.*;
import java.math.*;

// The main method must be in a class named "Main".
class Main {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        String s=sc.next();
        String k=new StringBuilder(s).reverse().toString();
        if(s.equals(k)){
            System.out.println(1);
        }else{
            System.out.println(0);
        }
    }
}