#include<stdio.h>
int main(){
    int width,height,b_len,value,pre=-1,cnt=1;
    getchar();
    getchar();
    scanf("%d%d%d",&width,&height,&b_len);
    b_len++;
    printf("%d %d %d ",width,height,b_len);
    while(scanf("%d",&value)!=EOF){
        if(value==pre){
            cnt++;
        }else{
            if(pre!=-1){
                printf("%d %d ",pre,cnt);
            }
        pre=value;
        cnt=1;
        }
    }
    printf("%d %d ",pre,cnt);
    return 0;
}
