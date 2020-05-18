# CONDOR-Launcher

Code to launch single jobs to a CONDOR queue.

## Installation 

The repo must be installed on top a CMSSW release, e.g. for 9_4_4:

```
cmsrel CMSSW_9_4_4

cd CMSSW_9_4_4/src

scram b

cmsenv

git clone https://github.com/CeliaFernandez/CONDOR-Launcher.git 
```

Then, an alias must be included in the .bashrc file:
```
alias toCONDOR="python [yourpath]/toCONDOR.py"
```


## Instructions to run

Once the .bashrc file has been modified accordingly, the command to launch a job is:

```
toCONDOR [queue] [command]
```

Usage example:

```
toCONDOR espresso python my/python/file/prueba.py
```

or:

```
toCONDOR espresso python $PWD/prueba.py
```


Important: The path to the script we want to run e.g. prueba.py, must be an absolute path.

