from WMCore.Configuration import Configuration
config = Configuration()
config.section_("General")
config.General.requestName   = 'singleEl-16E-N1'
config.General.transferLogs = True

config.section_("JobType")
config.JobType.pluginName  = 'Analysis'
config.JobType.inputFiles = ['Spring16_23Sep2016EFV2_DATA_L1FastJet_AK4PFchs.txt','Spring16_23Sep2016EFV2_DATA_L2Relative_AK4PFchs.txt','Spring16_23Sep2016EFV2_DATA_L3Absolute_AK4PFchs.txt','Spring16_23Sep2016EFV2_DATA_L2L3Residual_AK4PFchs.txt','Spring16_23Sep2016EFV2_DATA_L1FastJet_AK8PFchs.txt','Spring16_23Sep2016EFV2_DATA_L2Relative_AK8PFchs.txt','Spring16_23Sep2016EFV2_DATA_L3Absolute_AK8PFchs.txt','Spring16_23Sep2016EFV2_DATA_L2L3Residual_AK8PFchs.txt','Spring16_23Sep2016EFV2_DATA_L1FastJet_AK8PFPuppi.txt','Spring16_23Sep2016EFV2_DATA_L2Relative_AK8PFPuppi.txt','Spring16_23Sep2016EFV2_DATA_L3Absolute_AK8PFPuppi.txt','Spring16_23Sep2016EFV2_DATA_L2L3Residual_AK8PFPuppi.txt']

# Name of the CMSSW configuration file
#config.JobType.psetName    = 'bkg_ana.py'
config.JobType.psetName    = 'analysis_EF.py'
#config.JobType.allowUndistributedCMSSW = True
config.JobType.allowUndistributedCMSSW = True

config.section_("Data")
config.Data.inputDataset = '/SingleElectron/Run2016E-23Sep2016-v1/MINIAOD'
#config.Data.inputDataset = '/SingleElectron/Run2016E-PromptReco-v2/MINIAOD'#Run2015D-PromptReco-v3/MINIAOD'
#config.Data.inputDataset = '/SingleMuon/Run2015B-PromptReco-v1/MINIAOD'
#config.Data.inputDataset = '/SingleMu/Run2012B-13Jul2012-v1/AOD'
config.Data.inputDBS = 'global'
config.Data.splitting = 'LumiBased'
config.Data.unitsPerJob = 100
config.Data.lumiMask = 'Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt'#'Cert_246908-254879_13TeV_PromptReco_Collisions15_JSON.txt' #'Cert_246908-251883_13TeV_PromptReco_Collisions15_JSON.txt'#Cert_246908-251252_13TeV_PromptReco_Collisions15_JSON.txt'#'lumiSummary_13_07_2015_JSON.txt'#https://twiki.cern.ch/twiki/pub/CMS/ExoDijet13TeV/lumiSummary_13_07_2015_JetHT.json'#https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions12/8TeV/Prompt/Cert_190456-208686_8TeV_PromptReco_Collisions12_JSON.txt'
config.Data.runRange = ''#'250843-250932' # '193093-194075'
#config.Data.runRange = '251244-251252'#'250843-250932' # '193093-194075'
#config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())
config.Data.publication = False
config.Data.outputDatasetTag = 'singleEl-16E-N1'

config.section_("Site")
config.Site.storageSite = 'T2_CH_CERN'
#config.Site.storageSite = 'T3_US_FNALLPC'


##config.Data.inputDataset = '/WJetsToLNu_13TeV-madgraph-pythia8-tauola/Phys14DR-PU20bx25_PHYS14_25_V1-v1/MINIAODSIM'
#config.Data.inputDataset = '/WJetsToLNu_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1/MINIAODSIM'
#config.Data.inputDBS = 'global'
##config.Data.inputDBS = 'phys03'
#config.Data.splitting = 'FileBased'
#config.Data.unitsPerJob =10 
#config.Data.totalUnits = 279
#config.Data.publication = False
#
## This string is used to construct the output dataset name
#config.Data.outputDatasetTag = 'WJets100To200_weight'
#
#config.section_("Site")
## Where the output files will be transmitted to
