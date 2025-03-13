import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int N = Integer.parseInt(input.readLine());
        HashMap<String, Integer> h = new HashMap<>();
        int max = 1;
        for (int i = 0; i < N; i++) {
            String s = input.readLine();
            int temp = 0;
            h.put(s, (h.containsKey(s)) ? temp = h.get(s)+1 : 1);
            max = Math.max(max, temp);
        }
        HashSet<String> set = new HashSet<>();
        for (String s : h.keySet())
            if(h.get(s) == max) set.add(s);
        List<String> list = new ArrayList<>(set);
        Collections.sort(list);
        bw.write(list.get(0));
        bw.flush();
        bw.close();
        input.close();
    }
}
