import java.util.*;
import java.lang.*;
import java.io.*;

class Main {
    public static void main(String[] args) {
        Scanner s=new Scanner(System.in);
        String t=s.nextLine();
        int start=10000;
        for(char k:t.toCharArray()){
            System.out.printf("[%d]\n",(int)(k-'0')*start);
            start/=10;
        }
    }
}