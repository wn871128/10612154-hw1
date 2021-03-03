''' main '''
# 使用自建的套件 myMath 來計算使用者輸入的五個數的平均值
import myStatistics
A = []

for i in range(5):
    number = int(input("? "))
    A.append(number)
print(myStatistics.myMean(A))
