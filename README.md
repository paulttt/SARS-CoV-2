# SARS-CoV-2
For the [#WIRVSVIRUS Hackathon](https://wirvsvirushackathon.org/) 
- tackling project 46 on slack, the [COVID-19 Clusterdiagramm für Deutschland](https://airtable.com/shrs71ccUVKyvLlUA/tbl6Br4W3IyPGk1jt/viwk1wafE5cvUwOr7?blocks=hide)
- Visit us on [Devpost](https://devpost.com/software/corona-cases-forecasting-for-germany-on-a-county-level#updates)

## Corona Cases Forecasting for Germany on a County Level
#### COVID-19 Clusterdiagramm für Deutschland
##### Problems:
Derzeit gibt es in der Öffentlichkeit lediglich allgemeine Informationen zu Krankheitsfällen und geheilten Menschen (pro Bundesland/deutschlandweit). Ich wünsche mir zur effizienten Informationsvermittlung eine Übersicht pro Krankheitscluster nach Vorbild von Singapur. Zur Unterbrechung der Infektionskette ist eine detaillierte Auflistung aller Fälle und der Zusammenhänge essentiell.

##### Challenge:
Um die Einschränkungen für das öffentliche Leben so gering wie möglich zu halten, könnte jeder aufgetretene Fall innerhalb eines Clusters mit einem Radius versehen und auf einer Deutschlandkarte markiert werden. Die Größe des Radius ergibt sich hier entweder aus dem durchschnittlichen Aktionsradius eines erwerbstätigen Menschen (die Finanzämter haben hierzu sicher Werte aufgrund der angegebenen Kilometer) oder optional den (freiwillig) ausgelesenen Bewegungsdaten des Smartphones vom Infizierten.
Alle Infizierten eines Clusters erhöhen so den Aktionsradius des Virus (rot markiert auf der Karte), dies ermöglicht eine erhöhte lokale Alarmbereitschaft für medizinische Dienste (Krankenhäuser) und ebenfalls eine örtlich beschränkte Ausgangssperre (z.B. Verhängung von Maßnahmen pro Landkreis via Katwarn oder lokale Medien). Nach Genesung aller Infizierten innerhalb eines Clusters können diese Maßnahmen entsprechend heruntergefahren werden. Auf Basis dieser Daten können schneller und plausibler Maßnahmen beschlossen werden (ist eine landesweite Ausgangssperre nötig, obwohl der Virus nur noch in einem Landkreis aktiv ist?).

#### Solution:
Ich orientiere mich bei dieser Herausforderung am [Clusterdiagramm von Singapur](https://infographics.channelnewsasia.com/covid-19/coronavirus-singapore-clusters.html??cid=h3_referral_inarticlelinks_24082018_cna)
Zusätzlich die Bekanntmachung der Fälle auf einer [dedizierten Webseite](https://www.gov.sg/article/covid-19-cases-in-singapore)






##### Ideas:
Forecasting of Corona cases based on
1) Data from Telekom:
	- here is an [article](https://www.heise.de/newsticker/meldung/Corona-Krise-Deutsche-Telekom-liefert-anonymisierte-Handydaten-an-RKI-4685191.html)
	- dataset not available yet???
	- contains averaged mobility information from groups of 30
2) Data from [John Hopkins](https://github.com/CSSEGISandData/COVID-19)






#### Datasets
1) [John Hopkins dataset](https://github.com/CSSEGISandData/COVID-19)
2) [Kaggle dataset](https://www.kaggle.com/sudalairajkumar/novel-corona-virus-2019-dataset)
3) [#WIRVSVIRUS website](https://wirvsvirushackathon.org/ressourcen/)
- many different datasets based on the challenge

###### not so useful:
- [Italy dataset](https://github.com/pcm-dpc/COVID-19)
- [California dataset]()






#### to do:
Henrik: 
- look at/visualize John Hopkins dataset <br/>

Paul: <br/>

Dan: 
- look at/visualize Geodataset

Ralph:
- netflix 


#### other ideas to help: 
Building an app to help track sick people
1) from Hochschule Hannover/ Unilabs: [geoHealthApp](https://www.geohealthapp.de/)

- more details in this [article](https://www.heise.de/newsticker/meldung/Medizinische-Hochschule-Hannover-und-Ubilabs-entwickeln-Corona-App-4680487.html)
- needs voluntary local-history-location data from sick people
- launch in 2 weeks
- not sure if collected data is freely available

2) from South Korea ??




