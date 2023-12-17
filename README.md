# Awesome BIDS [![Awesome](https://awesome.re/badge.svg)](https://github.com/sindresorhus/awesome#readme)

<img src="https://raw.githubusercontent.com/bids-standard/bids-specification/master/BIDS_logo/BIDS_logo_white_transparent_background_crop.png#gh-dark-mode-only" alt="bids-logo" width="600"/>
<img src="https://raw.githubusercontent.com/bids-standard/bids-specification/master/BIDS_logo//BIDS_logo_black_transparent_background_crop.png#gh-light-mode-only" alt="bids-logo" width="600"/>

A curated list of awesome projects, proposals, apps and resources
related to the Brain Imaging Data Structure.

## Documentation

Documentation related to BIDS.

- The central [BIDS website](http://www.bids-standard.org/) to get general information about BIDS.
- The [BIDS Starter Kit](https://bids-standard.github.io/bids-starter-kit/)
  is the best place to get started with BIDS.
- The official [BIDS Specification](https://bids-specification.readthedocs.io) to get into the details.
- The [BIDS youtube channel](https://www.youtube.com/channel/UCxZUcYfd_nvIVWAbzRB1tlw)
  where we try to curate [playlists](https://www.youtube.com/@brainimagingdatastructure6721/playlists) of BIDS related videos.
- Slides of many BIDS related presentations are available on the [Open Science Framework](https://osf.io/yn93h/).
- The [FieldTrip](https://www.fieldtriptoolbox.org/example/bids/) websites contains
  many BIDS  tips and  examples, mainly for MEG, EEG, fNIRS, etc.
- If you help to mention BIDS in one of your grant,
  make sure that to check out the [BIDS grant writing kit](https://github.com/bids-standard/grant_writing_kit#bids-grant-writing-kit).

## Community

- The [Neurostars discourse forum](https://neurostars.org/tag/bids)
  run by the International Neuroinformatics Coordinating Facility ([INCF](https://www.incf.org/))
  with its own [BIDS category](https://neurostars.org/tag/bids).
  With a lot BIDS users and developers,
  it is the best place where to ask BIDS related questions.

- [BIDS mailing list](https://groups.google.com/g/bids-discussion):
  a google group for announcements and discussions around BIDS.

- [BIDS in the Brainhack mattersmost](https://mattermost.brainhack.org/brainhack/channels/bids_general):
  [mattermost](https://mattermost.com/) is the open source equivalent of slack
  and the [Brainhack](https://brainhack.org/) instance has over 5000 members
  with its own channel dedicated BIDS channel.

## Social media

Here are the official BIDS account on several social media.

- [Twitter / X](https://twitter.com/BIDSstandard)
- [Mastodon](https://fosstodon.org/@bidsstandard/)
- [Bluesky](https://bsky.app/profile/bidsstandard.bsky.social)
- [YouTube](https://www.youtube.com/channel/UCxZUcYfd_nvIVWAbzRB1tlw)
- Our podcast on [anchor](https://anchor.fm/bids-maintenance)

## Datasets

- The [BIDS examples](https://bids-standard.github.io/bids-examples/) host dataset of each modality.
  with empty raw data files. These datasets can be useful to:
  - serve as an example on how a BIDS dataset can be structured
  - write lightweight software tests
- [OpenNeuro](https://openneuro.org/) host more than 1000 open BIDS datasets of all datatypes.

## Converters

Tools for converting data to/from BIDS from other standard or custom formats and layouts.

<!-- Converters starts -->

### MRI

-  [Autobids](https://github.com/khanlab/autobids): Automated Dicom to BIDS and pipelines using compute canada. From the Center for Functional and Metabolic Mapping (CFMM) at Western’s Robarts Research Institute.
  <br>[![Last commit](https://img.shields.io/github/last-commit/khanlab/autobids?style=plastic)](https://github.com/khanlab/autobids)
- <img src='./images/logo_python.png' width='14px'>  [BIDScoin](https://bidscoin.readthedocs.io/en/stable/): BIDScoin converts your source-level neuroimaging data to BIDS
  <br>[![Last commit](https://img.shields.io/github/last-commit/Donders-Institute/bidscoin?style=plastic)](https://github.com/Donders-Institute/bidscoin)[![PyPI version](https://badge.fury.io/py/bidscoin.svg)](https://pypi.org/project/bidscoin)[![License: GPL-3.0](https://img.shields.io/badge/License-GPLv3-blue.svg?style=plastic)](https://www.gnu.org/licenses/gpl-3.0)
- <img src='./images/logo_R.png' width='18px'>  [BIDSconvertR](https://bidsconvertr.github.io/): The BIDSconvertR R package provides a user-friendly workflow with graphical user interfaces. It consists of the following steps: (i) convert DICOM data to NIfTI data using dcm2niix (ii) structure this data according to the BIDS specification (iii) provide the papayaWidget viewer for inspecting the images
  <br>[![Last commit](https://img.shields.io/github/last-commit/bidsconvertr/bidsconvertr?style=plastic)](https://github.com/bidsconvertr/bidsconvertr)[![License: GPL-3.0](https://img.shields.io/badge/License-GPLv3-blue.svg?style=plastic)](https://www.gnu.org/licenses/gpl-3.0)
- <img src='./images/logo_python.png' width='14px'>  [bidsify](https://github.com/NILAB-UvA/bidsify): Tool to convert source MRI datasets to BIDS-compatible datasets.
  <br>[![Last commit](https://img.shields.io/github/last-commit/NILAB-UvA/bidsify?style=plastic)](https://github.com/NILAB-UvA/bidsify)[![PyPI version](https://badge.fury.io/py/bidsify.svg)](https://pypi.org/project/bidsify)[![Docker version](https://img.shields.io/docker/pulls/lukassnoek/bidsify.svg?style=plastic)](https://hub.docker.com/r/lukassnoek/bidsify)
- <img src='./images/logo_python.png' width='14px'>  [bidskit](https://github.com/jmtyszka/bidskit/blob/master/docs/QuickStart.md): Utility functions for working with DICOM and BIDS neuroimaging data.
  <br>[![Last commit](https://img.shields.io/github/last-commit/jmtyszka/bidskit?style=plastic)](https://github.com/jmtyszka/bidskit)[![PyPI version](https://badge.fury.io/py/bidskit.svg)](https://pypi.org/project/bidskit)[![Docker version](https://img.shields.io/docker/pulls/jmtyszka/bidskit.svg?style=plastic)](https://hub.docker.com/r/jmtyszka/bidskit)[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=plastic)](https://opensource.org/licenses/MIT)
- <img src='./images/logo_python.png' width='14px'>  [BIDSme](https://gitlab.uliege.be/CyclotronResearchCentre/Public/bidstools/bidsme/bidsme_example/-/tree/master/example1):
  <br>[![Last commit](https://img.shields.io/github/last-commit/nbeliy/bidsme?style=plastic)](https://github.com/nbeliy/bidsme)[![License: GPL-2.0](https://img.shields.io/badge/License-GPLv2-blue.svg?style=plastic)](https://www.gnu.org/licenses/gpl-2.0)
- <img src='./images/logo_python.png' width='14px'>  [BMAT](https://github.com/ColinVDB/BMAT):
  <br>[![Last commit](https://img.shields.io/github/last-commit/ColinVDB/BMAT?style=plastic)](https://github.com/ColinVDB/BMAT)[![Docker version](https://img.shields.io/docker/pulls/colinvdb/bmat-dcm2niix.svg?style=plastic)](https://hub.docker.com/r/colinvdb/bmat-dcm2niix)[![License: GPL-3.0](https://img.shields.io/badge/License-GPLv3-blue.svg?style=plastic)](https://www.gnu.org/licenses/gpl-3.0)
- <img src='./images/logo_python.png' width='14px'>  [BrkRaw](https://github.com/BrkRaw/brkraw): For a preclinical Bruker MRI scanner
  <br>[![Last commit](https://img.shields.io/github/last-commit/BrkRaw/brkraw?style=plastic)](https://github.com/BrkRaw/brkraw)[![License: GPL-3.0](https://img.shields.io/badge/License-GPLv3-blue.svg?style=plastic)](https://www.gnu.org/licenses/gpl-3.0)
- <img src='./images/logo_python.png' width='14px'>  [Clinica](https://aramislab.paris.inria.fr/clinica/docs/public/latest/):
  <br>[![Last commit](https://img.shields.io/github/last-commit/aramis-lab/clinica?style=plastic)](https://github.com/aramis-lab/clinica)[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=plastic)](https://opensource.org/licenses/MIT)
- <img src='./images/logo_python.png' width='14px'>  [dac2bids](https://github.com/dangom/dac2bids): Create a BIDS structure for a DICOM folder.
  <br>[![Last commit](https://img.shields.io/github/last-commit/dangom/dac2bids?style=plastic)](https://github.com/dangom/dac2bids)
- <img src='./images/logo_python.png' width='14px'>  [Data2Bids](https://github.com/SIMEXP/Data2Bids): Converts MRI files from extension supported by nibabel into NIfTI and convert them to BIDS
  <br>[![Last commit](https://img.shields.io/github/last-commit/SIMEXP/Data2Bids?style=plastic)](https://github.com/SIMEXP/Data2Bids)[![PyPI version](https://badge.fury.io/py/data2bids.svg)](https://pypi.org/project/data2bids)[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=plastic)](https://opensource.org/licenses/MIT)
- <img src='./images/logo_python.png' width='14px'>  [Dcm2Bids](https://unfmontreal.github.io/Dcm2Bids/): converts DICOM files using dcm2niix into BIDS
  <br>[![Last commit](https://img.shields.io/github/last-commit/cbedetti/Dcm2Bids?style=plastic)](https://github.com/cbedetti/Dcm2Bids)[![PyPI version](https://badge.fury.io/py/Dcm2Bids.svg)](https://pypi.org/project/Dcm2Bids)[![Docker version](https://img.shields.io/docker/pulls/unfmontreal/dcm2bids.svg?style=plastic)](https://hub.docker.com/r/unfmontreal/dcm2bids)[![License: GPL-3.0](https://img.shields.io/badge/License-GPLv3-blue.svg?style=plastic)](https://www.gnu.org/licenses/gpl-3.0)
- <img src='./images/logo_matlab.png' width='17px'>  [Explore ASL](https://exploreasl.github.io/Documentation/1.8.0/Tutorials-ASL-BIDS/): Convert DICOM and NIFTI data to the ASL-BIDS format.
  <br>[![Last commit](https://img.shields.io/github/last-commit/ExploreASL/ExploreASL?style=plastic)](https://github.com/ExploreASL/ExploreASL)
- <img src='./images/logo_python.png' width='14px'>  [ezBIDS](https://brainlife.io/docs/using_ezBIDS/): A web-based BIDS conversion tool with four unique features: (1) No installation or programming requirements. (2) Handling of both imaging and task events data and metadata. (3) Semi-automated inference and guidance for adherence to BIDS. (4) Multiple data management options, including download BIDS data to local system, or transfer to OpenNeuro.org or to brainlife.io.
  <br>![](https://img.shields.io/badge/Javascript-yellow.svg?style=plastic)![](https://img.shields.io/badge/shell-black.svg?style=plastic)[![Last commit](https://img.shields.io/github/last-commit/brainlife/ezbids?style=plastic)](https://github.com/brainlife/ezbids)[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=plastic)](https://opensource.org/licenses/MIT)
- <img src='./images/logo_python.png' width='14px'>  [HeuDiConv](https://heudiconv.readthedocs.io/): A flexible DICOM converter for organizing brain imaging data into structured directory layouts
  <br>[![Last commit](https://img.shields.io/github/last-commit/nipy/heudiconv?style=plastic)](https://github.com/nipy/heudiconv)[![PyPI version](https://badge.fury.io/py/heudiconv.svg)](https://pypi.org/project/heudiconv)[![Docker version](https://img.shields.io/docker/pulls/nipy/heudiconv.svg?style=plastic)](https://hub.docker.com/r/nipy/heudiconv)[![License: Apache 2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg?style=plastic)](https://opensource.org/licenses/Apache-2.0)
-  [Horos (Osirix) export plugin](https://github.com/mslw/horos-bids-output): Horos plugin for BIDS output.
  <br>[![Last commit](https://img.shields.io/github/last-commit/mslw/horos-bids-output?style=plastic)](https://github.com/mslw/horos-bids-output)[![License: GPL-3.0](https://img.shields.io/badge/License-GPLv3-blue.svg?style=plastic)](https://www.gnu.org/licenses/gpl-3.0)
- <img src='./images/logo_python.png' width='14px'>  [mercure-dcm2bids](https://github.com/mercure-imaging/mercure-dcm2bids): A containerized app that can be used to perform BIDS conversion of  DICOM studies sent directly to mercure from a scanner or PACS. mercure  is an open-source DICOM orchestration platform that can integrate  containerized apps into clinical workflows. It has a graphical user  interface making it easy to setup and manage BIDS configurations for  multiple protocols. The Dcm2Bids tool is used for conversion.
  <br>[![Last commit](https://img.shields.io/github/last-commit/mercure-imaging/mercure-dcm2bids?style=plastic)](https://github.com/mercure-imaging/mercure-dcm2bids)[![Docker version](https://img.shields.io/docker/pulls/mercureimaging/mercure-dcm2bids.svg?style=plastic)](https://hub.docker.com/r/mercureimaging/mercure-dcm2bids)[![License: GPL-3.0](https://img.shields.io/badge/License-GPLv3-blue.svg?style=plastic)](https://www.gnu.org/licenses/gpl-3.0)
- <img src='./images/logo_python.png' width='14px'>  [niix2bids](https://github.com/benoitberanger/niix2bids): Use this package as a command line to organize your Nifti dataset into BIDS.
  <br>[![Last commit](https://img.shields.io/github/last-commit/benoitberanger/niix2bids?style=plastic)](https://github.com/benoitberanger/niix2bids)[![License: GPL-3.0](https://img.shields.io/badge/License-GPLv3-blue.svg?style=plastic)](https://www.gnu.org/licenses/gpl-3.0)
-  [OpenfMRI2BIDS](https://github.com/bids-standard/openfmri2bids): Convert OpenfMRI dataset to BIDS
  <br>[![Last commit](https://img.shields.io/github/last-commit/bids-standard/openfmri2bids?style=plastic)](https://github.com/bids-standard/openfmri2bids)
- <img src='./images/logo_matlab.png' width='17px'> <img src='./images/logo_python.png' width='14px'>  [PET2BIDS](https://github.com/openneuropet/PET2BIDS): Helps you convert your PET data! raw PET scanner files (for example ecat, dicom) and additional side file like excel sheets.
  <br>[![Last commit](https://img.shields.io/github/last-commit/openneuropet/PET2BIDS?style=plastic)](https://github.com/openneuropet/PET2BIDS)[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=plastic)](https://opensource.org/licenses/MIT)
- <img src='./images/logo_python.png' width='14px'>  [ReproIn](https://github.com/ReproNim/reproin): HeuDiConv-based turnkey solution: a setup for automatic generation of shareable, version-controlled BIDS datasets from MR scanners.
  <br>[![Last commit](https://img.shields.io/github/last-commit/ReproNim/reproin?style=plastic)](https://github.com/ReproNim/reproin)[![Docker version](https://img.shields.io/docker/pulls/repronim/reproin.svg?style=plastic)](https://hub.docker.com/r/repronim/reproin)[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=plastic)](https://opensource.org/licenses/MIT)
- <img src='./images/logo_python.png' width='14px'>  [SAMRI](https://doi.org/10.3389/fninf.2020.00005): Full stack Small Animal MRI data analysis package, including the `bru2bids` repositing pipeline, which can convert Bruker archives to the BIDS format. From the ETH and University of Zurich, with collaboration from MIT and Dartmouth College.
  <br>![](https://img.shields.io/badge/shell-black.svg?style=plastic)[![Last commit](https://img.shields.io/github/last-commit/IBT-FMI/SAMRI?style=plastic)](https://github.com/IBT-FMI/SAMRI)
-  [XNAT2BIDS](https://github.com/kamillipi/2bids): Simple xnat pipeline to convert DICOM scans to BIDS-compatible output (nii+json).
  <br>![](https://img.shields.io/badge/shell-black.svg?style=plastic)[![Last commit](https://img.shields.io/github/last-commit/kamillipi/2bids?style=plastic)](https://github.com/kamillipi/2bids)

### MEEG

- <img src='./images/logo_python.png' width='14px'>  [BIDSme](https://gitlab.uliege.be/CyclotronResearchCentre/Public/bidstools/bidsme/bidsme_example/-/tree/master/example1):
  <br>[![Last commit](https://img.shields.io/github/last-commit/nbeliy/bidsme?style=plastic)](https://github.com/nbeliy/bidsme)[![License: GPL-2.0](https://img.shields.io/badge/License-GPLv2-blue.svg?style=plastic)](https://www.gnu.org/licenses/gpl-2.0)
- <img src='./images/logo_python.png' width='14px'>  [Biscuit](https://macquarie-meg-research.github.io/Biscuit/): GUI for easy MEG to BIDS conversion
  <br>[![Last commit](https://img.shields.io/github/last-commit/Macquarie-MEG-Research/Biscuit?style=plastic)](https://github.com/Macquarie-MEG-Research/Biscuit)[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=plastic)](https://opensource.org/licenses/MIT)
- <img src='./images/logo_python.png' width='14px'>  [EEG2BIDS](None): A tool for converting raw EEG and iEEG data into the BIDS standard data structure, prepared for LORIS (Longitudinal Online Research and Imaging System).
  <br>![](https://img.shields.io/badge/Javascript-yellow.svg?style=plastic)[![Last commit](https://img.shields.io/github/last-commit/aces/EEG2BIDS?style=plastic)](https://github.com/aces/EEG2BIDS)
- <img src='./images/logo_matlab.png' width='17px'>  [EEGLAB](https://eeglab.org/tutorials/04_Import/BIDS.html): <a href='https://github.com/arnodelorme/bids-MATLAB-tools'>See plugins</a>
  <br>[![Last commit](https://img.shields.io/github/last-commit/sccn/eeglab?style=plastic)](https://github.com/sccn/eeglab)
- <img src='./images/logo_matlab.png' width='17px'>  [FieldTrip - data2bids](https://www.fieldtriptoolbox.org/example/bids/):
  <br>[![Last commit](https://img.shields.io/github/last-commit/fieldtrip/fieldtrip?style=plastic)](https://github.com/fieldtrip/fieldtrip)[![License: GPL-3.0](https://img.shields.io/badge/License-GPLv3-blue.svg?style=plastic)](https://www.gnu.org/licenses/gpl-3.0)
- <img src='./images/logo_python.png' width='14px'>  [MNE-BIDS](https://mne.tools/mne-bids): MNE-BIDS is a Python package that allows you to read and write BIDS-compatible datasets with the help of MNE-Python.
  <br>[![Last commit](https://img.shields.io/github/last-commit/mne-tools/mne-bids?style=plastic)](https://github.com/mne-tools/mne-bids)[![PyPI version](https://badge.fury.io/py/mne-bids.svg)](https://pypi.org/project/mne-bids)[![License: BSD-3-Clause](https://img.shields.io/badge/License-BSD_3--Clause-blue.svg?style=plastic)](https://opensource.org/licenses/BSD-3-Clause)
- <img src='./images/logo_python.png' width='14px'>  [sovabids](https://sovabids.readthedocs.io/en/latest/): A Python package for the automatic conversion of EEG datasets to the BIDS standard, with a focus on making the most out of metadata.
  <br>[![Last commit](https://img.shields.io/github/last-commit/yjmantilla/sovabids?style=plastic)](https://github.com/yjmantilla/sovabids)

### physiological

- <img src='./images/logo_python.png' width='14px'>  [BIDScoin](https://bidscoin.readthedocs.io/en/stable/): BIDScoin converts your source-level neuroimaging data to BIDS
  <br>[![Last commit](https://img.shields.io/github/last-commit/Donders-Institute/bidscoin?style=plastic)](https://github.com/Donders-Institute/bidscoin)[![PyPI version](https://badge.fury.io/py/bidscoin.svg)](https://pypi.org/project/bidscoin)
- <img src='./images/logo_python.png' width='14px'>  [bidsphysio](None): Converts physio data (CMRR, AcqKnowledge, Siemens PMU) to BIDS physiological recording
  <br>[![Last commit](https://img.shields.io/github/last-commit/cbinyu/bidsphysio?style=plastic)](https://github.com/cbinyu/bidsphysio)[![PyPI version](https://badge.fury.io/py/bidsphysio.svg)](https://pypi.org/project/bidsphysio/)[![Docker version](https://img.shields.io/docker/pulls/cbinyu/bidsphysio.svg?style=plastic)](https://hub.docker.com/r/cbinyu/bidsphysio/)
- <img src='./images/logo_python.png' width='14px'>  [phys2bids](https://phys2bids.readthedocs.io/en/latest/): Python3 library to format physiological files in BIDS.
  <br>[![Last commit](https://img.shields.io/github/last-commit/physiopy/phys2bids?style=plastic)](https://github.com/physiopy/phys2bids)[![PyPI version](https://badge.fury.io/py/phys2bids.svg)](https://pypi.org/project/phys2bids)

### others

- <img src='./images/logo_python.png' width='14px'>  [convert-eprime](https://github.com/tsalo/convert-eprime): Python functions to convert E-Prime files to csvs. Not currently being developed.
  <br>[![Last commit](https://img.shields.io/github/last-commit/tsalo/convert-eprime?style=plastic)](https://github.com/tsalo/convert-eprime)[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=plastic)](https://opensource.org/licenses/MIT)
-  [DCM2NIIx](https://github.com/neurolabusc/dcm2niix): dcm2nii DICOM to NIfTI converter
  <br>[![Last commit](https://img.shields.io/github/last-commit/neurolabusc/dcm2niix?style=plastic)](https://github.com/neurolabusc/dcm2niix)
- <img src='./images/logo_matlab.png' width='17px'>  [DICM2NII](https://github.com/xiangruili/dicm2nii): dcm2nii DICOM to NIfTI converter
  <br>[![Last commit](https://img.shields.io/github/last-commit/xiangruili/dicm2nii?style=plastic)](https://github.com/xiangruili/dicm2nii)
- <img src='./images/logo_python.png' width='14px'>  [sim2bids](https://github.com/dissagaliyeva/sim2bids): GUI to easily convert simulation results to BIDS format, according to <a herf="https://bids.neuroimaging.io/bep034" target="_blank">   BEP 34 </a>.
  <br>[![Last commit](https://img.shields.io/github/last-commit/dissagaliyeva/sim2bids?style=plastic)](https://github.com/dissagaliyeva/sim2bids)[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=plastic)](https://opensource.org/licenses/MIT)
<!-- Converters ends -->

## Validation

Make sure you use to validate any BIDS dataset you are working with.

You can [use it in a browser](https://bids-standard.github.io/bids-validator/)
or [install the package](https://github.com/bids-standard/bids-validator#quickstart)
and use it as a command line tool.

## BIDS Apps

BIDS apps are containerized tools to automatically process BIDS datasets.
For more information check the [BIDS Apps website](https://bids-apps.neuroimaging.io/apps/).

<!-- APP starts -->
- [aa](https://github.com/bids-apps/aa): BIDS App containing an instance of the Automatic Analysis
  <br>[![Docker version](https://img.shields.io/docker/pulls/bids/aa.svg?style=plastic)](https://hub.docker.com/r/bids/aa)
- [afni_proc](https://github.com/bids-apps/afni_proc): prototype AFNI bids app implementing participant level preprocessing with afni_proc.py
  <br>[![Docker version](https://img.shields.io/docker/pulls/bids/afni_proc.svg?style=plastic)](https://hub.docker.com/r/bids/afni_proc)
- [antsCorticalThickness](https://github.com/bids-apps/antsCorticalThickness): BIDS App for calculating cortical thickness using ANTs
  <br>[![Docker version](https://img.shields.io/docker/pulls/bids/antscorticalthickness.svg?style=plastic)](https://hub.docker.com/r/bids/antscorticalthickness)
- [baracus](https://github.com/bids-apps/baracus): Predicts brain age, based on data from Freesurfer 5.3
  <br>[![Docker version](https://img.shields.io/docker/pulls/bids/baracus.svg?style=plastic)](https://hub.docker.com/r/bids/baracus)
- [brainiak-srm](https://github.com/bids-apps/brainiak-srm): This is the BIDS-app version of the Shared Response Model (SRM) of BrainIAK
  <br>[![Docker version](https://img.shields.io/docker/pulls/bids/brainiak-srm.svg?style=plastic)](https://hub.docker.com/r/bids/brainiak-srm)
- [BrainSuite](https://github.com/bids-apps/BrainSuite): BrainSuite's structural, diffusion, and functional MRI processing pipelines with QC functionalities.
  <br>[![Docker version](https://img.shields.io/docker/pulls/bids/brainsuite.svg?style=plastic)](https://hub.docker.com/r/bids/brainsuite)
- [BROCCOLI](https://github.com/bids-apps/BROCCOLI): BIDS App for BROCCOLI
  <br>[![Docker version](https://img.shields.io/docker/pulls/bids/broccoli.svg?style=plastic)](https://hub.docker.com/r/bids/broccoli)
- [CPAC](https://github.com/bids-apps/CPAC): BIDS Application for the Configurable Pipeline for the Analysis of Connectomes (C-PAC)
  <br>[![Docker version](https://img.shields.io/docker/pulls/bids/cpac.svg?style=plastic)](https://hub.docker.com/r/bids/cpac)
- [DPARSF](https://github.com/bids-apps/DPARSF): Docker version of DPARSF, also deployed at OpenNeuro.org
  <br>[![Docker version](https://img.shields.io/docker/pulls/bids/dparsf.svg?style=plastic)](https://hub.docker.com/r/bids/dparsf)
- [freesurfer](https://github.com/bids-apps/freesurfer): BIDS app wrapping recon-all from FreeSurfer
  <br>[![Docker version](https://img.shields.io/docker/pulls/bids/freesurfer.svg?style=plastic)](https://hub.docker.com/r/bids/freesurfer)
- [HCPPipelines](https://github.com/bids-apps/HCPPipelines): A BIDS App for minimal preprocessing using the HCP Pipelines
  <br>[![Docker version](https://img.shields.io/docker/pulls/bids/hcppipelines.svg?style=plastic)](https://hub.docker.com/r/bids/hcppipelines)
- [hyperalignment](https://github.com/bids-apps/hyperalignment): Hyperalignment is a functional alignment method that aligns subjects' brain data in a high-dimensional space of voxels/features.
  <br>[![Docker version](https://img.shields.io/docker/pulls/bids/hyperalignment.svg?style=plastic)](https://hub.docker.com/r/bids/hyperalignment)
- [mindboggle](https://github.com/bids-apps/mindboggle): Improve the accuracy, precision, and consistency of automated labeling and shape analysis of human brain image data
  <br>[![Docker version](https://img.shields.io/docker/pulls/bids/mindboggle.svg?style=plastic)](https://hub.docker.com/r/bids/mindboggle)
- [MRtrix3_connectome](https://github.com/bids-apps/MRtrix3_connectome): Generate subject connectomes from raw BIDS data & perform inter-subject connection density normalisation, using  the MRtrix3 software package.
  <br>[![Docker version](https://img.shields.io/docker/pulls/bids/mrtrix3_connectome.svg?style=plastic)](https://hub.docker.com/r/bids/mrtrix3_connectome)
- [ndmg](https://github.com/bids-apps/ndmg): BIDS app for NeuroData's MRI to Graphs pipeline
  <br>[![Docker version](https://img.shields.io/docker/pulls/bids/ndmg.svg?style=plastic)](https://hub.docker.com/r/bids/ndmg)
- [nipypelines](https://github.com/bids-apps/nipypelines): Preprocess functional tasks in a BIDS dataset.
  <br>[![Docker version](https://img.shields.io/docker/pulls/bids/nipypelines.svg?style=plastic)](https://hub.docker.com/r/bids/nipypelines)
- [oppni](https://github.com/bids-apps/oppni): runs fast optimization of preprocessing pipelines for BOLD fMRI
  <br>[![Docker version](https://img.shields.io/docker/pulls/bids/oppni.svg?style=plastic)](https://hub.docker.com/r/bids/oppni)
- [PyMVPA](https://github.com/bids-apps/PyMVPA): runs MVPA and RSA analysis BIDS bold derivative data
  <br>[![Docker version](https://img.shields.io/docker/pulls/bids/pymvpa.svg?style=plastic)](https://hub.docker.com/r/bids/pymvpa)
- [QAP](https://github.com/bids-apps/QAP): PCP Quality Assessment Protocol
  <br>[![Docker version](https://img.shields.io/docker/pulls/bids/qap.svg?style=plastic)](https://hub.docker.com/r/bids/qap)
- [rs_signal_extract](https://github.com/bids-apps/rs_signal_extract): BIDS App for resting state signal extraction using nilearn.
  <br>[![Docker version](https://img.shields.io/docker/pulls/bids/rs_signal_extract.svg?style=plastic)](https://hub.docker.com/r/bids/rs_signal_extract)
- [rsHRF](https://github.com/bids-apps/rsHRF): Resting state HRF estimation from BOLD-fMRI signal
  <br>[![Docker version](https://img.shields.io/docker/pulls/bids/rshrf.svg?style=plastic)](https://hub.docker.com/r/bids/rshrf)
- [SPM](https://github.com/bids-apps/SPM): BIDS App containing an instance of the SPM software.
  <br>[![Docker version](https://img.shields.io/docker/pulls/bids/spm.svg?style=plastic)](https://hub.docker.com/r/bids/spm)
- [tracula](https://github.com/bids-apps/tracula): implements Freesurfer's TRACULA (TRActs Constrained by UnderLying Anatomy) tool for cross-sectional as well as longitudinal (multi session) input data.
  <br>[![Docker version](https://img.shields.io/docker/pulls/bids/tracula.svg?style=plastic)](https://hub.docker.com/r/bids/tracula)
- [connectomemapper3](https://github.com/connectomicslab/connectomemapper3): Connectome Mapper 3 is a BIDS App that implements full anatomical, diffusion, resting/state functional MRI, and recently EEG processing pipelines, from raw T1 / DWI / BOLD , and preprocessed EEG data to multi-resolution brain parcellation with corresponding connection matrices.
  <br>[![Docker version](https://img.shields.io/docker/pulls/sebastientourbier/connectomemapper-bidsapp.svg?style=plastic)](https://hub.docker.com/r/sebastientourbier/connectomemapper-bidsapp)
- [bidsMReye](https://github.com/cpp-lln-lab/bidsMReye): BIDS app using deepMReye to decode eye motion for fMRI time series data.
  <br>[![Docker version](https://img.shields.io/docker/pulls/cpplab/bidsmreye.svg?style=plastic)](https://hub.docker.com/r/cpplab/bidsmreye)
- [bidspm](https://github.com/cpp-lln-lab/bidspm): an SPM centric BIDS app
  <br>[![Docker version](https://img.shields.io/docker/pulls/cpplab/bidspm.svg?style=plastic)](https://hub.docker.com/r/cpplab/bidspm)
- [fmriprep-fake](https://github.com/djarecka/fmriprep-fake): None
  <br>[![Docker version](https://img.shields.io/docker/pulls/djarecka/fmriprep_fake.svg?style=plastic)](https://hub.docker.com/r/djarecka/fmriprep_fake)
- [funcmasker-flex](https://github.com/khanlab/funcmasker-flex): BIDS App for U-net brain masking of fetal bold MRI
  <br>[![Docker version](https://img.shields.io/docker/pulls/khanlab/funcmasker-flex.svg?style=plastic)](https://hub.docker.com/r/khanlab/funcmasker-flex)
- [hippunfold](https://github.com/khanlab/hippunfold): BIDS App for Hippunfold (automated hippocampal unfolding and subfield segmentation)
  <br>[![Docker version](https://img.shields.io/docker/pulls/khanlab/hippunfold.svg?style=plastic)](https://hub.docker.com/r/khanlab/hippunfold)
- [mialsuperresolutiontoolkit](https://github.com/Medical-Image-Analysis-Laboratory/mialsuperresolutiontoolkit): The Medical Image Analysis Laboratory Super-Resolution ToolKit (MIALSRTK) consists of a set of C++ and Python processing and workflow tools necessary to perform motion-robust super-resolution fetal MRI reconstruction in the BIDS Apps framework.
  <br>[![Docker version](https://img.shields.io/docker/pulls/sebastientourbier/mialsuperresolutiontoolkit.svg?style=plastic)](https://hub.docker.com/r/sebastientourbier/mialsuperresolutiontoolkit)
- [micapipe](https://github.com/MICA-MNI/micapipe): micapipe from the Multimodal imaging and connectome analysis lab (http://mica-mni.github.io) at the Montreal Neurological Institute. Read The Docs documentation below
  <br>[![Docker version](https://img.shields.io/docker/pulls/micalab/micapipe.svg?style=plastic)](https://hub.docker.com/r/micalab/micapipe)
- [dmriprep](https://github.com/nipreps/dmriprep): dMRIPrep is a robust and easy-to-use pipeline for preprocessing of diverse dMRI data. The transparent workflow dispenses of manual intervention, thereby ensuring the reproducibility of the results.
  <br>[![Docker version](https://img.shields.io/docker/pulls/nipreps/dmriprep.svg?style=plastic)](https://hub.docker.com/r/nipreps/dmriprep)
- [fmriprep](https://github.com/nipreps/fmriprep): fMRIPrep is a robust and easy-to-use pipeline for preprocessing of diverse fMRI data. The transparent workflow dispenses of manual intervention, thereby ensuring the reproducibility of the results.
  <br>[![Docker version](https://img.shields.io/docker/pulls/nipreps/fmriprep.svg?style=plastic)](https://hub.docker.com/r/nipreps/fmriprep)
- [mriqc](https://github.com/nipreps/mriqc): Automated Quality Control and visual reports for Quality Assessment of structural (T1w, T2w) and functional MRI of the brain
  <br>[![Docker version](https://img.shields.io/docker/pulls/nipreps/mriqc.svg?style=plastic)](https://hub.docker.com/r/nipreps/mriqc)
- [nibabies](https://github.com/nipreps/nibabies): Processing tools for magnetic resonance images of infant brains
  <br>[![Docker version](https://img.shields.io/docker/pulls/nipreps/nibabies.svg?style=plastic)](https://hub.docker.com/r/nipreps/nibabies)
- [nirodents](https://github.com/nipreps/nirodents): None
  <br>[![Docker version](https://img.shields.io/docker/pulls/nipreps/nirodents.svg?style=plastic)](https://hub.docker.com/r/nipreps/nirodents)
- [smriprep](https://github.com/nipreps/smriprep): Structural MRI PREProcessing (sMRIPrep) workflows for NIPreps (NeuroImaging PREProcessing tools)
  <br>[![Docker version](https://img.shields.io/docker/pulls/nipreps/smriprep.svg?style=plastic)](https://hub.docker.com/r/nipreps/smriprep)
- [BIDSonym](https://github.com/PeerHerholz/BIDSonym): a BIDS app for pseudo-anonymization of neuroimaging data
  <br>[![Docker version](https://img.shields.io/docker/pulls/peerherholz/bidsonym.svg?style=plastic)](https://hub.docker.com/r/peerherholz/bidsonym)
- [aslprep](https://github.com/PennLINC/aslprep): Preprocessing of arterial spin labeling data
  <br>[![Docker version](https://img.shields.io/docker/pulls/pennlinc/aslprep.svg?style=plastic)](https://hub.docker.com/r/pennlinc/aslprep)
- [qsiprep](https://github.com/PennLINC/qsiprep): Preprocessing and reconstruction of diffusion MRI
  <br>[![Docker version](https://img.shields.io/docker/pulls/pennbbl/qsiprep.svg?style=plastic)](https://hub.docker.com/r/pennbbl/qsiprep)
- [xcp_d](https://github.com/PennLINC/xcp_d): Post-processing of fMRIPrep, nibabies, HCP, and DCAN BOLD derivatives for functional connectivity analysis
  <br>[![Docker version](https://img.shields.io/docker/pulls/pennlinc/xcp_d.svg?style=plastic)](https://hub.docker.com/r/pennlinc/xcp_d)
- [fitlins](https://github.com/poldracklab/fitlins): Fit Linear Models to BIDS Datasets
  <br>[![Docker version](https://img.shields.io/docker/pulls/poldracklab/fitlins.svg?style=plastic)](https://hub.docker.com/r/poldracklab/fitlins)
- [multiscalebrainparcellator](https://github.com/sebastientourbier/multiscalebrainparcellator): Multi-Scale Brain Parcellator, part of the Connectome Mapping Toolkit (CMTK), is a BIDS App that implements a full anatomical MRI processing pipeline, from raw T1w data to structural brain parcellation at five different scales.
  <br>[![Docker version](https://img.shields.io/docker/pulls/sebastientourbier/multiscalebrainparcellator.svg?style=plastic)](https://hub.docker.com/r/sebastientourbier/multiscalebrainparcellator)
- [gift-bids](https://github.com/trendscenter/gift-bids): None
  <br>[![Docker version](https://img.shields.io/docker/pulls/trends/gift-bids.svg?style=plastic)](https://hub.docker.com/r/trends/gift-bids)
<!-- APP ends -->

## Tools

Software packages for working with BIDS datasets.

<!-- TOOLS starts -->
- <img src='./images/logo_python.png' width='14px'> [babs](https://pennlinc-babs.readthedocs.io/): BIDS App Bootstrap (BABS) is a reproducible, generalizable, and scalable Python package for BIDS App analysis of large datasets. It uses DataLad and adopts FAIRly big framework.
  <br>[![Last commit](https://img.shields.io/github/last-commit/PennLINC/babs?style=plastic)](https://github.com/PennLINC/babs) [![PyPI version](https://badge.fury.io/py/babs.svg)](https://pypi.org/project/babs/)
- <img src='./images/logo_python.png' width='14px'> [bids stats model](https://bids-standard.github.io/stats-models/index.html): Validate BIDS statistical model. To learn more the [BIDS stats model website](https://bids-standard.github.io/stats-models/index.html)
  <br> [![PyPI version](https://badge.fury.io/py/bsmschema.svg)](https://pypi.org/project/bsmschema/)
- <img src='./images/logo_python.png' width='14px'> [bids-cfood](https://gitlab.indiscale.com/caosdb/src/crawler-cfoods/bids-cfood): a module to handle BIDS dataset for the caosDB data crawler
- <img src='./images/logo_matlab.png' width='17px'> <img src='./images/logo_octave.png' width='16px'> [bids-matlab](https://github.com/bids-standard/bids-matlab): MATLAB/Octave tools to interact with datasets conforming to the BIDS format
  <br>[![Last commit](https://img.shields.io/github/last-commit/bids-standard/bids-matlab?style=plastic)](https://github.com/bids-standard/bids-matlab)
- <img src='./images/logo_python.png' width='14px'> [BIDS-pydantic](https://github.com/gold-standard-phantoms/bids-pydantic): Pulls a specified version of the BIDS schema and creates corresponding Pydantic models, which will provide BIDS data validation using Python type annotations. See also [BIDS-pydantic-models](https://pypi.org/project/BIDS-pydantic-models/).
  <br>[![Last commit](https://img.shields.io/github/last-commit/gold-standard-phantoms/bids-pydantic?style=plastic)](https://github.com/gold-standard-phantoms/bids-pydantic) [![PyPI version](https://badge.fury.io/py/BIDS-pydantic.svg)](https://pypi.org/project/BIDS-pydantic/)
- <img src='./images/logo_python.png' width='14px'> [bids2cite](https://github.com/Remi-Gau/bids2cite): package to interactively update `dataset_description.json` and generate citation files (for example `datacite.yml`) for BIDS datasets.
  <br>[![Last commit](https://img.shields.io/github/last-commit/Remi-Gau/bids2cite?style=plastic)](https://github.com/Remi-Gau/bids2cite)
- <img src='./images/logo_R.png' width='18px'> [bidser](https://bbuchsbaum.github.io/bidser/): Working with Brain Imaging Data Structure in R
  <br>[![Last commit](https://img.shields.io/github/last-commit/bbuchsbaum/bidser?style=plastic)](https://github.com/bbuchsbaum/bidser)
- <img src='./images/logo_python.png' width='14px'> [BIDSHandler](https://github.com/Macquarie-MEG-Research/BIDSHandler): Python module allowing complete manipulation of BIDS data
  <br>[![Last commit](https://img.shields.io/github/last-commit/Macquarie-MEG-Research/BIDSHandler?style=plastic)](https://github.com/Macquarie-MEG-Research/BIDSHandler)
- <img src='./images/logo_matlab.png' width='17px'> [Brainstorm](http://neuroimage.usc.edu/brainstorm/): MEG/EEG analysis package
- <img src='./images/logo_python.png' width='14px'> [clpipe](https://clpipe.readthedocs.io/en/latest/index.html): streamlined processing pipeline for MRI data centered around BIDS
  <br>[![Last commit](https://img.shields.io/github/last-commit/cohenlabUNC/clpipe?style=plastic)](https://github.com/cohenlabUNC/clpipe)
- <img src='./images/logo_python.png' width='14px'> [cuBIDS](https://cubids.readthedocs.io/en/latest/): a Python package designed to facilitate reproducible curation of neuroimaging BIDS datasets
  <br>[![Last commit](https://img.shields.io/github/last-commit/pennlinc/cubids?style=plastic)](https://github.com/pennlinc/cubids) [![PyPI version](https://badge.fury.io/py/cubids.svg)](https://pypi.org/project/cubids/)
- <img src='./images/logo_python.png' width='14px'> [File mapper](https://github.com/DCAN-Labs/file-mapper): An easy tool to copy/move/symlink files from one directory to the other! Can be used to "convert" dataset to be BIDS compliant.
  <br>[![Last commit](https://img.shields.io/github/last-commit/DCAN-Labs/file-mapper?style=plastic)](https://github.com/DCAN-Labs/file-mapper)
- <img src='./images/logo_python.png' width='14px'> [GUI dataset description generator](None): GUI form that generates `dataset_description.json`
  <br>[![Last commit](https://img.shields.io/github/last-commit/tolik-g/BIDS?style=plastic)](https://github.com/tolik-g/BIDS)
- [Hierarchical Event Descriptors (HED) online tools](https://www.hed-resources.org): Online tools for annotation, validation, summary, and assembly of event file contents and annotations.
- [Hierarchical Event Descriptors (HED) python tools](https://www.hed-resources.org): HED libraries supporting schema development as well as annotation, validation, and analysis.
  <br>[![Last commit](https://img.shields.io/github/last-commit/hed-standard/hed-python?style=plastic)](https://github.com/hed-standard/hed-python) [![PyPI version](https://badge.fury.io/py/hedtools.svg)](https://pypi.org/project/hedtools/)
- <img src='./images/logo_matlab.png' width='17px'> [Lead-DBS](https://www.lead-dbs.org/): A toolbox facilitating Deep Brain Stimulation electrode reconstructions  and computer simulations supports BIDS conversion and ingestion of BIDS datasets.
- <img src='./images/logo_python.png' width='14px'> [mne-bids](https://mne.tools/mne-bids/stable/index.html): collection of tools for converting magnetoencephalography (MEG) data into BIDS format, as well as some helper functions for creating the folders and metadata needed for a BIDS dataset.
  <br>[![Last commit](https://img.shields.io/github/last-commit/mne-tools/mne-bids?style=plastic)](https://github.com/mne-tools/mne-bids)
- [neurobagel annotate](https://neurobagel.org/data_prep/): This tool allows you to create a machine readable data dictionary in .json format for a tabular phenotypic file in .tsv format ("Data table").
- [neurobagel query](https://neurobagel.org/query_tool/): Neurobagel's query tool is a web interface for searching across a BIDS datasets based on various subject clinical-demographic and imaging parameters.
- <img src='./images/logo_python.png' width='14px'> [nipopy](https://neurobagel.org/nipoppy/overview/): Lightweight neuroimaging workflow manager to help with DICOM to BIDS conversion and running BIDS apps.
  <br>[![Last commit](https://img.shields.io/github/last-commit/neurodatascience/nipoppy?style=plastic)](https://github.com/neurodatascience/nipoppy)
- [OpenNeuro](http://openneuro.org): A free and open platform for validating and sharing BIDS-compliant data.
- [PRFmodel](https://github.com/vistalab/PRFmodel/wiki): a set of tools to fit population receptive field models to BIDS datasets
  <br>[![Last commit](https://img.shields.io/github/last-commit/vistalab/PRFmodel?style=plastic)](https://github.com/vistalab/PRFmodel)
- <img src='./images/logo_python.png' width='14px'> [PyBIDS](None): Python package to quickly parse / search the components of a BIDS dataset. It also contains functionality for running analyses on your data.
  <br>[![Last commit](https://img.shields.io/github/last-commit/bids-standard/pybids?style=plastic)](https://github.com/bids-standard/pybids) [![PyPI version](https://badge.fury.io/py/pybids.svg)](https://pypi.org/project/pybids/)
- <img src='./images/logo_R.png' width='18px'> [rbids](https://github.com/mathesong/rbids): aims to make BIDS datasets more easily accessible for packages written in R
  <br>[![Last commit](https://img.shields.io/github/last-commit/mathesong/rbids?style=plastic)](https://github.com/mathesong/rbids)
- <img src='./images/logo_matlab.png' width='17px'> <img src='./images/logo_octave.png' width='16px'> [spm_2_bids](https://spm-2-bids.readthedocs.io/en/latest/): a tool convert SPM preprocessed output to BIDS derivatives (trying to follow [BEP12](https://bids.neuroimaging.io/bep012))
  <br>[![Last commit](https://img.shields.io/github/last-commit/cpp-lln-lab/spm_2_bids?style=plastic)](https://github.com/cpp-lln-lab/spm_2_bids)
<!-- TOOLS ends -->

## Code

Most of the repositories for BIDS are centralized in:

- the [BIDS standard github organization](https://github.com/bids-standard)
- the [BIDS-app github organization](https://github.com/bids-apps)

Make sure to also check repositories tagged for the following topics:

- on GitHub:

  - [BIDS](https://github.com/topics/bids)
  - [BIDS-Apps](https://github.com/topics/bidsapp)
  - [bids-format](https://github.com/topics/bids-format)

- on GitLab:

  - [BIDS](https://gitlab.com/search?search=bids&nav_source=navbar)

## BIDS Extension Proposals (BEP)

Ongoing community proposals for extending the BIDS specification to new datatypes ([raw](#raw)),
to specify how to organized processed data ([derivatives](#derivatives)),
or interoperating with BIDS datasets.

Make sure to check the list to see if some people are not already working
on making sure BIDS supports your favorite datatype.

If you are working on an extension proposal
make sure to check our [documentation regarding the BIDS extension proposal process](https://bids-extensions.readthedocs.io/).

<!-- BEP starts -->

### raw

- [BEP004](https://bids.neuroimaging.io/bep004): Susceptibility Weighted Imaging (SWI)
- [BEP020](https://bids.neuroimaging.io/bep020): Eye Tracking including Gaze Position and Pupil Size
- [BEP022](https://bids.neuroimaging.io/bep022): Magnetic Resonance Spectroscopy (MRS)
- [BEP024](https://bids.neuroimaging.io/bep024): Computed Tomography scan (CT)
- [BEP026](https://bids.neuroimaging.io/bep026): Microelectrode Recordings
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
- [BEP041](https://bids.neuroimaging.io/bep041): Statistical Model Derivatives
<!-- BEP ends -->

## Publications

BIDS references are centralized in [our zotero group](https://www.zotero.org/groups/5111637/bids).

## Contribute

Contributions welcome! Read the [contribution guidelines](contributing.md) first.
