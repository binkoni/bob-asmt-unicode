#include <cstdio>
#include <fstream>
#include <iostream>
#include <iconv.h>

void printLine(std::string& line)
{
    line.length()
    std::cout << line << std::endl;
}

int main(int argc, char* argv[])
{
    if(argc < 2)
        return -1;
    std::ifstream input{argv[1]};
    std::string line;
    while(!input.eof() && !input.bad())
    {
        std::getline(input, line);
        printLine(line);
    }
}
