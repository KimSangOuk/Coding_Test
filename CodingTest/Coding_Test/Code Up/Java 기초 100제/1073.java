import java.util.*;
import java.lang.*;
import java.io.*;

class Main {
    public static void main(String[] args) {
        Scanner scanner=new Scanner(System.in);
        for(int i=0;;i++){
            int t=scanner.nextInt();
            if(t==0){
                break;
            }
            System.out.printf("%d\n",t);
        }
    }
}