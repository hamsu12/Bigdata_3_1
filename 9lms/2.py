def showList(hList):
    for data in hList:
        print(data, end="\t")
    print()

with open(r"\빅분실\파이썬 Beginner 소스\CSV\singer1.csv", "r", encoding="cp949") as inFp:
    with open(r"\빅분실\singerOver165.csv", "w", encoding="cp949") as outFp:
        header = inFp.readline()
        header = header.strip()
        headerList = header.split(',')
        cmNo = headerList.index("평균 키")
        yearNo = headerList.index("데뷔 일자")

        headerList = [headerList[0], headerList[1], headerList[cmNo], headerList[yearNo]]

        headerStr = ",".join(map(str, headerList))
        outFp.write(headerStr + "\n")

        for data in inFp:
            inStr = data.strip()
            row = inStr.split(',')

            if int(row[cmNo]) >= 165:
                rowList = [row[0], row[1], row[cmNo], row[yearNo]]
                rowStr = ",".join(map(str, rowList))
                outFp.write(rowStr + "\n")