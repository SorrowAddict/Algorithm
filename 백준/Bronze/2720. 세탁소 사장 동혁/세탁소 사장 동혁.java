import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	public static void main(String[] args) throws IOException {
			BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
			int T = Integer.parseInt(br.readLine());
			StringBuilder sb = new StringBuilder();
			for (int t = 0; t < T; t++) {
				int C = Integer.parseInt(br.readLine());
				int quarters = C / 25;
				C %= 25;
				int dimes = C / 10;
				C %= 10;
				int nickels = C / 5;
				C %= 5;
				int pennies = C;
				sb.append(quarters + " " + dimes + " " + nickels + " " + pennies + "\n");
			}
			System.out.print(sb.toString());
	}
}
