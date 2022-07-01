from qgis.core import *
from PyQt4.QtCore import QVariant 

#Adding a layer: "Nadlesnictwa"
layer = QgsVectorLayer("/qgis_data/nadlesnictwa/nadlesnictwa_2016_region.shp", "Nadlesnictwa", "ogr")
if not layer.isValid():
  print("Layer {} did not load".format(layer.name()))
QgsMapLayerRegistry.instance().addMapLayers([layer])

#Adding a layer: "RDLP"

layer2 = QgsVectorLayer("/qgis_data/RDLP/RDLP_granice.shp", "RDLP", "ogr")
if not layer2.isValid():
  print("Layer {} did not load".format(layer2.name()))
QgsMapLayerRegistry.instance().addMapLayers([layer2])


#Adding a layer: "Nieruchome zabytki punktowe"

layer3 = QgsVectorLayer("/qgis_data/dane/UN_P/UNESCO_point.shp", "Nieruchome zabytki obszarowe", "ogr")
if not layer3.isValid():
  print("Layer {} did not load".format(layer3.name()))
QgsMapLayerRegistry.instance().addMapLayers([layer3])

# Adding a Field: NADL and RDLP  to layer "Nieruchome zabytki punktowe "

layer3.isValid()
vpr = layer3.dataProvider()
vpr.addAttributes([QgsField("NADL", QVariant.String),QgsField("RDLP", QVariant.String)])
layer3.updateFields()

feats_A = [ feat for feat in layer.getFeatures() ]
feats_B = [ feat2 for feat2 in layer2.getFeatures() ]
feats_C = [ feat3 for feat3 in layer3.getFeatures() ]
layer3.startEditing()

for i, feat in enumerate(feats_A):
    for j, feat2 in enumerate(feats_C):
        if feat.geometry().intersects(feat2.geometry()):
            if feat.geometry().contains(feat2.geometry()):
                feat2["NADL"]=feat["Nazwa"]
            elif feat2["NADL"]==NULL:
                feat2["NADL"]=feat["Nazwa"]
            else:
                feat2["NADL"]= feat2["NADL"]+" / "+feat["Nazwa"]
    
            layer3.updateFeature(feat2)
            
for i, feat in enumerate(feats_B):
    for j, feat2 in enumerate(feats_C):
        if feat.geometry().intersects(feat2.geometry()):
            if feat.geometry().contains(feat2.geometry()):
                feat2["RDLP"]=feat["NAZWA"]
            elif feat2["RDLP"]==NULL:
                feat2["RDLP"]=feat["NAZWA"]
            else:
                feat2["RDLP"]= feat2["RDLP"]+" / "+feat["NAZWA"]
    
            layer3.updateFeature(feat2)  
            
            
