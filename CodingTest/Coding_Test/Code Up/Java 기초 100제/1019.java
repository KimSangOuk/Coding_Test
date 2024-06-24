import java.util.*;
import java.lang.*;
import java.io.*;

class Main {
    public static void main(String[] args) {
        Scanner s=new Scanner(System.in);
        String[] t=s.nextLine().split("\\.");
        System.out.printf("%04d.%02d.%02d",Integer.parseInt(t[0]),Integer.parseInt(t[1]),Integer.parseInt(t[2]));
    }
}