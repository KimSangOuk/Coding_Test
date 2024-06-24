import java.util.*;
import java.lang.*;
import java.io.*;

class Main {
    public static void main(String[] args) {
        Scanner scanner=new Scanner(System.in);
        char c=scanner.next().charAt(0);
        for(int i=(int)'a';i<=(int)c;i++){
            System.out.printf("%c ",(char)i);
        }
    }
}