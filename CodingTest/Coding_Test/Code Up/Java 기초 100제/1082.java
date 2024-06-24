import java.util.*;
import java.lang.*;
import java.io.*;

class Main {
    public static void main(String[] args) {
        Scanner scanner=new Scanner(System.in);
        String s=scanner.next();
        int k=Integer.parseInt(s,16);
        for(int i=1;i<16;i++){
            System.out.printf("%X*%X=%X\n",k,i,k*i);
        }
    }
}