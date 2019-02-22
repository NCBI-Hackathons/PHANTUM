# Use official Ubuntu 16.04 as parent image
FROM conda/miniconda3

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

#RUN apt-get update

# Install all OS dependencies for notebook server that starts but lacks all
# features (e.g., download as all possible file formats)
RUN apt-get update && apt-get -yq dist-upgrade \
 && apt-get install -yq --no-install-recommends \
    wget \
    bzip2 \
    ca-certificates \
    sudo \
    locales \
    fonts-liberation \
    vim \
###
    openjdk-8-jdk \
    git \
    curl \
###
 && apt-get clean

# Install any needed packages specified in requirements.txt
#RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 5002

# Define environment variable
#ENV NAME World

RUN conda install --quiet --yes -c conda-forge flask
RUN conda install --quiet --yes -c conda-forge flask-cors
RUN conda install --quiet --yes -c conda-forge flask-restful
RUN conda install --quiet --yes pandas
RUN conda install --quiet --yes scikit-learn
RUN conda install --quiet --yes requests

#RUN git clone https://github.com/NCBI-Hackathons/PHANTUM.git

# Set the working directory to /app/PHANTUM/server_service_provider
#WORKDIR /app/PHANTUM/server_service_provider

# Set the working directory to /app/bind
WORKDIR /app/bind

# Run app.py when the container launches
#CMD ["echo", "hey!"]
#CMD ["python", "service_provider_backend.py"]
CMD ["./run_script"]
