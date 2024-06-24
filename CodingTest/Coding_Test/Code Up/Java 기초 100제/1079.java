import java.util.*;
import java.lang.*;
import java.io.*;

class Main {
    public static void main(String[] args) {
        Scanner scanner=new Scanner(System.in);

        while(true){
            char c=scanner.next().charAt(0);
            if(c=='q'){
                System.out.printf("%c",c);
            }
        }
    }
}