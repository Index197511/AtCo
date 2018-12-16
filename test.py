#include<stdio.h>
#include<math.h>
int main(){
   int n,m,a,ans;
   scanf("%d%d",&n,&m );
   a=m/n;
   for (int i = 0; i < a+1; i++) {
     if (m%i==0) {
       if (ans<i) {
         ans=i;
       }
     }
   }
printf("%d", ans);
return 0;



}
