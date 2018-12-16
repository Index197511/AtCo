import itertools

list(itertools.permutations(list_name, n))
# list_nameで指定したリストからn個の順列のパターンを全列挙
list(itertools.combinations(list_name, n))
# list_nameで指定したリストからn個の組み合わせのパターンを全列挙
list(itertools.product(list_name, repeat=n))
# list_nameで指定したリストからn個の重複順列のパターンを全列挙
list(itertools.combinations_with_replacement(list_name, n))
# list_nameで指定したリストからn個の重複組み合わせのパターンを全列挙




from scipy.sparse.csgraph import floyd_warshall
from scipy.sparse.csgraph import dijkstra

temp=floyd_warshall(list_name)
#list_nameで指定したリストにワーシャルフロイド法を適用する。
temp=dijkstra(list_name)
#list_nameで指定したリストにダイクストラ法を適用する。


from colections import Counter

temp = Counter(list_name)
c = temp.most_common()
# 出現回数の多い順番にカウントして返す。
