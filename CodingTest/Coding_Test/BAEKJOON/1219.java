import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
    static class Edge {
        int u, v;
        long w;

        Edge(int u, int v, long w) {
            this.u = u;
            this.v = v;
            this.w = w;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int startCity = Integer.parseInt(st.nextToken());
        int endCity = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        List<Edge> edges = new ArrayList<>();
        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            long w = Long.parseLong(st.nextToken());
            edges.add(new Edge(u, v, w));
        }

        long[] income = new long[n];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            income[i] = Long.parseLong(st.nextToken());
        }

        String result = bellmanFord(n, startCity, endCity, edges, income);
        StringBuilder sb = new StringBuilder();
        sb.append(result);
        System.out.println(sb);
    }

    public static String bellmanFord(int n, int startCity, int endCity, List<Edge> edges, long[] income) {
        long INF = Long.MAX_VALUE;
        long[] distance = new long[n];
        Arrays.fill(distance, INF);
        distance[startCity] = -income[startCity];

        for (int i = 0; i < n - 1; i++) {
            for (Edge edge : edges) {
                int u = edge.u;
                int v = edge.v;
                long w = edge.w - income[v];
                if (distance[u] != INF && distance[u] + w < distance[v]) {
                    distance[v] = distance[u] + w;
                }
            }
        }

        boolean[] cycleInfluence = new boolean[n];
        for (Edge edge : edges) {
            int u = edge.u;
            int v = edge.v;
            long w = edge.w - income[v];
            if (distance[u] != INF && distance[u] + w < distance[v]) {
                cycleInfluence[v] = true;
            }
        }

        for (int i = 0; i < n; i++) {
            for (Edge edge : edges) {
                if (cycleInfluence[edge.u]) {
                    cycleInfluence[edge.v] = true;
                }
            }
        }

        if (cycleInfluence[endCity]) {
            return "Gee";
        } else if (distance[endCity] == INF) {
            return "gg";
        } else {
            return String.valueOf(-distance[endCity]);
        }
    }
}
