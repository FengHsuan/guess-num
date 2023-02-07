# 產生一個隨機整數1~100(不要印出來)
# 讓使用者重複輸入數字去猜
# 猜對的話 印出“終於猜對了”
# 猜錯的話 要告訴他 比答案大還是小
# 衍伸題 1
# 顯示猜的次數
# 衍伸題 2
# 讓使用者決定數字範圍

import random
start = input('請決定數字範圍的開始值：')
end = input('請決定數字範圍的結束值：')
start = int(start)
end = int(end)

r = random.randint(1, 100)
count = 0
while True:
	count += 1 # count = count + 1
	num = input('請猜數字：')
	num = int(num)
	if num == r:
		print('恭喜猜對了！')
		print('這是你猜的第', count,'次')
		break
	elif num > r:
		print('比答案大')
	elif num < r:
		print('比答案小')
	print('這是你猜的第', count,'次')