import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    int N = Integer.parseInt(br.readLine());
    int cnt = 0;

    for (int i = 1; i < N + 1; i++) {
      String str = Integer.toString(i);
      if (str.length() < 3) {
        cnt++;
      } else {
        Integer[] arr = new Integer[str.length()];
        for (int j = 0; j < str.length(); j++) {
          arr[j] = Integer.parseInt(String.valueOf(str.charAt(j)));
        }
        if (arr[0] - arr[1] == arr[1] - arr[2]) {
          cnt++;
        }
      }
    }
    System.out.println(cnt);
  }
}
