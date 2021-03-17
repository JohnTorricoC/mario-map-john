from Search import *

estados = { '0' :['4'], 
            '1' :[], 
            '2' :['3','6'], 
            '3' :['2'],
            '4' :['5','8','0'],
            '5' :['4','6'],
            '6' :['5','2','10'],
            '7' :[],
            '8' :['4','12'],
            '9' :[],
            '10' :['6','14'],
            '11' :[],
            '12' :['8'],
            '13' :[],
            '14' :['10','15'],
            '15' :['14']
          }

#print(getHijos('5', estados))

<<<<<<< Updated upstream
busqueda_amplitud('0', '3', estados)


=======
res1 = busqueda_amplitud('0', '3', estados)
res2 = busqueda_amplitud('0', '12', estados)
print("\n")
if(res1 > res2):
    print("El camino optimo a nuestro objetivo tiene solo: ", res2 , "pasos")
else:
    print("El camino optimo a nuestro objetivo tiene solo: ", res1 , "pasos")
>>>>>>> Stashed changes
