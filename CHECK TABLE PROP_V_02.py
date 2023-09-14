import os, arcpy, sys
from arcpy import env

#PAR�METROS DA TOOLBOX
#inputFolder = arcpy.GetParameterAsText(0)
#arcpy.env.workspace = "D:\\ARCGIS\\UPAR\\INPUT\\"
shape = arcpy.GetParameterAsText(0)

# Create a Describe object from the table.
#list_shp = os.listdir(inputFolder)
#desc = arcpy.Describe(shape)
lstFields = arcpy.ListFields(shape)
fieldCount = len(lstFields)
field_name = [f.name for f in arcpy.ListFields(shape)]
imagem_lyr = arcpy.mapping.Layer(r"S:\UPAR\06_ARCGIS_DEMANDAS\02_SHAPES_GEOPORTAL\IMAGEM_2021.lyr")
sr = arcpy.SpatialReference(r"S:\UPAR\06_ARCGIS_DEMANDAS\02_SHAPES_GEOPORTAL\SIRGAS 2000 UTM Zone 23S.prj")

#CRIA A FUN��O
def CHKPROP(shape):

	mxd = arcpy.mapping.MapDocument("CURRENT")
	df = arcpy.mapping.ListDataFrames(mxd)[0]
	df.spatialReference = sr
	addLayer = arcpy.mapping.Layer(shape)
	arcpy.mapping.AddLayer(df, addLayer, "TOP")
	arcpy.mapping.AddLayer(df, imagem_lyr)
	ext = addLayer.getExtent()
	df.extent = ext
	df.scale = 10000

	for fieldname in ['UPT','n_UPT','ra','setor','quadra','conjunto','lote','end_cart','projeto','leg_proj','situacao','data_reg','area','norma','leg_nor','codigo_reg','padrao_cor','uos_setor']:
		if not fieldname in field_name:
			arcpy.AddError ('{0} - coluna errada ou ausente!'.format(fieldname))

	for field in lstFields:
		if field.name == "FID":
			arcpy.AddWarning ("FID_OK")
		elif field.name == "Shape":
			arcpy.AddWarning ("Shape_OK")
		elif field.name == "UPT":
			if field.name == "UPT" and field.type == "String" and field.length == 20:
				arcpy.AddWarning ("Item 1 UPT OK")
			else:
				arcpy.AddError ("Item 1 UPT ERRO!!!")
		elif field.name == "n_UPT":
			if field.name == "n_UPT" and field.type == "String" and field.length == 10:
				arcpy.AddWarning ("Item 2 n_UPT OK")
			else:
				arcpy.AddError ("Item 2 n_UPT ERRO!!!")
		elif field.name == "ra":			
			if field.name == "ra" and field.type == "Double":
				arcpy.AddWarning ("Item 3 ra OK")
			else:
				arcpy.AddError ("Item 3 ra ERRO!!!")
		elif field.name == "setor":
			if field.name == "setor" and field.type == "String" and field.length == 50:
				arcpy.AddWarning ("Item 4 setor OK")
			else:
				arcpy.AddError ("Item 4 setor ERRO!!!")
		elif field.name == 'quadra':
			if field.name == "quadra" and field.type == "String" and field.length == 50:
				arcpy.AddWarning ("Item 5 quadra OK")
			else:
				arcpy.AddError ("Item 5 quadra ERRO!!!")
		elif field.name == "conjunto":
			if field.name == "conjunto" and field.type == "String" and field.length == 50:
				arcpy.AddWarning ("Item 6 conjunto OK")
			else:
				arcpy.AddError ("Item 6 conjunto ERRO!!!")
		elif field.name == "lote":
			if field.name == "lote" and field.type == "String" and field.length == 50:
				arcpy.AddWarning ("Item 7 lote OK")
			else:
				arcpy.AddError ("Item 7 lote ERRO!!!")
		elif field.name == "end_cart":
			if field.name == "end_cart" and field.type == "String" and field.length == 180:
				arcpy.AddWarning ("Item 8 end_cart OK")
			else:
				arcpy.AddError ("Item 8 end_cart ERRO!!!")
		elif field.name == "projeto":
			if field.name == "projeto" and field.type == "String" and field.length == 50:
				arcpy.AddWarning ("Item 9 projeto OK")
			else:
				arcpy.AddError ("Item 9 projeto ERRO!!!")
		elif field.name == "leg_proj":
			if field.name == "leg_proj" and field.type == "String" and field.length == 150:
				arcpy.AddWarning ("Item 10 leg_proj OK")
			else:
				arcpy.AddError ("Item 10 leg_proj ERRO!!!")
		elif field.name == "situacao":
			if field.name == "situacao" and field.type == "String" and field.length == 20:
				arcpy.AddWarning ("Item 11 situacao OK")
			else:
				arcpy.AddError ("Item 11 situacao ERRO!!!")
		elif field.name == "data_reg":
			if field.name == "data_reg" and field.type == "String" and field.length == 10:
				arcpy.AddWarning ("Item 12 data_reg OK")
			else:
				arcpy.AddError ("Item 12 data_reg ERRO!!!")
		elif field.name == "area":
			if field.name == "area" and field.type == "Double":
				arcpy.AddWarning ("Item 13 area OK")
			else:
				arcpy.AddError ("Item 13 area ERRO!!!")
		elif field.name == "norma":
			if field.name == "norma" and field.type == "String" and field.length == 70:
				arcpy.AddWarning ("Item 14 norma OK")
			else:
				arcpy.AddError ("Item 14 norma ERRO!!!")
		elif field.name == "leg_nor":
			if field.name == "leg_nor" and field.type == "String" and field.length == 120:
				arcpy.AddWarning ("Item 15 leg_nor OK")
			else:
				arcpy.AddError ("Item 15 leg_nor ERRO!!!")
		elif field.name == "codigo_reg":
			if field.name == "codigo_reg" and field.type == "Integer" and field.length == 10:
				arcpy.AddWarning ("Item 16 codigo_reg OK")
			else:
				arcpy.AddError ("Item 16 codigo_reg ERRO!!!")
		elif field.name == "padrao_cor":
			if field.name == "padrao_cor" and field.type == "String" and field.length == 20:
				arcpy.AddWarning ("Item 17 padrao_cor OK")
			else:
				arcpy.AddError ("Item 17 padrao_cor ERRO!!!")
		elif field.name == "uos_setor":
			if field.name == "uos_setor" and field.type == "String" and field.length == 150:
				arcpy.AddWarning ("Item 18 uos_setor OK")
			else:
				arcpy.AddError ("Item 18 uos_setor ERRO!!!")

CHKPROP(shape)
