# similar-articles

This project trains embeddings for scientific articles
using data collected from the INSPIRE-HEP API.  
See [here](https://celis.github.io/personal/recommender/gensim/python/aws/flask/2020/02/20/hep-recommender.html) for more details about the project.

The embeddings are used by the [hep-recommender](https://www.hep-recommender.com) web application
to provide similar article recommendations in the field of 
High Energy Physics.   The web application can be found in [this](https://github.com/celis/hep-recommender) repository.


### Usage: 

Start a virtual environment and install the necessary dependencies using 

    pip install -r requirements.txt
    
Data is stored in a AWS S3 bucket, adjust 'aws_config.json' 
with the corresponding credentials. 

Model training is done by running the script

    python model_training.py
    
The trained embeddings will be uploaded to AWS S3 at the end.    