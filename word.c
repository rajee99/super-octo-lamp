#include<stdio.h>
#include<string.h>

int main (){

char s[101];
int countUP=0, countD = 0;

scanf("%100s", s);

int len = strlen(s);


        for(int i=0; i<len; i++){
        if (s[i]>='A' && s[i]<='Z'){
            countUP++;
        }
        else if (s[i]>='a' && s[i]<='z'){
            countD++;
        }
        }

if (countUP>countD){

        for(int i = 0; i<len; i++){
                if (s[i]>='a' && s[i]<='z'){
                    s[i] = s[i] - 32;
        }
    }
}

else{

       for(int i = 0; i<len; i++){
            if (s[i]>='A' && s[i]<='Z'){
                s[i] = s[i] + 32;
    }
}
}

printf("%s",s);


}