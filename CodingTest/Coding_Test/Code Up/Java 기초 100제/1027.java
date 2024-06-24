import java.util.*;
import java.lang.*;
import java.io.*;

class Main {
    public static void main(String[] args) {
        Scanner s=new Scanner(System.in);
        String[] t=s.nextLine().split("\\.");
        System.out.printf("%02d-%02d-%04d",Integer.parseInt(t[2]),Integer.parseInt(t[1]),Integer.parseInt(t[0]));
    }
}