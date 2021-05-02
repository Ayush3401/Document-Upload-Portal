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
	ll r,b,d;
	cin>>r>>b>>d;
	int np = min(r,b);
	int mb = max(r, b) % np;
	if(max(r, b) / np - 1>d)
	{
		cout << "NO\n";
		return;
	}
	if (mb)
	{
		if(max(r,b)/np > d)
		{
			cout << "NO\n";
			return;
		}	
	}
	cout << "YES\n";
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