import collections,itertools;input();print(sum((s*(s-1))//2 for s in collections.Counter((i for i in itertools.accumulate([0]+[int(i) for i in input().split()]))).values()))
