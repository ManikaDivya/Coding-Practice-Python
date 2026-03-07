import java.util.*;

class Main 
{
    public static void main(String[] args) 
    {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int sum = 0;

        int num[] = new int[n];

        for(int i = 0; i < n; i++)
        {
            num[i] = sc.nextInt();
            sum = sum + num[i];
        }

        int max = num[0];
        int min = num[0];

        for(int i = 0; i < n; i++)
        {
            if(num[i] > max)
            {
                max = num[i];
            }

            if(num[i] < min)
            {
                min = num[i];
            }
        }

        System.out.println("Highest marks: " + max);
        System.out.println("Lowest marks: " + min);

        float avg = (float)sum / n;

        System.out.println("Average marks: " + avg);
    }
}
