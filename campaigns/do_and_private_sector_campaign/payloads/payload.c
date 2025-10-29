#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <libgen.h>
#include <string.h>

int main()
{
    char path[1024];
    char *dir;
    readlink("/proc/self/exe", path, 1024);
    dir = dirname(path);
    chdir(dir);
    system("python3 ../tools/custom_backdoor.py");
    return 0;
}
