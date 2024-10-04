#include <iostream>
#include <unordered_set>
using namespace std;

struct pair_hash {
    inline std::size_t operator()(const std::pair<int,int> & v) const {
        return v.first*100+v.second;
    }
};

int n;
int count;
int** l;
unordered_set<pair<int,int>, pair_hash> visited;

void f(char p, int x, int y){
    if (visited.find({x,y})!=visited.end())return;
    if (x==n-1 && y==n-1) {count++; return;}
    visited.insert({x,y});
    if (x<n-1 && y<n-1 && l[x+1][y]!=1 && l[x][y+1]!=1 && l[x+1][y+1]!=1)
        f('d',x+1,y+1);
    if ((x<n-2 || y==n-1) && l[x+1][y]!=1 && p!='h')
        f('v',x+1,y);
    if ((y<n-2 || x==n-1) && l[x][y+1]!=1 && p!='v')
        f('h',x,y+1);
    visited.erase({x,y});
}

int main(void){
    visited.insert({0,0});
    cin >> n;

    l = new int*[n];
    for(int i=0; i<n; i++){
        l[i] = new int[n];
        for(int j=0; j<n; j++){
            cin >> l[i][j];
        }
    }
    
    f('h',0,1);
    cout << count << endl;
}