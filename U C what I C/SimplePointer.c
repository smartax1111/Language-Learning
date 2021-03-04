#include <stdio.h>

int main()
{
    printf("\n\n\t\tStudytonight - Best place to learn\n\n\n");
    int var = 24;
    int *p;
    p = &var;

    printf("\n\nAddress of var variable is: %x \n\n", &var);
    printf("\n\nAddress store in pointer variable p is : %x", p);
    printf("\n\nValue of var variable or the vlaue stored at address p is   %d ", *p);
    printf("\n\n\t\t\tCoding is Fun !\n\n\n");

    return 0;
}