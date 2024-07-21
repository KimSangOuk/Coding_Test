import java.util.*;

class Solution {
    public List<int[]> generateProducts(int[] arr, int repeat){
        List<int[]> products =new ArrayList<>();
        int[] product =new int[repeat];
        generateProduct(arr,products,product,repeat,0);
        return products;
    }
    public void generateProduct(int[] arr,List<int[]> products, int[] product, int repeat, int index){
        if(repeat==index){
            products.add(product.clone());
            return;
        }
        for(int i=0;i<arr.length;i++){
            product[index]=arr[i];
            generateProduct(arr,products,product,repeat,index+1);
        }
    }

    public int[] solution(int n, int[] info) {
        int[] answer = new int[11];
        int maxDiffScore=0;
        int[] arr={0,1};
        List<List<Integer>> answerList=new ArrayList<>();
        List<int[]> caseList=generateProducts(arr,11);
        for(int[] oneCase : caseList){
            int lionScore=0;
            int appeachScore=0;
            int lionShot=n;
            boolean caseTf=true;
            List<Integer> caseResult=new ArrayList<>();
            for(int i=0;i<11;i++){
                if(oneCase[i]==1){
                    if(lionShot>info[i]){
                        lionShot-=info[i]+1;
                        lionScore+=(10-i);
                        caseResult.add(info[i]+1);
                    }else{
                        caseTf=false;
                        break;
                    }
                }else{
                    if(info[i]>0){
                        appeachScore+=(10-i);
                    }
                    caseResult.add(0);
                }
            }
            if(caseTf&&lionScore>appeachScore){
                int index=10;
                while(lionShot>0){
                    if(oneCase[index]==1){
                        lionShot-=1;
                        caseResult.set(index,caseResult.get(index)+1);
                    }else{
                        if(info[index]>caseResult.get(index)+1){
                            lionShot-=1;
                            caseResult.set(index,caseResult.get(index)+1);
                        }else{
                            index-=1;
                        }
                    }
                }
                if(maxDiffScore<Math.abs(lionScore-appeachScore)){
                    maxDiffScore=Math.abs(lionScore-appeachScore);
                    answerList=new ArrayList<>();
                    answerList.add(caseResult);
                }else if(maxDiffScore==Math.abs(lionScore-appeachScore)){
                    answerList.add(caseResult);
                }
            }
        }

        if(maxDiffScore==0){
            return new int[]{-1};
        }

        List<StringBuilder> strList=new ArrayList<>();
        for(List<Integer> k : answerList){
            StringBuilder t=new StringBuilder();
            for(int i=0;i<11;i++){
                t=t.append(k.get(i));
            }
            t.reverse();
            strList.add(t);
        }
        Collections.sort(strList,new Comparator<StringBuilder>(){
            @Override
            public int compare(StringBuilder sb1,StringBuilder sb2){
                return sb1.toString().compareTo(sb2.toString());
            }
        }.reversed());
        int index=0;
        for(String i:strList.get(0).reverse().toString().split("")){
            answer[index++]=Integer.parseInt(i);
        }
        return answer;
    }
}