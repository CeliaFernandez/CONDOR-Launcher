import optparse
import os
import sys
import __main__
from datetime import datetime

#################
##-  globals  -##
#################

# Time:
global time 
now = datetime.now()
time = now.strftime("%y%m%d_%H%M%S")

# Global paths:
global workdir 
workdir = os.path.dirname(os.path.abspath(__main__.__file__))

global logpath
logpath = workdir + '/' + 'logs/'


##############
##-  Init  -##
##############

if not os.path.exists('logs'): os.makedirs('logs')
if not os.path.exists('bashFiles'): os.makedirs('bashFiles')
if not os.path.exists('condorFiles'): os.makedirs('condorFiles')


###################
##-  Functions  -##
###################

def identifyCMSSW(command):

    """ Function to identify release of a given path """
    cmsswpart = False
    for part in command.split():
        if 'CMSSW' in part:
            cmsswpart = part

    cmsswpath = '' 
    for level in cmsswpart.split('/'):
        cmsswpath += level + '/'
        if 'CMSSW' in level: 
            cmsswpath += 'src'
            break

    return cmsswpath

def makeBashFile(command):

    cmssw = identifyCMSSW(command)

    bashTemplate = """#!/bin/bash
pushd {0}
eval `scramv1 runtime -sh`
pushd
""".format(cmssw)

    bashTemplate += command

    bashpath = workdir + '/bashFiles/' + 'bash_' + time + '.sh'
    _f = open(bashpath, 'w')
    _f.write(bashTemplate)
    _f.close()

    return bashpath


def makeCondorFile(queue, bashpath):

    condorTemplate = """
universe                = vanilla
executable              = $(filename)
output                  = {0}$(ClusterId).$(ProcId).out
error                   = {0}$(ClusterId).$(ProcId).err
log                     = {0}$(ClusterId).log
Notify_user             = fernance@cern.ch
+JobFlavour = "{1}" 
queue filename matching {2}
""".format(logpath, queue, bashpath)

    condorpath = workdir + '/condorFiles/' + 'condor_' + time + '.sh'
    _f = open(condorpath, 'w')
    _f.write(condorTemplate)
    _f.close()

    return condorpath


##############
##-  main  -##
##############

if __name__ == "__main__":


    ## -> Exit if there are missed arguments
    if not len(sys.argv) > 2:
        sys.exit("Usage: toCONDOR [queue] [command to launch]")

    ## Collect parameters:
    queue = sys.argv[1]
    command = ''
    for i in range(2, len(sys.argv)):
        command += sys.argv[i]
        if not i == (len(sys.argv) - 1): command += ' ' 

    ## Verbose:
    print(" > Launching to queue: " + queue)
    print(" > Command to launch: " + command)


    ## Create bash and condor files for submission:
    bashFile = makeBashFile(command)
    condorFile = makeCondorFile(queue, bashFile)

    ## Launch job.
    os.system('chmod +x ' + bashFile)
    os.system('chmod +x ' + condorFile)
    os.system('condor_submit ' + condorFile)











