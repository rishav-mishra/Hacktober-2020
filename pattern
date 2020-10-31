import java.util.*;
class Pattern
{
    public static void main ()
    {
        int i,sp,j,k,l;
        Scanner in= new Scanner(System.in);
        System.out.println("Enter the String ="); //accepting string
        String s = in.nextLine();
        l=s.length();
        /*printing the pattern*/
        for(i=0;i<l;i++)
        if(i==l/2)
        System.out.println(s);
        else 
        { 
            sp=Math.abs((l/2)-i);
        for(j=sp;j<l/2;j++)
        System.out.print(" "); 
         k=0;
        while(k<3)
        {
          System.out.print(s.charAt(i));
          for(j=0;j<sp-1;j++)
          System.out.print(" ");
          k++;
        }
        System.out.println(" "); 
        }
}
}
