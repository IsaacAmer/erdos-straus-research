#include <bits/stdc++.h>
using namespace std;
static inline long long gcdll(long long a,long long b){ while(b){long long t=a%b;a=b;b=t;}return a; }

// Exact bounded-Q search for a normalized Type-II witness at fixed p,u.
// Dahan form: gcd(u,a)=1, s | a*p+u, s == -1 (mod 4*u*a).
// Write s=4*u*a*k-1 and Q=(a*p+u)/s. Then
// a | u+Q and p+(u+Q)/a = 4*u*Q*k, with
// 1 <= Q <= floor((p+u)/(4*u-1)).
bool witness(long long p, int u, long long &outA, long long &outQ,
             long long &outK, long long &outS){
    long long qmax=(p+u)/(4*u-1);
    for(long long Q=1; Q<=qmax; ++Q){
        long long n=u+Q;
        auto test=[&](long long a)->bool{
            if(gcdll(a,u)!=1) return false;
            long long r=n/a;
            long long mod=4LL*u*Q;
            long long val=p+r;
            if(val%mod) return false;
            long long k=val/mod;
            if(k<1) return false;
            long long s=4LL*u*a*k-1;
            if((a*p+u)%s) abort();
            if((s+1)%(4LL*u*a)) abort();
            outA=a; outQ=Q; outK=k; outS=s;
            return true;
        };
        for(long long a=1;a*a<=n;++a){
            if(n%a) continue;
            if(test(a)) return true;
            long long b=n/a;
            if(b!=a && test(b)) return true;
        }
    }
    return false;
}

int main(int argc,char**argv){
    int N= argc>1? atoi(argv[1]):1000000;
    vector<bool> prime(N+1,true); prime[0]=prime[1]=false;
    for(int i=2;1LL*i*i<=N;++i) if(prime[i])
        for(long long j=1LL*i*i;j<=N;j+=i) prime[(int)j]=false;

    long long cnt=0, dist[5]={0}, fails=0;
    long long maxQ=0,maxA=0,maxK=0;
    long long maxQp=0,maxQa=0,maxQk=0,maxAp=0,maxAq=0,maxApk=0,maxKp=0,maxKa=0,maxKq=0;
    vector<int> failureList;
    for(int p=73;p<=N;p+=24){
        if(!prime[p]) continue;
        ++cnt;
        bool found=false;
        for(int u=1;u<=4;++u){
            long long a=0,Q=0,k=0,s=0;
            if(witness(p,u,a,Q,k,s)){
                dist[u]++; found=true;
                if(Q>maxQ){maxQ=Q;maxQp=p;maxQa=a;maxQk=k;}
                if(a>maxA){maxA=a;maxAp=p;maxAq=Q;maxApk=k;}
                if(k>maxK){maxK=k;maxKp=p;maxKa=a;maxKq=Q;}
                break;
            }
        }
        if(!found){++fails;failureList.push_back(p);}
    }
    cout<<"N="<<N<<" primes_p_mod24_1="<<cnt<<"\n";
    for(int u=1;u<=4;++u) cout<<"min_u="<<u<<" count="<<dist[u]<<"\n";
    cout<<"no_witness_u_le_4="<<fails<<"\n";
    if(fails){cout<<"failures:";for(int p:failureList)cout<<" "<<p;cout<<"\n";}
    cout<<"max_Q="<<maxQ<<" at p="<<maxQp<<" a="<<maxQa<<" k="<<maxQk<<"\n";
    cout<<"max_a="<<maxA<<" at p="<<maxAp<<" Q="<<maxAq<<" k="<<maxApk<<"\n";
    cout<<"max_k="<<maxK<<" at p="<<maxKp<<" a="<<maxKa<<" Q="<<maxKq<<"\n";
}
