from qgis.core import *
from PyQt5.QtCore import QVariant 


layer = QgsVectorLayer("C:/Users\kalina.juszczyk/Desktop/BDL_ZASIEGI_NADLESNICTW_2021/g_inspectorate.shp", "Nadlesnictwa", "ogr")

QgsProject.instance().addMapLayers([layer])




layer3 = QgsVectorLayer("C:/Users/kalina.juszczyk\Desktop/szlaki/turystyka_szlaki_lp.shp", "Szlaki", "ogr")

QgsProject.instance().addMapLayers([layer3])



layer3.isValid()
vpr = layer3.dataProvider()
vpr.addAttributes([QgsField("NADL", QVariant.String)])
vpr.addAttributes([QgsField("RDLP", QVariant.String)])
layer3.updateFields()

feats_A = [ feat for feat in layer.getFeatures() ]

feats_C = [ feat3 for feat3 in layer3.getFeatures() ]
layer3.startEditing()


for i, feat in enumerate(feats_A):
    for j, feat2 in enumerate(feats_C):
        b=str(feat["reg_cd"])+'-'+ str(feat["ins_cd"])
        if str(feat2["kod_nadl"])==b:
            feat2["NADL"]=feat["ins_name"]
            feat2["RDLP"]=feat["reg_name"]
        layer3.updateFeature(feat2)