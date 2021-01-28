//Write a C program that accepts an employee's ID, 
//total worked hours of a month and the amount he received per hour. Print the employee's ID and salary (with two decimal places) of a particular month.

//Test Data :
//Input the Employees ID(Max. 10 chars): 0342
//Input the working hrs: 8
//Salary amount/hr: 15000
//Expected Output:
//Employees ID = 0342
//Salary = U$ 120000.00
#include <stdio.h>

int main()
{
    double Work, Sal;
    char empID[4];
    printf("Input your Employee ID: ");
    scanf("%s",&empID);
    printf("Input the hours you worked: ");
    scanf("%lf",&Work);
    printf("Input your salary: ");
    scanf("%lf",&Sal);

    printf("Employee's ID = %s\n", empID);
    printf("Salary = U$ %.2lf", Sal * Work);
}
