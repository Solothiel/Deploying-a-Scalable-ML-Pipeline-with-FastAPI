Working in a command line environment is recommended for ease of use with git and dvc. If on Windows, WSL1 or 2 is recommended.

original readme file renamed README2

# Environment Set up (pip or conda)
* used the supplied file `environment.yml` to create a new environment with conda
* Jupyter-Lab
* Windows WSL1 installed Unbuntu
* Visual Studio Code
    
## Repositories
* Forked Repository then cloned it locally.
* https://github.com/Solothiel/Deploying-a-Scalable-ML-Pipeline-with-FastAPI

# Data
* Census.csv

# Model
* Used a Random Forest Classification
* Framework was scikit-learn and OneHotEncoder
* Model card created

# API Creation
*  Create a RESTful API using FastAPI.
    *http://127.01.01.1:8000  
    * Created a Welcome Message ["Waking up the gerbil on the Wheel!"]
    * POST that does model inference.