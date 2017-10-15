
cont = 1
bradies = []
while (cont != 0):
    probata = raw_input('Dwse arithmo probatwn xerismenwn me keno ')
    bradies.append(probata.split())
    cont = int(raw_input('An thelete na eisagete kai allo bradi, dwste 1, alliws dwste 0 '))

sum_probata = int(raw_input('Dwste ton sinoliko arithmo twn probatwn '))

probata_stin_stani = 0
for i in bradies[-1]:
    probata_stin_stani = int(i) + probata_stin_stani

print sum_probata
print probata_stin_stani

if (probata_stin_stani < sum_probata):
    loipoun = sum_probata - probata_stin_stani
    print "Loipoun probata" + str(loipoun)+ " apo to kopadi"
else:
    print "Ola ta probata einai edo"