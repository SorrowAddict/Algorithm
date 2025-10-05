import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    Long s = Long.parseLong(br.readLine());
    Long sum = 0L;
    int i = 1;
    while (s >= i) {
      s -= i;
      sum++; i++;
    }
    System.out.println(sum);
  }
}
