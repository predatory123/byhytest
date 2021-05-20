# （1）利用VB编程求10000以内完全数。
Dim a as Integer,b as Integer,c as Integer
For a = 1 To 10000
c = 0
For b = 1 To a \ 2
If a Mod b = 0 Then c = c + b
Next b
If a = c Then Print Str(a)
Next a

# （2）利用C语言编程求1000以内完全数。
#include<stdio.h>
int main()
{
int i, j, s, n; /*变量i控制选定数范围，j控制除数范围，s记录累加因子之和*/
printf("请输入所选范围上限：");
scanf("%d", &n); /* n的值由键盘输入*/
for( i=2; i<=n; i++ )
{
s=0; /*保证每次循环时s的初值为0*/
for( j=1; j<i; j++ )
{
if(i%j == 0) /*判断j是否为i的因子*/
s += j;
}
if(s == i) /*判断因子这和是否和原数相等*/
printf("It's a perfect number:%d\n", i);
}
return 0;
}

# （3）利用java语言编程求1000以内完全数。
public class test46 {
 public static void main(String args[]) {
  int sum = 0;
  int i = 2,j = 1;
  for(i = 2; i <= 10000; i++)
  {
   for(j = 1; j < i; j++)
   {
    if(i%j == 0)
     sum = sum+j;
   }
   if(sum == i)
    System.out.println(" " + sum);
   sum = 0;
  }
 }
}

# （4）利用JavaScript语言编程求N以内完全数。


function
perfectNumber(N)
{
    var
nums = [], sum, i, j;
// 0
除以任意数都是0，所以从1开始
for (i = 0; i <= N; i++){
    sum = 0
// 完全数除以自己一半，求余肯定会大于0，所以用i / 2
for (j = 1; j <= i / 2; j++){
if (i % j == = 0){
sum += j;
}
}
if (sum == = i){
nums.push(i);
}
}
return nums;
}