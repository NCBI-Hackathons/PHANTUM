# PHANTUM2: Predicting Human Adolescent outcomes from Text-and-image-data Using Machine Learning

*An ODSET Emerging Leader in Data Science Fellows (ELFs) at NIH/NIAID Product*


![alt text](https://github.com/NCBI-Hackathons/Expanding-a-versatile-antimicrobial-resistance-pipeline/blob/master/final%20elf-icon%20size.png "elf logo") 

###### Icon made by [Eucalyp](https://www.flaticon.com/authors/eucalyp) from flaticon.com and edited by Chris Shin


## What's New?
At the 12th NIH Research Festival Collaborative Data Science and Machine Learning Hackathon that took place from September 10th to 12th, 2018, PHANTUM (Predicting Human ANtimicrobial-resistant Tuberculosis Using Machine Learning), web tool for rapid prediction of TB drug resistance probability at point-of-care, was born.

We came together again for the February 2019 NIH BioData Science Hackathon to tie up any loose ends we had left and to try to incorporate a new data set from the ABCD study. 

## What is the ABCD study?
The ABCD (Adolescent Brain and Cognitive Development) study is a multi-center longitudinal study that follows the brain development and health of 11,875 9-10 year olds through adolescence. This study aims to understand how childhood experiences interact with each other during childhood and adolescence to affect brain development and other outcomes, including social, behavioral, and health. We chose to look at the data released 

## What is TB?
Tuberculosis (TB) is an infectious bacterial disease that usually affects the lungs but can also affect other parts of the body, such as the brain, the kidneys, or the spine. Most cases of TB are treatable and curable, but because the majority of TB cases occur in developing areas of the world, the majority of people with TB do not have access to proper treatment. 

There are 10 drugs currently [approved by the U.S. Food and Drug Administration (FDA)](https://www.cdc.gov/tb/topic/treatment/tbdisease.htm) for treating TB. Of these approved drugs, the first-line anti-TB agents that form the core of treatment regimens are isoniazid, rifampin, ethambutol, and pyrazinamide. 

Drug-resistant TB occurs when bacteria become resistant to the drugs used to treat TB. The [WHO](http://www.who.int/tb/areas-of-work/drug-resistant-tb/types/en/) describes 5 resistance types: mono-resistance, poly-resistance, multidrug resistance (MDR), etensive drug resistance (XDR), and Rifampicin resistance (RR). People who are diagnosed with drug-resistant TB are placed on a regimen of second-line drugs that are less effective than and have more severe side effects than first-line drugs. Mismanagement of TB treatment can lead to spread of drug-resistant TB and higher rates of death. 

To learn more about TB and NIAID's efforts to combat it, visit the [NIAID Tuberculosis Page](https://www.niaid.nih.gov/diseases-conditions/tuberculosis-tb ).

## How Bad is TB?
TB is one of the top 10 causes of death [worldwide](http://www.who.int/en/news-room/fact-sheets/detail/tuberculosis). Currently, 2 billion people (about a third of the world's population) are infected with TB. The latest statistics from the [CDC](https://www.cdc.gov/tb/statistics/default.htm) show an estimate of 10.4 million new cases of TB in 2016. Of these, the [WHO](http://www.who.int/tb/areas-of-work/drug-resistant-tb/en/) reports that 580,000 of these cases are MDR-TB/RR-TB. Only about 20% of new cases of MDR-TB/RR-TB are [estimated to be enrolled in treatment](http://apps.who.int/medicinedocs/en/d/Js23098en/). 

## What Are We Doing About TB?
Inspired by the [fast.ai deep learning MOOC](http://www.fast.ai/), we decided to develop a web tool for rapid diagnosis of TB drug resistance at point-of-care powered by ML-AI technologies. 

Three of the top 30 high-burden MDR-TB [countries](http://www.who.int/tb/publications/global_report/en/) (Azerbaijan, Belarus, and the Republic of Moldova) have data available through the [TB Portals program](https://tbportals.niaid.nih.gov/). Georgia and Romania also currently have accessible data, and TB Portals staff are currently working to collect data from other TB endemic countries such as India, China, South Africa. 

We decided to use both chest x-ray (CXR) images and clinical measures in our prediction model. CXR has high sensitivity for pulmonary TB but low specificity, and diagnosis varies depending on the observer of the CXR, and the [WHO](http://apps.who.int/iris/bitstream/handle/10665/252424/9789241511506-eng.pdf?sequence=1) recommends that TB diagnosis should be bacteriologically confirmed by sputum-sear microscopy, culture, or a molecular test. 

### Who is PHANTUM developed for?
PHANTUM was developed clinicians who have the necessary clinical measures and corresponding CXR for a patient(see section: How to Use PHANTOM for a list of clinical measures). 

## How Does PHANTUM work?
PHANTUM uses a weighted average of two prediction modules (for the two different types of data) to make a final decision. We decided to use the [RWeka package](https://cran.r-project.org/web/packages/RWeka/index.html) in the R statistical language to generat C4.5 pruned decision trees using the following clinical values: age of TB onset, gender, BMI, and clinical decision/type of resistance.

We used the [PyTorch package](https://github.com/pytorch/pytorch) in Python to develop a convoluted neural network (CNN) trained on a proportion of the CXR images from TB Portals. 

![alt text](https://github.com/NCBI-Hackathons/Expanding-a-versatile-antimicrobial-resistance-pipeline/blob/master/Slide1.PNG "architecture flowchart 1")

## How to Use PHANTUM
The frontend of PHANTUM consists of a website where users can upload a CXR and enter clinical measures into a form. 

### Website coming soon (:sweat_smile:)

### Software workflow diagram coming soon (:sweat_smile:)

### File structure diagram coming soon (:sweat_smile:)

## Installation options coming soon (:sweat_smile:)

### Docker image coming soon (:sweat_smile:)

The Docker image contains PHANTUM as well as a webserver and FTP server in case you want to deploy the FTP server. It does also contain a web server for testing the PHANTUM main website (but should only be used for debug purposes).

1. `docker pull ncbihackathons/PHANTUM` command to pull the image from the DockerHub
2. `docker run ncbihackathons/PHANTUM` Run the docker image from the master shell script
3. Edit the configuration files as below

### Installing PHANTUM from Github coming soon (:sweat_smile:)
1. `git clone https://github.com/NCBI-Hackathons/PHANTUM.git`
2. Edit the configuration files as below
3. `sh server/<this software>.sh` to test
4. Add cron job as required (to execute <this software>.sh script)
  
### Configuration coming soon (:sweat_smile:)

# Testing In Progress (:construction_worker:)

# Additional Functionality In Progress (:construction_worker:)

### DockerFile coming soon (:sweat_smile:)

PHANTUM comes with a Dockerfile which can be used to build the Docker image.

  1. `git clone https://github.com/NCBI-Hackathons/PHANTUM.git`
  2. `cd server`
  3. `docker build --rm -t <this software>/<this software> .`
  4. `docker run -t -i <this software>/<this software>`
  


### Website coming soon (:sweat_smile:)

There is also a Docker image for hosting the main website. This should only be used for debug purposes.

  1. `git clone https://github.com/NCBI-Hackathons/PHANTUM.git`
  2. `cd Website`
  3. `docker build --rm -t <this software>/website .`
  4. `docker run -t -i <this software>/website`
  
 # Next Steps
There exists many ways this project can be improved in the future. As TB Portals collects more data from high-burden TB countries throughout the world, these models can be trained and updated to ensure a wider applicability of drug-resistant TB probability to more populations. As more data is collected, the opportunity to retrain these models to use clinical data and XCR images to be able to predict the probability of specific drug resistance (e.g. MDR-TB, XDR-TB, RR_TB) also increases. A final future goal for PHANTUM is to ensure that the entire workflow can be HIPAA compliant (or compliant to whichever regulatory body exists for each end user) to help maintain the integrity of this project. 
  
# Hackathon Members
* Kelly Carey, Writer, NIH/NIAID/OD/OSMO/ODSET, kelly.carey@nih.gov :blossom:
* Byron Gaskin, Lead, NIH/NIAID/OD/OSMO/ODSET, byron.gaskin@nih.gov :evergreen_tree:
* Octavio Juarez-Espinosa, Sysadmin, octavio.juarez-espinosa@nih.gov :evergreen_tree:
* Leo Meister, Sysadmin, NIH/NIAID/OD/OSMO/ODSET, leo.meister@nih.gov :deciduous_tree:
* Chris Shin, Writer, NIH/NIAID/OD/OSMO/ODSET, chris.shin@nih.gov :cherry_blossom:
* Kyle Webb, Sysadmin, NIH/NIAID/OD/OSMO/ODSET, kyle.webb@nih.gov :deciduous_tree:
