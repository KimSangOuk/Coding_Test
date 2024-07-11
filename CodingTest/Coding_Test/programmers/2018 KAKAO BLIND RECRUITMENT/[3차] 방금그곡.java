import java.util.*;

class Solution {
    public String solution(String m, String[] musicinfos) {
        String answer = "";
        int longest_play_time=0;

        // m(기억한 멜로디) 분할
        String[] m_split=m.split("");
        ArrayList<StringBuilder> m_list=new ArrayList<>();
        Queue<String> mq=new LinkedList<>();
        for(String s:m_split){
            mq.offer(s);
        }
        int index_m=0;
        while(!mq.isEmpty()){
            String s=mq.poll();
            if(!s.equals("#")){
                m_list.add(new StringBuilder(s));
                index_m+=1;
            }else{
                m_list.get(index_m-1).append(s);
            }
        }
        for(int i=0;i<musicinfos.length;i++){
            String[] arr=musicinfos[i].split(",");
            int hour_diff=Integer.parseInt(arr[1].substring(0,2))-Integer.parseInt(arr[0].substring(0,2));
            int minute_diff=Integer.parseInt(arr[1].substring(3,5))-Integer.parseInt(arr[0].substring(3,5));
            int play_time=hour_diff*60+minute_diff;
            String title=arr[2];

            String[] melody_split=arr[3].split("");
            // 이게 노래가 분할된거
            ArrayList<StringBuilder> melody_list=new ArrayList<>();
            Queue<String> q=new LinkedList<>();
            for(String s:melody_split){
                q.offer(s);
            }
            int index_melody=0;
            while(!q.isEmpty()){
                String s=q.poll();
                if(!s.equals("#")){
                    melody_list.add(new StringBuilder(s));
                    index_melody+=1;
                }else{
                    melody_list.get(index_melody-1).append(s);
                }
            }
            ArrayList<StringBuilder> total_melody=new ArrayList<>();
            for(int t=0;t<play_time;t++){
                total_melody.add(melody_list.get(t%melody_list.size()));
            }
            for(int start=0;start<total_melody.size();start++){
                boolean tf=true;
                for(int st=0;st<m_list.size();st++){
                    if(start+st>=total_melody.size() || !total_melody.get(st+start).toString().equals(m_list.get(st).toString()))                     {
                        tf=false;
                        break;
                    }
                }
                if(tf){
                    if(longest_play_time<play_time){
                        longest_play_time=play_time;
                        answer=title;
                    }
                    break;
                }
            }
        }
        if(answer.equals("")){
            answer="(None)";
        }

        return answer;
    }