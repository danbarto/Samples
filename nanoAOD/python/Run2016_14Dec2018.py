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
dbFile = dbDir+"DB_Run2016_14Dec2018.sql"

# specify a local directory if you want to create (and afterwards automatically use) a local copy of the sample, otherwise use the grid.

## DoubleMuon
DoubleMuon_Run2016B_14Dec2018_ver1  = Sample.nanoAODfromDAS("DoubleMuon_Run2016B_14Dec2018_ver1",   "/DoubleMuon/Run2016B_ver1-Nano14Dec2018_ver1-v1/NANOAOD", dbFile=dbFile, redirector=redirector)
DoubleMuon_Run2016B_14Dec2018_ver2  = Sample.nanoAODfromDAS("DoubleMuon_Run2016B_14Dec2018_ver2",   "/DoubleMuon/Run2016B_ver2-Nano14Dec2018_ver2-v1/NANOAOD", dbFile=dbFile, redirector=redirector)
DoubleMuon_Run2016C_14Dec2018       = Sample.nanoAODfromDAS("DoubleMuon_Run2016C_14Dec2018",        "/DoubleMuon/Run2016C-Nano14Dec2018-v1/NANOAOD",           dbFile=dbFile, redirector=redirector)
DoubleMuon_Run2016D_14Dec2018       = Sample.nanoAODfromDAS("DoubleMuon_Run2016D_14Dec2018",        "/DoubleMuon/Run2016D-Nano14Dec2018-v1/NANOAOD",           dbFile=dbFile, redirector=redirector)
DoubleMuon_Run2016E_14Dec2018       = Sample.nanoAODfromDAS("DoubleMuon_Run2016E_14Dec2018",        "/DoubleMuon/Run2016E-Nano14Dec2018-v1/NANOAOD",           dbFile=dbFile, redirector=redirector)
DoubleMuon_Run2016F_14Dec2018       = Sample.nanoAODfromDAS("DoubleMuon_Run2016F_14Dec2018",        "/DoubleMuon/Run2016F-Nano14Dec2018-v1/NANOAOD",           dbFile=dbFile, redirector=redirector)
DoubleMuon_Run2016G_14Dec2018       = Sample.nanoAODfromDAS("DoubleMuon_Run2016G_14Dec2018",        "/DoubleMuon/Run2016G-Nano14Dec2018-v1/NANOAOD",           dbFile=dbFile, redirector=redirector)
DoubleMuon_Run2016H_14Dec2018       = Sample.nanoAODfromDAS("DoubleMuon_Run2016H_14Dec2018",        "/DoubleMuon/Run2016H-Nano14Dec2018-v1/NANOAOD",           dbFile=dbFile, redirector=redirector)

DoubleMuon_Run2016 = [\
    DoubleMuon_Run2016B_14Dec2018_ver1,
    DoubleMuon_Run2016B_14Dec2018_ver2,
    DoubleMuon_Run2016C_14Dec2018,
    DoubleMuon_Run2016D_14Dec2018,
    DoubleMuon_Run2016E_14Dec2018,
    DoubleMuon_Run2016F_14Dec2018,
    DoubleMuon_Run2016G_14Dec2018,
    DoubleMuon_Run2016H_14Dec2018,
    ]

## MuonEG
MuonEG_Run2016B_14Dec2018_ver1  = Sample.nanoAODfromDAS("MuonEG_Run2016B_14Dec2018_ver1",   "/MuonEG/Run2016B_ver1-Nano14Dec2018_ver1-v1/NANOAOD", dbFile=dbFile, redirector=redirector)
MuonEG_Run2016B_14Dec2018_ver2  = Sample.nanoAODfromDAS("MuonEG_Run2016B_14Dec2018_ver2",   "/MuonEG/Run2016B_ver2-Nano14Dec2018_ver2-v1/NANOAOD", dbFile=dbFile, redirector=redirector)
MuonEG_Run2016C_14Dec2018       = Sample.nanoAODfromDAS("MuonEG_Run2016C_14Dec2018",        "/MuonEG/Run2016C-Nano14Dec2018-v1/NANOAOD",           dbFile=dbFile, redirector=redirector)
MuonEG_Run2016D_14Dec2018       = Sample.nanoAODfromDAS("MuonEG_Run2016D_14Dec2018",        "/MuonEG/Run2016D-Nano14Dec2018-v1/NANOAOD",           dbFile=dbFile, redirector=redirector)
MuonEG_Run2016E_14Dec2018       = Sample.nanoAODfromDAS("MuonEG_Run2016E_14Dec2018",        "/MuonEG/Run2016E-Nano14Dec2018-v1/NANOAOD",           dbFile=dbFile, redirector=redirector)
MuonEG_Run2016F_14Dec2018       = Sample.nanoAODfromDAS("MuonEG_Run2016F_14Dec2018",        "/MuonEG/Run2016F-Nano14Dec2018-v1/NANOAOD",           dbFile=dbFile, redirector=redirector)
MuonEG_Run2016G_14Dec2018       = Sample.nanoAODfromDAS("MuonEG_Run2016G_14Dec2018",        "/MuonEG/Run2016G-Nano14Dec2018-v1/NANOAOD",           dbFile=dbFile, redirector=redirector)
MuonEG_Run2016H_14Dec2018       = Sample.nanoAODfromDAS("MuonEG_Run2016H_14Dec2018",        "/MuonEG/Run2016H-Nano14Dec2018-v1/NANOAOD",           dbFile=dbFile, redirector=redirector)

MuonEG_Run2016 = [\
    MuonEG_Run2016B_14Dec2018_ver1,
    MuonEG_Run2016B_14Dec2018_ver2,
    MuonEG_Run2016C_14Dec2018,
    MuonEG_Run2016D_14Dec2018,
    MuonEG_Run2016E_14Dec2018,
    MuonEG_Run2016F_14Dec2018,
    MuonEG_Run2016G_14Dec2018,
    MuonEG_Run2016H_14Dec2018,
    ]

## DoubleEG
DoubleEG_Run2016B_14Dec2018_ver1    = Sample.nanoAODfromDAS("DoubleEG_Run2016B_14Dec2018_ver1", "/DoubleEG/Run2016B_ver1-Nano14Dec2018_ver1-v1/NANOAOD", dbFile=dbFile, redirector=redirector)
DoubleEG_Run2016B_14Dec2018_ver2    = Sample.nanoAODfromDAS("DoubleEG_Run2016B_14Dec2018_ver2", "/DoubleEG/Run2016B_ver2-Nano14Dec2018_ver2-v1/NANOAOD", dbFile=dbFile, redirector=redirector)
DoubleEG_Run2016C_14Dec2018         = Sample.nanoAODfromDAS("DoubleEG_Run2016C_14Dec2018",      "/DoubleEG/Run2016C-Nano14Dec2018-v1/NANOAOD",           dbFile=dbFile, redirector=redirector)
DoubleEG_Run2016D_14Dec2018         = Sample.nanoAODfromDAS("DoubleEG_Run2016D_14Dec2018",      "/DoubleEG/Run2016D-Nano14Dec2018-v1/NANOAOD",           dbFile=dbFile, redirector=redirector)
DoubleEG_Run2016E_14Dec2018         = Sample.nanoAODfromDAS("DoubleEG_Run2016E_14Dec2018",      "/DoubleEG/Run2016E-Nano14Dec2018-v1/NANOAOD",           dbFile=dbFile, redirector=redirector)
DoubleEG_Run2016F_14Dec2018         = Sample.nanoAODfromDAS("DoubleEG_Run2016F_14Dec2018",      "/DoubleEG/Run2016F-Nano14Dec2018-v1/NANOAOD",           dbFile=dbFile, redirector=redirector)
DoubleEG_Run2016G_14Dec2018         = Sample.nanoAODfromDAS("DoubleEG_Run2016G_14Dec2018",      "/DoubleEG/Run2016G-Nano14Dec2018-v1/NANOAOD",           dbFile=dbFile, redirector=redirector)
DoubleEG_Run2016H_14Dec2018         = Sample.nanoAODfromDAS("DoubleEG_Run2016H_14Dec2018",      "/DoubleEG/Run2016H-Nano14Dec2018-v1/NANOAOD",           dbFile=dbFile, redirector=redirector)

DoubleEG_Run2016 = [\
    DoubleEG_Run2016B_14Dec2018_ver1,
    DoubleEG_Run2016B_14Dec2018_ver2,
    DoubleEG_Run2016C_14Dec2018,
    DoubleEG_Run2016D_14Dec2018,
    DoubleEG_Run2016E_14Dec2018,
    DoubleEG_Run2016F_14Dec2018,
    DoubleEG_Run2016G_14Dec2018,
    DoubleEG_Run2016H_14Dec2018,
    ]
    
## SingleElectron
SingleElectron_Run2016B_14Dec2018_ver1    = Sample.nanoAODfromDAS("SingleElectron_Run2016B_14Dec2018_ver1", "/SingleElectron/Run2016B_ver1-Nano14Dec2018_ver1-v1/NANOAOD", dbFile=dbFile, redirector=redirector)
SingleElectron_Run2016B_14Dec2018_ver2    = Sample.nanoAODfromDAS("SingleElectron_Run2016B_14Dec2018_ver2", "/SingleElectron/Run2016B_ver2-Nano14Dec2018_ver2-v1/NANOAOD", dbFile=dbFile, redirector=redirector)
SingleElectron_Run2016C_14Dec2018         = Sample.nanoAODfromDAS("SingleElectron_Run2016C_14Dec2018",      "/SingleElectron/Run2016C-Nano14Dec2018-v1/NANOAOD",           dbFile=dbFile, redirector=redirector)
SingleElectron_Run2016D_14Dec2018         = Sample.nanoAODfromDAS("SingleElectron_Run2016D_14Dec2018",      "/SingleElectron/Run2016D-Nano14Dec2018-v1/NANOAOD",           dbFile=dbFile, redirector=redirector)
SingleElectron_Run2016E_14Dec2018         = Sample.nanoAODfromDAS("SingleElectron_Run2016E_14Dec2018",      "/SingleElectron/Run2016E-Nano14Dec2018-v1/NANOAOD",           dbFile=dbFile, redirector=redirector)
SingleElectron_Run2016F_14Dec2018         = Sample.nanoAODfromDAS("SingleElectron_Run2016F_14Dec2018",      "/SingleElectron/Run2016F-Nano14Dec2018-v1/NANOAOD",           dbFile=dbFile, redirector=redirector)
SingleElectron_Run2016G_14Dec2018         = Sample.nanoAODfromDAS("SingleElectron_Run2016G_14Dec2018",      "/SingleElectron/Run2016G-Nano14Dec2018-v1/NANOAOD",           dbFile=dbFile, redirector=redirector)
SingleElectron_Run2016H_14Dec2018         = Sample.nanoAODfromDAS("SingleElectron_Run2016H_14Dec2018",      "/SingleElectron/Run2016H-Nano14Dec2018-v1/NANOAOD",           dbFile=dbFile, redirector=redirector)

SingleElectron_Run2016 = [\
    SingleElectron_Run2016B_14Dec2018_ver1,
    SingleElectron_Run2016B_14Dec2018_ver2,
    SingleElectron_Run2016C_14Dec2018,
    SingleElectron_Run2016D_14Dec2018,
    SingleElectron_Run2016E_14Dec2018,
    SingleElectron_Run2016F_14Dec2018,
    SingleElectron_Run2016G_14Dec2018,
    SingleElectron_Run2016H_14Dec2018,
    ]
    
## SingleMuon
SingleMuon_Run2016B_14Dec2018_ver1    = Sample.nanoAODfromDAS("SingleMuon_Run2016B_14Dec2018_ver1", "/SingleMuon/Run2016B_ver1-Nano14Dec2018_ver1-v1/NANOAOD", dbFile=dbFile, redirector=redirector)
SingleMuon_Run2016B_14Dec2018_ver2    = Sample.nanoAODfromDAS("SingleMuon_Run2016B_14Dec2018_ver2", "/SingleMuon/Run2016B_ver2-Nano14Dec2018_ver2-v1/NANOAOD", dbFile=dbFile, redirector=redirector)
SingleMuon_Run2016C_14Dec2018         = Sample.nanoAODfromDAS("SingleMuon_Run2016C_14Dec2018",      "/SingleMuon/Run2016C-Nano14Dec2018-v1/NANOAOD",           dbFile=dbFile, redirector=redirector)
SingleMuon_Run2016D_14Dec2018         = Sample.nanoAODfromDAS("SingleMuon_Run2016D_14Dec2018",      "/SingleMuon/Run2016D-Nano14Dec2018-v1/NANOAOD",           dbFile=dbFile, redirector=redirector)
SingleMuon_Run2016E_14Dec2018         = Sample.nanoAODfromDAS("SingleMuon_Run2016E_14Dec2018",      "/SingleMuon/Run2016E-Nano14Dec2018-v1/NANOAOD",           dbFile=dbFile, redirector=redirector)
SingleMuon_Run2016F_14Dec2018         = Sample.nanoAODfromDAS("SingleMuon_Run2016F_14Dec2018",      "/SingleMuon/Run2016F-Nano14Dec2018-v1/NANOAOD",           dbFile=dbFile, redirector=redirector)
SingleMuon_Run2016G_14Dec2018         = Sample.nanoAODfromDAS("SingleMuon_Run2016G_14Dec2018",      "/SingleMuon/Run2016G-Nano14Dec2018-v1/NANOAOD",           dbFile=dbFile, redirector=redirector)
SingleMuon_Run2016H_14Dec2018         = Sample.nanoAODfromDAS("SingleMuon_Run2016H_14Dec2018",      "/SingleMuon/Run2016H-Nano14Dec2018-v1/NANOAOD",           dbFile=dbFile, redirector=redirector)

SingleMuon_Run2016 = [\
    SingleMuon_Run2016B_14Dec2018_ver1,
    SingleMuon_Run2016B_14Dec2018_ver2,
    SingleMuon_Run2016C_14Dec2018,
    SingleMuon_Run2016D_14Dec2018,
    SingleMuon_Run2016E_14Dec2018,
    SingleMuon_Run2016F_14Dec2018,
    SingleMuon_Run2016G_14Dec2018,
    SingleMuon_Run2016H_14Dec2018,
    ]
    
allSamples = DoubleMuon_Run2016 + MuonEG_Run2016 + DoubleEG_Run2016 + SingleElectron_Run2016 + SingleMuon_Run2016

for s in allSamples:
    s.isData = True