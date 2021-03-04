/*
Write a C program to find maximum between two numbers using conditional operator.
*/
#include <stdio.h>

int main(){
    int num1;
    int num2;

    printf("Give two numbers to compare values: ");
    scanf("%d", &num1);
    scanf("%d", &num2);
    num1 > num2 ? printf("%d is greater than %d", num1, num2) : printf("%d is greater than %d", num2, num1);
}
