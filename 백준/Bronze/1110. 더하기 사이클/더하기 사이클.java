import java.io.*;

public class Main {
  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    int N = Integer.parseInt(br.readLine());
    int tmp = N;
    int cnt = 0;

    while (true) {
      int a = tmp / 10;
      int b = tmp % 10;
      int c = (a + b) % 10;
      tmp = (b * 10) + c;
      cnt++;
      if (tmp == N) {
        System.out.println(cnt);
        break;
      }
    }
  }
}
