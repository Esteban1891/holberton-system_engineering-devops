#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>

/**
 * infinite_while - creates an infinite loop
 *
 * Return: always 0 (success)
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - entry point
 *
 * Return: always 0 (success)
 */
int main(void)
{
	pid_t pid;
	unsigned int i;

	for (i = 0; i < 5; i++)
	{
		pid = fork();
		if (pid < 0)
			perror("fork error");
		else if (pid == 0)
			exit(0);
		printf("Zombie process created, PID: %ld\n", (long) pid);
	}
	infinite_while();
	return (0);
}
