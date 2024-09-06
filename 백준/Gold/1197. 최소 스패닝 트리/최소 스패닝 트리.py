import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline #빨리 입력받기

v, e = map(int, input().split()) #정점과 간선의 개수
vertices = [ i for i in range(v+1)] #정점들, 리스트의 값이 가리키는건 각 정점의 부모, 초깃값은 자기자신임(전부 분리집합)
edges = [] #간선들, 리스트에는 [시작 정점, 끝 정점, 가중치] 가 들어감

for x in range(e):
    edges.append(list(map(int, input().split()))) #입력받기

edges.sort(key = lambda x:x[2]) #가중치 기준으로 정렬


#Union-Find 알고리즘
def findRoot(a):
    if vertices[a] != a: #자기가 Root가 아니면
        vertices[a] = findRoot(vertices[a]) #경로압축, 정점들의 부모를 전부 Root으로 해둠
    return vertices[a] #Root 반환


weightsTotal = 0
#Kruskal 알고리즘 적용
for v1, v2, w in edges: #시작 정점, 끝 정점, 가중치
    v1Root = findRoot(v1)
    v2Root = findRoot(v2)
    if v1Root == v2Root: #사이클 형성하면 안되니까 제외
        continue
    else:
        weightsTotal += w
        if v1Root < v2Root: #숫자가 작은 곳으로 부모를 할당
            vertices[v2Root] = v1Root #합집합 시키기
        else:
            vertices[v1Root] = v2Root #합집합 시키기
        

print(weightsTotal)