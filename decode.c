#include<stdio.h>
int main(){
    int value,amount,width,height,b_len,i;
    scanf("%d%d%d",&width,&height,&b_len);
    printf("P2\n");
    printf("%d\n",width);
    printf("%d\n",height);
    printf("%d\n",b_len-1);
    while(scanf("%d",&value)!=EOF){
        for(i=0;i<value/b_len;i++){
            printf("%d\n",value%b_len);
        }
    }
    return 0;
}
