
const int N=100000;
uint64_t q[N];
int front, back;
vector<int> adj1[N], adj2[N];
class Solution {
public:
    static inline void build_adj(const vector<vector<int>>& edges,  auto& adj){
        for (const auto& e: edges){
            const int u=e[0], v=e[1];
            adj[u].push_back(v);
            adj[v].push_back(u);
        }
    }
    static int bfs(bitset<100001>& mod2, const auto& adj){
        front=back=0;
        q[back++]=N;
        bool isEven=1;
        int cnt=0;
        for( ;front<back; isEven=!isEven){
            int qz=back-front;
            for(int a=0; a<qz; a++){
                auto ip=q[front++];
                int i=ip>>32, parent=ip&ULLONG_MAX;
                mod2[i]=isEven;
                cnt+=isEven;
                for(int j:adj[i]){
                    if (j==parent) continue;
                    q[back++]=((uint64_t)j<<32ULL)+i;
                }
            }
        }
        return cnt;
    }
    static vector<int> maxTargetNodes(vector<vector<int>>& edges1, vector<vector<int>>& edges2) {
        const int n=edges1.size()+1, m=edges2.size()+1;
        for(int i=0; i<n; i++) adj1[i].clear();
        for(int j=0; j<m; j++) adj2[j].clear();
        bitset<100001> mod2=0;
        build_adj(edges1, adj1);
        build_adj(edges2, adj2);
        int y=bfs( mod2, adj2);
        int x=bfs( mod2, adj1);
        
        vector<int> ans(n);
        const int cnt2=max(y, m-y);
        int cnt[2]={(n-x)+cnt2, x+cnt2};
        for(int i=0; i<n; i++){
            ans[i]=cnt[mod2[i]];
        }
        return ans;
    }
};

auto init = []() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
    return 'c';
}();