import java.util.*;
import java.lang.*;
import java.io.*;

class Main {
    public static void main(String[] args) {
        Scanner scanner=new Scanner(System.in);
        char a=scanner.next().charAt(0);

        if(a=='A'){
            System.out.printf("best!!!\n");
        }else if(a=='B'){
            System.out.printf("good!!\n");
        }else if(a=='C'){
            System.out.printf("run!\n");
        }else if(a=='D'){
            System.out.printf("slowly~\n");
        }else{
            System.out.printf("what?\n");
        }
    }
}