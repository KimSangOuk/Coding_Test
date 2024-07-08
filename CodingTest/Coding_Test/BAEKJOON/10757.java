import java.util.*;
import java.lang.*;
import java.io.*;
import java.math.*;

// The main method must be in a class named "Main".
class Main {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        BigInteger a=new BigInteger(sc.next());
        BigInteger b= new BigInteger(sc.next());
        System.out.println(a.add(b));
    }
}