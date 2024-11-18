import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int[] arr = new int[n];

        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }

        int answer = Integer.MAX_VALUE;

        for (int i = 0; i < n - 1; i++) {
            answer = binarySearch(arr, i, i + 1, n - 1, answer);
            if (answer == 0) {
                break;
            }
        }

        System.out.println(answer);
    }

    private static int binarySearch(int[] arr, int targetIdx, int start, int end, int answer) {
        while (start <= end) {
            int mid = (start + end) / 2;
            int sum = arr[mid] + arr[targetIdx];

            if (sum == 0) {
                return 0;
            } else if (sum < 0) {
                start = mid + 1;
            } else {
                end = mid - 1;
            }

            if (Math.abs(sum) < Math.abs(answer)) {
                answer = sum;
            }
        }
        return answer;
    }
}
