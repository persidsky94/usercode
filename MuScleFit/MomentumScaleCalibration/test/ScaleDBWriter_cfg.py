import FWCore.ParameterSet.Config as cms

process = cms.Process("SCALEDBWRITER")

process.source = cms.Source("EmptySource",
    numberEventsInRun = cms.untracked.uint32(1),
    firstRun = cms.untracked.uint32(1)
)

process.load("Configuration.StandardSequences.MagneticField_cff")

process.load("Geometry.CMSCommonData.cmsIdealGeometryXML_cfi")

process.load("Geometry.CommonDetUnit.globalTrackingGeometry_cfi")

process.load("RecoMuon.DetLayers.muonDetLayerGeometry_cfi")

process.load("Geometry.MuonNumbering.muonNumberingInitialization_cfi")

process.load("RecoMuon.TrackingTools.MuonServiceProxy_cff")

# process.source = cms.Source("PoolSource",
#     fileNames = cms.untracked.vstring()
# )

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(1)
)

process.PoolDBOutputService = cms.Service(
    "PoolDBOutputService",
    BlobStreamerName = cms.untracked.string('TBufferBlobStreamingService'),
    DBParameters = cms.PSet(
        messageLevel = cms.untracked.int32(2),
        authenticationPath = cms.untracked.string('/afs/cern.ch/cms/DB/conddb')
    ),
    timetype = cms.untracked.string('runnumber'),
    connect = cms.string('sqlite_file:dummyScale.db'),
    toPut = cms.VPSet(cms.PSet(
        record = cms.string('MuScleFitScaleRcd'),
        tag = cms.string('MuScleFitScale_2_1_12')
    ))
)

process.ScaleDBWriterModule = cms.EDAnalyzer(
    "ScaleDBWriter",

    # Specify the corrections to use
    CorrectionsIdentifier = cms.untracked.string('MCcorrDerivedFromY_globalMuons_test')
)

process.p1 = cms.Path(process.ScaleDBWriterModule)

