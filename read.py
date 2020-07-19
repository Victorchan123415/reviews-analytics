data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:
			print(len(data))
print(len(data), '筆資料已讀取完畢')
alllen = 0
for comment in data:
	alllen = alllen + len(comment)
print('每筆資料的平均長度為', alllen / len(data), 'byte')

new = []
for comment in data:
	if len(comment) < 100:
		new.append(comment)
print(len(new))
print(new[0])


