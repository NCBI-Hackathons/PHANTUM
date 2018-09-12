# PHANTUM: Predicting Human Antimicrobial-resistant Tuberculosis Using Machine Learning

*A Collaboration Between OCICB Bioinformatics and Computational Biosciences Branch and ODSET Emerging Leader in Data Science Fellows at NIH/NIAID*


![alt text](https://github.com/NCBI-Hackathons/Expanding-a-versatile-antimicrobial-resistance-pipeline/blob/master/final%20elf-icon%20size.png "elf logo") 

###### Icon made by [Eucalyp](https://www.flaticon.com/authors/eucalyp) from flaticon.com and edited by Chris Shin




## What is TB?
Tuberculosis (TB) is an infectious bacterial disease that usually affects the lungs but can also affect other parts of the body, such as the brain, the kidneys, or the spine. Most cases of TB are treatable and curable, but because the majority of TB cases occur in developing areas of the world, the majority of people with TB do not have access to proper treatment. 

There are 10 drugs currently [approved by the U.S. Food and Drug Administration (FDA)](https://www.cdc.gov/tb/topic/treatment/tbdisease.htm) for treating TB. Of these approved drugs, the first-line anti-TB agents that form the core of treatment regimens are isoniazid, rifampin, ethambutol, and pyrazinamide. 

Sometimes drug-resistant TB occurs when bacteria become resistant to the drugs used to treat TB. The [WHO](http://www.who.int/tb/areas-of-work/drug-resistant-tb/types/en/) describes 5 resistance types: 
* mono-resistance: resistance to one first-line anti-TB drug
* poly-resistance: resistance to more than one first-line anti-TB drug, other than both isoniazid and rifampicin
* multidrug resistance (MDR): resistance to at least both isoniazid and rifampicin
* extensive drug resistance (XDR): resistance to any fluoroquinolone, and at least one of three second-line injectable drugs (capreomycin, kanamycin and amikacin), in addition to multidrug resistance
* Rifampicin resistance (RR): resistance to rifampicin detected using phenotypic or genotypic methods, with or without resistance to other anti-TB drugs. It includes any resistance to rifampicin, in the form of mono-resistance, poly-resistance, MDR or XDR.

People who are diagnosed with drug-resistant TB are placed on a regimen of second-line drugs that are less effective than and have more severe side effects than first-line drugs. Mismanagement of TB treatment can lead to spread of drug-resistant TB and higher rates of death. 

There are several tests recommended by the [WHO](http://www.who.int/tb/publications/implementing_TB_diagnostics/en/) for diagnosing TB. Factors that influence which methodology to use include availability of resources, prevalence of TB in the area, and risk factors. There are also tests used to diagnose drug susceptibility and drug resistance. Drug-susceptibility testing (DST) can be done phenotypically or genotypically. 

## How Bad is TB?
TB is one of the top 10 causes of death [worldwide](http://www.who.int/en/news-room/fact-sheets/detail/tuberculosis). Currently, 2 billion people (about a third of the world's population) are infected with TB. The latest statistics from the [CDC](https://www.cdc.gov/tb/statistics/default.htm) show an estimate of 10.4 million new cases of TB in 2016. Of these, the [WHO](http://www.who.int/tb/areas-of-work/drug-resistant-tb/en/) reports that 580,000 of these cases are MDR-TB/RR-TB. Only about 20% of new cases of MDR-TB/RR-TB are [estimated to be enrolled in treatment](http://apps.who.int/medicinedocs/en/d/Js23098en/). 

To learn more about NIAID's efforts to combat TB, visit the [NIAID Tuberculosis Page](https://www.niaid.nih.gov/diseases-conditions/tuberculosis-tb ).

## What Are We Doing About TB?
We developed a web tool for rapid diagnosis of TB drug resistance at point-of-care powered by ML-AI technologies. We wanted to take advantage of the data made available by the [TB Portals Program](https://tbportals.niaid.nih.gov/). 

Three of the top 30 high-burden MDR-TB [countries](http://www.who.int/tb/publications/global_report/en/) (Azerbaijan, Belarus, and the Republic of Moldova) have data available through the TB Portals program. Georgia and Romania also currently have data accessible, and TB Portals staff are currently working to collect data from other TB endemic countries such as India, China, South Africa. 

### A Multi-Pronged Approach

We decided to use both chest x-ray (CXR) images and clinical measures in our prediction model. CXR has high sensitivity for pulmonary TB but low specificity, and diagnosis varies depending on the observer of the CXR. The [WHO](http://apps.who.int/iris/bitstream/handle/10665/252424/9789241511506-eng.pdf?sequence=1) recommends that TB diagnosis should be bacteriologically confirmed by sputum-sear microscopy, culture, or a molecular test. Currently there are no guidelines that place CXR as a triage test before bacteriological testing. 

![alt text](https://github.com/NCBI-Hackathons/Expanding-a-versatile-antimicrobial-resistance-pipeline/blob/master/Slide1.PNG "architecture flowchart 1")

## How to Use ____

### Insert link to website here

### Insert software workflow diagram here

### Insert file structure diagram here

## Installation options

We provide two options for installing <this software>: Docker or directly from Github.

### Docker

The Docker image contains <this software> as well as a webserver and FTP server in case you want to deploy the FTP server. It does also contain a web server for testing the <this software> main website (but should only be used for debug purposes).

1. `docker pull ncbihackathons/<this software>` command to pull the image from the DockerHub
2. `docker run ncbihackathons/<this software>` Run the docker image from the master shell script
3. Edit the configuration files as below

### Installing <this software> from Github

1. `git clone https://github.com/NCBI-Hackathons/<this software>.git`
2. Edit the configuration files as below
3. `sh server/<this software>.sh` to test
4. Add cron job as required (to execute <this software>.sh script)

### Configuration

```Examples here```

# Testing

We tested four different tools with <this software>. They can be found in [server/tools/](server/tools/) . 

# Additional Functionality

### DockerFile

<this software> comes with a Dockerfile which can be used to build the Docker image.

  1. `git clone https://github.com/NCBI-Hackathons/<this software>.git`
  2. `cd server`
  3. `docker build --rm -t <this software>/<this software> .`
  4. `docker run -t -i <this software>/<this software>`
  


### Website

There is also a Docker image for hosting the main website. This should only be used for debug purposes.

  1. `git clone https://github.com/NCBI-Hackathons/<this software>.git`
  2. `cd Website`
  3. `docker build --rm -t <this software>/website .`
  4. `docker run -t -i <this software>/website`
  
 # Next Steps
There exists many ways this project can be improved in the future. As TB Portals collects more data from high-burden TB countries throughout the world, these models can be trained and updated to ensure a wider applicability of drug-resistant TB probability to more populations. As more data is collected, the opportunity to retrain these models to use clinical data and XCR images to be able to predict the probability of specific drug resistance (e.g. MDR-TB, XDR-TB, RR_TB) also increases. A final future goal for PHANTUM is to ensure that the entire workflow can be HIPAA compliant (or compliant to whichever regulatory body exists for each end user) to help maintain the integrity of this project. 
  
# Contributors 
* Kelly Carey, MPH
* Byron Gaskin, PhD
* Octavio Juarez-Espinosa, PhD
* Leo Meister, MS
* Chris Shin, BS
* Kyle Webb, MS
