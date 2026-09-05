


n = [5,3,2,5,1,5,6,2,1,2,4,5,6,3,1,4,2,4,6]
m = [3,2,5,1,3,6,4,9,7,2,7,4,3,1,5]


hash_map = {}

for i in n:
  hash_map[i] = hash_map.get(i,0)+1

print(hash_map)

for num in m:
  if num < 0 or num > 10:
    print(f"{num}:0")
  elif num not in hash_map:
    print(f"{num}:0")
  else:
    print(f"{num}:{hash_map.get(num)}")


# O(n+m)
