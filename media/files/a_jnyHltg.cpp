#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef long double ld;
typedef pair<ll, ll> pi;
typedef pair<double, double> pd;
typedef vector<ll> vi;
typedef vector<vector<ll>> vvi;
typedef vector<vector<pi>> vvpi;
typedef vector<pi> vpi;

ll INF = 2e18;
double eps = 1e-12;

#define forn(i, e) for (ll i = 0; i < e; i++)
#define forsn(i, s, e) for (ll i = s; i < e; i++)
#define rforn(i, s) for (ll i = s; i >= 0; i--)
#define rforsn(i, s, e) for (ll i = s; i >= e; i--)
#define ln "\n"
#define dbg(x) cout << #x << " = " << x << ln
#define mp make_pair
#define pb push_back
#define fi first
#define se second
#define all(x) (x).begin(), (x).end()
#define sz(x) ((ll)(x).size())



void fast_cin()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
}

void read(vi &x)
{
	for (ll i = 0; i < sz(x); i++)
	{
		cin >> x[i];
	}
	return;
}

void read(vvi &x)
{
	for (ll i = 0; i < sz(x); i++)
	{
		for (ll j = 0; j < sz(x[i]); j++)
		{
			cin >> x[i][j];
		}
	}
	return;
}

void solve()
{
	ll n;
	cin>>n;
	vi a(n);
	read(a);
	vi pre(n);
	pre[0] = 0;
	for (int i = 1;i<n;i++)
	{
		if(a[i] > a[pre[i-1]])
		{
			pre[i] = i;
		}
		else{
			pre[i] = pre[i - 1];
		}
	}
	// for(auto it:pre)
	// 	cout << it << ln;
	for (int i = n - 1; i >= 0;i--)
	{
		int j = pre[i];
		for (; j <= i;j++)
		{
			cout << a[j] << " ";
		}
		i = pre[i];
	}
	cout << endl;
	return;
}

int main()
{
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif

	fast_cin();
	ll t;
	cin >> t;
	for (int it = 1; it <= t; it++)
	{
		// cout << "Case #" << it << ": ";
		solve();
	}
	return 0;
}