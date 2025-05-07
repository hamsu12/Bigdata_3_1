import csv

infile = open(r"빅분실\weather.csv", "r", encoding="cp949")
data = csv.reader(infile)

header = next(data)
temp = 1000

for row in data:
    if temp > float(row[3]):
        temp = float(row[3])

print("서울이 가장 추웠던 날의 기온: ", temp, "도 입니다.")

infile.close()