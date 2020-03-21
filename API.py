from arcgis.gis import GIS
gis = GIS("http://www.arcgis.com/home/webmap/viewer.html?url=https://services7.arcgis.com/mOBPykOjAyBO2ZKk/ArcGIS/rest/services/RKI_Landkreisdaten/FeatureServer/0/&source=sd", "pteufel", "***REMOVED***")
print(f"Connected to {gis.properties.portalHostname} as {gis.users.me.username}")

