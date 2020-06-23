//run a infinite loop
#include <stdio.h>
#include <unistd.h>

int main(void)
{
    size_t pid_t = getpid();
    while (1)
    {
        printf("hi world, my process id is %ld\n", pid_t);
        sleep(2);
    }
    return (0);
}