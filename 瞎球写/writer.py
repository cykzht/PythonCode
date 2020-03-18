import csv
csvFile=open("csvData.csv","w",newline="")
writer=csv.writer(csvFile)
writer.writerow(["编号","姓名","成绩"])
writer.writerows([[]])
writer.writerows([[2,"张三",85]])
csvFile.close()
