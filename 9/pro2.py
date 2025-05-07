inF = open("data2.txt","r")
ouF = open("result.txt","w")

sum = cnt = 0
line = inF.readline()
while line!="":
    sum += int(line)
    cnt += 1
    line = inF.readline()

ouF.write("총점 = "+str(sum)+"점 \n")
ouF.write("수강자 수 = "+str(cnt)+"명 \n")
ouF.write("과목 평균 = "+str(sum/cnt)+"점 \n")

inF.close()
ouF.close()