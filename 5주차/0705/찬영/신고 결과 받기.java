public class PRO신고결과받기 {
    public static void main(String[] args) {
        //입력값 예시
        String[] id_list ={"muzi", "frodo", "apeach", "neo"};
        String[] report ={"muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"};
        int k =2;

        boolean[][] singo = new boolean[id_list.length][id_list.length];
        int[] cnt = new int[id_list.length];
        int[] answer = new int[id_list.length];
        
        for (int i = 0; i < report.length; i++) {
            int user = findUseridx(id_list, report[i].split(" ")[0]);
            int bad =findUseridx(id_list, report[i].split(" ")[1]);

            singo[user][bad] = true;
        }
        
        for (int i = 0; i < id_list.length; i++) {
            for (int j = 0; j < id_list.length; j++) {
                if(singo[i][j]==true){
                    cnt[j]++;
                }
            }
        }

        System.out.print("신고 당한 횟수: "+" ");
        for (int i = 0; i < cnt.length; i++) {
            System.out.print(cnt[i]+" ");
        }
        System.out.println();


        for (int i = 0; i < id_list.length; i++) {
            if(cnt[i]>=k){
                for (int j = 0; j < id_list.length; j++) {

                    if(singo[j][i]==true) answer[j]++;
                }
            }
        }

        System.out.print("답: "+" ");
        for (int i = 0; i < answer.length; i++) {
            System.out.print(answer[i] + " ");
        }
    }
    
    private static int findUseridx(String[] id_list, String name) {
        for(int i=0; i<id_list.length; i++)
        {
            if(id_list[i].equals(name))
                return i;
        } return -1;

    }
}