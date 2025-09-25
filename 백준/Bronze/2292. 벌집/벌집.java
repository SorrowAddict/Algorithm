import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    int n = Integer.parseInt(br.readLine());
    int range = 1;
    int count = 1;
    while (n > range) {
      range += 6 * count;
      count++;
    }
    System.out.println(count);
    br.close();
  }
}
