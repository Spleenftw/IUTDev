#include <stdio.h>
int main()

{
 int i=1;
 while (i <= 4)
{
	//printf("%d\n", i);
	int n=0;
	while (n<i) 
	{
		printf("*");
		n++;
	}
	printf("\n");
	i++;
	
}

  return 0;
}
