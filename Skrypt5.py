from qgis.core import *
from PyQt5.QtCore import QVariant 


layer = QgsVectorLayer("/qgis_data/nadlesnictwa/g_inspectorate.shp", "Nadlesnictwa", "ogr")

QgsProject.instance().addMapLayers([layer])




layer3 = QgsVectorLayer("/qgis_data/SZCZECINEK_LES/SZCZECINEK_LES.shp", "SZCZECINEK_LES", "ogr")

QgsProject.instance().addMapLayers([layer3])

# Adding a Field: NADL and RDLP  to layer "Nieruchome zabytki punktowe "

layer3.isValid()
vpr = layer3.dataProvider()
vpr.addAttributes([QgsField("NADL", QVariant.String)])
layer3.updateFields()

feats_A = [ feat for feat in layer.getFeatures() ]

feats_C = [ feat3 for feat3 in layer3.getFeatures() ]
layer3.startEditing()


for i, feat in enumerate(feats_A):
    for j, feat2 in enumerate(feats_C):
        b=str(feat["reg_cd"])+'-'+ str(feat["ins_cd"])
        #print(str(feat2["adr_for"])[0:5])
        if str(feat2["adr_for"])[0:5]==b:
            feat2["NADL"]=feat["ins_name"]
        layer3.updateFeature(feat2)