import java.util.Scanner;

public class Main {
	static int n;
	static int answer = Integer.MAX_VALUE;
	static boolean[] resultArray;
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		n = sc.nextInt();
		String light = sc.next();
		String target = sc.next();
		
		boolean[] lightArray1 = new boolean[n];
		boolean[] lightArray2 = new boolean[n];
		resultArray = new boolean[n];
		
		for (int i=0; i<n; i++) {
			lightArray1[i] = light.charAt(i) != '0';
			lightArray2[i] = light.charAt(i) != '0';
			resultArray[i] = target.charAt(i) != '0';
		}
		
		// 0번 스위치 누르지 않은 경우
		switchChoice(1, 0, lightArray1);
		
		// 0번 스위치 누른 경우
		switchChoice(1, 1, switchUsed(0, lightArray2));
		
		System.out.println(answer == Integer.MAX_VALUE ? -1 : answer);;
	}
	
	static void switchChoice(int idx, int cnt, boolean[] lightArray) {
		if (idx == n) {
			if (lightArray[idx-1] == resultArray[idx-1]) {
				answer = Math.min(answer,  cnt);
			}
			return ;
		}
		if (lightArray[idx-1] != resultArray[idx-1]) {
			switchChoice(idx+1, cnt+1, switchUsed(idx, lightArray));
		} else {
			switchChoice(idx+1, cnt, lightArray);
		}
	}
	
	static boolean[] switchUsed(int idx, boolean[] lightArray) {
		for(int i = idx-1; i <= idx+1; i++) {
			if(i >= 0 && i < n) {
				lightArray[i] = !lightArray[i];
			}
		}
		return lightArray;
	}
}