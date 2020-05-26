#!/bin/bash
pushd /afs/cern.ch/work/f/fernance/private/Long_Lived_Analysis/CMSSW_9_4_4/src
eval `scramv1 runtime -sh`
pushd
python /afs/cern.ch/work/f/fernance/private/Long_Lived_Analysis/CMSSW_9_4_4/src/MyAnalysis/Galapago-Framework/RECOEff_globalmuons.py -t global_1000_150_100 -f /eos/user/f/fernance/LLPNTuples/2016/HXX/v1/HXX_1000_150_100.root