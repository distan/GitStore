#include<stdio.h>
#include<string.h>
#include<stdlib.h>

#define N 1000

void delay(int x){
    int i,j;
    for (i = 0; i < x; i++)
        for(j = 0;j < 120; j++);
}

int main(void){
    int count = 0;
    char str[N + 1];
    char putstr[N + 1];
    char str0[] = "www";
    char str1[] = "项目名称：";    char str1_1[] = "项目名称:";
    char str1_2[] = "项目名称及";   
    char str2[] = "供应商名称：";   char str2_1[] = "供应商名称:";
    char str2_2[] = "中标人名称："; char str2_3[] = "中标人名称:";
    char str3[] = "供应商地址：";   char str3_1[] = "供应商地址:";
    char str3_2[] = "中标人地址："; char str3_3[] = "中标人地址:";
    char str3_4[] = "中标单位";
    char str4[] = "中标金额：";     char str4_1[] = "中标金额:";
    char str5[] = "联系方式：";
    char str6[] = "联系人：";
    char str7[] = "中国政府采购网江苏分网";
    FILE *fp,*fp1; 
    fp = fopen("raw.txt","r+");
    fp1 = fopen("final.txt","w");
    if(fp == NULL)
    {
        printf("Fail to open file\n");
        exit(0);
    }
    if(fp1 == NULL)
    {
        printf("Fail to open final.txt\n");
        exit(0);
    }
    while (fgets(str , N , fp) != NULL)
    {
        if (strstr(str,str0) != NULL)
        {
            printf("%s",str);
            fprintf(fp1,"%s",str);
            continue;
        }
        if ((strstr(str,str1) != NULL)||(strstr(str,str1_1) != NULL)||(strstr(str,str1_2) != NULL))
        {
            printf("%s",str);
            fprintf(fp1,"%s",str);
            continue;
        }
        if ((strstr(str,str2) != NULL)||(strstr(str,str2_1) != NULL)||(strstr(str,str2_2) != NULL)||(strstr(str,str2_3) != NULL))
        {
            printf("%s",str);
            fprintf(fp1,"%s",str);
            continue;
        }
        if ((strstr(str,str3) != NULL)||(strstr(str,str3_1) != NULL)||(strstr(str,str3_2) != NULL)||(strstr(str,str3_3) != NULL)||(strstr(str,str3_4) != NULL))
        {
            printf("%s",str);
            fprintf(fp1,"%s",str);
            continue;
        }
        if ((strstr(str,str4) != NULL)||((strstr(str,str4_1) != NULL)))
        {
            printf("%s",str);
            fprintf(fp1,"%s",str);
            continue;
        }
        if ((strstr(str,str5) != NULL))
        {
            printf("%s",str);
            fprintf(fp1,"%s",str);
            continue;
        }
        if ((strstr(str,str6) != NULL))
        {
            printf("%s",str);
            fprintf(fp1,"%s",str);
            continue;
        }
        if ((strstr(str,str7) != NULL))
        {
            printf("----------------------------------------\n");
            fprintf(fp1,"----------------------------------------\n");
            count++;
            continue;
        }
        //delay(100);
    }
    fprintf(fp1,"%d",count);
    fclose(fp);
    fclose(fp1);
    return 0;
}