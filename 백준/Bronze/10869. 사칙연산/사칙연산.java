import java.io.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String[] str = br.readLine().split(" ");
        int A = Integer.parseInt(str[0]);
        int B = Integer.parseInt(str[1]);

        bw.write(A + B + "\n");
        bw.write(A - B + "\n");
        bw.write(A * B + "\n");
        bw.write(A / B + "\n");
        bw.write(A % B + "\n");
        bw.flush();
        bw.close();
    }
}
