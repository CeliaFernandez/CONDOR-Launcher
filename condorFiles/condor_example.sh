
universe                = vanilla
executable              = $(filename)
output                  = /afs/cern.ch/work/f/fernance/private/Analysis-Utils/CMSSW_9_4_4/src/Analysis/CONDOR-Launcher/logs/$(ClusterId).$(ProcId).out
error                   = /afs/cern.ch/work/f/fernance/private/Analysis-Utils/CMSSW_9_4_4/src/Analysis/CONDOR-Launcher/logs/$(ClusterId).$(ProcId).err
log                     = /afs/cern.ch/work/f/fernance/private/Analysis-Utils/CMSSW_9_4_4/src/Analysis/CONDOR-Launcher/logs/$(ClusterId).log
Notify_user             = fernance@cern.ch
+JobFlavour = "microcentury" 
queue filename matching /afs/cern.ch/work/f/fernance/private/Analysis-Utils/CMSSW_9_4_4/src/Analysis/CONDOR-Launcher/bashFiles/bash_200522_163050.sh
