import arcpy
from datetime import datetime
import sys, string, os

start_time = datetime.now()


outpath = r"C:/Users/artur/Desktop/101MEDIA"

arcpy.env.workspace= outpath


arcpy.env.overwriteOutput = True

arcpy.CheckOutExtension("3D")

# Entre com o diretório e o nome do arquivo texto de saída"
My_txt = "C:/Users/artur/Desktop/101MEDIA/CAVLocal.txt"

# Entre com o diretório e o nome do modelo"
My_surface= "C:/Users/artur/Desktop/101MEDIA/demacude.tif"

direction = "below"

# Cota do Nível de Referência da Batimetria
startingplane = 728.72

# Fator de Escala - Normalmente usado em transformação de unidades
z = 1

# Passo para cálculo da CAV "1 = 1m; 0.1 = 10cm; 0.01 = 1cm"
# y = 0.01 
y = 0.1

# Cota do Fundo do Reservatório
q = 723.68


print("please wait...this script is processing...(CAV processing)")
#error handler
try:


	if direction == "below":
		x=startingplane
		while x > q:
			arcpy.SurfaceVolume_3d(My_surface, My_txt, direction, x, z)
			x = x - y

	# if direction == "above":
		# x = startingplane
		# while x < q:
			# arcpy.SurfaceVolume_3d(My_surface, My_txt, direction, x, z)
			# x = x + y

except:
    arcpy.AddMessage(arcpy.GetMessages(2))
    print(arcpy.GetMessages(2))

end_time = datetime.now()
print('FIM, PROCESSAMENTO CONCLUÍDO')
print ('TEMPO DE PROCESSAMENTO: {}'.format(end_time - start_time))






