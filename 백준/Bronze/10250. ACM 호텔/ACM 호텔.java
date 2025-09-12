import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());

    int T = Integer.parseInt(st.nextToken());

    for (int i = 0; i < T; i++) {
      st = new StringTokenizer(br.readLine());
      int H = Integer.parseInt(st.nextToken());
      int W = Integer.parseInt(st.nextToken());
      int N = Integer.parseInt(st.nextToken());

      int floor = N % H;
      int room = N / H + 1;

      if (floor == 0) {
        floor = H;
        room -= 1;
      }

      System.out.println(floor * 100 + room);
    }
  }
}
