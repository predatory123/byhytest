# # 1.Javascript代码实现
# function* fibo()
# {
#     let [pre,curr] = [0,1];
#     for(;;)
#     {
#         yield curr;
#         [pre,curr] = [curr,pre + curr];
#     }
# }
# for(let i of fibo())
# {
#     if(i > 10000)
#     {
#         break;
#     }
#     console.log(i);
# }
# //实现10000以内的数列
#
# # 2.C++代码实现
# # include <bits/stdc++.h>
#
# using
# namespace
# std;
#
# int
# main()
# {
#
#     int
# a = 0, b = 1, c = 1, n;
#
# cin >> n; // 输入n
#
# for (int i=3;i <= n;i++)
# {
#
# a = b;
#
# b = c;
#
# c = a + b;
#
# }
#
# cout << c; // 输出最终结果
#
# return 0;
#
# }
#
# # 3.递归算法实现
# # include <bits/stdc++.h>
# using namespace std;
# int f(int n)
# {
#     if(n==0) return 0;
#     if(n==1) return 1;
#     if(n>=2)
#     {
#         return f(n-1)+f(n-2);
#     }
# }
# int main()
# {
#     int n;
#     cin>>n;
#     cout<<f[n];
#     return 0;
# }
#
# # 4.递归算法优化(记忆化搜索)
# # include <bits/stdc++.h>
# const int MAX=101;
# using namespace std;
# int a[MAX];
# int f(int n)
# {
#     if(a[n]!=-1) return a[n];
#     else
# {
#         a[n]=f(n-1)+f(n-2);
#         return a[n];
#     }
# }
# int main()
# {
#     int n;
#     cin>>n;
#     for(int i=0;i<=MAX-1;i++)
#     {//初始化
#         a[i]=-1;
#     }
#     a[0]=0;a[1]=1;
#     cout<<f[n];
#     return 0;
# }
#
# # 5.高精度计算
# #include <bits/stdc++.h>
# using namespace std;
# char sum[1200];
# int s=0,m=0,n;
# int main()
# {
#     cin>>n;
#     string s1,s2;
#     int a[1200],b[1200];
#     int he,i;
#     s1="0";
#     s2="1";
#     for(m=2;m<n+1;m++)
#     {
#         memset(a,0,sizeof a);
#         memset(b,0,sizeof b);
#         a[0]=s1.length();
#         for(i=1;i<=a[0];i++)
#         {
#             a[i]=s1[a[0]-i]-'0';
#         }
#         b[0]=s2.length();
#         for(i=1;i<=b[0];i++)
#         {
#             b[i]=s2[b[0]-i]-'0';
#         }
#         he=(a[0]>b[0]?a[0]:b[0]);
#         for(i=1;i<=he;i++)
#         {
#             a[i]+=b[i];
#             a[i+1]+=a[i]/10;
#             a[i]%=10;
#         }
#         he++;
#         while((a[he]==0)&&(he>1))
#         he--;
#             for(i=he,s=0;i>=1;i--,s++)
#             {
#                 sum[s]=a[i]+'0';
#             }
#         s1=s2;
#         s2=sum;
#     }
#     cout<<s2<<endl;
#     return 0;
# }
#
# # 6.python3代码实现
def fib(n):
    a, b = 1, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b


fib(100)  # 输出的是100以内的斐波那契数列

i = 1
j = 1
print(i,'\n', j)
for x in range(2, 100):
    if x == i + j:
        print(x)
        j = i
        i = x