#include <string.h>
#include <stdio.h>
 
int main()
{
    const char* str = "probablement la question 2";
    for(unsigned int i = 0; i < strlen(str); ++i)
    {
        printf("%d ", str[i]);
    }
}