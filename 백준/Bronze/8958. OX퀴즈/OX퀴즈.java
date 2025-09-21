import java.util.Scanner;

public class Main{
	public static void main(String[]args)
	{
		Scanner sc = new Scanner(System.in);
		int num=sc.nextInt();
		for(int j=0;j<num;j++)
		{
			int score=0;
			int sum =0;
			String ox=sc.next();
			for(int i=0;i<ox.length();i++)
			{
				if(ox.charAt(i)=='O')
				{
					score+=1;
				}
				else
					score=0;
				sum+=score;
			}
			System.out.println(sum);
		}
		sc.close();
	}
}
