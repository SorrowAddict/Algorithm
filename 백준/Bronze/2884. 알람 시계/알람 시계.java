import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    String[] input = br.readLine().split(" ");
    int H = Integer.parseInt(input[0]);
    int M = Integer.parseInt(input[1]);
    
    if (M - 45 < 0) {
      if (H - 1 < 0) {
        System.out.println((H - 1 + 24) + " " + (M - 45 + 60));
      } else {
        System.out.println((H - 1) + " " + (M - 45 + 60));
      }
    } else {
      System.out.println(H + " " + (M - 45));
    }
  }
}
