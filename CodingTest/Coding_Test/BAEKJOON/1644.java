import java.util.*;
import java.lang.*;
import java.io.*;

// The main method must be in a class named "Main".
class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());

        // N이 1일 경우 예외 처리
        if (N == 1) {
            System.out.println(0);
            return;
        }

        boolean[] isPrime = new boolean[N + 1];
        Arrays.fill(isPrime, true);
        isPrime[1] = false;
        isPrime[0] = false;

        for (int i = 2; i <= Math.sqrt(N); i++) {
            if (isPrime[i]) {
                for (int j = i * i; j <= N; j += i) {
                    isPrime[j] = false;
                }
            }
        }

        List<Integer> primes = new ArrayList<>();
        for (int i = 2; i <= N; i++) {
            if (isPrime[i]) {
                primes.add(i);
            }
        }

        // 소수 리스트가 비어 있는 경우 예외 처리
        if (primes.isEmpty()) {
            System.out.println(0);
            return;
        }

        int startIdx = 0;
        int endIdx = 0;
        int answer = 0;
        int sum = primes.get(0);

        while (true) {
            if (sum <= N) {
                if (sum == N) {
                    answer++;
                }
                if (endIdx >= primes.size() - 1) {
                    break;
                }
                endIdx++;
                sum += primes.get(endIdx);
            } else {
                sum -= primes.get(startIdx);
                startIdx++;
                if (startIdx >= primes.size()) break;
            }
        }
        System.out.println(answer);
    }
}
