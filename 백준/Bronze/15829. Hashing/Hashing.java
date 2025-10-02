import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());
    int L = Integer.parseInt(st.nextToken());
    String S = br.readLine();
    long result = 0;
    long R = 31;
    long M = 1234567891;
    for (int i = 0; i < L; i++) {
      result += (S.charAt(i) - 'a' + 1) * Math.pow(R, i) % M;
      result %= M;
    }
    System.out.println(result);
  }
}
