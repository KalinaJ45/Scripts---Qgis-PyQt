from qgis.core import *
from PyQt4.QtCore import QVariant 

#Adding a layer: "Nadlesnictwa"
layer = QgsVectorLayer("/qgis_data/dane/oddzialy/oddz_pol_2019.shp", "Oddzialy", "ogr")
if not layer.isValid():
  print("Layer {} did not load".format(layer.name()))
QgsMapLayerRegistry.instance().addMapLayers([layer])


#Adding a layer: "Nieruchome zabytki punktowe"

layer3 = QgsVectorLayer("/qgis_data/dane/eksport_warstw/rejestr_poligony.shp", "Poligony", "ogr")
if not layer3.isValid():
  print("Layer {} did not load".format(layer3.name()))
QgsMapLayerRegistry.instance().addMapLayers([layer3])

# Adding a Field: NADL and RDLP  to layer "Nieruchome zabytki punktowe "

layer3.isValid()
vpr = layer3.dataProvider()
vpr.addAttributes([QgsField("JEST", QVariant.String)])
layer3.updateFields()


feats_A = [ feat for feat in layer.getFeatures() ]
feats_C = [ feat3 for feat3 in layer3.getFeatures() ]
layer3.startEditing()

for i, feat in enumerate(feats_A):
    for j, feat2 in enumerate(feats_C):
        if feat.geometry().intersects(feat2.geometry()):
                feat2["JEST"]= "TAK"
                layer3.updateFeature(feat2)
            

            
            
