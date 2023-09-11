# Awesome BIDS [![Awesome](https://awesome.re/badge.svg)](https://github.com/sindresorhus/awesome#readme)

<img src="https://raw.githubusercontent.com/bids-standard/bids-specification/master/BIDS_logo/BIDS_logo_white_transparent_background_crop.png#gh-dark-mode-only" alt="bids-logo" width="600"/>
<img src="https://raw.githubusercontent.com/bids-standard/bids-specification/master/BIDS_logo//BIDS_logo_black_transparent_background_crop.png#gh-light-mode-only" alt="bids-logo" width="600"/>

A curated list of awesome BIDS projects, proposals, apps and resources

Make sure to also check repositories tagged for the following topics:

- [BIDS](https://github.com/topics/bids)
- [BIDS-Apps](https://github.com/topics/bidsapp)


## Contents

- [Apps](#apps)
- [Converters](#converters)
- [Documentation](#documentation)
- [Extension proposals](#extension-proposals)
- [Libraries](#libraries)


## Apps

BIDS apps are containerized tools to automatically process BIDS datasets.

BIDS Apps are also listed on [BIDS Apps](https://bids-apps.neuroimaging.io/apps/).

<!-- APP starts -->
- [![Docker version](https://img.shields.io/docker/pulls/bids/aa.svg?style=plastic)](https://hub.docker.com/r/bids/aa) [aa](https://github.com/bids-apps/aa): BIDS App containing an instance of the Automatic Analysis
- [![Docker version](https://img.shields.io/docker/pulls/bids/afni_proc.svg?style=plastic)](https://hub.docker.com/r/bids/afni_proc) [afni_proc](https://github.com/bids-apps/afni_proc): prototype AFNI bids app implementing participant level preprocessing with afni_proc.py
- [![Docker version](https://img.shields.io/docker/pulls/bids/antscorticalthickness.svg?style=plastic)](https://hub.docker.com/r/bids/antscorticalthickness) [antsCorticalThickness](https://github.com/bids-apps/antsCorticalThickness): BIDS App for calculating cortical thickness using ANTs
- [![Docker version](https://img.shields.io/docker/pulls/bids/baracus.svg?style=plastic)](https://hub.docker.com/r/bids/baracus) [baracus](https://github.com/bids-apps/baracus): Predicts brain age, based on data from Freesurfer 5.3
- [![Docker version](https://img.shields.io/docker/pulls/bids/brainiak-srm.svg?style=plastic)](https://hub.docker.com/r/bids/brainiak-srm) [brainiak-srm](https://github.com/bids-apps/brainiak-srm): This is the BIDS-app version of the Shared Response Model (SRM) of BrainIAK
- [![Docker version](https://img.shields.io/docker/pulls/bids/brainsuite.svg?style=plastic)](https://hub.docker.com/r/bids/brainsuite) [BrainSuite](https://github.com/bids-apps/BrainSuite): BrainSuite's structural, diffusion, and functional MRI processing pipelines with QC functionalities.
- [![Docker version](https://img.shields.io/docker/pulls/bids/broccoli.svg?style=plastic)](https://hub.docker.com/r/bids/broccoli) [BROCCOLI](https://github.com/bids-apps/BROCCOLI): BIDS App for BROCCOLI
- [![Docker version](https://img.shields.io/docker/pulls/bids/cpac.svg?style=plastic)](https://hub.docker.com/r/bids/cpac) [CPAC](https://github.com/bids-apps/CPAC): BIDS Application for the Configurable Pipeline for the Analysis of Connectomes (C-PAC)
- [![Docker version](https://img.shields.io/docker/pulls/bids/dparsf.svg?style=plastic)](https://hub.docker.com/r/bids/dparsf) [DPARSF](https://github.com/bids-apps/DPARSF): Docker version of DPARSF, also deployed at OpenNeuro.org
- [![Docker version](https://img.shields.io/docker/pulls/bids/freesurfer.svg?style=plastic)](https://hub.docker.com/r/bids/freesurfer) [freesurfer](https://github.com/bids-apps/freesurfer): BIDS app wrapping recon-all from FreeSurfer
- [![Docker version](https://img.shields.io/docker/pulls/bids/hcppipelines.svg?style=plastic)](https://hub.docker.com/r/bids/hcppipelines) [HCPPipelines](https://github.com/bids-apps/HCPPipelines): A BIDS App for minimal preprocessing using the HCP Pipelines
- [![Docker version](https://img.shields.io/docker/pulls/bids/hyperalignment.svg?style=plastic)](https://hub.docker.com/r/bids/hyperalignment) [hyperalignment](https://github.com/bids-apps/hyperalignment): Hyperalignment is a functional alignment method that aligns subjects' brain data in a high-dimensional space of voxels/features.
- [![Docker version](https://img.shields.io/docker/pulls/bids/mindboggle.svg?style=plastic)](https://hub.docker.com/r/bids/mindboggle) [mindboggle](https://github.com/bids-apps/mindboggle): Improve the accuracy, precision, and consistency of automated labeling and shape analysis of human brain image data
- [![Docker version](https://img.shields.io/docker/pulls/bids/mrtrix3_connectome.svg?style=plastic)](https://hub.docker.com/r/bids/mrtrix3_connectome) [MRtrix3_connectome](https://github.com/bids-apps/MRtrix3_connectome): Generate subject connectomes from raw BIDS data & perform inter-subject connection density normalisation, using  the MRtrix3 software package.
- [![Docker version](https://img.shields.io/docker/pulls/bids/ndmg.svg?style=plastic)](https://hub.docker.com/r/bids/ndmg) [ndmg](https://github.com/bids-apps/ndmg): BIDS app for NeuroData's MRI to Graphs pipeline
- [![Docker version](https://img.shields.io/docker/pulls/bids/nipypelines.svg?style=plastic)](https://hub.docker.com/r/bids/nipypelines) [nipypelines](https://github.com/bids-apps/nipypelines): Preprocess functional tasks in a BIDS dataset.
- [![Docker version](https://img.shields.io/docker/pulls/bids/oppni.svg?style=plastic)](https://hub.docker.com/r/bids/oppni) [oppni](https://github.com/bids-apps/oppni): runs fast optimization of preprocessing pipelines for BOLD fMRI
- [![Docker version](https://img.shields.io/docker/pulls/bids/pymvpa.svg?style=plastic)](https://hub.docker.com/r/bids/pymvpa) [PyMVPA](https://github.com/bids-apps/PyMVPA): runs MVPA and RSA analysis BIDS bold derivative data
- [![Docker version](https://img.shields.io/docker/pulls/bids/qap.svg?style=plastic)](https://hub.docker.com/r/bids/qap) [QAP](https://github.com/bids-apps/QAP): PCP Quality Assessment Protocol
- [![Docker version](https://img.shields.io/docker/pulls/bids/rs_signal_extract.svg?style=plastic)](https://hub.docker.com/r/bids/rs_signal_extract) [rs_signal_extract](https://github.com/bids-apps/rs_signal_extract): BIDS App for resting state signal extraction using nilearn.
- [![Docker version](https://img.shields.io/docker/pulls/bids/rshrf.svg?style=plastic)](https://hub.docker.com/r/bids/rshrf) [rsHRF](https://github.com/bids-apps/rsHRF): Resting state HRF estimation from BOLD-fMRI signal
- [![Docker version](https://img.shields.io/docker/pulls/bids/spm.svg?style=plastic)](https://hub.docker.com/r/bids/spm) [SPM](https://github.com/bids-apps/SPM): BIDS App containing an instance of the SPM software.
- [![Docker version](https://img.shields.io/docker/pulls/bids/tracula.svg?style=plastic)](https://hub.docker.com/r/bids/tracula) [tracula](https://github.com/bids-apps/tracula): implements Freesurfer's TRACULA (TRActs Constrained by UnderLying Anatomy) tool for cross-sectional as well as longitudinal (multi session) input data.
- [![Docker version](https://img.shields.io/docker/pulls/sebastientourbier/connectomemapper-bidsapp.svg?style=plastic)](https://hub.docker.com/r/sebastientourbier/connectomemapper-bidsapp) [connectomemapper3](https://github.com/connectomicslab/connectomemapper3): Connectome Mapper 3 is a BIDS App that implements full anatomical, diffusion, resting/state functional MRI, and recently EEG processing pipelines, from raw T1 / DWI / BOLD , and preprocessed EEG data to multi-resolution brain parcellation with corresponding connection matrices.
- [![Docker version](https://img.shields.io/docker/pulls/cpplab/bidsmreye.svg?style=plastic)](https://hub.docker.com/r/cpplab/bidsmreye) [bidsMReye](https://github.com/cpp-lln-lab/bidsMReye): BIDS app using deepMReye to decode eye motion for fMRI time series data.
- [![Docker version](https://img.shields.io/docker/pulls/cpplab/bidspm.svg?style=plastic)](https://hub.docker.com/r/cpplab/bidspm) [bidspm](https://github.com/cpp-lln-lab/bidspm): an SPM centric BIDS app
- [![Docker version](https://img.shields.io/docker/pulls/djarecka/fmriprep_fake.svg?style=plastic)](https://hub.docker.com/r/djarecka/fmriprep_fake) [fmriprep-fake](https://github.com/djarecka/fmriprep-fake): None
- [![Docker version](https://img.shields.io/docker/pulls/khanlab/funcmasker-flex.svg?style=plastic)](https://hub.docker.com/r/khanlab/funcmasker-flex) [funcmasker-flex](https://github.com/khanlab/funcmasker-flex): BIDS App for U-net brain masking of fetal bold MRI
- [![Docker version](https://img.shields.io/docker/pulls/khanlab/hippunfold.svg?style=plastic)](https://hub.docker.com/r/khanlab/hippunfold) [hippunfold](https://github.com/khanlab/hippunfold): BIDS App for Hippunfold (automated hippocampal unfolding and subfield segmentation)
- [![Docker version](https://img.shields.io/docker/pulls/sebastientourbier/mialsuperresolutiontoolkit.svg?style=plastic)](https://hub.docker.com/r/sebastientourbier/mialsuperresolutiontoolkit) [mialsuperresolutiontoolkit](https://github.com/Medical-Image-Analysis-Laboratory/mialsuperresolutiontoolkit): The Medical Image Analysis Laboratory Super-Resolution ToolKit (MIALSRTK) consists of a set of C++ and Python processing and workflow tools necessary to perform motion-robust super-resolution fetal MRI reconstruction in the BIDS Apps framework.
- [![Docker version](https://img.shields.io/docker/pulls/micalab/micapipe.svg?style=plastic)](https://hub.docker.com/r/micalab/micapipe) [micapipe](https://github.com/MICA-MNI/micapipe): micapipe from the Multimodal imaging and connectome analysis lab (http://mica-mni.github.io) at the Montreal Neurological Institute. Read The Docs documentation below
- [![Docker version](https://img.shields.io/docker/pulls/nipreps/dmriprep.svg?style=plastic)](https://hub.docker.com/r/nipreps/dmriprep) [dmriprep](https://github.com/nipreps/dmriprep): dMRIPrep is a robust and easy-to-use pipeline for preprocessing of diverse dMRI data. The transparent workflow dispenses of manual intervention, thereby ensuring the reproducibility of the results.
- [![Docker version](https://img.shields.io/docker/pulls/nipreps/fmriprep.svg?style=plastic)](https://hub.docker.com/r/nipreps/fmriprep) [fmriprep](https://github.com/nipreps/fmriprep): fMRIPrep is a robust and easy-to-use pipeline for preprocessing of diverse fMRI data. The transparent workflow dispenses of manual intervention, thereby ensuring the reproducibility of the results.
- [![Docker version](https://img.shields.io/docker/pulls/nipreps/mriqc.svg?style=plastic)](https://hub.docker.com/r/nipreps/mriqc) [mriqc](https://github.com/nipreps/mriqc): Automated Quality Control and visual reports for Quality Assessment of structural (T1w, T2w) and functional MRI of the brain
- [![Docker version](https://img.shields.io/docker/pulls/nipreps/nibabies.svg?style=plastic)](https://hub.docker.com/r/nipreps/nibabies) [nibabies](https://github.com/nipreps/nibabies): Processing tools for magnetic resonance images of infant brains
- [![Docker version](https://img.shields.io/docker/pulls/nipreps/nirodents.svg?style=plastic)](https://hub.docker.com/r/nipreps/nirodents) [nirodents](https://github.com/nipreps/nirodents): None
- [![Docker version](https://img.shields.io/docker/pulls/nipreps/smriprep.svg?style=plastic)](https://hub.docker.com/r/nipreps/smriprep) [smriprep](https://github.com/nipreps/smriprep): Structural MRI PREProcessing (sMRIPrep) workflows for NIPreps (NeuroImaging PREProcessing tools)
- [![Docker version](https://img.shields.io/docker/pulls/peerherholz/bidsonym.svg?style=plastic)](https://hub.docker.com/r/peerherholz/bidsonym) [BIDSonym](https://github.com/PeerHerholz/BIDSonym): a BIDS app for pseudo-anonymization of neuroimaging data
- [![Docker version](https://img.shields.io/docker/pulls/pennlinc/toy_bids_app.svg?style=plastic)](https://hub.docker.com/r/pennlinc/toy_bids_app) [babs_tests](https://github.com/PennLINC/babs_tests): Tests for BABS
- [![Docker version](https://img.shields.io/docker/pulls/pennbbl/qsiprep.svg?style=plastic)](https://hub.docker.com/r/pennbbl/qsiprep) [qsiprep](https://github.com/PennLINC/qsiprep): Preprocessing and reconstruction of diffusion MRI
- [![Docker version](https://img.shields.io/docker/pulls/poldracklab/fitlins.svg?style=plastic)](https://hub.docker.com/r/poldracklab/fitlins) [fitlins](https://github.com/poldracklab/fitlins): Fit Linear Models to BIDS Datasets
- [![Docker version](https://img.shields.io/docker/pulls/sebastientourbier/multiscalebrainparcellator.svg?style=plastic)](https://hub.docker.com/r/sebastientourbier/multiscalebrainparcellator) [multiscalebrainparcellator](https://github.com/sebastientourbier/multiscalebrainparcellator): Multi-Scale Brain Parcellator, part of the Connectome Mapping Toolkit (CMTK), is a BIDS App that implements a full anatomical MRI processing pipeline, from raw T1w data to structural brain parcellation at five different scales.
- [![Docker version](https://img.shields.io/docker/pulls/trends/gift-bids.svg?style=plastic)](https://hub.docker.com/r/trends/gift-bids) [gift-bids](https://github.com/trendscenter/gift-bids): None
<!-- APP ends -->

## Converters

Tools for converting data to/from BIDS from other standard or custom formats and layouts.

<!-- Converters starts -->

 ### MRI

-  [Autobids](https://github.com/khanlab/autobids): Automated Dicom to BIDS and pipelines using compute canada. From the Center for Functional and Metabolic Mapping (CFMM) at Western’s Robarts Research Institute.
  [![Last commit](https://img.shields.io/github/last-commit/khanlab/autobids?style=plastic)](https://github.com/khanlab/autobids)
- <img src='./images/logo_python.png' width='14px'> [BIDScoin](https://bidscoin.readthedocs.io/en/stable/): BIDScoin converts your source-level neuroimaging data to BIDS
  [![Last commit](https://img.shields.io/github/last-commit/Donders-Institute/bidscoin?style=plastic)](https://github.com/Donders-Institute/bidscoin)[![PyPI version](https://badge.fury.io/py/bidscoin.svg)](https://pypi.org/project/bidscoin)[![License: GPL-3.0](https://img.shields.io/badge/License-GPLv3-blue.svg?style=plastic)](https://www.gnu.org/licenses/gpl-3.0)
- <img src='./images/logo_R.png' width='18px'> [BIDSconvertR](https://bidsconvertr.github.io/): The BIDSconvertR R package provides a user-friendly workflow with graphical user interfaces. It consists of the following steps: (i) convert DICOM data to NIfTI data using dcm2niix (ii) structure this data according to the BIDS specification (iii) provide the papayaWidget viewer for inspecting the images
  [![Last commit](https://img.shields.io/github/last-commit/bidsconvertr/bidsconvertr?style=plastic)](https://github.com/bidsconvertr/bidsconvertr)[![License: GPL-3.0](https://img.shields.io/badge/License-GPLv3-blue.svg?style=plastic)](https://www.gnu.org/licenses/gpl-3.0)
- <img src='./images/logo_python.png' width='14px'> [bidsify](https://github.com/NILAB-UvA/bidsify): Tool to convert source MRI datasets to BIDS-compatible datasets.
  [![Last commit](https://img.shields.io/github/last-commit/NILAB-UvA/bidsify?style=plastic)](https://github.com/NILAB-UvA/bidsify)[![PyPI version](https://badge.fury.io/py/bidsify.svg)](https://pypi.org/project/bidsify)[![Docker version](https://img.shields.io/docker/pulls/lukassnoek/bidsify.svg?style=plastic)](https://hub.docker.com/r/lukassnoek/bidsify)
- <img src='./images/logo_python.png' width='14px'> [bidskit](https://github.com/jmtyszka/bidskit/blob/master/docs/QuickStart.md): Utility functions for working with DICOM and BIDS neuroimaging data.
  [![Last commit](https://img.shields.io/github/last-commit/jmtyszka/bidskit?style=plastic)](https://github.com/jmtyszka/bidskit)[![PyPI version](https://badge.fury.io/py/bidskit.svg)](https://pypi.org/project/bidskit)[![Docker version](https://img.shields.io/docker/pulls/jmtyszka/bidskit.svg?style=plastic)](https://hub.docker.com/r/jmtyszka/bidskit)[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=plastic)](https://opensource.org/licenses/MIT)
- <img src='./images/logo_python.png' width='14px'> [BIDSme](https://gitlab.uliege.be/CyclotronResearchCentre/Public/bidstools/bidsme/bidsme_example/-/tree/master/example1):
  [![Last commit](https://img.shields.io/github/last-commit/nbeliy/bidsme?style=plastic)](https://github.com/nbeliy/bidsme)[![License: GPL-2.0](https://img.shields.io/badge/License-GPLv2-blue.svg?style=plastic)](https://www.gnu.org/licenses/gpl-2.0)
- <img src='./images/logo_python.png' width='14px'> [BMAT](https://github.com/ColinVDB/BMAT):
  [![Last commit](https://img.shields.io/github/last-commit/ColinVDB/BMAT?style=plastic)](https://github.com/ColinVDB/BMAT)[![Docker version](https://img.shields.io/docker/pulls/colinvdb/bmat-dcm2niix.svg?style=plastic)](https://hub.docker.com/r/colinvdb/bmat-dcm2niix)[![License: GPL-3.0](https://img.shields.io/badge/License-GPLv3-blue.svg?style=plastic)](https://www.gnu.org/licenses/gpl-3.0)
- <img src='./images/logo_python.png' width='14px'> [BrkRaw](https://github.com/BrkRaw/brkraw): For a preclinical Bruker MRI scanner
  [![Last commit](https://img.shields.io/github/last-commit/BrkRaw/brkraw?style=plastic)](https://github.com/BrkRaw/brkraw)[![License: GPL-3.0](https://img.shields.io/badge/License-GPLv3-blue.svg?style=plastic)](https://www.gnu.org/licenses/gpl-3.0)
- <img src='./images/logo_python.png' width='14px'> [Clinica](https://aramislab.paris.inria.fr/clinica/docs/public/latest/):
  [![Last commit](https://img.shields.io/github/last-commit/aramis-lab/clinica?style=plastic)](https://github.com/aramis-lab/clinica)[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=plastic)](https://opensource.org/licenses/MIT)
- <img src='./images/logo_python.png' width='14px'> [dac2bids](https://github.com/dangom/dac2bids): Create a BIDS structure for a DICOM folder.
  [![Last commit](https://img.shields.io/github/last-commit/dangom/dac2bids?style=plastic)](https://github.com/dangom/dac2bids)
- <img src='./images/logo_python.png' width='14px'> [Data2Bids](https://github.com/SIMEXP/Data2Bids): Converts MRI files from extension supported by nibabel into NIfTI and convert them to BIDS
  [![Last commit](https://img.shields.io/github/last-commit/SIMEXP/Data2Bids?style=plastic)](https://github.com/SIMEXP/Data2Bids)[![PyPI version](https://badge.fury.io/py/data2bids.svg)](https://pypi.org/project/data2bids)[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=plastic)](https://opensource.org/licenses/MIT)
- <img src='./images/logo_python.png' width='14px'> [Dcm2Bids](https://unfmontreal.github.io/Dcm2Bids/): converts DICOM files using dcm2niix into BIDS
  [![Last commit](https://img.shields.io/github/last-commit/cbedetti/Dcm2Bids?style=plastic)](https://github.com/cbedetti/Dcm2Bids)[![PyPI version](https://badge.fury.io/py/Dcm2Bids.svg)](https://pypi.org/project/Dcm2Bids)[![Docker version](https://img.shields.io/docker/pulls/unfmontreal/dcm2bids.svg?style=plastic)](https://hub.docker.com/r/unfmontreal/dcm2bids)[![License: GPL-3.0](https://img.shields.io/badge/License-GPLv3-blue.svg?style=plastic)](https://www.gnu.org/licenses/gpl-3.0)
- <img src='./images/logo_matlab.png' width='17px'> [Explore ASL](https://exploreasl.github.io/Documentation/1.8.0/Tutorials-ASL-BIDS/): Convert DICOM and NIFTI data to the ASL-BIDS format.
  [![Last commit](https://img.shields.io/github/last-commit/ExploreASL/ExploreASL?style=plastic)](https://github.com/ExploreASL/ExploreASL)
- <img src='./images/logo_python.png' width='14px'> [HeuDiConv](https://heudiconv.readthedocs.io/): A flexible DICOM converter for organizing brain imaging data into structured directory layouts
  [![Last commit](https://img.shields.io/github/last-commit/nipy/heudiconv?style=plastic)](https://github.com/nipy/heudiconv)[![PyPI version](https://badge.fury.io/py/heudiconv.svg)](https://pypi.org/project/heudiconv)[![Docker version](https://img.shields.io/docker/pulls/nipy/heudiconv.svg?style=plastic)](https://hub.docker.com/r/nipy/heudiconv)[![License: Apache 2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg?style=plastic)](https://opensource.org/licenses/Apache-2.0)
-  [Horos (Osirix) export plugin](https://github.com/mslw/horos-bids-output): Horos plugin for BIDS output.
  [![Last commit](https://img.shields.io/github/last-commit/mslw/horos-bids-output?style=plastic)](https://github.com/mslw/horos-bids-output)[![License: GPL-3.0](https://img.shields.io/badge/License-GPLv3-blue.svg?style=plastic)](https://www.gnu.org/licenses/gpl-3.0)
- <img src='./images/logo_python.png' width='14px'> [niix2bids](https://github.com/benoitberanger/niix2bids): Use this package as a command line to organize your Nifti dataset into BIDS.
  [![Last commit](https://img.shields.io/github/last-commit/benoitberanger/niix2bids?style=plastic)](https://github.com/benoitberanger/niix2bids)[![License: GPL-3.0](https://img.shields.io/badge/License-GPLv3-blue.svg?style=plastic)](https://www.gnu.org/licenses/gpl-3.0)
-  [OpenfMRI2BIDS](https://github.com/bids-standard/openfmri2bids): Convert OpenfMRI dataset to BIDS
  [![Last commit](https://img.shields.io/github/last-commit/bids-standard/openfmri2bids?style=plastic)](https://github.com/bids-standard/openfmri2bids)
- <img src='./images/logo_matlab.png' width='17px'> <img src='./images/logo_python.png' width='14px'> [PET2BIDS](https://github.com/openneuropet/PET2BIDS): Helps you convert your PET data! raw PET scanner files (for example ecat, dicom) and additional side file like excel sheets.
  [![Last commit](https://img.shields.io/github/last-commit/openneuropet/PET2BIDS?style=plastic)](https://github.com/openneuropet/PET2BIDS)[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=plastic)](https://opensource.org/licenses/MIT)
- <img src='./images/logo_python.png' width='14px'> [ReproIn](https://github.com/ReproNim/reproin): HeuDiConv-based turnkey solution: a setup for automatic generation of shareable, version-controlled BIDS datasets from MR scanners.
  [![Last commit](https://img.shields.io/github/last-commit/ReproNim/reproin?style=plastic)](https://github.com/ReproNim/reproin)[![Docker version](https://img.shields.io/docker/pulls/repronim/reproin.svg?style=plastic)](https://hub.docker.com/r/repronim/reproin)[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=plastic)](https://opensource.org/licenses/MIT)
- <img src='./images/logo_python.png' width='14px'> [SAMRI](https://doi.org/10.3389/fninf.2020.00005): Full stack Small Animal MRI data analysis package, including the `bru2bids` repositing pipeline, which can convert Bruker archives to the BIDS format. From the ETH and University of Zurich, with collaboration from MIT and Dartmouth College.
  ![](https://img.shields.io/badge/shell-black.svg?style=plastic)[![Last commit](https://img.shields.io/github/last-commit/IBT-FMI/SAMRI?style=plastic)](https://github.com/IBT-FMI/SAMRI)
-  [XNAT2BIDS](https://github.com/kamillipi/2bids): Simple xnat pipeline to convert DICOM scans to BIDS-compatible output (nii+json).
  ![](https://img.shields.io/badge/shell-black.svg?style=plastic)[![Last commit](https://img.shields.io/github/last-commit/kamillipi/2bids?style=plastic)](https://github.com/kamillipi/2bids)

 ### MEEG

- <img src='./images/logo_python.png' width='14px'> [BIDSme](https://gitlab.uliege.be/CyclotronResearchCentre/Public/bidstools/bidsme/bidsme_example/-/tree/master/example1):
  [![Last commit](https://img.shields.io/github/last-commit/nbeliy/bidsme?style=plastic)](https://github.com/nbeliy/bidsme)[![License: GPL-2.0](https://img.shields.io/badge/License-GPLv2-blue.svg?style=plastic)](https://www.gnu.org/licenses/gpl-2.0)
- <img src='./images/logo_python.png' width='14px'> [Biscuit](https://macquarie-meg-research.github.io/Biscuit/): GUI for easy MEG to BIDS conversion
  [![Last commit](https://img.shields.io/github/last-commit/Macquarie-MEG-Research/Biscuit?style=plastic)](https://github.com/Macquarie-MEG-Research/Biscuit)[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=plastic)](https://opensource.org/licenses/MIT)
- <img src='./images/logo_python.png' width='14px'> [EEG2BIDS](None): A tool for converting raw EEG and iEEG data into the BIDS standard data structure, prepared for LORIS (Longitudinal Online Research and Imaging System).
  ![](https://img.shields.io/badge/Javascript-yellow.svg?style=plastic)[![Last commit](https://img.shields.io/github/last-commit/aces/EEG2BIDS?style=plastic)](https://github.com/aces/EEG2BIDS)
- <img src='./images/logo_matlab.png' width='17px'> [EEGLAB](https://eeglab.org/tutorials/04_Import/BIDS.html): <a href='https://github.com/arnodelorme/bids-MATLAB-tools'>See plugins</a>
  [![Last commit](https://img.shields.io/github/last-commit/sccn/eeglab?style=plastic)](https://github.com/sccn/eeglab)
- <img src='./images/logo_matlab.png' width='17px'> [FieldTrip - data2bids](https://www.fieldtriptoolbox.org/example/bids/):
  [![Last commit](https://img.shields.io/github/last-commit/fieldtrip/fieldtrip?style=plastic)](https://github.com/fieldtrip/fieldtrip)[![License: GPL-3.0](https://img.shields.io/badge/License-GPLv3-blue.svg?style=plastic)](https://www.gnu.org/licenses/gpl-3.0)
- <img src='./images/logo_python.png' width='14px'> [MNE-BIDS](https://mne.tools/mne-bids): MNE-BIDS is a Python package that allows you to read and write BIDS-compatible datasets with the help of MNE-Python.
  [![Last commit](https://img.shields.io/github/last-commit/mne-tools/mne-bids?style=plastic)](https://github.com/mne-tools/mne-bids)[![PyPI version](https://badge.fury.io/py/mne-bids.svg)](https://pypi.org/project/mne-bids)[![License: BSD-3-Clause](https://img.shields.io/badge/License-BSD_3--Clause-blue.svg?style=plastic)](https://opensource.org/licenses/BSD-3-Clause)
- <img src='./images/logo_python.png' width='14px'> [sovabids](https://sovabids.readthedocs.io/en/latest/): A Python package for the automatic conversion of EEG datasets to the BIDS standard, with a focus on making the most out of metadata.
  [![Last commit](https://img.shields.io/github/last-commit/yjmantilla/sovabids?style=plastic)](https://github.com/yjmantilla/sovabids)

 ### physiological

- <img src='./images/logo_python.png' width='14px'> [BIDScoin](https://bidscoin.readthedocs.io/en/stable/): BIDScoin converts your source-level neuroimaging data to BIDS
  [![Last commit](https://img.shields.io/github/last-commit/Donders-Institute/bidscoin?style=plastic)](https://github.com/Donders-Institute/bidscoin)[![PyPI version](https://badge.fury.io/py/bidscoin.svg)](https://pypi.org/project/bidscoin)
- <img src='./images/logo_python.png' width='14px'> [bidsphysio](None): Converts physio data (CMRR, AcqKnowledge, Siemens PMU) to BIDS physiological recording
  [![Last commit](https://img.shields.io/github/last-commit/cbinyu/bidsphysio?style=plastic)](https://github.com/cbinyu/bidsphysio)[![PyPI version](https://badge.fury.io/py/bidsphysio.svg)](https://pypi.org/project/bidsphysio/)[![Docker version](https://img.shields.io/docker/pulls/cbinyu/bidsphysio.svg?style=plastic)](https://hub.docker.com/r/cbinyu/bidsphysio/)
- <img src='./images/logo_python.png' width='14px'> [phys2bids](https://phys2bids.readthedocs.io/en/latest/): Python3 library to format physiological files in BIDS.
  [![Last commit](https://img.shields.io/github/last-commit/physiopy/phys2bids?style=plastic)](https://github.com/physiopy/phys2bids)[![PyPI version](https://badge.fury.io/py/phys2bids.svg)](https://pypi.org/project/phys2bids)

 ### others

- <img src='./images/logo_python.png' width='14px'> [convert-eprime](https://github.com/tsalo/convert-eprime): Python functions to convert E-Prime files to csvs. Not currently being developed.
  [![Last commit](https://img.shields.io/github/last-commit/tsalo/convert-eprime?style=plastic)](https://github.com/tsalo/convert-eprime)[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=plastic)](https://opensource.org/licenses/MIT)
-  [DCM2NIIx](https://github.com/neurolabusc/dcm2niix): dcm2nii DICOM to NIfTI converter
  [![Last commit](https://img.shields.io/github/last-commit/neurolabusc/dcm2niix?style=plastic)](https://github.com/neurolabusc/dcm2niix)
- <img src='./images/logo_matlab.png' width='17px'> [DICM2NII](https://github.com/xiangruili/dicm2nii): dcm2nii DICOM to NIfTI converter
  [![Last commit](https://img.shields.io/github/last-commit/xiangruili/dicm2nii?style=plastic)](https://github.com/xiangruili/dicm2nii)
- <img src='./images/logo_python.png' width='14px'> [sim2bids](https://github.com/dissagaliyeva/sim2bids): GUI to easily convert simulation results to BIDS format, according to <a herf="https://bids.neuroimaging.io/bep034" target="_blank">   BEP 34 </a>.
  [![Last commit](https://img.shields.io/github/last-commit/dissagaliyeva/sim2bids?style=plastic)](https://github.com/dissagaliyeva/sim2bids)[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=plastic)](https://opensource.org/licenses/MIT)
<!-- Converters ends -->

## Documentation

Documentation and publications related to BIDS.

- [BIDS Specification](https://bids-specification.readthedocs.io)
- [BIDS Starter Kit](https://bids-standard.github.io/bids-starter-kit/)
- [FieldTrip](https://www.fieldtriptoolbox.org/example/bids/) examples, mainly for MEG, EEG, fNIRS, etc.
- ...

## Extension proposals

Ongoing community proposals for extending the BIDS specification or interoperating with BIDS datasets.

<!-- BEP starts -->

 ### raw

- [BEP004](https://bids.neuroimaging.io/bep004): Susceptibility Weighted Imaging (SWI)
- [BEP020](https://bids.neuroimaging.io/bep020): Eye Tracking including Gaze Position and Pupil Size
- [BEP022](https://bids.neuroimaging.io/bep022): Magnetic Resonance Spectroscopy (MRS)
- [BEP024](https://bids.neuroimaging.io/bep024): Computed Tomography scan (CT)
- [BEP026](https://bids.neuroimaging.io/bep026): Microelectrode Recordings
- [BEP029](https://bids.neuroimaging.io/bep029): Virtual and physical motion data
- [BEP032](https://bids.neuroimaging.io/bep032): Animal electrophysiology
- [BEP033](https://bids.neuroimaging.io/bep033): Advanced Diffusion Weighted Imaging (aDWI)
- [BEP036](https://bids.neuroimaging.io/bep036): Phenotypic Data Guidelines
- [BEP037](https://bids.neuroimaging.io/bep037): Non-Invasive Brain Stimulation (NIBS)
- [BEP038](https://bids.neuroimaging.io/bep038): Atlases
- [BEP039](https://bids.neuroimaging.io/bep039): Dimensionality reduction-based networks
- [BEP040](https://bids.neuroimaging.io/bep040): Functional Ultrasound (fUS)

 ### derivative

- [BEP011](https://bids.neuroimaging.io/bep011): Structural preprocessing derivatives
- [BEP012](https://bids.neuroimaging.io/bep012): Functional preprocessing derivatives
- [BEP014](https://bids.neuroimaging.io/bep014): Affine transformations and nonlinear field warps
- [BEP016](https://bids.neuroimaging.io/bep016): Diffusion weighted imaging derivatives
- [BEP017](https://bids.neuroimaging.io/bep017): Generic BIDS connectivity data schema
- [BEP021](https://bids.neuroimaging.io/bep021): Common Electrophysiological Derivatives
- [BEP023](https://bids.neuroimaging.io/bep023): PET Preprocessing derivatives
- [BEP034](https://bids.neuroimaging.io/bep034): Computational modeling
- [BEP035](https://bids.neuroimaging.io/bep035): Modular extensions for individual participant data mega-analyses with non-compliant derivatives
<!-- BEP ends -->

## Software

Software packages for working with BIDS datasets.

<!-- TOOLS starts -->
- <img src='./images/logo_python.png' width='14px'> [babs](https://pennlinc-babs.readthedocs.io/): BIDS App Bootstrap (BABS) is a reproducible, generalizable, and scalable Python package for BIDS App analysis of large datasets. It uses DataLad and adopts FAIRly big framework. [![Last commit](https://img.shields.io/github/last-commit/PennLINC/babs?style=plastic)](https://github.com/PennLINC/babs) [![PyPI version](https://badge.fury.io/py/babs.svg)](https://pypi.org/project/babs/)
- <img src='./images/logo_python.png' width='14px'> [bids-cfood](https://gitlab.indiscale.com/caosdb/src/crawler-cfoods/bids-cfood): a module to handle BIDS dataset for the caosDB data crawler
- <img src='./images/logo_matlab.png' width='17px'> <img src='./images/logo_octave.png' width='16px'> [bids-matlab](https://github.com/bids-standard/bids-matlab): MATLAB/Octave tools to interact with datasets conforming to the BIDS format [![Last commit](https://img.shields.io/github/last-commit/bids-standard/bids-matlab?style=plastic)](https://github.com/bids-standard/bids-matlab)
- <img src='./images/logo_python.png' width='14px'> [BIDS-pydantic](https://github.com/gold-standard-phantoms/bids-pydantic): Pulls a specified version of the BIDS schema and creates corresponding Pydantic models, which will provide BIDS data validation using Python type annotations. See also [BIDS-pydantic-models](https://pypi.org/project/BIDS-pydantic-models/). [![Last commit](https://img.shields.io/github/last-commit/gold-standard-phantoms/bids-pydantic?style=plastic)](https://github.com/gold-standard-phantoms/bids-pydantic) [![PyPI version](https://badge.fury.io/py/BIDS-pydantic.svg)](https://pypi.org/project/BIDS-pydantic/)
- <img src='./images/logo_python.png' width='14px'> [bids2cite](https://github.com/Remi-Gau/bids2cite): package to interactively update `dataset_description.json` and generate citation files (for example `datacite.yml`) for BIDS datasets. [![Last commit](https://img.shields.io/github/last-commit/Remi-Gau/bids2cite?style=plastic)](https://github.com/Remi-Gau/bids2cite)
- <img src='./images/logo_R.png' width='18px'> [bidser](https://bbuchsbaum.github.io/bidser/): Working with Brain Imaging Data Structure in R [![Last commit](https://img.shields.io/github/last-commit/bbuchsbaum/bidser?style=plastic)](https://github.com/bbuchsbaum/bidser)
- <img src='./images/logo_python.png' width='14px'> [BIDSHandler](https://github.com/Macquarie-MEG-Research/BIDSHandler): Python module allowing complete manipulation of BIDS data [![Last commit](https://img.shields.io/github/last-commit/Macquarie-MEG-Research/BIDSHandler?style=plastic)](https://github.com/Macquarie-MEG-Research/BIDSHandler)
- <img src='./images/logo_matlab.png' width='17px'> [Brainstorm](http://neuroimage.usc.edu/brainstorm/): MEG/EEG analysis package
- <img src='./images/logo_python.png' width='14px'> [clpipe](https://clpipe.readthedocs.io/en/latest/index.html): streamlined processing pipeline for MRI data centered around BIDS [![Last commit](https://img.shields.io/github/last-commit/cohenlabUNC/clpipe?style=plastic)](https://github.com/cohenlabUNC/clpipe)
- <img src='./images/logo_python.png' width='14px'> [cuBIDS](https://cubids.readthedocs.io/en/latest/): a Python package designed to facilitate reproducible curation of neuroimaging BIDS datasets [![Last commit](https://img.shields.io/github/last-commit/pennlinc/cubids?style=plastic)](https://github.com/pennlinc/cubids) [![PyPI version](https://badge.fury.io/py/cubids.svg)](https://pypi.org/project/cubids/)
- <img src='./images/logo_python.png' width='14px'> [GUI dataset description generator](None): GUI form that generates `dataset_description.json` [![Last commit](https://img.shields.io/github/last-commit/tolik-g/BIDS?style=plastic)](https://github.com/tolik-g/BIDS)
- <img src='./images/logo_matlab.png' width='17px'> [Lead-DBS](https://www.lead-dbs.org/): A toolbox facilitating Deep Brain Stimulation electrode reconstructions  and computer simulations supports BIDS conversion and ingestion of BIDS datasets.
- <img src='./images/logo_python.png' width='14px'> [mne-bids](https://mne.tools/mne-bids/stable/index.html): collection of tools for converting magnetoencephalography (MEG) data into BIDS format, as well as some helper functions for creating the folders and metadata needed for a BIDS dataset. [![Last commit](https://img.shields.io/github/last-commit/mne-tools/mne-bids?style=plastic)](https://github.com/mne-tools/mne-bids)
-  [OpenNeuro](http://openneuro.org): A free and open platform for validating and sharing BIDS-compliant data.
-  [PRFmodel](https://github.com/vistalab/PRFmodel/wiki): a set of tools to fit population receptive field models to BIDS datasets [![Last commit](https://img.shields.io/github/last-commit/vistalab/PRFmodel?style=plastic)](https://github.com/vistalab/PRFmodel)
- <img src='./images/logo_python.png' width='14px'> [PyBIDS](None): Python package to quickly parse / search the components of a BIDS dataset. It also contains functionality for running analyses on your data. [![Last commit](https://img.shields.io/github/last-commit/bids-standard/pybids?style=plastic)](https://github.com/bids-standard/pybids) [![PyPI version](https://badge.fury.io/py/pybids.svg)](https://pypi.org/project/pybids/)
- <img src='./images/logo_R.png' width='18px'> [rbids](https://github.com/mathesong/rbids): aims to make BIDS datasets more easily accessible for packages written in R [![Last commit](https://img.shields.io/github/last-commit/mathesong/rbids?style=plastic)](https://github.com/mathesong/rbids)
- <img src='./images/logo_matlab.png' width='17px'> <img src='./images/logo_octave.png' width='16px'> [spm_2_bids](https://spm-2-bids.readthedocs.io/en/latest/): a tool convert SPM preprocessed output to BIDS derivatives (trying to follow [BEP12](https://bids.neuroimaging.io/bep012)) [![Last commit](https://img.shields.io/github/last-commit/cpp-lln-lab/spm_2_bids?style=plastic)](https://github.com/cpp-lln-lab/spm_2_bids)
<!-- TOOLS ends -->

## Contribute

Contributions welcome! Read the [contribution guidelines](contributing.md) first.
