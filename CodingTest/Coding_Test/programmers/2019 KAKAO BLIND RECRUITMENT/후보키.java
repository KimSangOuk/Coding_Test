import java.util.*;

class Solution {

    static public List<int[]> generateCombinations(int[] arr, int r) {
        List<int[]> combinations = new ArrayList<>();
        int[] combination = new int[r];
        generateCombination(arr, combination, 0, 0, r, combinations);
        return combinations;
    }

    static public void generateCombination(int[] arr, int[] combination, int start, int index, int r, List<int[]> combinations) {
        if (index == r) {
            combinations.add(combination.clone());
            return;
        }
        for (int i = start; i <= arr.length - r + index; i++) {
            combination[index] = arr[i];
            generateCombination(arr, combination, i + 1, index + 1, r, combinations);
        }
    }

    public int solution(String[][] relation) {
        int answer = 0;

        int c = relation[0].length;
        int r = relation.length;
        List<int[]> uniqueCases = new ArrayList<>();
        int[] by_num_list = new int[c];
        for (int i = 0; i < c; i++) {
            by_num_list[i] = i;
        }

        for (int j = 1; j <= c; j++) {
            List<int[]> cases = generateCombinations(by_num_list, j);
            for (int[] cs : cases) {
                HashSet<String> keys = new HashSet<>();
                for (int i = 0; i < r; i++) {
                    StringBuilder oneKey = new StringBuilder();
                    for (int k : cs) {
                        oneKey.append(relation[i][k]).append(",");
                    }
                    keys.add(oneKey.toString());
                }

                if (keys.size() == r) {  // 유일성 확인
                    boolean minimality = true;
                    for (int[] uc : uniqueCases) {
                        // 기존의 후보키가 현재 cs의 부분집합인지 확인
                        boolean isSubset = true;
                        for (int ucElem : uc) {
                            boolean found = false;
                            for (int cElem : cs) {
                                if (ucElem == cElem) {
                                    found = true;
                                    break;
                                }
                            }
                            if (!found) {
                                isSubset = false;
                                break;
                            }
                        }
                        if (isSubset) {
                            minimality = false;
                            break;
                        }
                    }
                    if (minimality) {
                        uniqueCases.add(cs);
                        answer++;
                    }
                }
            }
        }

        return answer;
    }
}
