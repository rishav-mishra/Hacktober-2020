#include <iostream>
#include <string.h>
using namespace std;

class Employee {
protected:
       int id,salary;
       char name[30];
  public:
   Employee (char *s,int i)
   {
     strcpy(name,s);
     id=i;
     salary = 0;
   }
    virtual void show()
    {

    }
} ;

  class regular : public Employee
    {
      private :
      int bs;
      float hra,da;
      public :
      regular(char *s,int p, int b):Employee(s,p)
      {
      bs=b;
      da=0.8*bs;
      hra=0.1*bs;
      salary = bs + da + hra;
      }


        void show()
        {
        cout<<"Name : \t"<<name<<endl;
        cout<<"ID : \t"<<id<<endl;
        cout<<"Salary : \t"<<salary<<endl;
        }
    };

    class part_time : public Employee
      {
        private :
        int hr, pph;
        public :
        part_time(char *s,int i, int h,int p):Employee(s,i)
        {
        hr=h;
        pph=p;
        salary = hr*pph;
        }


          void show()
          {
          cout<<"Name : \t"<<name<<endl;
          cout<<"ID : \t"<<id<<endl;
          cout<<"Salary : \t"<<salary<<endl;
          }
      };

int main() {
Employee *t1,*t2;
char c1[20],c2[20];
int p1,p2,sal,p,h;
cout<<"For the regular employee : \n\n";
cout<<"Enter the name : \n";
cin>>c1;
cout<<"Enter the ID : \n";
cin>>p1;
cout<<"Enter the basic salary : \n";
cin>>sal;
regular r(c1,p1,sal);
t1=&r;

cout<<"For the part time employee : \n\n";
cout<<"Enter the name : \n";
cin>>c2;
cout<<"Enter the ID : \n";
cin>>p2;
cout<<"Enter the no. of hours : \n";
cin>>h;
cout<<"Enter the pay per hour : \n";
cin>>p;

part_time pt(c2,p2,h,p);
t2=&pt;

cout<<"\n\nRegular employee Details : \n\n";
t1->show();
cout<<"\n\nPart-Time employee Details : \n\n";
t2->show();
return 0;
}
