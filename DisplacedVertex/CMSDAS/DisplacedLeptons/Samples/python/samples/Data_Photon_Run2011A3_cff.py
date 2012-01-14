sampleDataSet = '/Photon/Run2011A-05Aug2011-v1/AOD'
sampleNumEvents = 11949265 # according to DBS, 24 Nov 2011

# global tag needs to be chosen to match release, trigger menu and alignment conditions.
# see https://twiki.cern.ch/twiki/bin/view/CMS/SWGuideFrontierConditions
sampleGlobalTag = 'GR_R_42_V21A::All'
sampleHLTProcess = '*'

# data quality run/lumi section selection
sampleJSON = "https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions11/7TeV/Reprocessing/Cert_170249-172619_7TeV_ReReco5Aug_Collisions11_JSON_v3.txt"

# restrict run range (mainly to get a sample with consistent trigger configuration)
sampleRunRange = [160000,999999]

# use checkAllFilesOpened whenever possible, and noDuplicateCheck when necessary
sampleDuplicateCheckMode = "checkAllFilesOpened"

# "DATA" or "MC"
sampleType = "DATA"

sampleRelease = "CMSSW_4_2_7" # original (i.e. RECO file) release,
                                     # not the one we plan to process them with

sampleProcessRelease = "CMSSW_4_2_7" # release used to create new files with

sampleBaseDir = "root://xrootd.rcac.purdue.edu//store/user/demattia/longlived/"+sampleProcessRelease+"/Data_Photon_Run2011A3"

sampleRecoFiles = []

samplePatFiles = [
  sampleBaseDir+"/pat/PATtuple_1_1_tX0.root",
  sampleBaseDir+"/pat/PATtuple_2_1_eYU.root",
  sampleBaseDir+"/pat/PATtuple_3_1_2Bt.root",
  sampleBaseDir+"/pat/PATtuple_4_1_4l7.root",
  sampleBaseDir+"/pat/PATtuple_5_1_R4Z.root",
  sampleBaseDir+"/pat/PATtuple_6_1_r1Z.root",
  sampleBaseDir+"/pat/PATtuple_7_1_sR8.root",
  sampleBaseDir+"/pat/PATtuple_8_1_TCz.root",
  sampleBaseDir+"/pat/PATtuple_9_1_FrJ.root",
  sampleBaseDir+"/pat/PATtuple_10_1_g65.root",
  sampleBaseDir+"/pat/PATtuple_11_1_XZT.root",
  sampleBaseDir+"/pat/PATtuple_12_1_grW.root",
  sampleBaseDir+"/pat/PATtuple_13_1_F9c.root",
  sampleBaseDir+"/pat/PATtuple_14_1_NgT.root",
  sampleBaseDir+"/pat/PATtuple_15_1_8E1.root",
  sampleBaseDir+"/pat/PATtuple_16_1_x4J.root",
  sampleBaseDir+"/pat/PATtuple_17_1_XZz.root",
  sampleBaseDir+"/pat/PATtuple_18_1_iB4.root",
  sampleBaseDir+"/pat/PATtuple_19_1_YKu.root",
  sampleBaseDir+"/pat/PATtuple_20_1_CAr.root",
  sampleBaseDir+"/pat/PATtuple_21_1_clq.root",
  sampleBaseDir+"/pat/PATtuple_22_1_aMC.root",
  sampleBaseDir+"/pat/PATtuple_23_1_OGp.root",
  sampleBaseDir+"/pat/PATtuple_24_1_I2Y.root",
  sampleBaseDir+"/pat/PATtuple_25_1_Ftx.root",
  sampleBaseDir+"/pat/PATtuple_26_1_0cR.root",
  sampleBaseDir+"/pat/PATtuple_27_1_UpN.root",
  sampleBaseDir+"/pat/PATtuple_28_1_MtA.root",
  sampleBaseDir+"/pat/PATtuple_29_1_Onf.root",
  sampleBaseDir+"/pat/PATtuple_30_1_yjQ.root",
  sampleBaseDir+"/pat/PATtuple_31_1_FvJ.root",
  sampleBaseDir+"/pat/PATtuple_32_1_vcd.root",
  sampleBaseDir+"/pat/PATtuple_33_1_cPJ.root",
  sampleBaseDir+"/pat/PATtuple_34_1_4I2.root",
  sampleBaseDir+"/pat/PATtuple_35_1_GCB.root",
  sampleBaseDir+"/pat/PATtuple_36_1_d7X.root",
  sampleBaseDir+"/pat/PATtuple_37_1_iGm.root",
  sampleBaseDir+"/pat/PATtuple_38_1_zT6.root",
  sampleBaseDir+"/pat/PATtuple_39_1_pYu.root",
  sampleBaseDir+"/pat/PATtuple_40_1_qbw.root",
  sampleBaseDir+"/pat/PATtuple_41_1_QMN.root",
  sampleBaseDir+"/pat/PATtuple_42_1_vqO.root",
  sampleBaseDir+"/pat/PATtuple_43_1_KzR.root",
  sampleBaseDir+"/pat/PATtuple_44_1_BOT.root",
  sampleBaseDir+"/pat/PATtuple_45_1_TMd.root",
  sampleBaseDir+"/pat/PATtuple_46_1_JRT.root",
  sampleBaseDir+"/pat/PATtuple_47_1_tDs.root",
  sampleBaseDir+"/pat/PATtuple_48_1_bkL.root",
  sampleBaseDir+"/pat/PATtuple_49_1_VrI.root",
  sampleBaseDir+"/pat/PATtuple_50_1_qzC.root",
  sampleBaseDir+"/pat/PATtuple_51_1_Qwk.root",
  sampleBaseDir+"/pat/PATtuple_52_1_o1Q.root",
  sampleBaseDir+"/pat/PATtuple_53_1_eHS.root",
  sampleBaseDir+"/pat/PATtuple_54_1_QJW.root",
  sampleBaseDir+"/pat/PATtuple_55_1_Je0.root",
  sampleBaseDir+"/pat/PATtuple_56_1_Xt6.root",
  sampleBaseDir+"/pat/PATtuple_57_1_rcK.root",
  sampleBaseDir+"/pat/PATtuple_58_1_Yef.root",
  sampleBaseDir+"/pat/PATtuple_59_1_ela.root",
  sampleBaseDir+"/pat/PATtuple_60_1_Z1A.root",
  sampleBaseDir+"/pat/PATtuple_61_1_0tW.root",
  sampleBaseDir+"/pat/PATtuple_62_1_NB0.root",
  sampleBaseDir+"/pat/PATtuple_63_1_xD4.root",
  sampleBaseDir+"/pat/PATtuple_64_1_Qr3.root",
  sampleBaseDir+"/pat/PATtuple_65_1_35t.root",
  sampleBaseDir+"/pat/PATtuple_66_1_nHC.root",
  sampleBaseDir+"/pat/PATtuple_67_1_cK9.root",
  sampleBaseDir+"/pat/PATtuple_68_1_FlN.root",
  sampleBaseDir+"/pat/PATtuple_69_1_dZ8.root",
  sampleBaseDir+"/pat/PATtuple_70_1_sp1.root",
  sampleBaseDir+"/pat/PATtuple_71_1_Ks1.root",
  sampleBaseDir+"/pat/PATtuple_72_1_l0R.root",
  sampleBaseDir+"/pat/PATtuple_73_1_RHw.root",
  sampleBaseDir+"/pat/PATtuple_74_1_LmS.root",
  sampleBaseDir+"/pat/PATtuple_75_1_sF2.root",
  sampleBaseDir+"/pat/PATtuple_76_1_EYm.root",
  sampleBaseDir+"/pat/PATtuple_77_1_uZZ.root",
  sampleBaseDir+"/pat/PATtuple_78_1_unz.root",
  sampleBaseDir+"/pat/PATtuple_79_1_KPX.root",
  sampleBaseDir+"/pat/PATtuple_80_1_Ouw.root",
  sampleBaseDir+"/pat/PATtuple_81_1_S2H.root",
  sampleBaseDir+"/pat/PATtuple_82_1_pfV.root",
  sampleBaseDir+"/pat/PATtuple_83_1_rdw.root",
  sampleBaseDir+"/pat/PATtuple_84_1_B0H.root",
  sampleBaseDir+"/pat/PATtuple_85_1_ZUE.root",
  sampleBaseDir+"/pat/PATtuple_86_1_J3P.root",
  sampleBaseDir+"/pat/PATtuple_87_1_Psf.root",
  sampleBaseDir+"/pat/PATtuple_88_1_Jwv.root",
  sampleBaseDir+"/pat/PATtuple_89_1_HRz.root",
  sampleBaseDir+"/pat/PATtuple_90_1_7MD.root",
  sampleBaseDir+"/pat/PATtuple_91_1_oc9.root",
  sampleBaseDir+"/pat/PATtuple_92_1_Z7R.root",
  sampleBaseDir+"/pat/PATtuple_93_1_6zS.root",
  sampleBaseDir+"/pat/PATtuple_94_1_ZXs.root",
  sampleBaseDir+"/pat/PATtuple_95_1_Zzi.root",
  sampleBaseDir+"/pat/PATtuple_96_1_8aA.root",
  sampleBaseDir+"/pat/PATtuple_97_1_trY.root",
  sampleBaseDir+"/pat/PATtuple_98_1_hm7.root",
  sampleBaseDir+"/pat/PATtuple_99_1_v33.root",
  sampleBaseDir+"/pat/PATtuple_100_1_r6Q.root",
  sampleBaseDir+"/pat/PATtuple_101_1_9QQ.root",
  sampleBaseDir+"/pat/PATtuple_102_1_b1K.root",
  sampleBaseDir+"/pat/PATtuple_103_1_58w.root",
  sampleBaseDir+"/pat/PATtuple_104_1_KJm.root",
  sampleBaseDir+"/pat/PATtuple_105_1_EFs.root",
  sampleBaseDir+"/pat/PATtuple_106_1_0s3.root",
  sampleBaseDir+"/pat/PATtuple_107_1_zVi.root",
  sampleBaseDir+"/pat/PATtuple_108_1_1i0.root",
  sampleBaseDir+"/pat/PATtuple_109_1_wrg.root",
  sampleBaseDir+"/pat/PATtuple_110_1_tWt.root",
  sampleBaseDir+"/pat/PATtuple_111_1_Irw.root",
  sampleBaseDir+"/pat/PATtuple_112_1_CQS.root",
  sampleBaseDir+"/pat/PATtuple_113_1_oEG.root",
  sampleBaseDir+"/pat/PATtuple_114_2_LD4.root",
  sampleBaseDir+"/pat/PATtuple_115_2_bTC.root",
  sampleBaseDir+"/pat/PATtuple_116_1_0Io.root",
  sampleBaseDir+"/pat/PATtuple_117_2_Gog.root",
  sampleBaseDir+"/pat/PATtuple_118_1_08L.root",
  sampleBaseDir+"/pat/PATtuple_119_2_w5k.root",
  sampleBaseDir+"/pat/PATtuple_120_1_4fO.root",
  sampleBaseDir+"/pat/PATtuple_121_2_Sxi.root",
  sampleBaseDir+"/pat/PATtuple_122_1_mNb.root",
  sampleBaseDir+"/pat/PATtuple_123_1_3X6.root",
  sampleBaseDir+"/pat/PATtuple_124_2_NjL.root",
  sampleBaseDir+"/pat/PATtuple_125_2_zyn.root",
  sampleBaseDir+"/pat/PATtuple_126_2_hRl.root",
  sampleBaseDir+"/pat/PATtuple_127_2_Z7U.root",
  sampleBaseDir+"/pat/PATtuple_128_1_UeB.root",
  sampleBaseDir+"/pat/PATtuple_129_1_iyh.root",
  sampleBaseDir+"/pat/PATtuple_130_1_9yM.root",
  sampleBaseDir+"/pat/PATtuple_131_1_mw2.root",
  sampleBaseDir+"/pat/PATtuple_132_1_h3U.root",
  sampleBaseDir+"/pat/PATtuple_133_1_y2g.root",
  sampleBaseDir+"/pat/PATtuple_134_1_zwh.root",
  sampleBaseDir+"/pat/PATtuple_135_1_UmQ.root",
  sampleBaseDir+"/pat/PATtuple_136_1_tdG.root",
  sampleBaseDir+"/pat/PATtuple_137_1_CEG.root",
  sampleBaseDir+"/pat/PATtuple_138_1_6Gx.root",
  sampleBaseDir+"/pat/PATtuple_139_1_9Fw.root",
  sampleBaseDir+"/pat/PATtuple_140_1_nG6.root",
  sampleBaseDir+"/pat/PATtuple_141_1_wQR.root",
  sampleBaseDir+"/pat/PATtuple_142_1_WOC.root",
  sampleBaseDir+"/pat/PATtuple_143_1_3hv.root",
  sampleBaseDir+"/pat/PATtuple_144_1_NCd.root",
  sampleBaseDir+"/pat/PATtuple_145_1_7k5.root",
  sampleBaseDir+"/pat/PATtuple_146_1_Im4.root",
  sampleBaseDir+"/pat/PATtuple_147_1_Er9.root",
  sampleBaseDir+"/pat/PATtuple_148_1_7Qy.root",
  sampleBaseDir+"/pat/PATtuple_149_1_gwj.root",
  sampleBaseDir+"/pat/PATtuple_150_1_4rS.root",
  sampleBaseDir+"/pat/PATtuple_151_1_GPH.root",
  sampleBaseDir+"/pat/PATtuple_152_1_0Ur.root",
  sampleBaseDir+"/pat/PATtuple_153_1_KBF.root",
  sampleBaseDir+"/pat/PATtuple_154_1_4x0.root",
  sampleBaseDir+"/pat/PATtuple_155_1_Adm.root",
  sampleBaseDir+"/pat/PATtuple_156_1_u2b.root",
  sampleBaseDir+"/pat/PATtuple_157_1_SyP.root",
  sampleBaseDir+"/pat/PATtuple_158_1_l3Z.root",
  sampleBaseDir+"/pat/PATtuple_159_1_htO.root",
  sampleBaseDir+"/pat/PATtuple_160_1_Bjj.root",
  sampleBaseDir+"/pat/PATtuple_161_1_w2I.root",
  sampleBaseDir+"/pat/PATtuple_162_1_4E1.root",
  sampleBaseDir+"/pat/PATtuple_163_1_UEZ.root",
  sampleBaseDir+"/pat/PATtuple_164_1_vdA.root",
  sampleBaseDir+"/pat/PATtuple_165_1_pV7.root",
  sampleBaseDir+"/pat/PATtuple_166_1_5vb.root",
  sampleBaseDir+"/pat/PATtuple_167_1_FiK.root",
  sampleBaseDir+"/pat/PATtuple_168_1_iq0.root",
  sampleBaseDir+"/pat/PATtuple_169_1_eTN.root",
  sampleBaseDir+"/pat/PATtuple_170_1_AJw.root",
  sampleBaseDir+"/pat/PATtuple_171_1_GJl.root",
  sampleBaseDir+"/pat/PATtuple_172_1_4q2.root",
  sampleBaseDir+"/pat/PATtuple_173_1_ghx.root",
  sampleBaseDir+"/pat/PATtuple_174_1_L34.root",
  sampleBaseDir+"/pat/PATtuple_175_1_8Dz.root",
  sampleBaseDir+"/pat/PATtuple_176_1_ttB.root",
  sampleBaseDir+"/pat/PATtuple_177_1_Ouw.root"
]
