#include <bits/stdc++.h>


using namespace std;

vector<long long> solve() {
    long long v, e;
    cin >> v >> e;
    
    vector<vector<long long> > edges;
    map<long long, long long> weight;
    map<long long, long long> distance;
    
    for (long long i = 1; i <= v; i++) {
        distance[i] = 1e9;
    }
    distance[1] = 0;
    
    for (long long i = 0; i < e; i++) {
        vector<long long> edge;
        for (long long j = 0; j < 3; j++) {
            long long x;
            cin >> x;
            edge.push_back(x);
        }
        edges.push_back(edge);
    }
    
    for (long long i = 0; i < v - 1; i++) {
        for (const auto& edge : edges) {
            long long u = edge[0];
            long long v = edge[1];
            long long w = edge[2];
            
            if (distance[u] != 1e9 && distance[u] + w < distance[v]) {
                distance[v] = distance[u] + w;
            }
        }
    }
    
    for (auto& d : distance) {
        if (d.second == 1e9) {
            d.second = 30000;
        }
    }
    
    vector<long long> result;
    for (const auto& pair : distance) {
        result.push_back(pair.second);
    }
    
    return result;
}

int main() {
    vector<long long> result = solve();
    for (long long i = 0; i < result.size(); i++) {
        cout << result[i] << " ";
    }
    cout << endl;
    
    return 0;
}
