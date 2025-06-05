bucket = [1, 2, 3, 4, 5]    
n1, m1 = map(int, input().split())
bucket.insert(m1, bucket[n1])   # m1 + 1
num = bucket[m1 + 1]
bucket.pop(m1 + 1)
bucket.insert(n1, num)
bucket.pop(n1 + 1)
print(bucket)