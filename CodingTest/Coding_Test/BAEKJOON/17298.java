import java.util.*;
import java.io.*;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];

        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }

        Stack<Integer> stack = new Stack<>();
        int[] answer = new int[n];

        for (int i = n - 1; i >= 0; i--) {
            int current = arr[i];
            while (!stack.isEmpty() && stack.peek() <= current) {
                stack.pop();
            }
            if (stack.isEmpty()) {
                answer[i] = -1;
            } else {
                answer[i] = stack.peek();
            }
            stack.push(current);
        }

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < n; i++) {
            sb.append(answer[i]).append(" ");
        }
        System.out.println(sb.toString().trim());
    }
}
