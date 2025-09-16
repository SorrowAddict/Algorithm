import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    int A = Integer.parseInt(br.readLine());
    int B = Integer.parseInt(br.readLine());
    int C = Integer.parseInt(br.readLine());
    int ABC = A * B * C;
    int[] arr = new int[10];

    while (ABC > 0) {
      arr[ABC % 10]++;
      ABC /= 10;
    }
    for (int i : arr) {
      System.out.println(i);
    }
  }
}
