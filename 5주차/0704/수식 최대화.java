import java.util.*;
class Solution {
    static char[] cmd = {'+', '-', '*'};
    static ArrayList<Long> nums;
    static ArrayList<Character> cmds;
    static  long answer = 0;
    public long solution(String expression) {
        refine(expression);
        permutation(0, new char[3], new boolean[3]);
        return answer;
    }
    static void refine(String ex){
        nums = new ArrayList<>();
        cmds = new ArrayList<>();
        String temps[] = ex.split("[-+*]");
        for(String s: temps){
            nums.add(Long.valueOf(s));
        }        
        for(int i=0; i<ex.length(); i++){
            if(ex.charAt(i)=='+' || ex.charAt(i)=='*'||ex.charAt(i)=='-'){
                cmds.add(ex.charAt(i));
            }
        }
    }
    static void permutation(int depth, char array[], boolean visited[]){
        if(depth == 3){
            long res=Math.abs(simulation(array));
            answer=Math.max(answer, res);
            return;
        }
        for(int i=0; i<3; i++){
            if(visited[i]) continue;
            visited[i] = true;
            array[depth] = cmd[i];
            permutation(depth+1, array, visited);
            visited[i] = false;
            array[depth] = '0';
        }
    }
    static long simulation(char array[]){
        ArrayList<Long> copynums = new ArrayList<>();
        ArrayList<Character> copycmds = new ArrayList<>();
        copynums.addAll(nums);
        copycmds.addAll(cmds);
        for(char target: array){
            while(copycmds.size()>0){
                boolean flag = false;
                for(int i=0; i<copycmds.size(); i++){
                    if(copycmds.get(i)==target){
                        long temp = calc(copynums.get(i), copynums.get(i+1), target);
                        copynums.remove(i);copynums.remove(i);
                        copynums.add(i, temp);
                        copycmds.remove(i);
                        flag = true;
                        break;
                    }
                }
                if(!flag)
                    break;
            }
        }
        return copynums.get(0);
    }
    static long calc(long o1, long o2, char cmd){
        switch(cmd){
            case '+':
                return o1+o2;
            case '-':
                return o1-o2;
            case '*':
                return o1*o2;
            default:
                return 0;
        }
    }
}
출처: https://moons-memo.tistory.com/181 [devmoon 알고리즘:티스토리]