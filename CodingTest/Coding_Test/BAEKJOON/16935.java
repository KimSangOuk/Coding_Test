import java.util.*;
import java.lang.*;
import java.io.*;

// The main method must be in a class named "Main".
class Main {
    static int[][] oper_arr(int[] oper,int[][] arr){
        for(int i=0;i<oper.length;i++){
            // System.out.println(oper[i]);
            switch(oper[i]){
                case 1:
                    arr=oper1(arr);
                    break;
                case 2:
                    arr=oper2(arr);
                    break;
                case 3:
                    arr=oper3(arr);
                    break;
                case 4:
                    arr=oper4(arr);
                    break;
                case 5:
                    arr=oper5(arr);
                    break;
                case 6:
                    arr=oper6(arr);
                    break;
            }
        }
        return arr;
    }
    static int[][] oper1(int[][] arr){
        int n=arr.length;
        int m=arr[0].length;
        int[][] new_arr=new int[n][m];
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                new_arr[n-1-i][j]=arr[i][j];
            }
        }

        return new_arr;
    }

    static int[][] oper2(int[][] arr){
        int n=arr.length;
        int m=arr[0].length;
        int[][] new_arr=new int[n][m];
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                new_arr[i][m-1-j]=arr[i][j];
            }
        }
        return new_arr;
    }

    static int[][] oper3(int[][] arr){
        int n=arr.length;
        int m=arr[0].length;
        int[][] new_arr=new int[m][n];
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                new_arr[j][n-1-i]=arr[i][j];
            }
        }
        return new_arr;
    }

    static int[][] oper4(int[][] arr){
        int n=arr.length;
        int m=arr[0].length;
        int[][] new_arr=new int[m][n];
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                new_arr[m-1-j][i]=arr[i][j];
            }
        }
        return new_arr;
    }

    static int[][] oper5(int[][] arr){
        int n=arr.length;
        int m=arr[0].length;
        int[][] new_arr=new int[n][m];
        for(int i=0;i<n/2;i++){
            for(int j=0;j<m/2;j++){
                new_arr[i][j+m/2]=arr[i][j];
            }
        }
        for(int i=0;i<n/2;i++){
            for(int j=0;j<m/2;j++){
                new_arr[i+n/2][j+m/2]=arr[i][j+m/2];
            }
        }
        for(int i=0;i<n/2;i++){
            for(int j=0;j<m/2;j++){
                new_arr[i+n/2][j]=arr[i+n/2][j+m/2];
            }
        }
        for(int i=0;i<n/2;i++){
            for(int j=0;j<m/2;j++){
                new_arr[i][j]=arr[i+n/2][j];
            }
        }

        return new_arr;
    }

    static int[][] oper6(int[][] arr){
        int n=arr.length;
        int m=arr[0].length;
        int[][] new_arr=new int[n][m];
        for(int i=0;i<n/2;i++){
            for(int j=0;j<m/2;j++){
                new_arr[i][j]=arr[i][j+m/2];
            }
        }
        for(int i=0;i<n/2;i++){
            for(int j=0;j<m/2;j++){
                new_arr[i][j+m/2]=arr[i+n/2][j+m/2];
            }
        }
        for(int i=0;i<n/2;i++){
            for(int j=0;j<m/2;j++){
                new_arr[i+n/2][j+m/2]=arr[i+n/2][j];
            }
        }
        for(int i=0;i<n/2;i++){
            for(int j=0;j<m/2;j++){
                new_arr[i+n/2][j]=arr[i][j];
            }
        }

        return new_arr;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st=new StringTokenizer(br.readLine());
        int n=Integer.parseInt(st.nextToken());
        int m=Integer.parseInt(st.nextToken());
        int r=Integer.parseInt(st.nextToken());
        int[] opers=new int[r];
        int[][] arr=new int[n][m];
        for(int i=0;i<n;i++){
            st=new StringTokenizer(br.readLine());
            for(int j=0;j<m;j++){
                arr[i][j]=Integer.parseInt(st.nextToken());
            }
        }
        st=new StringTokenizer(br.readLine());
        for(int i=0;i<r;i++){
            opers[i]=Integer.parseInt(st.nextToken());
        }
        arr=oper_arr(opers,arr);
        StringBuilder sb=new StringBuilder();
        for(int i=0;i<arr.length;i++){
            for(int j=0;j<arr[0].length;j++){
                sb.append(arr[i][j]);
                sb.append(" ");
            }
            sb.append("\n");
        }
        System.out.println(sb.toString());
    }
}