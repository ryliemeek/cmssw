# /dev/CMSSW_3_1_0/pre6/HLT/V9 (CMSSW_3_1_0_pre6_HLT3)

import FWCore.ParameterSet.Config as cms


HLTConfigVersion = cms.PSet(
  tableName = cms.string('/dev/CMSSW_3_1_0/pre6/HLT/V9')
)

block_hltDebugOutput = cms.PSet(
outputCommands = cms.untracked.vstring( 'drop *_hlt*_*_*',
  'keep edmTriggerResults_*_*_*',
  'keep triggerTriggerEvent_*_*_*',
  'keep triggerTriggerEventWithRefs_*_*_*',
  'keep *_hltTowerMakerForAll_*_*',
  'keep *_hltCtfL1IsoWithMaterialTracks_*_*',
  'keep *_hltMuonTauIsoL3IsoFiltered_*_*',
  'keep *_hltElectronL1NonIsoLargeWindowDetaDphi_*_*',
  'keep *_hltBLifetimeL3BJetTagsRelaxed_*_*',
  'keep *_hltBLifetimeHighestEtJets_*_*',
  'keep *_hltL1NonIsoLargeWindowElectronPixelSeeds_*_*',
  'keep *_hltL1NonIsolatedPhotonEcalIsol_*_*',
  'keep *_hltRpcRecHits_*_*',
  'keep *_hltL1HLTDoubleLooseIsoTau15JetsMatch_*_*',
  'keep *_hltBSoftmuonL3BJetTagsByDR_*_*',
  'keep *_hltCorrectedMulti5x5EndcapSuperClustersWithPreshowerL1Isolated_*_*',
  'keep *_hltBLifetimeL3Associator_*_*',
  'keep *_hltPixelVertices_*_*',
  'keep *_hltBLifetimeL3AssociatorRelaxed_*_*',
  'keep *_hltBLifetimeL25BJetTags_*_*',
  'keep *_hltCtfL1NonIsoWithMaterialTracks_*_*',
  'keep *_hltHITIPTCorrector8E29_*_*',
  'keep *_hltL1HLTSingleIsoTau30JetsMatch_*_*',
  'keep *_hltMuTracks_*_*',
  'keep *_hltL25TauPixelTracksConeIsolation_*_*',
  'keep *_hltMuonTauL1Filtered_*_*',
  'keep *_hltL3MuonCandidates_*_*',
  'keep *_hltL25TauPixelTracksConeIsolationNoL2_*_*',
  'keep *_hltL2TauIsolationProducer_*_*',
  'keep *_hltMumukPixelSeedFromL2Candidate_*_*',
  'keep *_hltBLifetimeL3TagInfos_*_*',
  'keep *_hltL1NonIsolatedElectronHcalIsol_*_*',
  'keep *_hltL3TrackCandidateFromL2_*_*',
  'keep *_hltSiStripRawToClustersFacility_*_*',
  'keep *_hltIsolPixelTrackProd8E29_*_*',
  'keep *_hltPixelMatchLargeWindowElectronsL1Iso_*_*',
  'keep *_hltL25TauPixelTracksLeadingTrackPtCutSelector_*_*',
  'keep *_hltL2TauRelaxingIsolationSelector_*_*',
  'keep *_hltMuonTauIsoL3PreFiltered_*_*',
  'keep *_hltMet_*_*',
  'keep *_hltL25TauCtfWithMaterialTracks_*_*',
  'keep *_hltBLifetimeRegionalCtfWithMaterialTracks_*_*',
  'keep *_hltL1NonIsoElectronTrackIsol_*_*',
  'keep *_hltBLifetimeL25Associator_*_*',
  'keep *_hltBLifetimeL25Jets_*_*',
  'keep *_hltCorrectedHybridSuperClustersL1NonIsolated_*_*',
  'keep *_hltCorrectedMulti5x5EndcapSuperClustersWithPreshowerL1NonIsolated_*_*',
  'keep *_hltBSoftmuonL25BJetTags_*_*',
  'keep *_hltBSoftmuonL25Jets_*_*',
  'keep *_hltCsc2DRecHits_*_*',
  'keep *_hltL1NonIsoElectronsRegionalCTFFinalFitWithMaterial_*_*',
  'keep *_hltMuonTauIsoL3IsoFilteredNoL1Tau_*_*',
  'keep *_hltBLifetimeL25JetsRelaxed_*_*',
  'keep *_hltL2MuonSeeds_*_*',
  'keep *_hltHtMet_*_*',
  'keep *_hltMuonTauIsoL2IsoFilteredNoL1Tau_*_*',
  'keep *_hltMulti5x5SuperClustersL1Isolated_*_*',
  'keep *_hltL2TauNarrowConeIsolationProducer_*_*',
  'keep *_hltL3MuonIsolations_*_*',
  'keep *_hltL25TauJetTracksAssociator_*_*',
  'keep *_hltCtfL1IsoLargeWindowWithMaterialTracks_*_*',
  'keep *_hltGctDigis_*_*',
  'keep *_hltL1IsolatedElectronHcalIsol_*_*',
  'keep *_hltL25TauPixelTracksIsolationSelectorNoL2_*_*',
  'keep *_hltBLifetimeL25AssociatorRelaxed_*_*',
  'keep *_hltHITIPTCorrector1E31_*_*',
  'keep *_hltOfflineBeamSpot_*_*',
  'keep *_hltL1NonIsoStartUpElectronPixelSeeds_*_*',
  'keep *_hltL1IsoStartUpElectronPixelSeeds_*_*',
  'keep *_hltHITCtfWithMaterialTracks8E29_*_*',
  'keep *_hltHybridSuperClustersL1NonIsolated_*_*',
  'keep *_hltMulti5x5SuperClustersL1NonIsolated_*_*',
  'keep *_hltL3TauIsolationSelector_*_*',
  'keep *_hltMumuPixelSeedFromL2Candidate_*_*',
  'keep *_hltDt4DSegments_*_*',
  'keep *_hltBSoftmuonL3TagInfos_*_*',
  'keep *_hltL25TauLeadingTrackPtCutSelector_*_*',
  'keep *_hltIsolPixelTrackProd1E31_*_*',
  'keep *_hltL25TauPixelTracksLeadingTrackPtCutSelectorNoL2_*_*',
  'keep *_hltCkfTrackCandidatesMumuk_*_*',
  'keep *_hltPixelMatchLargeWindowElectronsL1NonIso_*_*',
  'keep *_hltMCJetCorJetIcone5Regional_*_*',
  'keep *_hltL1IsoElectronsRegionalCTFFinalFitWithMaterial_*_*',
  'keep *_hltL1HLTDoubleLooseIsoTau15Trk5JetsMatch_*_*',
  'keep *_hltIterativeCone5CaloJets_*_*',
  'keep *_hltL3TauCtfWithMaterialTracks_*_*',
  'keep *_hltSiPixelRecHits_*_*',
  'keep *_hltBLifetimeL3Jets_*_*',
  'keep *_hltCtfWithMaterialTracksMumuk_*_*',
  'keep *_hltL3TauConeIsolation_*_*',
  'keep *_hltBLifetimeL3JetsRelaxed_*_*',
  'keep *_hltL25TauJetPixelTracksAssociator_*_*',
  'keep *_hltDt1DRecHits_*_*',
  'keep *_hltHybridSuperClustersL1Isolated_*_*',
  'keep *_hltL25TauJetPixelTracksAssociatorNoL2_*_*',
  'keep *_hltPixelMatchElectronsL1Iso_*_*',
  'keep *_hltTowerMakerForMuons_*_*',
  'keep *_hltIterativeCone5CaloJetsRegional_*_*',
  'keep *_hltCorrectedHybridSuperClustersL1Isolated_*_*',
  'keep *_hltBLifetimeL3TagInfosRelaxed_*_*',
  'keep *_hltGtDigis_*_*',
  'keep *_hltMuonTauIsoL2PreFiltered_*_*',
  'keep *_hltL1NonIsoHLTClusterShape_*_*',
  'keep *_hltMuonTauIsoL2PreFilteredNoL1Tau_*_*',
  'keep *_hltL2TauIsolationSelectorNoCut_*_*',
  'keep *_hltSiPixelClusters_*_*',
  'keep *_hltElectronL1IsoLargeWindowDetaDphi_*_*',
  'keep *_hltL3Muons_*_*',
  'keep *_hltL1NonIsolatedPhotonHcalIsol_*_*',
  'keep *_hltL1IsoRecoEcalCandidate_*_*',
  'keep *_hltL1extraParticles_*_*',
  'keep *_hltL3TrajectorySeed_*_*',
  'keep *_hltBLifetimeL25TagInfosRelaxed_*_*',
  'keep *_hltL1IsoLargeWindowElectronPixelSeeds_*_*',
  'keep *_hltL1NonIsoPhotonHollowTrackIsol_*_*',
  'keep *_hltL1IsolatedPhotonEcalIsol_*_*',
  'keep *_hltCscSegments_*_*',
  'keep *_hltMulti5x5EndcapSuperClustersWithPreshowerL1NonIsolated_*_*',
  'keep *_hltL1IsoEgammaRegionalCTFFinalFitWithMaterial_*_*',
  'keep *_hltBSoftmuonL3BJetTags_*_*',
  'keep *_hltL1GtObjectMap_*_*',
  'keep *_hltL3TauJetTracksAssociator_*_*',
  'keep *_hltMuonTauIsoL2IsoFiltered_*_*',
  'keep *_hltL3TkTracksFromL2_*_*',
  'keep *_hltL1IsoElectronTrackIsol_*_*',
  'keep *_hltL1HLTSingleLooseIsoTau20JetsMatch_*_*',
  'keep *_hltL2Muons_*_*',
  'keep *_hltL1IsoHLTClusterShape_*_*',
  'keep *_hltMCJetCorJetIcone5_*_*',
  'keep *_hltBLifetimeL3BJetTags_*_*',
  'keep *_hltPixelTracks_*_*',
  'keep *_hltBLifetimeL25BJetTagsRelaxed_*_*',
  'keep *_hltL25TauPixelTracksIsolationSelector_*_*',
  'keep *_hltL2MuonIsolations_*_*',
  'keep *_hltL25TauConeIsolation_*_*',
  'keep *_hltBLifetimeL25TagInfos_*_*',
  'keep *_hltPixelMatchElectronsL1NonIso_*_*',
  'keep *_hltBSoftmuonHighestEtJets_*_*',
  'keep *_hltMuonTauIsoL3PreFilteredNoL1Tau_*_*',
  'keep *_hltL1NonIsoEgammaRegionalCTFFinalFitWithMaterial_*_*',
  'keep *_hltL2MuonCandidates_*_*',
  'keep *_hltL1IsoPhotonHollowTrackIsol_*_*',
  'keep *_hltBSoftmuonL25TagInfos_*_*',
  'keep *_hltL1IsolatedPhotonHcalIsol_*_*',
  'keep *_hltL1NonIsoRecoEcalCandidate_*_*',
  'keep *_hltCtfWithMaterialTracksMumu_*_*',
  'keep *_hltMulti5x5EndcapSuperClustersWithPreshowerL1Isolated_*_*',
  'keep *_hltHITCtfWithMaterialTracks1E31_*_*',
  'keep *_hltCtfL1NonIsoLargeWindowWithMaterialTracks_*_*',
  'keep *_hltCkfTrackCandidatesMumu_*_*',
  'keep *_hltMuonTauL1FilteredNoL1Tau_*_*',
  'keep *_hltL2TauJets_*_*',
  'keep *_hltBLifetimeRegionalCtfWithMaterialTracksRelaxed_*_*',
  'keep *_hltMumukAllConeTracks_*_*' )
)
