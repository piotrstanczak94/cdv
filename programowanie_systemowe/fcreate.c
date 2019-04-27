#include <stdio.h>
     2 #include <stdlib.h>
     3 #include <string.h>
     4
     5 int main(int argc, char *argv[])
     6 {
     7     FILE *wp;
     8     char word[50];
     9
    10     if((wp = fopen("words.txt", "a+")) == NULL)
    11     {
    12         printf("Couldn't open file\n");
    13         return 1;
    14     }
    15
    16     printf("Enter words to add them to a file.\nTo finish put #\n");
    17
    18     while((fscanf(stdin, "%50s", word) == 1) && (word[0] != '#'))
    19     {
    20         fprintf(wp, "%s", word);
    21         fprintf(wp, "%s", " ");
    22     }
    23
    24     rewind(wp);
    25
    26     printf("\nContent of the file: \n");
    27
    28     while(fscanf(wp, "%s", word) == 1)
    29     {
    30     puts(word);
    31     }
    32
    33     printf("\nDone!\n");
    34
    35     if(fclose(wp) != 0)
    36     {
    37         printf("Error while closing a file\n");
    38         return 1;
    39     }
    40
    41     return 0;
    42 }
