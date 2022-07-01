from qgis.core import *



for layer in QgsProject.instance().mapLayers().values():
    layer.startEditing()
    prov = layer.dataProvider()
    field_names = [field.name() for field in prov.fields()]
    layer.deleteAttributes([i for i in range (0,len(field_names))])
    
    layer.updateFields()
    layer.commitChanges()
