N, M = map(int, input().split())

sitePassword = {}

for i in range(N):
    site, password = input().split()
    sitePassword[site] = password
for i in range(M):
    site = input()
    print(sitePassword[site])