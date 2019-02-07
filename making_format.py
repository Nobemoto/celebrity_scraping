import csv

rf = open('key_links.csv', 'r')
dataReader = csv.reader(rf)

i = 1
wf = open("format.txt", "w")
for person in dataReader:
    wf.write("---------------"+"\n"+str(i)+" "+person[0]+"\n"+"Career: \n\n"+person[1]+"\n\n"+"linkedinPic: \n\n"+person[2]+"\n\n"+person[3]+"\n\n"+person[4]+"\n\n")
    i += 1

wf.close()
rf.close()

print('finished making format for research')
