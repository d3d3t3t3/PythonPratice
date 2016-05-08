# List Comprehension을 이용한 소수 구하기
# MAX = 1000
# noprimes = [
#  j
#  for i in range(2, int(MAX ** 0.5) + 1)
#  for j in range(i*2, MAX, i)
# ]
# primes = [
#  x for x in range(2, MAX) if x not in noprimes
# ]

# lambda operator를 이용한 소수 구하기
import functools
MAX = 1000
noprimes_lists = list(map(lambda x: list(range(x*2, MAX, x)) , range(2, int(MAX ** 0.5) + 1)))
noprimes = functools.reduce(lambda x,y: x+y, noprimes_lists)
primes = list(filter(lambda x: x not in noprimes, range(2, MAX)))
primes