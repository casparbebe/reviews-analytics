data = []
count = 0

with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:
			print(len(data))
print('檔案讀取完了, 總共有', len(data), '筆資料')

length = 0

for comment in data:
	length += len(comment)
print('留言平均長度為', int(length / 1000000), '個字')


new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('一共有', len(new), '筆留言長度小於100個字')
print(new[0])
print(new[1])

good = []
for g in data:
	if 'good' in g:
		good.append(g) # 27~30行進階寫法 = good[g for g in data if 'good' in g]
print('一共有', len(good), '筆留言裡面有good')
print(good[0])
print(good[1])

# 進階寫法 list
# good = [1 for d in data if 'good' in d]
# print(good)

# bad = ['bad' in d for d in data]
# print(bad)