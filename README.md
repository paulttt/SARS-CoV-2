# SARS-CoV-2
For the [#WIRVSVIRUS Hackathon](https://wirvsvirushackathon.org/) 
- tackling project 91 on slack, the [COVID-19 Clusterdiagramm für Deutschland](https://airtable.com/shrs71ccUVKyvLlUA/tbl6Br4W3IyPGk1jt/viwk1wafE5cvUwOr7?blocks=hide)
- Visit us on [Devpost](https://devpost.com/software/corona-cases-forecasting-for-germany-on-a-county-level#updates)

## Corona Cases Forecasting for Germany on a County Level
#### COVID-19 Clusterdiagramm für Deutschland
##### Problems:
Der Verlauf der Covid-19 Infektionen wird aktuell in Deutschland von staatlicher Seite und durch die Presse überwiegend anhand von statistischen Momentaufnahmen dokumentiert, z.B. durch die täglich aktualisierten Fallzahlen des Robert Koch Instituts (s. https://www.rki.de/DE/Content/InfAZ/N/Neuartiges_Coronavirus/Fallzahlen.html und nachgeordnete Seiten). Aufgrund des exponentiellen Wachstumsverhaltens der Infektion führen diese Momentaufnahmen allerdings dazu, dass neue Infektionsschwerpunkte nur verzögert erkannt werden und präventive Maßnahmen dadurch zu spät anlaufen. Gleichzeitig sind die Ressourcen für präventive Maßnahmen begrenzt, was eine starke Fokussierung und exzellente Priorisierung erfordert. Hilfreich wäre stattdessen eine feingranulare Vorhersage (Forecast) der Infektionsverläufe (z.B. pro Landkreis, pro demografischer Gruppe, pro Industriebranche, pro Funktion von medizinischem Personal, …) anhand von untertägig aktualisierten Daten.

##### Challenge:
Es wird eine Lösung gesucht, die die feingranulare Vorhersage der zu erwarteten Covid-19- Infektionsverläufe ermöglicht. Der Granularitätsgrad muss so hoch sein, dass eine effektive Priorisierung von Maßnahmen zur Verlangsamung und Eindämmung ermöglicht wird (geographisch also mindestens auf Landkreisebene, demographisch mindestens nach Alter und Geschlecht, wirtschaftlich nach relevanten Industriezweigen, sowie nach relevanter medizinischer Funktion/Qualifikation, um nur einige Dimensionen zu nennen). Die Vorhersagen müssen sich anhand von stündlich aktualisierten Datenquellen weitestgehend automatisch aktualisieren und robust gegen Veränderung in Datenformat und -qualität sein. Übergeordnetes Ziel ist es, Entscheidungsträgern in Verwaltung, Politik und Wirtschaft eine bessere Bündelung von präventiven Maßnahmen zu ermöglichen, sodass knappe Ressourcen rechtzeitig am richtigen Ort sind und es vermieden wird dem Geschehen „hinterherzulaufen“.

#### Solution:
Das Robert Koch Institut veröffentlicht [tägliche Momentaufnahmen](https://www.rki.de/DE/Content/InfAZ/N/Neuartiges_Coronavirus/Situationsberichte/2020-03-18-de.pdf?__blob=publicationFile) des Infektionsverlaufes bis auf Landkreisebene, jedoch keine Vorhersagen. Die Süddeutsche Zeitung betrachtet als einzige (?) deutsche Publikation die [Trendentwicklung](https://www.sueddeutsche.de/thema/Coronavirus), jedoch nur bundesweit und nur auf drei Granularitätsstufen. Die US-amerikanische Johns Hopkins Universität stellt [stündliche Momentaufnahmen](https://coronavirus.jhu.edu/map.html) des weltweiten Infektionsverlaufes zusammen. Diverse zumeist individuelle online Data-Science-Projekte, zumeist aus dem nordamerikanischem Raum, erstellen Vorhersagen, jedoch nicht auf einem für deutsche Entscheidungsträger relevanten Granularitätsgrad.

Also have a look at this interesing [Dashboard](https://experience.arcgis.com/experience/478220a4c454480e823b17327b2bf1d4/page/page_1/) about German Corona data by County





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
4) [Statista] (https://de.statista.com)
5) [GovData] (https://www.govdata.de)
6) [Informationssystem der
Gesundheitsberichterstattung des Bundes] (http://www.gbe-bund.de/gbe10/pkg_isgbe5.prc_isgbe?p_uid=gast&p_aid=24350729&p_sprache=D)
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




