import java.util.*;

class Solution {
    public ArrayList<Integer>[] graphs;
    public boolean[][][] visited;
    public int answer = 1;
    public int[] infos;
    
    public int solution(int[] info, int[][] edges) {
        graphs = new ArrayList[info.length];
        
        for(int i = 0; i < info.length; i++){
            graphs[i] = new ArrayList<>();
        }
        
        for(int i = 0; i < edges.length; i++){
            int[] edge = edges[i];

            graphs[edge[0]].add(edge[1]);
            graphs[edge[1]].add(edge[0]);
        }
        
        visited = new boolean[info.length][info.length+1][info.length+1];
        infos = info;
        visited[0][0][0] = true;
        dfs(0,0,0);
        return answer;
    }
    
    public void dfs(int idx, int sheep, int wolf){
        

        if(infos[idx] != -1){
            if(infos[idx] == 0){
                temp = 0;
                sheep++;
            }else{
                temp = 1;
                wolf++;
            }
        }
        

        if(sheep <= wolf){
            return;
        }else{
            answer = Math.max(answer,sheep);
        }
        

        for(int i = 0; i < graphs[idx].size(); i++){
            int next = graphs[idx].get(i);

            if(visited[next][sheep][wolf] == true){
                continue;
            }

            infos[idx] = -1;

            visited[idx][sheep][wolf] = true;
            dfs(next,sheep,wolf);

            infos[idx] = temp;
            visited[idx][sheep][wolf] = false;
        }
    }
}