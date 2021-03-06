import copy, os, sys
from RootTools.core.Sample import Sample
import ROOT

def get_parser():
    import argparse
    argParser = argparse.ArgumentParser(description = "Argument parser for samples file")
    argParser.add_argument('--overwrite',   action='store_true',    help="Overwrite current entry in db?")
    argParser.add_argument('--update',      action='store_true',    help="Update current entry in db?")
    return argParser

# Logging
if __name__=="__main__":
    import Samples.Tools.logger as logger
    logger = logger.get_logger("INFO", logFile = None )
    import RootTools.core.logger as logger_rt
    logger_rt = logger_rt.get_logger("INFO", logFile = None )
    options = get_parser().parse_args()
    ov = options.overwrite
    if options.update:
        ov = 'update'
else:
    import logging
    logger = logging.getLogger(__name__)
    ov = False

# Redirector
try:
    redirector = sys.modules['__main__'].redirector
except:
    from Samples.Tools.config import  redirector as redirector

# DB
from Samples.Tools.config import dbDir
dbFile = dbDir+"DB_Autumn18_private_legacy.sql"

logger.info("Using db file: %s", dbFile)

## DY
DYJetsToLL_M50_LO        = Sample.nanoAODfromDAS("DYJetsToLL_M50_LO",       "/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/llechner-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1_legacy_nano_v1-1a762c888624ed9dff74191bdeed5e1a/USER",   dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=2008.*3)
#DYJetsToLL_M50_LO_ext2   = Sample.nanoAODfromDAS("DYJetsToLL_M50_LO_ext2",  "/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/dspitzba-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v2_legacy_nano_v1-b9659cf3bef5e21efe24288a402778f7/USER",   dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=2008.*3)
DYJetsToLL_M50           = Sample.nanoAODfromDAS("DYJetsToLL_M50",          "/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/llechner-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1_legacy_nano_v1-1a762c888624ed9dff74191bdeed5e1a/USER",  dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=2008.*3)
DYJetsToLL_M10to50_LO    = Sample.nanoAODfromDAS("DYJetsToLL_M10to50_LO",   "/DYJetsToLL_M-10to50_TuneCP5_13TeV-madgraphMLM-pythia8/llechner-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2_legacy_nano_v2-1a762c888624ed9dff74191bdeed5e1a/USER",   dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=18610)


#DYJetsToLL_M50_HT70to100      =   Sample.nanoAODfromDAS("DYJetsToLL_M50_HT70to100"    ,     "/DYJetsToLL_M-50_HT-70to100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/dspitzba-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2_legacy_nano_v1-b9659cf3bef5e21efe24288a402778f7/USER",         dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=170.4*1.23)
#DYJetsToLL_M50_HT100to200_ext =   Sample.nanoAODfromDAS("DYJetsToLL_M50_HT100to200_ext",    "/DYJetsToLL_M-50_HT-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/dspitzba-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2_legacy_nano_v1-b9659cf3bef5e21efe24288a402778f7/USER",   dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=147.4*1.23)
#DYJetsToLL_M50_HT200to400     =   Sample.nanoAODfromDAS("DYJetsToLL_M50_HT200to400",        "/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/dspitzba-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2_legacy_nano_v1-b9659cf3bef5e21efe24288a402778f7/USER",        dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=40.99*1.23)
#DYJetsToLL_M50_HT200to400_ext =   Sample.nanoAODfromDAS("DYJetsToLL_M50_HT200to400_ext",    "/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/dspitzba-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2_legacy_nano_v1-b9659cf3bef5e21efe24288a402778f7/USER",   dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=40.99*1.23)
#DYJetsToLL_M50_HT400to600     =   Sample.nanoAODfromDAS("DYJetsToLL_M50_HT400to600",        "/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/dspitzba-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2_legacy_nano_v1-b9659cf3bef5e21efe24288a402778f7/USER",        dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=5.678*1.23)
#DYJetsToLL_M50_HT400to600_ext =   Sample.nanoAODfromDAS("DYJetsToLL_M50_HT400to600_ext",    "/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/dspitzba-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2_legacy_nano_v1-b9659cf3bef5e21efe24288a402778f7/USER",   dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=5.678*1.23)
#DYJetsToLL_M50_HT600to800     =   Sample.nanoAODfromDAS("DYJetsToLL_M50_HT600to800"   ,     "/DYJetsToLL_M-50_HT-600to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/dspitzba-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2_legacy_nano_v1-b9659cf3bef5e21efe24288a402778f7/USER",        dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=1.367*1.23 )
#DYJetsToLL_M50_HT800to1200    =   Sample.nanoAODfromDAS("DYJetsToLL_M50_HT800to1200"  ,     "/DYJetsToLL_M-50_HT-800to1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/dspitzba-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1_legacy_nano_v1-b9659cf3bef5e21efe24288a402778f7/USER",       dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=0.6304*1.23 )
#DYJetsToLL_M50_HT1200to2500   =   Sample.nanoAODfromDAS("DYJetsToLL_M50_HT1200to2500" ,     "/DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/dspitzba-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1_legacy_nano_v1-b9659cf3bef5e21efe24288a402778f7/USER",      dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=0.1514*1.23 )
#DYJetsToLL_M50_HT2500toInf    =   Sample.nanoAODfromDAS("DYJetsToLL_M50_HT2500toInf"  ,     "/DYJetsToLL_M-50_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/dspitzba-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1_legacy_nano_v1-b9659cf3bef5e21efe24288a402778f7/USER",       dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=0.003565*1.23 )

DYJetsM50HT = [
#    DYJetsToLL_M50_HT70to100   , 
#   DYJetsToLL_M50_HT100to200_ext,
#   DYJetsToLL_M50_HT200to400,
#   DYJetsToLL_M50_HT200to400_ext,
#   DYJetsToLL_M50_HT400to600,
#   DYJetsToLL_M50_HT400to600_ext,
#   DYJetsToLL_M50_HT600to800  ,
#   DYJetsToLL_M50_HT800to1200 ,
#   DYJetsToLL_M50_HT1200to2500,
#   DYJetsToLL_M50_HT2500toInf ,
]

#DYJetsToLL_M5to50_HT70to100      = Sample.nanoAODfromDAS("DYJetsToLL_M5to50_HT70to100"     , "/DYJetsToLL_M-5to50_HT-70to100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/dspitzba-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2_legacy_nano_v1-b9659cf3bef5e21efe24288a402778f7/USER",         dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=303.4) #LO without 1.23 k-factor
#DYJetsToLL_M5to50_HT100to200     = Sample.nanoAODfromDAS("DYJetsToLL_M5to50_HT100to200"    , "/DYJetsToLL_M-5to50_HT-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/dspitzba-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2_legacy_nano_v1-b9659cf3bef5e21efe24288a402778f7/USER",        dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=224.2) #LO without 1.23 k-factor
#DYJetsToLL_M5to50_HT100to200_ext = Sample.nanoAODfromDAS("DYJetsToLL_M5to50_HT100to200_ext", "/DYJetsToLL_M-5to50_HT-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/dspitzba-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2_legacy_nano_v1-b9659cf3bef5e21efe24288a402778f7/USER",   dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=224.2) #LO without 1.23 k-factor
#DYJetsToLL_M5to50_HT200to400     = Sample.nanoAODfromDAS("DYJetsToLL_M5to50_HT200to400"    , "/DYJetsToLL_M-5to50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/dspitzba-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2_legacy_nano_v1-b9659cf3bef5e21efe24288a402778f7/USER",        dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=37.2) #LO without 1.23 k-factor
#DYJetsToLL_M5to50_HT200to400_ext = Sample.nanoAODfromDAS("DYJetsToLL_M5to50_HT200to400_ext", "/DYJetsToLL_M-5to50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/dspitzba-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2_legacy_nano_v1-b9659cf3bef5e21efe24288a402778f7/USER",   dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=37.2) #LO without 1.23 k-factor
#DYJetsToLL_M5to50_HT400to600     = Sample.nanoAODfromDAS("DYJetsToLL_M5to50_HT400to600"    , "/DYJetsToLL_M-5to50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/dspitzba-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2_legacy_nano_v1-b9659cf3bef5e21efe24288a402778f7/USER",        dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=3.581) #LO without 1.23 k-factor
#DYJetsToLL_M5to50_HT400to600_ext = Sample.nanoAODfromDAS("DYJetsToLL_M5to50_HT400to600_ext", "/DYJetsToLL_M-5to50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/dspitzba-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2_legacy_nano_v1-b9659cf3bef5e21efe24288a402778f7/USER",   dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=3.581) #LO without 1.23 k-factor
#DYJetsToLL_M5to50_HT600toInf     = Sample.nanoAODfromDAS("DYJetsToLL_M5to50_HT600toInf"    , "/DYJetsToLL_M-5to50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/dspitzba-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2_legacy_nano_v1-b9659cf3bef5e21efe24288a402778f7/USER",        dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=1.124) #LO without 1.23 k-factor

DYJetsM5to50HT = [
#   DYJetsToLL_M5to50_HT70to100,
#   DYJetsToLL_M5to50_HT100to200,
#   DYJetsToLL_M5to50_HT100to200_ext,
#   DYJetsToLL_M5to50_HT200to400,
#   DYJetsToLL_M5to50_HT200to400_ext,
#   DYJetsToLL_M5to50_HT400to600,
#   DYJetsToLL_M5to50_HT400to600_ext,
#   DYJetsToLL_M5to50_HT600toInf,
]


DY = [
    DYJetsToLL_M50_LO,
#    DYJetsToLL_M50_LO_ext2,
    DYJetsToLL_M10to50_LO,
    DYJetsToLL_M50,
] + DYJetsM50HT + DYJetsM5to50HT

## ttbar
TTLep_pow       = Sample.nanoAODfromDAS("TTLep_pow",       "/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/llechner-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1_legacy_nano_v1-1a762c888624ed9dff74191bdeed5e1a/USER",           dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=831.76*((3*0.108)**2))
TTSemiLep_pow   = Sample.nanoAODfromDAS("TTSemiLep_pow",   "/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/llechner-crab_RunIIAutumn18MiniAOD-NZSFlatPU28to62_102X_upgrade2018_realistic_v15_ext5-v1_legacy_nano_v1-1a762c888624ed9dff74191bdeed5e1a/USER",           dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=831.76*(3*0.108)*(1-3*0.108)*2)
TTHad_pow       = Sample.nanoAODfromDAS("TTHad_pow",       "/TTToHadronic_TuneCP5_13TeV-powheg-pythia8/llechner-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1_legacy_nano_v1-1a762c888624ed9dff74191bdeed5e1a/USER",           dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=831.76*((1-3*0.108)**2))
#TTbar           = Sample.nanoAODfromDAS("TTbar",           "/TT_TuneCUETP8M2T4_13TeV-powheg-pythia8/RunIISummer16NanoAOD-PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/NANOAODSIM", dbFile=dbFile, instance="phys03", overwrite=ov, redirector=redirector, xSection=831.76)
TTLep_NLO       = Sample.nanoAODfromDAS("TTLep_NLO",       "/TT_DiLept_TuneCP5_13TeV-amcatnlo-pythia8/llechner-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2_legacy_nano_v1-1a762c888624ed9dff74191bdeed5e1a/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=831.76*((3*0.108)**2))

## single top
TToLeptons_sch_amcatnlo = Sample.nanoAODfromDAS("TToLeptons_sch_amcatnlo", "/ST_s-channel_4f_leptonDecays_TuneCP5_13TeV-madgraph-pythia8/llechner-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v4_legacy_nano_v2-1a762c888624ed9dff74191bdeed5e1a/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=(7.20+4.16)*0.108*3)

T_tch_pow           = Sample.nanoAODfromDAS("T_tch_pow",        "/ST_t-channel_top_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/llechner-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1_legacy_nano_v2-1a762c888624ed9dff74191bdeed5e1a/USER",       dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=136.02) # inclusive sample
TBar_tch_pow        = Sample.nanoAODfromDAS("TBar_tch_pow",     "/ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/llechner-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1_legacy_nano_v2-1a762c888624ed9dff74191bdeed5e1a/USER",   dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=80.95) # inclusive sample

T_tWch              = Sample.nanoAODfromDAS("T_tWch",           "/ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/llechner-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v3_legacy_nano_v2-1a762c888624ed9dff74191bdeed5e1a/USER",       dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=35.6)
TBar_tWch           = Sample.nanoAODfromDAS("TBar_tWch",        "/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/llechner-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v3_legacy_nano_v2-1a762c888624ed9dff74191bdeed5e1a/USER",   dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=35.6)

## ttH
#TTHbb               = Sample.nanoAODfromDAS("TTHbb",            "/ttHTobb_M125_13TeV_powheg_pythia8/dspitzba-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2_legacy_nano_v1-b9659cf3bef5e21efe24288a402778f7/USER",                                 dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=0.5085*(0.577))
#TTHnobb_pow         = Sample.nanoAODfromDAS("TTHnobb_pow",      "/ttHToNonbb_M125_TuneCUETP8M2_ttHtranche3_13TeV-powheg-pythia8/dspitzba-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2_legacy_nano_v1-b9659cf3bef5e21efe24288a402778f7/USER",     dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=0.5085*(1-0.577))

#THQ                 = Sample.nanoAODfromDAS("THQ",              "/THQ_Hincl_13TeV-madgraph-pythia8_TuneCUETP8M1/dspitzba-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2_legacy_nano_v1-b9659cf3bef5e21efe24288a402778f7/USER",                     dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=0.07096)
#THW                 = Sample.nanoAODfromDAS("THW",              "/THW_Hincl_13TeV-madgraph-pythia8_TuneCUETP8M1/dspitzba-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2_legacy_nano_v1-b9659cf3bef5e21efe24288a402778f7/USER",                     dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=0.1472)

## ttV
#TGJets              = Sample.nanoAODfromDAS("TGJets",     "/TGJets_TuneCUETP8M1_13TeV_amcatnlo_madspin_pythia8/RunIISummer16NanoAOD-PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/NANOAODSIM", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=2.967)
#TGJets_ext          = Sample.nanoAODfromDAS("TGJets_ext", "/TGJets_TuneCUETP8M1_13TeV_amcatnlo_madspin_pythia8/RunIISummer16NanoAOD-PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2_ext1-v1/NANOAODSIM", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=2.967)
tZq_ll              = Sample.nanoAODfromDAS("tZq_ll",           "/ttWJets_TuneCP5_13TeV_madgraphMLM_pythia8/llechner-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2_legacy_nano_v2-1a762c888624ed9dff74191bdeed5e1a/USER",                             dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=0.09418 ) #0.0758 )
tWll                = Sample.nanoAODfromDAS("tWll",             "/ST_tWll_5f_LO_TuneCP5_PSweights_13TeV-madgraph-pythia8/llechner-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v1_legacy_nano_v2-1a762c888624ed9dff74191bdeed5e1a/USER",                              dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=0.01123)
#tWnunu              = Sample.nanoAODfromDAS("tWnunu",           "/ST_tWnunu_5f_LO_13TeV-MadGraph-pythia8/dspitzba-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1_legacy_nano_v1-b9659cf3bef5e21efe24288a402778f7/USER",                            dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=0.01123*1.9822)
TTWToLNu            = Sample.nanoAODfromDAS("TTWToLNu",         "/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/llechner-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2_legacy_nano_v2-1a762c888624ed9dff74191bdeed5e1a/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=0.2043)
TTWToQQ             = Sample.nanoAODfromDAS("TTWToQQ",          "/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/llechner-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1_legacy_nano_v2-1a762c888624ed9dff74191bdeed5e1a/USER",       dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=0.40620)
TTW_LO              = Sample.nanoAODfromDAS("TTW_LO",           "/ttWJets_TuneCP5_13TeV_madgraphMLM_pythia8/llechner-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2_legacy_nano_v2-1a762c888624ed9dff74191bdeed5e1a/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=0.6105)
#TTZToQQ             = Sample.nanoAODfromDAS("TTZToQQ",          "/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/dspitzba-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2_legacy_nano_v1-b9659cf3bef5e21efe24288a402778f7/USER",                       dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=0.5297)
TTZToLLNuNu         = Sample.nanoAODfromDAS("TTZToLLNuNu",      "/TTZToLLNuNu_M-10_TuneCP5_13TeV-amcatnlo-pythia8/llechner-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2_legacy_nano_v2-1a762c888624ed9dff74191bdeed5e1a/USER",         dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=0.2728)
TTZToLLNuNu_m1to10  = Sample.nanoAODfromDAS("TTZToLLNuNu_m1to10", "/TTZToLL_M-1to10_TuneCP5_13TeV-amcatnlo-pythia8/llechner-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1_legacy_nano_v2-1a762c888624ed9dff74191bdeed5e1a/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=0.0493)
TTZ_LO              = Sample.nanoAODfromDAS("TTZ_LO",           "/ttZJets_TuneCP5_13TeV_madgraphMLM_pythia8/llechner-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2_legacy_nano_v2-1a762c888624ed9dff74191bdeed5e1a/USER",                                 dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=0.5297/0.692)
#TTGJets             = Sample.nanoAODfromDAS("TTGJets",          "/TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/dspitzba-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2_legacy_nano_v1-b9659cf3bef5e21efe24288a402778f7/USER",           dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=3.697)
#TTGJets_ext         = Sample.nanoAODfromDAS("TTGJets_ext",      "/TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/dspitzba-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2_legacy_nano_v1-b9659cf3bef5e21efe24288a402778f7/USER",      dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=3.697)
TTGHad              = Sample.nanoAODfromDAS("TTGHad",           "/TTGamma_Hadronic_TuneCP5_13TeV_madgraph_pythia8/llechner-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2_legacy_nano_v2-1a762c888624ed9dff74191bdeed5e1a/USER",            dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=0.794*3.062342569) # MadGraph LO xsec * k factor estimated in TOPAZ (TOP-18-010)
TTGSemiTbar         = Sample.nanoAODfromDAS("TTGSemiTbar",      "/TTGamma_SingleLeptFromTbar_TuneCP5_13TeV_madgraph_pythia8/llechner-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2_legacy_nano_v2-1a762c888624ed9dff74191bdeed5e1a/USER",  dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=0.769*2.028673602) # MadGraph LO xsec * k factor estimated in TOPAZ (TOP-18-010)
TTGSemiT            = Sample.nanoAODfromDAS("TTGSemiT",         "/TTGamma_SingleLeptFromT_TuneCP5_13TeV_madgraph_pythia8/llechner-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2_legacy_nano_v2-1a762c888624ed9dff74191bdeed5e1a/USER",     dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=0.769*2.028673602) # MadGraph LO xsec * k factor estimated in TOPAZ (TOP-18-010)
TTGLep              = Sample.nanoAODfromDAS("TTGLep",           "/TTGamma_Dilept_TuneCP5_13TeV_madgraph_pythia8/llechner-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2_legacy_nano_v2-1a762c888624ed9dff74191bdeed5e1a/USER",              dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=0.607*1.574299835) # MadGraph LO xsec * k factor estimated in TOPAZ (TOP-18-010)

TTV = [
#    TGJets,
#    TGJets_ext,
    TTGHad,
    TTGSemiT,
    TTGSemiTbar,
    TTGLep,
    tZq_ll,
    tWll,
#    tWnunu,
    TTWToLNu,
    TTWToQQ,
    TTW_LO,
#    TTZToQQ,
    TTZToLLNuNu,
    TTZToLLNuNu_m1to10,
    TTZ_LO,
#    TTGJets,
#    TTGJets_ext
]

top = [
    TTLep_pow,
    TTSemiLep_pow,
    TTHad_pow,
#    TTbar,
    TTLep_NLO,
    TToLeptons_sch_amcatnlo,
    T_tch_pow,
    TBar_tch_pow,
    T_tWch,
    TBar_tWch,
#    TTHbb,
#    TTHnobb_pow,
#    TTHnobb_mWCutfix_ext,
#    THQ,
#    THW,
    ] + TTV

## di/multiboson
WWTo2L2Nu           = Sample.nanoAODfromDAS("WWTo2L2Nu",        "/WWTo2L2Nu_DoubleScattering_13TeV-pythia8/llechner-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1_legacy_nano_v2-1a762c888624ed9dff74191bdeed5e1a/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=10.481 )
#WWToLNuQQ           = Sample.nanoAODfromDAS("WWToLNuQQ",        "/WWToLNuQQ_13TeV-powheg/RunIISummer16NanoAOD-PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/NANOAODSIM", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=43.53 )
#WWToLNuQQ_ext       = Sample.nanoAODfromDAS("WWToLNuQQ_ext",    "/WWToLNuQQ_13TeV-powheg/RunIISummer16NanoAOD-PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2_ext1-v1/NANOAODSIM", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=43.53 )
#WWTo1L1Nu2Q         = Sample.nanoAODfromDAS("WWTo1L1Nu2Q",          "/WWTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8/dspitzba-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2_legacy_nano_v1-b9659cf3bef5e21efe24288a402778f7/USER",        dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=49.997 )

ZZTo2L2Nu           = Sample.nanoAODfromDAS("ZZTo2L2Nu",            "/ZZTo2L2Nu_TuneCP5_13TeV_powheg_pythia8/llechner-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2_legacy_nano_v2-1a762c888624ed9dff74191bdeed5e1a/USER",                   dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=0.564)
ZZTo2L2Q            = Sample.nanoAODfromDAS("ZZTo2L2Q",             "/ZZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8/llechner-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1_legacy_nano_v2-1a762c888624ed9dff74191bdeed5e1a/USER",                   dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=3.28)
#ZZTo2Q2Nu           = Sample.nanoAODfromDAS("ZZTo2Q2Nu",            "/ZZTo2Q2Nu_13TeV_amcatnloFXFX_madspin_pythia8/dspitzba-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2_legacy_nano_v1-b9659cf3bef5e21efe24288a402778f7/USER",          dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=4.04)
ZZTo4L              = Sample.nanoAODfromDAS("ZZTo4L",               "/ZZTo4L_TuneCP5_13TeV_powheg_pythia8/llechner-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2_legacy_nano_v2-1a762c888624ed9dff74191bdeed5e1a/USER",                      dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=1.256*1.1)

#WZTo1L3Nu           = Sample.nanoAODfromDAS("WZTo1L3Nu"  ,          "/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/dspitzba-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2_legacy_nano_v1-b9659cf3bef5e21efe24288a402778f7/USER",          dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=(47.13)*(3*0.108)*(0.2) )
#WZTo1L1Nu2Q         = Sample.nanoAODfromDAS("WZTo1L1Nu2Q",          "/WZTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8/dspitzba-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2_legacy_nano_v1-b9659cf3bef5e21efe24288a402778f7/USER",        dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=10.71)
#WZTo2L2Q            = Sample.nanoAODfromDAS("WZTo2L2Q"   ,          "/WZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8/dspitzba-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2_legacy_nano_v1-b9659cf3bef5e21efe24288a402778f7/USER",           dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=5.60)
#WZTo3LNu_ext        = Sample.nanoAODfromDAS("WZTo3LNu_ext",         "/WZTo3LNu_TuneCUETP8M1_13TeV-powheg-pythia8/dspitzba-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1_legacy_nano_v1-b9659cf3bef5e21efe24288a402778f7/USER",       dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=4.42965)
WZTo3LNu_amcatnlo   = Sample.nanoAODfromDAS("WZTo3LNu_amcatnlo",    "/WZTo3LNu_TuneCP5_13TeV-amcatnloFXFX-pythia8/llechner-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2_legacy_nano_v2-1a762c888624ed9dff74191bdeed5e1a/USER",              dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=4.666)

VVTo2L2Nu           = Sample.nanoAODfromDAS("VVTo2L2Nu",            "/VVTo2L2Nu_13TeV_amcatnloFXFX_madspin_pythia8/llechner-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1_legacy_nano_v2-1a762c888624ed9dff74191bdeed5e1a/USER",                  dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=11.95)

#WGToLNuG                = Sample.nanoAODfromDAS("WGToLNuG", "/WGToLNuG_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAOD-PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/NANOAODSIM", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=585.8)
#WGToLNuG_amcatnlo_ext1  = Sample.nanoAODfromDAS("WGToLNuG_amcatnlo_ext1", "/WGToLNuG_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16NanoAOD-PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2_ext1-v1/NANOAODSIM", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=585.8) # cross section copied from MLM sample above, to be checked
#WGToLNuG_amcatnlo_ext3  = Sample.nanoAODfromDAS("WGToLNuG_amcatnlo_ext3", "/WGToLNuG_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16NanoAOD-PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2_ext3-v1/NANOAODSIM", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=585.8) # cross section copied from MLM sample above, to be checked
#WGJets              = Sample.nanoAODfromDAS("WGJets", "/WGJets_MonoPhoton_PtG-130_TuneCUETP8M1_13TeV-madgraph/RunIISummer16NanoAOD-PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/NANOAODSIM", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=0.6637)
#ZNuNuGJets              = Sample.nanoAODfromDAS("ZNuNuGJets", "/ZNuNuGJets_MonoPhoton_PtG-130_TuneCUETP8M1_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM",    dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=0.1903)
#ZNuNuGJets_40130    = Sample.nanoAODfromDAS("ZNuNuGJets_40130", "/ZNuNuGJets_MonoPhoton_PtG-40to130_TuneCUETP8M1_13TeV-madgraph/RunIISummer16NanoAOD-PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/NANOAODSIM", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=2.816)

#ZGTo2LG_ext         = Sample.nanoAODfromDAS("ZGTo2LG_ext",          "/ZGTo2LG_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/dspitzba-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1_legacy_nano_v1-b9659cf3bef5e21efe24288a402778f7/USER",  dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=131.3)
WWDoubleTo2L        = Sample.nanoAODfromDAS("WWDoubleTo2L",         "/WWTo2L2Nu_DoubleScattering_13TeV-pythia8/llechner-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1_legacy_nano_v2-1a762c888624ed9dff74191bdeed5e1a/USER",                      dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=0.1729)

WW                  = Sample.nanoAODfromDAS("WW",                   "/WW_TuneCP5_13TeV-pythia8/llechner-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2_legacy_nano_v1-1a762c888624ed9dff74191bdeed5e1a/USER",                         dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=63.21 * 1.82)
#WW_ext              = Sample.nanoAODfromDAS("WW_ext",               "/WW_TuneCUETP8M1_13TeV-pythia8/dspitzba-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2_legacy_nano_v1-b9659cf3bef5e21efe24288a402778f7/USER",                    dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=63.21 * 1.82)
WZ                  = Sample.nanoAODfromDAS("WZ",                   "/WZ_TuneCP5_13TeV-pythia8/llechner-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v3_legacy_nano_v2-1a762c888624ed9dff74191bdeed5e1a/USER",                         dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=47.13)
#WZ_ext              = Sample.nanoAODfromDAS("WZ_ext",               "/WZ_TuneCUETP8M1_13TeV-pythia8/dspitzba-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2_legacy_nano_v1-b9659cf3bef5e21efe24288a402778f7/USER",                    dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=47.13)
ZZ                  = Sample.nanoAODfromDAS("ZZ",                   "/ZZ_TuneCP5_13TeV-pythia8/llechner-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2_legacy_nano_v1-1a762c888624ed9dff74191bdeed5e1a/USER",                         dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=16.523)

#WWW_4F              = Sample.nanoAODfromDAS("WWW_4F",               "/WWW_4F_TuneCUETP8M1_13TeV-amcatnlo-pythia8/dspitzba-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2_legacy_nano_v1-b9659cf3bef5e21efe24288a402778f7/USER",            dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=0.2086)
WWZ                 = Sample.nanoAODfromDAS("WWZ",                  "/WWZ_TuneCP5_13TeV-amcatnlo-pythia8/llechner-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2_legacy_nano_v1-1a762c888624ed9dff74191bdeed5e1a/USER",               dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=0.1651)
WZZ                 = Sample.nanoAODfromDAS("WZZ",                  "/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/llechner-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2_legacy_nano_v1-1a762c888624ed9dff74191bdeed5e1a/USER",               dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=0.05565)
ZZZ                 = Sample.nanoAODfromDAS("ZZZ",                  "/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/llechner-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2_legacy_nano_v1-1a762c888624ed9dff74191bdeed5e1a/USER",               dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=0.01398)




boson = [
#    WWTo2L2Nu,
#    WWToLNuQQ,
#    WWToLNuQQ_ext,
#    WWTo1L1Nu2Q,
    ZZTo2L2Nu,
    ZZTo2L2Q,
#    ZZTo2Q2Nu,
    ZZTo4L,
#    WZTo1L1Nu2Q,
#    WZTo2L2Q,
#    WZTo3LNu_ext,
    WZTo3LNu_amcatnlo,
    VVTo2L2Nu,
#    WGToLNuG,
#    WGToLNuG_amcatnlo_ext1,
#    WGToLNuG_amcatnlo_ext3,
#    WGJets,
#    ZNuNuGJets_40130,
#    ZGTo2LG_ext,
    WWDoubleTo2L,
    WW,
#    WW_ext,
    WZ,
#    WZ_ext,
    ZZ,
#    WWW_4F,
    WWZ,
    WZZ,
    ZZZ,
    ]

# W+jets
#WJetsToLNu      = Sample.nanoAODfromDAS("WJetsToLNu",           "/WJetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/dspitzba-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2_legacy_nano_v3-b9659cf3bef5e21efe24288a402778f7/USER",         dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=3* 20508.9)
#WJetsToLNu_ext  = Sample.nanoAODfromDAS("WJetsToLNu_ext",       "/WJetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/dspitzba-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v2_legacy_nano_v3-b9659cf3bef5e21efe24288a402778f7/USER",    dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=3* 20508.9)

wjets = [
#    WJetsToLNu,
#    WJetsToLNu_ext,
    ]

## rare
#TTTT = Sample.nanoAODfromDAS("TTTT", "/TTTT_TuneCUETP8M2T4_13TeV-amcatnlo-pythia8/dspitzba-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1_legacy_nano_v1-b9659cf3bef5e21efe24288a402778f7/USER", dbFile=dbFile, redirector=redirector, instance="phys03", xSection=0.009103)
TTWW = Sample.nanoAODfromDAS("TTWW", "/TTWW_TuneCP5_13TeV-madgraph-pythia8/llechner-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2_legacy_nano_v2-1a762c888624ed9dff74191bdeed5e1a/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=0.007829)
TTWZ = Sample.nanoAODfromDAS("TTWZ", "/TTWZ_TuneCP5_13TeV-madgraph-pythia8/llechner-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2_legacy_nano_v1-1a762c888624ed9dff74191bdeed5e1a/USER",    dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=0.002919)
TTZZ = Sample.nanoAODfromDAS("TTZZ", "/TTZZ_TuneCP5_13TeV-madgraph-pythia8/llechner-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2_legacy_nano_v1-1a762c888624ed9dff74191bdeed5e1a/USER",    dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=0.001573)

rare = [
#    TTTT,
    TTWW,
    TTWZ,
    TTZZ,
    ]


signals = [
    ]

GluGluToContinToZZTo2e2mu   = Sample.nanoAODfromDAS("GluGluToContinToZZTo2e2mu",   "/GluGluToContinToZZTo2e2mu_13TeV_MCFM701_pythia8/llechner-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1_legacy_nano_v1-1a762c888624ed9dff74191bdeed5e1a/USER",    dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=0.005423)
GluGluToContinToZZTo2e2tau  = Sample.nanoAODfromDAS("GluGluToContinToZZTo2e2tau",  "/GluGluToContinToZZTo2e2tau_13TeV_MCFM701_pythia8/llechner-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1_legacy_nano_v1-1a762c888624ed9dff74191bdeed5e1a/USER",   dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=0.005423)
#GluGluToContinToZZTo2mu2tau = Sample.nanoAODfromDAS("GluGluToContinToZZTo2mu2tau", "/GluGluToContinToZZTo2mu2tau_13TeV_MCFM701_pythia8/dspitzba-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2_legacy_nano_v1-b9659cf3bef5e21efe24288a402778f7/USER",  dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=0.005423)
#GluGluToContinToZZTo4e      = Sample.nanoAODfromDAS("GluGluToContinToZZTo4e",      "/GluGluToContinToZZTo4e_13TeV_MCFM701_pythia8/dspitzba-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2_legacy_nano_v1-b9659cf3bef5e21efe24288a402778f7/USER",       dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=0.0027)
#GluGluToContinToZZTo4mu     = Sample.nanoAODfromDAS("GluGluToContinToZZTo4mu",     "/GluGluToContinToZZTo4mu_13TeV_MCFM701_pythia8/dspitzba-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2_legacy_nano_v1-b9659cf3bef5e21efe24288a402778f7/USER",      dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=0.0027)
#GluGluToContinToZZTo4tau    = Sample.nanoAODfromDAS("GluGluToContinToZZTo4tau",    "/GluGluToContinToZZTo4tau_13TeV_MCFM701_pythia8/dspitzba-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2_legacy_nano_v1-b9659cf3bef5e21efe24288a402778f7/USER",     dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=0.0027)

gluglu = [
    GluGluToContinToZZTo2e2mu,
    GluGluToContinToZZTo2e2tau,
#    GluGluToContinToZZTo2mu2tau,
#    GluGluToContinToZZTo4e,
#    GluGluToContinToZZTo4mu,
#    GluGluToContinToZZTo4tau,
]


other = [
    ]

allSamples = DY + top + boson + wjets + rare + other + signals + gluglu

for s in allSamples:
    s.isData = False

