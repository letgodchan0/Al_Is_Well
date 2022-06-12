import java.util.ArrayList;
import java.util.Arrays;

class Solution {

	public int solution(int n, int k) {
		String primeNumber = "";
		
		while(true) {
			primeNumber = Integer.toString(n%k) + primeNumber;

			n /= k;
			if (n == 0) {
				break;
			}
		}
		
		ArrayList<String> list = new ArrayList<String>();
		for (int i = 0; i<primeNumber.length(); i++) {
			list.add(String.valueOf(primeNumber.charAt(i)));
		}
		
		ArrayList<String> number = new ArrayList<String>();
		String num = "";
		for(String x : list) {
			if(x.equals("0")) {
				if(!num.equals("")) {
					number.add(num);
					num = "";
				}
			}else {
				num += x;
			}
		}
		if (!num.equals("")) {
			number.add(num);
		}

	
		int cnt = 0;
		for(String x : number) {

			if (isPrime(Long.parseLong(x))) {
				cnt += 1;
			}
		}
		return cnt;
		
	}
	public boolean isPrime(Long n) {
		if (n == 1) {
			return false;
		}
		int number = (int) Math.sqrt(n);
		for (int i = 2; i < number+1; i++) {
			if (n % i ==0) {
				return false;
			}
		}
		return true;
	}
}
