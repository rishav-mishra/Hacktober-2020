import java.util.*;
class q2
{
 boolean checkAnagram(String s1,String s2) 
 {
     int f=0;
     String a= s1;
     String b= s2;
     String n1= a;
     String n2= b;
     if(a.length()==b.length())
     {
         int l= a.length();
         char x[]= new char[l];
         char y[]= new char[l];
         for(int i= 0; i<a.length(); i++)
         {
             x[i]= a.charAt(i);
             y[i]= b.charAt(i);
         }
         
         for(int i=0; i<n1.length(); i++)
         {
             for(int j=0; j<n2.length(); j++)
             {
                 char k= n1.charAt(i);
                 char r= n2.charAt(j);
                 if(k==r)
                 {
                     n2= n2.substring(0,j)+n2.substring(j+1);
                     f++;
                     break;
                 }
             }
         }
         if(f==l)
         {
             return (true);
         }
         else
         {
             return (false);
         }
     }
     else
     {
        return (false);
     }
 }
 public static void main(String args[])
 {
     Scanner in= new Scanner (System.in);
     String s1, s2;
     System.out.println("Enter first word");
     s1= in.nextLine();
     s1= s1.toLowerCase();
     System.out.println("Enter second word");
     s2= in.nextLine();
     s2= s2.toLowerCase();
     q2 obj= new q2();
     if (obj.checkAnagram(s1,s2)== true)
     {
         System.out.println("Both the strings are anagram of each other");
     }
     else
     {
         System.out.println("Both the strings are not anagram of each other");
     }
 }
}
