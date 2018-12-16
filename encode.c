#include<stdio.h>

void Print(int value,int amount,int b_max){
    printf("%d",value+b_max*amount)
}

int main(){
    int width,height,b_len,value,pre=-1,cnt=1;
    getchar();
    getchar();
    scanf("%d%d%d",&width,&height,&b_len);
    b_len++;
    printf("%d %d %d",width,height,b_len);
    while(scanf("%d",&value)!=EOF){
        if(value==pre){
            cnt++;
        }else{
            if(pre!=-1){
                Print(pre,cnt,b_len);
            }
        pre=value;
        cnt=1;
        }
    }
    Print(pre,cnt,b_len);
    return 0;
}
