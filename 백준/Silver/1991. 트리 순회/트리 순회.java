import java.io.*;
import java.util.*;

public class Main {
    static class Node {
        char value;
        Node left;
        Node right;

        Node(char value) {
            this.value = value;
        }
    }

    static void preorder(Node node) {
        if (node != null) {
            System.out.print(node.value);
            preorder(node.left);
            preorder(node.right);
        }
    }

    static void inorder(Node node) {
        if (node != null) {
            inorder(node.left);
            System.out.print(node.value);
            inorder(node.right);
        }
    }

    static void postorder(Node node) {
        if (node != null) {
            postorder(node.left);
            postorder(node.right);
            System.out.print(node.value);
        }
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        Map<Character, Node> tree = new HashMap<>();
        StringTokenizer st;

        for (int i = 0; i < n; i++) {
            char node = (char) ('A' + i);
            tree.put(node, new Node(node));
        }

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            char parent = st.nextToken().charAt(0);
            char left = st.nextToken().charAt(0);
            char right = st.nextToken().charAt(0);

            Node parentNode = tree.get(parent);
            if (left != '.') {
                parentNode.left = tree.get(left);
            }
            if (right != '.') {
                parentNode.right = tree.get(right);
            }
        }
        Node root = tree.get('A');

        preorder(root);
        System.out.println();
        inorder(root);
        System.out.println();
        postorder(root);
    }
}
