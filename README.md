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
  [mattermost](https://mattermost.brainhack.org) is the open source equivalent of slack
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

- The [BIDS examples](https://bids-standard.github.io/bids-examples/) repository hosts dataset of each modality
  with empty raw data files. These datasets can be useful to:
  - serve as an example on how a BIDS dataset can be structured
  - write lightweight software tests
- [OpenNeuro](https://openneuro.org/) host more than 1000 open BIDS datasets of all datatypes.

## Converters

Tools for converting data to/from BIDS from other standard or custom formats and layouts.

<!-- Converters starts -->

### ASL

- <img src='./images/logo_matlab.png' width='17px'>  [Explore ASL](https://exploreasl.github.io/Documentation/1.8.0/Tutorials-ASL-BIDS/): Convert DICOM and NIFTI data to the ASL-BIDS format.
  <br>[![Last commit](https://img.shields.io/github/last-commit/ExploreASL/ExploreASL?style=plastic)](https://github.com/ExploreASL/ExploreASL)
- <img src='./images/logo_python.png' width='14px'>  [ezBIDS](https://brainlife.io/docs/using_ezBIDS/): A web-based BIDS conversion tool with four unique features: (1) No installation or programming requirements. (2) Handling of both imaging and task events data and metadata. (3) Semi-automated inference and guidance for adherence to BIDS. (4) Multiple data management options, including download BIDS data to local system, or transfer to OpenNeuro.org or to brainlife.io.
  <br>![](https://img.shields.io/badge/Javascript-yellow.svg?style=plastic)![](https://img.shields.io/badge/shell-black.svg?style=plastic)[![Last commit](https://img.shields.io/github/last-commit/brainlife/ezbids?style=plastic)](https://github.com/brainlife/ezbids)

### BIDS

- <img src='./images/logo_python.png' width='14px'>  [BIDS2ISATab](https://github.com/bids-standard/BIDS2ISATab): Extract ISA-Tab compatible metadata from BIDS
  <br>[![Last commit](https://img.shields.io/github/last-commit/bids-standard/BIDS2ISATab?style=plastic)](https://github.com/bids-standard/BIDS2ISATab)
- <img src='./images/logo_python.png' width='14px'>  [BIDS2NDA](https://github.com/bids-standard/BIDS2NDA): Extract NIHM Data Archive compatible metadata from BIDS
  <br>[![Last commit](https://img.shields.io/github/last-commit/bids-standard/BIDS2NDA?style=plastic)](https://github.com/bids-standard/BIDS2NDA)
- <img src='./images/logo_python.png' width='14px'>  [bids2xar - for XNAT import](https://github.com/lwallace23/bids2xar): Convert BIDS data set into XNAT XAR bundles
  <br>[![Last commit](https://img.shields.io/github/last-commit/lwallace23/bids2xar?style=plastic)](https://github.com/lwallace23/bids2xar)

### EEG

- <img src='./images/logo_python.png' width='14px'>  [BIDSme](https://gitlab.uliege.be/CyclotronResearchCentre/Public/bidstools/bidsme/bidsme_example/-/tree/master/example1):
  <br>[![Last commit](https://img.shields.io/github/last-commit/nbeliy/bidsme?style=plastic)](https://github.com/nbeliy/bidsme)
- <img src='./images/logo_python.png' width='14px'>  [EEG2BIDS](https://github.com/aces/EEG2BIDS): A tool for converting raw EEG and iEEG data into the BIDS standard data structure, prepared for LORIS (Longitudinal Online Research and Imaging System).
  <br>![](https://img.shields.io/badge/Javascript-yellow.svg?style=plastic)[![Last commit](https://img.shields.io/github/last-commit/aces/EEG2BIDS?style=plastic)](https://github.com/aces/EEG2BIDS)
- <img src='./images/logo_matlab.png' width='17px'>  [EEGLAB](https://eeglab.org/tutorials/04_Import/BIDS.html): <a href='https://github.com/arnodelorme/bids-MATLAB-tools'>See plugins</a>
  <br>[![Last commit](https://img.shields.io/github/last-commit/sccn/eeglab?style=plastic)](https://github.com/sccn/eeglab)
- <img src='./images/logo_matlab.png' width='17px'>  [FieldTrip - data2bids](https://www.fieldtriptoolbox.org/example/bids/):
  <br>[![Last commit](https://img.shields.io/github/last-commit/fieldtrip/fieldtrip?style=plastic)](https://github.com/fieldtrip/fieldtrip)
- <img src='./images/logo_python.png' width='14px'>  [MNE-BIDS](https://mne.tools/mne-bids): MNE-BIDS is a Python package that allows you to read and write BIDS-compatible datasets with the help of MNE-Python.
  <br>[![Last commit](https://img.shields.io/github/last-commit/mne-tools/mne-bids?style=plastic)](https://github.com/mne-tools/mne-bids)[![PyPI version](https://badge.fury.io/py/mne-bids.svg)](https://pypi.org/project/mne-bids)
- <img src='./images/logo_python.png' width='14px'>  [sovabids](https://sovabids.readthedocs.io/en/latest/): A Python package for the automatic conversion of EEG datasets to the BIDS standard, with a focus on making the most out of metadata.
  <br>[![Last commit](https://img.shields.io/github/last-commit/yjmantilla/sovabids?style=plastic)](https://github.com/yjmantilla/sovabids)

### MEG

- <img src='./images/logo_python.png' width='14px'>  [Biscuit](https://macquarie-meg-research.github.io/Biscuit/): GUI for easy MEG to BIDS conversion
  <br>[![Last commit](https://img.shields.io/github/last-commit/Macquarie-MEG-Research/Biscuit?style=plastic)](https://github.com/Macquarie-MEG-Research/Biscuit)
- <img src='./images/logo_matlab.png' width='17px'>  [EEGLAB](https://eeglab.org/tutorials/04_Import/BIDS.html): <a href='https://github.com/arnodelorme/bids-MATLAB-tools'>See plugins</a>
  <br>[![Last commit](https://img.shields.io/github/last-commit/sccn/eeglab?style=plastic)](https://github.com/sccn/eeglab)
- <img src='./images/logo_matlab.png' width='17px'>  [FieldTrip - data2bids](https://www.fieldtriptoolbox.org/example/bids/):
  <br>[![Last commit](https://img.shields.io/github/last-commit/fieldtrip/fieldtrip?style=plastic)](https://github.com/fieldtrip/fieldtrip)
- <img src='./images/logo_python.png' width='14px'>  [MNE-BIDS](https://mne.tools/mne-bids): MNE-BIDS is a Python package that allows you to read and write BIDS-compatible datasets with the help of MNE-Python.
  <br>[![Last commit](https://img.shields.io/github/last-commit/mne-tools/mne-bids?style=plastic)](https://github.com/mne-tools/mne-bids)[![PyPI version](https://badge.fury.io/py/mne-bids.svg)](https://pypi.org/project/mne-bids)

### MISC

- <img src='./images/logo_python.png' width='14px'>  [convert-eprime](https://github.com/tsalo/convert-eprime): Python functions to convert E-Prime files to CSVs. Not currently being developed.
  <br>[![Last commit](https://img.shields.io/github/last-commit/tsalo/convert-eprime?style=plastic)](https://github.com/tsalo/convert-eprime)
- <img src='./images/logo_python.png' width='14px'>  [sim2bids](https://github.com/dissagaliyeva/sim2bids): GUI to easily convert simulation results to BIDS format, according to <a href="https://bids.neuroimaging.io/bep034" target="_blank"> BEP 34 </a>.
  <br>[![Last commit](https://img.shields.io/github/last-commit/dissagaliyeva/sim2bids?style=plastic)](https://github.com/dissagaliyeva/sim2bids)

### MRI

- <img src='./images/logo_python.png' width='14px'>  [BIDScoin](https://bidscoin.readthedocs.io/en/stable/): BIDScoin is a flexible tool to convert (“coin”) source-level (raw) neuroimaging data sets to BIDS without needing to code anything. It features automatic data discovery based on header as well as filesystem information, and comes with a user-friendly GUI to add missing information and tweak the results. BIDScoin supports multiple source data formats with plugins (e.g. employing dcm2niix, spec2nii or nibabel) and allows customization of the prior knowledge about your data (allowing for fully automatic CLI data conversion if you like).
  <br>[![Last commit](https://img.shields.io/github/last-commit/Donders-Institute/bidscoin?style=plastic)](https://github.com/Donders-Institute/bidscoin)[![PyPI version](https://badge.fury.io/py/bidscoin.svg)](https://pypi.org/project/bidscoin)
- <img src='./images/logo_R.png' width='18px'>  [BIDSconvertR](https://bidsconvertr.github.io/): The BIDSconvertR R package provides a user-friendly workflow with graphical user interfaces. It consists of the following steps: (i) convert DICOM data to NIfTI data using dcm2niix (ii) structure this data according to the BIDS specification (iii) provide the papayaWidget viewer for inspecting the images
  <br>[![Last commit](https://img.shields.io/github/last-commit/bidsconvertr/bidsconvertr?style=plastic)](https://github.com/bidsconvertr/bidsconvertr)
- <img src='./images/logo_python.png' width='14px'>  [bidskit](https://github.com/jmtyszka/bidskit/blob/master/docs/QuickStart.md): Utility functions for working with DICOM and BIDS neuroimaging data.
  <br>[![Last commit](https://img.shields.io/github/last-commit/jmtyszka/bidskit?style=plastic)](https://github.com/jmtyszka/bidskit)[![PyPI version](https://badge.fury.io/py/bidskit.svg)](https://pypi.org/project/bidskit)[![Docker version](https://img.shields.io/docker/pulls/jmtyszka/bidskit.svg?style=plastic)](https://hub.docker.com/r/jmtyszka/bidskit)
- <img src='./images/logo_python.png' width='14px'>  [BIDSme](https://gitlab.uliege.be/CyclotronResearchCentre/Public/bidstools/bidsme/bidsme_example/-/tree/master/example1):
  <br>[![Last commit](https://img.shields.io/github/last-commit/nbeliy/bidsme?style=plastic)](https://github.com/nbeliy/bidsme)
- <img src='./images/logo_python.png' width='14px'>  [BMAT](https://github.com/ColinVDB/BMAT):
  <br>[![Last commit](https://img.shields.io/github/last-commit/ColinVDB/BMAT?style=plastic)](https://github.com/ColinVDB/BMAT)[![Docker version](https://img.shields.io/docker/pulls/colinvdb/bmat-dcm2niix.svg?style=plastic)](https://hub.docker.com/r/colinvdb/bmat-dcm2niix)
- <img src='./images/logo_python.png' width='14px'>  [BrkRaw](https://github.com/BrkRaw/brkraw): For a preclinical Bruker MRI scanner
  <br>[![Last commit](https://img.shields.io/github/last-commit/BrkRaw/brkraw?style=plastic)](https://github.com/BrkRaw/brkraw)
- <img src='./images/logo_python.png' width='14px'>  [Clinica](https://aramislab.paris.inria.fr/clinica/docs/public/dev/):
  <br>[![Last commit](https://img.shields.io/github/last-commit/aramis-lab/clinica?style=plastic)](https://github.com/aramis-lab/clinica)
- <img src='./images/logo_python.png' width='14px'>  [dac2bids](https://github.com/dangom/dac2bids): Create a BIDS structure for a DICOM folder.
  <br>[![Last commit](https://img.shields.io/github/last-commit/dangom/dac2bids?style=plastic)](https://github.com/dangom/dac2bids)
- <img src='./images/logo_python.png' width='14px'>  [Data2Bids](https://github.com/SIMEXP/Data2Bids): Converts MRI files from extension supported by nibabel into NIfTI and convert them to BIDS
  <br>[![Last commit](https://img.shields.io/github/last-commit/SIMEXP/Data2Bids?style=plastic)](https://github.com/SIMEXP/Data2Bids)[![PyPI version](https://badge.fury.io/py/data2bids.svg)](https://pypi.org/project/data2bids)
- <img src='./images/logo_python.png' width='14px'>  [Dcm2Bids](https://unfmontreal.github.io/Dcm2Bids/): converts DICOM files using dcm2niix into BIDS
  <br>[![Last commit](https://img.shields.io/github/last-commit/cbedetti/Dcm2Bids?style=plastic)](https://github.com/cbedetti/Dcm2Bids)[![PyPI version](https://badge.fury.io/py/Dcm2Bids.svg)](https://pypi.org/project/Dcm2Bids)[![Docker version](https://img.shields.io/docker/pulls/unfmontreal/dcm2bids.svg?style=plastic)](https://hub.docker.com/r/unfmontreal/dcm2bids)
- <img src='./images/logo_matlab.png' width='17px'>  [Explore ASL](https://exploreasl.github.io/Documentation/1.8.0/Tutorials-ASL-BIDS/): Convert DICOM and NIFTI data to the ASL-BIDS format.
  <br>[![Last commit](https://img.shields.io/github/last-commit/ExploreASL/ExploreASL?style=plastic)](https://github.com/ExploreASL/ExploreASL)
- <img src='./images/logo_python.png' width='14px'>  [ezBIDS](https://brainlife.io/docs/using_ezBIDS/): A web-based BIDS conversion tool with four unique features: (1) No installation or programming requirements. (2) Handling of both imaging and task events data and metadata. (3) Semi-automated inference and guidance for adherence to BIDS. (4) Multiple data management options, including download BIDS data to local system, or transfer to OpenNeuro.org or to brainlife.io.
  <br>![](https://img.shields.io/badge/Javascript-yellow.svg?style=plastic)![](https://img.shields.io/badge/shell-black.svg?style=plastic)[![Last commit](https://img.shields.io/github/last-commit/brainlife/ezbids?style=plastic)](https://github.com/brainlife/ezbids)
- <img src='./images/logo_matlab.png' width='17px'>  [FieldTrip - data2bids](https://www.fieldtriptoolbox.org/example/bids/):
  <br>[![Last commit](https://img.shields.io/github/last-commit/fieldtrip/fieldtrip?style=plastic)](https://github.com/fieldtrip/fieldtrip)
- <img src='./images/logo_python.png' width='14px'>  [HeuDiConv](https://heudiconv.readthedocs.io/): A flexible DICOM converter for organizing brain imaging data into structured directory layouts
  <br>[![Last commit](https://img.shields.io/github/last-commit/nipy/heudiconv?style=plastic)](https://github.com/nipy/heudiconv)[![PyPI version](https://badge.fury.io/py/heudiconv.svg)](https://pypi.org/project/heudiconv)[![Docker version](https://img.shields.io/docker/pulls/nipy/heudiconv.svg?style=plastic)](https://hub.docker.com/r/nipy/heudiconv)
-  [Horos (Osirix) export plugin](https://github.com/mslw/horos-bids-output): Horos plugin for BIDS output.
  <br>[![Last commit](https://img.shields.io/github/last-commit/mslw/horos-bids-output?style=plastic)](https://github.com/mslw/horos-bids-output)
- <img src='./images/logo_python.png' width='14px'>  [mercure-dcm2bids](https://github.com/mercure-imaging/mercure-dcm2bids): A containerized app that can be used to perform BIDS conversion of DICOM studies sent directly to mercure from a scanner or PACS. mercure is an open-source DICOM orchestration platform that can integrate containerized apps into clinical workflows. It has a graphical user interface making it easy to setup and manage BIDS configurations for multiple protocols. The Dcm2Bids tool is used for conversion.
  <br>[![Last commit](https://img.shields.io/github/last-commit/mercure-imaging/mercure-dcm2bids?style=plastic)](https://github.com/mercure-imaging/mercure-dcm2bids)[![Docker version](https://img.shields.io/docker/pulls/mercureimaging/mercure-dcm2bids.svg?style=plastic)](https://hub.docker.com/r/mercureimaging/mercure-dcm2bids)
- <img src='./images/logo_python.png' width='14px'>  [niix2bids](https://github.com/benoitberanger/niix2bids): Use this package as a command line to organize your Nifti dataset into BIDS.
  <br>[![Last commit](https://img.shields.io/github/last-commit/benoitberanger/niix2bids?style=plastic)](https://github.com/benoitberanger/niix2bids)
-  [OpenfMRI2BIDS](https://github.com/bids-standard/openfmri2bids): Convert OpenfMRI dataset to BIDS
  <br>[![Last commit](https://img.shields.io/github/last-commit/bids-standard/openfmri2bids?style=plastic)](https://github.com/bids-standard/openfmri2bids)
- <img src='./images/logo_python.png' width='14px'>  [ReproIn](https://github.com/ReproNim/reproin): HeuDiConv-based turnkey solution: a setup for automatic generation of shareable, version-controlled BIDS datasets from MR scanners.
  <br>[![Last commit](https://img.shields.io/github/last-commit/ReproNim/reproin?style=plastic)](https://github.com/ReproNim/reproin)[![Docker version](https://img.shields.io/docker/pulls/repronim/reproin.svg?style=plastic)](https://hub.docker.com/r/repronim/reproin)
- <img src='./images/logo_python.png' width='14px'>  [SAMRI](https://github.com/IBT-FMI/SAMRI): Full stack Small Animal MRI data analysis package, including the `bru2bids` repositing pipeline, which can convert Bruker archives to the BIDS format. From the ETH and University of Zurich, with collaboration from MIT and Dartmouth College.
  <br>![](https://img.shields.io/badge/shell-black.svg?style=plastic)[![Last commit](https://img.shields.io/github/last-commit/IBT-FMI/SAMRI?style=plastic)](https://github.com/IBT-FMI/SAMRI)
-  [XNAT2BIDS](https://github.com/kamillipi/2bids): Simple xnat pipeline to convert DICOM scans to BIDS-compatible output (nii+json).
  <br>![](https://img.shields.io/badge/shell-black.svg?style=plastic)[![Last commit](https://img.shields.io/github/last-commit/kamillipi/2bids?style=plastic)](https://github.com/kamillipi/2bids)

### NIRS

- <img src='./images/logo_python.png' width='14px'>  [MNE-BIDS](https://mne.tools/mne-bids): MNE-BIDS is a Python package that allows you to read and write BIDS-compatible datasets with the help of MNE-Python.
  <br>[![Last commit](https://img.shields.io/github/last-commit/mne-tools/mne-bids?style=plastic)](https://github.com/mne-tools/mne-bids)[![PyPI version](https://badge.fury.io/py/mne-bids.svg)](https://pypi.org/project/mne-bids)

### PET

- <img src='./images/logo_python.png' width='14px'>  [BIDScoin](https://bidscoin.readthedocs.io/en/stable/): BIDScoin is a flexible tool to convert (“coin”) source-level (raw) neuroimaging data sets to BIDS without needing to code anything. It features automatic data discovery based on header as well as filesystem information, and comes with a user-friendly GUI to add missing information and tweak the results. BIDScoin supports multiple source data formats with plugins (e.g. employing dcm2niix, spec2nii or nibabel) and allows customization of the prior knowledge about your data (allowing for fully automatic CLI data conversion if you like).
  <br>[![Last commit](https://img.shields.io/github/last-commit/Donders-Institute/bidscoin?style=plastic)](https://github.com/Donders-Institute/bidscoin)[![PyPI version](https://badge.fury.io/py/bidscoin.svg)](https://pypi.org/project/bidscoin)
- <img src='./images/logo_python.png' width='14px'>  [Clinica](https://aramislab.paris.inria.fr/clinica/docs/public/dev/):
  <br>[![Last commit](https://img.shields.io/github/last-commit/aramis-lab/clinica?style=plastic)](https://github.com/aramis-lab/clinica)
- <img src='./images/logo_matlab.png' width='17px'> <img src='./images/logo_python.png' width='14px'>  [PET2BIDS](https://github.com/openneuropet/PET2BIDS): Helps you convert your PET data! raw PET scanner files (for example ecat, dicom) and additional side file like excel sheets.
  <br>[![Last commit](https://img.shields.io/github/last-commit/openneuropet/PET2BIDS?style=plastic)](https://github.com/openneuropet/PET2BIDS)

### TSV

- <img src='./images/logo_python.png' width='14px'>  [BIDSto3col](https://github.com/bids-standard/bidsutils/tree/master/BIDSto3col): Reads BidsTSV and then creates 3 column event files, one per event type if a "trial_type" column is found.
  <br>![](https://img.shields.io/badge/shell-black.svg?style=plastic)[![Last commit](https://img.shields.io/github/last-commit/bids-standard/bidsutils/tree/master/BIDSto3col?style=plastic)](https://github.com/bids-standard/bidsutils/tree/master/BIDSto3col)

### behavioral

- <img src='./images/logo_python.png' width='14px'>  [convert-eprime](https://github.com/tsalo/convert-eprime): Python functions to convert E-Prime files to CSVs. Not currently being developed.
  <br>[![Last commit](https://img.shields.io/github/last-commit/tsalo/convert-eprime?style=plastic)](https://github.com/tsalo/convert-eprime)
- <img src='./images/logo_matlab.png' width='17px'>  [FieldTrip - data2bids](https://www.fieldtriptoolbox.org/example/bids/):
  <br>[![Last commit](https://img.shields.io/github/last-commit/fieldtrip/fieldtrip?style=plastic)](https://github.com/fieldtrip/fieldtrip)

### computational model

- <img src='./images/logo_python.png' width='14px'>  [sim2bids](https://github.com/dissagaliyeva/sim2bids): GUI to easily convert simulation results to BIDS format, according to <a href="https://bids.neuroimaging.io/bep034" target="_blank"> BEP 34 </a>.
  <br>[![Last commit](https://img.shields.io/github/last-commit/dissagaliyeva/sim2bids?style=plastic)](https://github.com/dissagaliyeva/sim2bids)

### events

- <img src='./images/logo_python.png' width='14px'>  [ezBIDS](https://brainlife.io/docs/using_ezBIDS/): A web-based BIDS conversion tool with four unique features: (1) No installation or programming requirements. (2) Handling of both imaging and task events data and metadata. (3) Semi-automated inference and guidance for adherence to BIDS. (4) Multiple data management options, including download BIDS data to local system, or transfer to OpenNeuro.org or to brainlife.io.
  <br>![](https://img.shields.io/badge/Javascript-yellow.svg?style=plastic)![](https://img.shields.io/badge/shell-black.svg?style=plastic)[![Last commit](https://img.shields.io/github/last-commit/brainlife/ezbids?style=plastic)](https://github.com/brainlife/ezbids)

### iEEG

- <img src='./images/logo_matlab.png' width='17px'>  [FieldTrip - data2bids](https://www.fieldtriptoolbox.org/example/bids/):
  <br>[![Last commit](https://img.shields.io/github/last-commit/fieldtrip/fieldtrip?style=plastic)](https://github.com/fieldtrip/fieldtrip)
- <img src='./images/logo_python.png' width='14px'>  [MNE-BIDS](https://mne.tools/mne-bids): MNE-BIDS is a Python package that allows you to read and write BIDS-compatible datasets with the help of MNE-Python.
  <br>[![Last commit](https://img.shields.io/github/last-commit/mne-tools/mne-bids?style=plastic)](https://github.com/mne-tools/mne-bids)[![PyPI version](https://badge.fury.io/py/mne-bids.svg)](https://pypi.org/project/mne-bids)

### physiological

- <img src='./images/logo_python.png' width='14px'>  [BIDScoin](https://bidscoin.readthedocs.io/en/stable/): BIDScoin is a flexible tool to convert (“coin”) source-level (raw) neuroimaging data sets to BIDS without needing to code anything. It features automatic data discovery based on header as well as filesystem information, and comes with a user-friendly GUI to add missing information and tweak the results. BIDScoin supports multiple source data formats with plugins (e.g. employing dcm2niix, spec2nii or nibabel) and allows customization of the prior knowledge about your data (allowing for fully automatic CLI data conversion if you like).
  <br>[![Last commit](https://img.shields.io/github/last-commit/Donders-Institute/bidscoin?style=plastic)](https://github.com/Donders-Institute/bidscoin)[![PyPI version](https://badge.fury.io/py/bidscoin.svg)](https://pypi.org/project/bidscoin)
- <img src='./images/logo_python.png' width='14px'>  [bidsphysio](None): Converts physio data to BIDS physiological recording
  <br>[![Last commit](https://img.shields.io/github/last-commit/cbinyu/bidsphysio?style=plastic)](https://github.com/cbinyu/bidsphysio)[![PyPI version](https://badge.fury.io/py/bidsphysio.svg)](https://pypi.org/project/bidsphysio/)[![Docker version](https://img.shields.io/docker/pulls/cbinyu/bidsphysio.svg?style=plastic)](https://hub.docker.com/r/cbinyu/bidsphysio/)
- <img src='./images/logo_python.png' width='14px'>  [phys2bids](https://phys2bids.readthedocs.io/en/latest/): Python3 library to format physiological files in BIDS.
  <br>[![Last commit](https://img.shields.io/github/last-commit/physiopy/phys2bids?style=plastic)](https://github.com/physiopy/phys2bids)[![PyPI version](https://badge.fury.io/py/phys2bids.svg)](https://pypi.org/project/phys2bids)
