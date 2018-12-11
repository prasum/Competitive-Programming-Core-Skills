#include <bits/stdc++.h>
#define ff first
#define ss second
#define pb push_back
#define MOD (1000000007LL)
#define LEFT(n) (2*(n))
#define RIGHT(n) (2*(n)+1)
 
using namespace std;
typedef long long ll;
typedef unsigned long long ull;
typedef pair<int, int> ii;
typedef pair<int, ii> iii;
 
ll pwr(ll base, ll p, ll mod = MOD){
ll ans = 1;while(p){if(p&1)ans=(ans*base)%mod;base=(base*base)%mod;p/=2;}return ans;
}
 
ll gcd(ll a, ll b){
    if(b == 0)  return a;
    return gcd(b, a%b);
}
 
 
int n, right_low[200005];
ll DP[200005], arr[200005];
 
 
int main(){
 
    ios_base::sync_with_stdio(0);
 
    cin>>n;
    for(int i=1;i<=n;i++)
        cin>>arr[i];
 
    stack<int> st;
    right_low[n] = n+1;
    st.push(n);
    for(int i=n-1;i>=1;i--){
        while(!st.empty() && arr[st.top()] >= arr[i])
            st.pop();
        if(st.empty())  right_low[i] = n+1;
        else    right_low[i] = st.top();
        st.push(i);
    }
 
// for(int i=1;i<=n;i++)   cout<<right_low[i]<<" ";cout<<endl;
 
    DP[n] = arr[n];
    for(int i=n-1;i>=1;i--){
        DP[i] = (right_low[i]-i)*arr[i] + DP[right_low[i]];
    }
 
    ll ans = 0;
    ans = accumulate(DP+1, DP+n+1, 0LL);
    cout<<ans;
    return 0;
}