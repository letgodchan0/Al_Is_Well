public int solution(String s){

    String[] strArray = {"zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
    "nine"};
    String[] numArray = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"};

    for (int i = 0; i < strArray.length; i++) {
      s = s.replaceAll(strArray[i], numArray[i]);
    }
    return Integer.parseInt(s);