data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		#f count % 1000 == 0:
			#print(len(data))
#print(len(data), '筆資料已讀取完畢')

#文字計數
wc = {}
for d in data:
	words = d.split()
	for word in words:
		if word in wc:
			wc[word] += 1 
		else:
			wc[word] = 1

for word in wc:
 	if wc[word] > 1000000:
 		print(word, wc[word])

while True:
	word = input('請問你想查什麼字: ')
	if word == 'q':
		break
	print(word, '出現過的次數為: ', wc[word])



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

good = []
for comment in data:
	if 'good' in comment:
		good.append(comment)
print(len(good),'have mentioned')
print(good[0])

