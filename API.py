from arcgis.gis import GIS
gis = GIS("https://services7.arcgis.com/mOBPykOjAyBO2ZKk/ArcGIS/rest/services/Corona_Gemeinden/FeatureServer/0", "pteufel", "W59echawo!o5")
print(f"Connected to {gis.properties.portalHostname} as {gis.users.me.username}")

f= gis.content.get('ObjectID')
print(f.layers[0])
