# RecoLearn
A Recommendation Engine for E-Learners

Operating System Tested on : Ubuntu 20.04

Run the following commands : 
```bash
sudo apt-get update
sudo apt-get install -y git bzip2 unzip

wget https://repo.continuum.io/miniconda/Miniconda2-latest-Linux-x86_64.sh
bash Miniconda2-latest-Linux-x86_64.sh
export PATH="/home/$USER/miniconda2/bin:$PATH"

git clone https://github.com/ParthPratim/RecoLearn.git
cd RecoLearn/recolearn/tensorflow-recommendation-wals
conda create -y -n tfrec
conda install -y -n tfrec --file conda.txt
source activate tfrec
pip install -r requirements.txt
pip install tensorflow==1.15
pip install django

cd ../
python manage.py runserver
```

Open in the browser : http://127.0.0.1:8000/recoapp/?user_id=X
                      where X can be any integer between 1-942

