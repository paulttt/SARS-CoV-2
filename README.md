# SARS-CoV-2
For the [#WIRVSVIRUS Hackathon](https://wirvsvirushackathon.org/) 
- tackling Challenge 36 of the Hackathon, the [COVID-19 Clusterdiagramm für Deutschland](https://airtable.com/shrs71ccUVKyvLlUA/tbl6Br4W3IyPGk1jt/viwk1wafE5cvUwOr7?blocks=hide)
- Visit us on [Devpost](https://devpost.com/software/corona-cases-forecasting-for-germany-on-a-county-level#updates)

## Corona Cases Forecasting for Germany on a County Level
#### Corona Cases Forecasting For Germany On A County Level
##### Problems:
The course of Covid-19 infections is currently documented in Germany by the state and by the press mainly using statistical snapshots, e.g. through the [daily updated case numbers of the Robert Koch Institute (RKI)](https://www.rki.de/DE/Content/InfAZ/N/Neuartiges_Coronavirus/Fallzahlen.html). However, due to the exponential growth behavior of the infection, these snapshots mean that new focal points of infection are only recognized with a delay and preventive measures are therefore started too late. At the same time, the resources for preventive measures are limited, which requires a strong focus and excellent prioritization. Instead, a fine-grained prediction (forecast) of the course of infections e.g. per county (german: Landkreise) would be helpful based on data updated during the day. We want to help the Mayors and local decision makers to better anticipate the load of sick people for the near future. As there is also data available on the capacities of Intensive Care Units on a german state level, it might be useful for further development to include a tool that can connect these information and predict early on a shortage in care capacities.


##### Challenge:

A solution is sought which enables the granular prediction of the expected Covid-19 infection courses. The degree of granularity must be so high that effective slowdown and containment measures can be prioritized (geographically at least at the district level, demographically at least according to age and gender, economically according to relevant branches of industry, and according to relevant medical function / qualification, by just a few dimensions to call). The forecasts must update themselves automatically as far as possible based on data sources updated at least once a day and be robust against changes in data format and quality. The epidemological modeling of a disease outbreak on such small scales is challenging. Also we need to consider local connectivity between the counties. Therefore data is needed like live traffic flow or [mobile phone data like the Telekom provided to the RKI](https://www.telekom.com/de/konzern/details/corona-vorhersage-telekom-unterstuetzt-rki-596772)
The overarching goal is to enable decision-makers in administration, politics and business to better bundle preventive measures so that scarce resources are in the right place at the right time and it is avoided to "run after" the action. 


#### Solution Idea(s):
Forecasting of Corona cases based on

##### Epidemological SEIR model + Particle Markov Chain Monte Carlo (PMCMC) Modeling
We want to model every county's infected cases as a Markov Chain process, where the observed variables is the data from the RKI and the hidden states are the true unknown population that are infected with the virus. Since in many cities the testing capabilities are limited or people don't have symptoms, these numbers shall be modeled in the hidden states variables. The most important parameter for describing hidden state change transitions is the transmission rate R. This rate is highly influenced by the behaviour of the people and political mitigation actions. We want to describe the R variable as a probabilistic variable that is evaluated in a Bayesian framework given the observed data at every time step. From the hidden states we employ a function that models the probability of how likely it is that a person that is infected with the Virus also gets a positive test result. For this we take in the information about test capacities per day/week per country. Furthermore we want to also include a term in the differential equation that includes the spatial connectivity and traffic flows between the counties. With that information we can better predict the spread of the virus between the counties.



### References
1) [Epidemic Calculator based on SEIR model](http://gabgoh.github.io/COVID/index.html)
2) [Modeling the Coronavirus pandemic in a city with python](https://towardsdatascience.com/modelling-the-coronavirus-epidemic-spreading-in-a-city-with-python-babd14d82fa2)
3) [Nowcasting and forecasting the potential domestic and international spread of the 2019-nCoV outbreak originating in Wuhan, China: a modelling study](https://www.thelancet.com/action/showPdf?pii=S0140-6736%2820%2930260-9)
4) [Analysis and projections of transmission dynamics of nCoV in Wuhan](https://cmmid.github.io/topics/covid19/current-patterns-transmission/wuhan-early-dynamics.html)
5) [Introduction to particle Markov-chain Monte Carlo for disease dynamics modellers](https://www.sciencedirect.com/science/article/pii/S1755436519300301)

##### SEIR-model explained
6) [Medium Article: SEIR Model](https://towardsdatascience.com/social-distancing-to-slow-the-coronavirus-768292f04296)
7) [SEIR model: Brief Introduction](http://www.public.asu.edu/~hnesse/classes/seir.html)
8) [Adding Local Connectivity into SEIR model](https://www.sciencedirect.com/science/article/abs/pii/S0025556413002113)

##### Parameter Distribution
9) [Temporal profiles of viral load in posterior oropharyngeal saliva samples and serum antibody responses during infection by SARS-CoV-2: an observational cohort study](https://www.thelancet.com/journals/laninf/article/PIIS1473-3099(20)30196-1/fulltext#seccestitle140)

#### Datasets
1) [John Hopkins dataset](https://github.com/CSSEGISandData/COVID-19)
2) [Kaggle dataset](https://www.kaggle.com/sudalairajkumar/novel-corona-virus-2019-dataset)
3) [#WIRVSVIRUS website](https://wirvsvirushackathon.org/ressourcen/)
4) [Statista](https://de.statista.com)
5) [GovData](https://www.govdata.de)
6) [Informationssystem der
Gesundheitsberichterstattung des Bundes](http://www.gbe-bund.de/gbe10/pkg_isgbe5.prc_isgbe?p_uid=gast&p_aid=24350729&p_sprache=D)
7) [Corona Wiki-Datenquellen](https://coronawiki.net/index.php?title=Datenquellen)
8) [Live Dataset that tracks the political restriction for each country](https://www.bsg.ox.ac.uk/research/research-projects/oxford-covid-19-government-response-tracker)
9) [Data from Telekom?!](https://www.heise.de/newsticker/meldung/Corona-Krise-Deutsche-Telekom-liefert-anonymisierte-Handydaten-an-RKI-4685191.html)

##### APIs
1) [Database on Live Cases sorted on Landkreise with population info](https://public.fusionbase.io/explore/covid19-germany/data)
2) [Hackathon API-Action, Cases, Measures, Population](https://bene.gridpiloten.de:4712/api/ui/#/Source)
3) [Krankenhäsuer in Deutschalnd mit Geo- und Ausstattungsinformation](https://npgeo-corona-npgeo-de.hub.arcgis.com/datasets/348b643c8b234cdc8b1b345210975b87_0?geometry=-21.311%2C46.261%2C42.365%2C55.880)

#### ToDo
Henrik: 
- Further specification of the SEIR and PMCMC model
- implementation with pystan
- Setup of probabilistic framework of the SEIR model
- prior distribution w.r.t. test capacity in Germany

Paul: 
- Further specification of the SEIR and PMCMC model
- Research on including local connectivity between Landkreise in the model
- gather new data sources/APIs
- documentation of the model

Theo: 
- Setup of APIs and Database
- Setup of Dashboard with flask

Dan: 
- visualize Geodataset
- html website

Ralph:
- organisation and coordination. Gather Informations. 


#### other ideas to help: 
Building an app to help track sick people
1) from Hochschule Hannover/ Unilabs: [geoHealthApp](https://www.geohealthapp.de/)

- more details in this [article](https://www.heise.de/newsticker/meldung/Medizinische-Hochschule-Hannover-und-Ubilabs-entwickeln-Corona-App-4680487.html)
- needs voluntary local-history-location data from sick people
- launch in 2 weeks
- not sure if collected data is freely available

2) Learning from South Korea ??
