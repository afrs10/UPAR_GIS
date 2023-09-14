import os, arcpy, sys
from arcpy import env 

#PAR�METROS DA TOOLBOX
#inputFolder = arcpy.GetParameterAsText(0)
fc = arcpy.GetParameterAsText(0)
outputFolder = arcpy.GetParameterAsText(1)

#DEFINE O AMBIENTE DE TRABALHO
arcpy.env.workspace = outputFolder 
aprx = arcpy.mp.ArcGISProject("CURRENT")
m = aprx.listMaps()[0]
arcpy.AddMessage("Map Name: {}".format(m.name))
sr = arcpy.SpatialReference(r"S:\UPAR\06_ARCGIS_DEMANDAS\02_SHAPES_GEOPORTAL\SIRGAS 2000 UTM Zone 23S.prj")
m.spatialReference = sr
LyrName = 'Poligonal_projeto'
newfile = os.path.join(outputFolder,"Poligonal_projeto.shp")
arcpy.AddMessage(newfile)
path = outputFolder

#CRIA A FUN��O
def INCAD(fc, outputFolder):

	# Step through each dataset in the list
	for file in fc:

		if arcpy.Exists(outputFolder):
			arcpy.Delete_management("Poligonal_projeto.shp")
			arcpy.Delete_management("Poligonal_projeto.lyr")

		# Select only the Polygon features on the drawing layer Poligonal_projeto
		arcpy.MakeFeatureLayer_management(fc + "/Polygon", LyrName, "\"Layer\" = 'Poligonal_projeto'")

		# Execute SaveToLayerFile
		arcpy.SaveToLayerFile_management(LyrName,os.path.join(outputFolder, LyrName + ".lyr"))
		arcpy.FeatureClassToShapefile_conversion(Input_Features="Poligonal_projeto", Output_Folder=outputFolder)

		# verifificar geometria
		desc = arcpy.Describe(newfile)
		arcpy.AddMessage("desc OK")
		geometria = desc.shapeType
		if geometria == 'Polygon':

			# calcula área (hectare)
			fieldName = "AREA_HA"
			expr ='!shape.area@hectares!'
			arcpy.management.AddField(newfile,"AREA_HA","DOUBLE") and arcpy.CalculateField_management(newfile,fieldName,expr,'PYTHON')
			arcpy.AddMessage("ÁREA OK")

			# Adiciona a camada "Poligonal_projeto" como primeira camada no data frame
			filepath = path + '\\' + "Poligonal_projeto.shp"
			arcpy.AddMessage("filepath")
			addLayer = m.addDataFromPath(newfile)
			arcpy.AddMessage("newfile")

			# Zoom para camada "Poligonal_projeto" na escala 1:25.000
			lyr = m.listLayers(LyrName)[0]
			arcpy.AddMessage("Map Name: {}".format(lyr.name))
			lyt = aprx.listLayouts("MAP_CONSULT_AUTOMATIZACAO")[0]
			arcpy.AddMessage("Map Name: {}".format(lyt.name))
			mf = lyt.listElements("mapframe_element", "Mapa Principal Map Frame")[0]
			arcpy.AddMessage("Map Name: {}".format(mf.name))
			mf.camera.setExtent(mf.getLayerExtent(addLayer, False, True))
			mf.defaultCamera = mf.camera
			mf.camera.scale = 25000

			# Label do campo "AREA_HA" com fonte de tamanho e cor personalizada
			for lyr in m.listLayers():
				if lyr.name == LyrName:  # Assuming you want to customize labels for the "Poligonal_projeto" layer
					if lyr.supports("LABELCLASSES"):
						for lblClass in lyr.labelClasses:
							lblClass.expression = "\"<CLR red = '150' green = '150' blue = '150'><FNT size = '12'>\" & [AREA_HA] & \"</FNT></CLR>\""
							lyr.showLabels = True

			lyt.exportToPDF("D:\ARCGIS\mylayout2.pdf")
		#arcpy.RefreshActiveView()
		#arcpy.RefreshTOC()
		#aprx.save()
		#del aprx, df, addLayer
		break

INCAD(fc, outputFolder)