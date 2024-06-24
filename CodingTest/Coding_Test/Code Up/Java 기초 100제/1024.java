import java.util.*;
import java.lang.*;
import java.io.*;

class Main {
    public static void main(String[] args) {
        Scanner s=new Scanner(System.in);
        String t=s.nextLine();
        for(char k:t.toCharArray()){
            System.out.printf("\'%c\'\n",k);
        }
    }
}