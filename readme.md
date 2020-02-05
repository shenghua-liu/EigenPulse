Overview
========
This is the implementation for the *EigenPulse* algorithm described in the paper: "EigenPulse: Detecting Surges in LargeStreaming Graphs with Row Augmentation".

In this paper, we  reasonably  model  the  streaming  graph  as  a  row-augmented matrix,  and  propose,  EigenPulse,  to  detect  surges  in  large  streaming  graphs, based on the singular spectrum of the matrix.  EigenPulse has the following advantages:  (1) Incremental singular value decomposition: we propose an algorithm, *AugSVD*, which can output the spectral values of graph nodes at each time window; (2) Robust: we theoretically analyze that the robust approximation of AugSVD to batch SVD. (3) Effectiveness:  EigenPulse  can  detect  suspicious  synchronized  activities accurately in real-world graphs.

Requirements
========
 This project is written in Python 3.6
 We suggest recreating the experimental environment using Anaconda through the following steps.
 
 1、Clone the project
```
git clone https://github.com/shenghua-liu/EigenPulse.git
```
2、Install the appropriate version for Anaconda from here - https://www.anaconda.com/distribution/

3、Create a new conda environment named "eigenpulse" and install requirements.
```bash
conda create -n eigenpulse python=3.6
conda activate eigenpulse
pip install --user --requirement requirements.txt
```
4、install code
```
pip install -e code
```

Experiments
========
- For demo, we use BeerAdvocate dataset
```
python beer.py
```
- Input data should be in chronological sequence, like */dataset/beer/input.tensor*,  a preprocessed BeerAdvocate data.
- The output dir is /output/beer/.
- See *beer.py* for  complete parameter introduction.
