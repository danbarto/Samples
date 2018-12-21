import copy, os, sys
from RootTools.core.Sample import Sample
import ROOT

# Logging
if __name__=="__main__":
    import Samples.Tools.logger as logger
    logger = logger.get_logger("INFO", logFile = None )
    import RootTools.core.logger as logger_rt
    logger_rt = logger_rt.get_logger("INFO", logFile = None )
else:
    import logging
    logger = logging.getLogger(__name__)

from Samples.Tools.config import dbDir, redirector, redirector_global
dbFile = dbDir+"DB_Autumn18.sql"

# specify a local directory if you want to create (and afterwards automatically use) a local copy of the sample, otherwise use the grid.

## DY
DYJetsToLL_M50_LO       = Sample.nanoAODfromDAS("DYJetsToLL_M50_LO", "/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIAutumn18NanoAOD-102X_upgrade2018_realistic_v15-v1/NANOAODSIM", dbFile=dbFile, redirector=redirector, xSection=2008.*3)
DYJetsToLL_M50          = Sample.nanoAODfromDAS("DYJetsToLL_M50", "/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAOD-102X_upgrade2018_realistic_v15-v1/NANOAODSIM", dbFile=dbFile, redirector=redirector, xSection=2008.*3)

DY = [
    DYJetsToLL_M50_LO,
    DYJetsToLL_M50,
]

## ttbar
TTLep_pow       = Sample.nanoAODfromDAS("TTLep_pow", "/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18NanoAOD-102X_upgrade2018_realistic_v15-v1/NANOAODSIM", dbFile=dbFile, redirector=redirector, xSection=831.76*((3*0.108)**2) )

TTV = [
]

top = [
    TTLep_pow,
    ] + TTV

## di/multiboson
WW      = Sample.nanoAODfromDAS("WW", "/WW_TuneCP5_13TeV-pythia8/RunIIAutumn18NanoAOD-102X_upgrade2018_realistic_v15-v1/NANOAODSIM", dbFile=dbFile, redirector=redirector, xSection=63.21 * 1.82)

boson = [
    WW,
]

wjets = [
]

## rare

rare = [
]

other = [
]

GluGluToContinToZZTo2e2mu   = Sample.nanoAODfromDAS("GluGluToContinToZZTo2e2mu",   "/GluGluToContinToZZTo2e2mu_13TeV_MCFM701_pythia8/RunIIAutumn18NanoAOD-102X_upgrade2018_realistic_v15-v1/NANOAODSIM", dbFile=dbFile, redirector=redirector, xSection=0.005423)
GluGluToContinToZZTo2e2tau  = Sample.nanoAODfromDAS("GluGluToContinToZZTo2e2tau",  "/GluGluToContinToZZTo2e2tau_13TeV_MCFM701_pythia8/RunIIAutumn18NanoAOD-102X_upgrade2018_realistic_v15-v1/NANOAODSIM", dbFile=dbFile, redirector=redirector, xSection=0.005423)

gluglu = [
    GluGluToContinToZZTo2e2mu,
    GluGluToContinToZZTo2e2tau,
]

allSamples = DY + top + boson + wjets + rare + other + gluglu

for s in allSamples:
    s.isData = False