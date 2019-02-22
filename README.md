# PHANTUM2: Predicting Human Adolescent outcomes from Text-and-image-data Using Machine Learning

*An ODSET Emerging Leader in Data Science Fellows (ELFs) at NIH/NIAID Product*


![alt text](https://github.com/NCBI-Hackathons/Expanding-a-versatile-antimicrobial-resistance-pipeline/blob/master/final%20elf-icon%20size.png "elf logo") 

###### Icon made by [Eucalyp](https://www.flaticon.com/authors/eucalyp) from flaticon.com and edited by Chris Shin


## What's New?
At the 12th NIH Research Festival Collaborative Data Science and Machine Learning Hackathon that took place from September 10th to 12th, 2018, PHANTUM (Predicting Human ANtimicrobial-resistant Tuberculosis Using Machine Learning), web tool for rapid prediction of TB drug resistance probability at point-of-care, was born.

We came together again for the February 2019 NIH BioData Science Hackathon to tie up any loose ends we had left and to try to incorporate a new data set from the ABCD study. During this second hackathon, we decided to update the acronym to reflect the new data set we incorporated. 

## What is the ABCD study?
The ABCD (Adolescent Brain and Cognitive Development) study is a multi-center longitudinal study that follows the brain development and health of 11,875 9-10 year olds through adolescence. This study aims to understand how childhood experiences interact with each other during childhood and adolescence to affect brain development and other outcomes, including social, behavioral, and health. The official study website is available [here] (https://abcdstudy.org/index.html). 

On October 31, 2018, there was an annual release (1.1 release) made available to qualified researchers on [NIMH Data Archive](https://data-archive.nimh.nih.gov/). We chose to use demographic and socioeconomic measures, MRI images, and results of the K-SADS questionnaire administered to the study participants. 

## What is K-SADS?
K-SADS is an acronym for Kiddie Schedule for Affective Disorders and Schizophrenia, and it is a semi-structured interview that measures symptoms of mood, anxiety, psychotic and disruptive behavior disorders in children aged 6-18. K-SADS results reflect the DSM-5, the Diagnostic and Statistical Manual of Mental Disorders 5th Edition which is used for psychiatric diagnoses.

The K-SADS can be administered to both children and parents (where the parents answer about their children). 

## Why Use the K-SADS?
We used the DSM-5 diagnosis of sleep problems as outcome points for our model to predict on using demographic and socioeconomic measures, history of traumatic events, and MRI images. By training on the data made available by the ABCD study, we may be able to develop a point-of-care diagnostic for predicting certain DSM-5 classifications using clinical data, developmental history data, and MRI scans.

### Who is PHANTUM/PHANTUM2 developed for?
PHANTUM was initially developed for clinicians who have the necessary clinical measures and corresponding CXR for a patient(see section: How to Use PHANTOM for a list of clinical measures). 

PHANTUM2 was developed for clinicals who have the necessary demographic information, results of the K-SADS, and MRI scans. 

## How Does PHANTUM work?
PHANTUM uses a weighted average of two prediction modules (for the two different types of data) to make a final decision. We decided to use the [RWeka package](https://cran.r-project.org/web/packages/RWeka/index.html) in the R statistical language to generat C4.5 pruned decision trees using the following clinical values: age of TB onset, gender, BMI, and clinical decision/type of resistance.

We used the [PyTorch package](https://github.com/pytorch/pytorch) in Python to develop a convoluted neural network (CNN) trained on a proportion of the CXR images from TB Portals. 

![alt text](https://github.com/NCBI-Hackathons/Expanding-a-versatile-antimicrobial-resistance-pipeline/blob/master/Slide1.PNG "architecture flowchart 1")

## How to Use PHANTUM/PHANTUM2
The frontend of PHANTUM consists of a website where users can upload a CXR and enter clinical measures into a form. 

The frontend of PHANTUM2 consists of ......

### Website 
https://ncbi-hackathons.github.io/PHANTUM/

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
* Leo Meister, Sysadmin, NIH/NIAID/OD/OSMO/ODSET, leo.meister@nih.gov :deciduous_tree:
* Chris Shin, Writer, NIH/NIAID/OD/OSMO/ODSET, chris.shin@nih.gov :cherry_blossom:
