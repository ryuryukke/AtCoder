#include <stdio.h>
int main(){
  char s[4];
  char t[4];
  scanf("%s",s);
  scanf("%s",t);
  int cnt = 0;
  for(int i=0;i<3;i++){
    if(s[i] == t[i]){
      cnt++;
    }
  }
  printf("%d\n",cnt);
}
