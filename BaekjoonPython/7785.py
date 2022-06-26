n = int(input())

log = {}
for i in range(n):
    name, status = input().split()
    log[name] = status
    if status == 'leave':
        log.pop(name)
result = dict(sorted(log.items(), reverse=True))
for key in result.keys():
    print(key)

