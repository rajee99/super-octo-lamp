#include<stdio.h>

int main() {
   
int k = 0, n = 0, w = 0, total = 0;

scanf("%d%d%d",&k,&n,&w);

for (int i = 1; i<=w; i++){
  total+=i*k;
}

total = total - n;

if (total<=0){
    total = 0;
}

printf("%d",total);


    return 0;
}