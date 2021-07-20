import random, math, pandas, itertools
import matplotlib.pyplot as plt

def jarak(x1,y1,x2,y2):
    return math.sqrt(abs(x1-x2)**2+abs(y1-y2)**2)

nama_sheet = pandas.read_excel('tgs6.xlsx','kota')
kota = nama_sheet.as_matrix()

jumlahkota = len(kota)
rute = random.sample(range(jumlahkota),jumlahkota)

def totaljarak(rute):
    total = 0
    for i in range (1,len(rute)):
        x1 = kota[rute[i-1]][0]
        y1 = kota[rute[i-1]][1]
        x2 = kota[rute[i]][0]
        y2 = kota[rute[i]][1]
        total = total+jarak(x1,y1,x2,y2)
    x1 = kota[rute[len(rute)-1]][0]
    y1 = kota[rute[len(rute)-1]][1]
    x2 = kota[rute[0]][0]
    y2 = kota[rute[0]][1]
    total = total+jarak(x1,y1,x2,y2)
    return total

semua_kemungkinan = list(itertools.permutations(rute))

jarak_paling_sedikit = 99999999
rute_paling_sedikit = rute

for i in range(len(semua_kemungkinan)):
    jarak_total = totaljarak(semua_kemungkinan[i])
    if jarak_total < jarak_paling_sedikit:
        jarak_paling_sedikit = jarak_total
        rute_paling_sedikit = i

plt.plot([kota[semua_kemungkinan[rute_paling_sedikit][i % jumlahkota]][0] for i in range (jumlahkota+1)]
    , [kota[semua_kemungkinan[rute_paling_sedikit][i%jumlahkota]][1] for i in range(jumlahkota+1)], 'xb-');

#print(jarak_paling_sedikit)
print(kota)     
print(semua_kemungkinan[rute_paling_sedikit])
print(totaljarak(semua_kemungkinan[rute_paling_sedikit]))