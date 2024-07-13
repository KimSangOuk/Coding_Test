import java.util.*;

class Solution {

    public static boolean check(String[][] board,List<int[]> people){

        int numOfPeople=people.size();
        for(int i=0;i<numOfPeople-1;i++){
            int x1=people.get(i)[0];
            int y1=people.get(i)[1];
            for(int j=i+1;j<numOfPeople;j++){
                int x2=people.get(j)[0];
                int y2=people.get(j)[1];
                int dist=Math.abs(x1-x2)+Math.abs(y1-y2);
                if(dist>2){
                    continue;
                }else if(dist<2){
                    return false;
                }else if(dist==2){
                    if((x1-x2)==0){
                        if(board[x1][(y1+y2)/2].equals("X")){
                            continue;
                        }else{
                            return false;
                        }
                    }else if((y1-y2)==0){
                        if(board[(x1+x2)/2][y1].equals("X")){
                            continue;
                        }else{
                            return false;
                        }
                    }else if(Math.abs(x1-x2)==1&&Math.abs(y1-y2)==1){
                        if(board[x1][y2].equals("X")&&board[x2][y1].equals("X")){
                            continue;
                        }else{
                            return false;
                        }
                    }
                }
            }
        }

        return true;
    }

    public int[] solution(String[][] places) {
        int[] answer = new int[5];

        for(int tc=0;tc<5;tc++){
            String[] k=places[tc];
            String[][] board=new String[5][5];
            List<int[]> people=new ArrayList<>();
            for(int i=0;i<5;i++){
                String[] tmp=k[i].split("");
                for(int j=0;j<5;j++){
                    if(tmp[j].equals("P")){
                        people.add(new int[]{i,j});
                    }
                }
                board[i]=tmp;
            }
            if(check(board,people)){
                answer[tc]=1;
            }
        }

        return answer;
    }
}