import csv
import operator
import math

#Memasukkan/Menginsialisasi data train dan data set dan dimasukkan ke dalam array
DataTrain = []
DataTest = []

with open("DataTrain_Tugas3_AI.csv","r") as myFile:
    myFile = csv.reader(myFile, delimiter=',')
    line_count = 0

    for line in myFile:
        if line_count == 0:
            line_count += 1
        else:
            DataTrain.append([int(line[0]), float(line[1]), float(line[2]), float(line[3]), float(line[4]), float(line[5]), int(line[6])])

with open("DataTest_Tugas3_AI.csv","r") as iFile:
    iFile = csv.reader(iFile, delimiter=',')
    line_count = 0

    for line in iFile:
        if line_count == 0:
            line_count += 1
        else:
            DataTest.append([int(line[0]), float(line[1]), float(line[2]), float(line[3]), float(line[4]), float(line[5])])

#Memasukan hasil dari perhitungan ke dalam Array
result = []

#Mencari 
for x in range(0,len(DataTest)):
    euclidian = []
    for p in range(0,len(DataTrain)):
        total = 0
        #Menentukan jarak antara masing? data train dengan data test menggunakan euclidean
        for n in range(1,len(DataTrain[0])-1):
            euclidianDistance=(pow(DataTrain[p][n]-DataTest[x][n],2))
            total = total + euclidianDistance
            math.sqrt(total)
        euclidian.append([p+1,total])
    #Men-sort data hasil dari perhitungan jarak-jarak yang sudah didapat dari terdekat (terkecil) ke terjauh
    euclidian.sort(key=operator.itemgetter(1))
    
    #Memilih data yg telah disorting sebanyak ?k? dari jarak terdekat ke jarak terjauh
    k=7
    
    #Menampung jumlah data y yakni 0,1,2,3
    baris=euclidian[0:k]

    for i in range(0,k):
        contar0,contar1,contar2,contar3 = 0,0,0,0
        if DataTrain[baris[0][0]][6] == 0:
            contar0 = contar0 + 1
        elif DataTrain[baris[i-1][0]][6] == 1:
            contar1 = contar1 + 1
        elif DataTrain[baris[i-1][0]][6] == 2:
            contar2 = contar2 + 1
        elif DataTrain[baris[i-1][0]][6] == 3:
            contar3 = contar3 + 1
    print('perhitungan ke-;', x)

    #Mengambil jumlah data y terbanyak dengan jumlah terbanyak
    if (contar0>contar1 and contar0>contar2 and contar0>contar3):
        result.append(0)
    elif (contar1 > contar0 and contar1 > contar2 and contar1 > contar3):
        result.append(1)
    elif (contar2 > contar0 and contar2 > contar1 and contar2 > contar3):
        result.append(2)
    elif (contar3 > contar0 and contar3 > contar1 and contar3 > contar2):
        result.append(3)
    else:
         result.append(DataTrain[baris[0][0] - 1][6])
    
print(result)

#Memasukkan hasil dari pencarian y ke dalam file .csv
with open("TebakanTugas3 .csv",'w', newline="") as new_file:
    csv_writer = csv.writer(new_file, delimiter=",")

    for l in range(0,len(result)):
        csv_writer.writerow([result[l]])
        

print("=====================Perhitungan Telah Selesai, File .csv Telah Tersimpan di Folder=====================")
