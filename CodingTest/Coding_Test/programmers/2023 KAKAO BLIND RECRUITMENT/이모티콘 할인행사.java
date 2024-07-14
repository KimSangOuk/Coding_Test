import java.util.*;

class Solution {
    public static List<int[]> generateProducts(int[] arr,int r){
        List<int[]> products=new ArrayList<>();
        int[] product=new int[r];
        generateProduct(arr,r,product,0,products);

        return products;
    }

    public static void generateProduct(int[] arr,int r,int[] product, int index,List<int[]> products){
        if(r==index){
            products.add(product.clone());
            return;
        }
        for(int i=0;i<arr.length;i++){
            product[index]=arr[i];
            generateProduct(arr,r,product,index+1,products);
        }
    }

    public int[] solution(int[][] users, int[] emoticons) {
        int[] answer = {};
        int[] percentList={10,20,30,40};
        List<int[]> allCases=generateProducts(percentList,emoticons.length);
        int caseMaxServiceOwnerNum=0;
        int caseMaxTotal=0;
        for(int[] oneCase:allCases){
            int caseServiceOwner=0;
            int caseTotal=0;
            for(int[] user:users){
                int oneUserTotal=0;
                boolean userServiceOwned=false;
                for(int i=0;i<emoticons.length;i++){
                    if(oneCase[i]>=user[0]){
                        oneUserTotal+=(emoticons[i])*(100-oneCase[i])/100;
                    }
                    if(oneUserTotal>=user[1]){
                        caseServiceOwner+=1;
                        userServiceOwned=true;
                        break;
                    }
                }
                if(!userServiceOwned){
                    caseTotal+=oneUserTotal;
                }
            }
            if(caseServiceOwner>caseMaxServiceOwnerNum){
                caseMaxServiceOwnerNum=caseServiceOwner;
                caseMaxTotal=caseTotal;
            }else if(caseServiceOwner==caseMaxServiceOwnerNum&&caseTotal>caseMaxTotal){
                caseMaxTotal=caseTotal;
            }
        }

        answer=new int[]{caseMaxServiceOwnerNum,caseMaxTotal};
        return answer;
    }
}