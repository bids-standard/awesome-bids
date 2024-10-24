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
  <br>
- <img src='./images/logo_python.png' width='14px'>  [ezBIDS](https://brainlife.io/docs/using_ezBIDS/): A web-based BIDS conversion tool with four unique features: (1) No installation or programming requirements. (2) Handling of both imaging and task events data and metadata. (3) Semi-automated inference and guidance for adherence to BIDS. (4) Multiple data management options, including download BIDS data to local system, or transfer to OpenNeuro.org or to brainlife.io.
  <br>![](https://img.shields.io/badge/Javascript-yellow.svg?style=plastic)![](https://img.shields.io/badge/shell-black.svg?style=plastic)[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=plastic)](https://opensource.org/licenses/MIT)

### BIDS

- <img src='./images/logo_python.png' width='14px'>  [BIDS2ISATab](https://github.com/bids-standard/BIDS2ISATab): Extract ISA-Tab compatible metadata from BIDS
  <br>
- <img src='./images/logo_python.png' width='14px'>  [BIDS2NDA](https://github.com/bids-standard/BIDS2NDA): Extract NIHM Data Archive compatible metadata from BIDS
  <br>
- <img src='./images/logo_python.png' width='14px'>  [bids2xar - for XNAT import](https://github.com/lwallace23/bids2xar): Convert BIDS data set into XNAT XAR bundles
  <br>

### EEG

- <img src='./images/logo_python.png' width='14px'>  [BIDSme](https://gitlab.uliege.be/CyclotronResearchCentre/Public/bidstools/bidsme/bidsme_example/-/tree/master/example1):
  <br>[![License: GPL-2.0](https://img.shields.io/badge/License-GPLv2-blue.svg?style=plastic)](https://www.gnu.org/licenses/gpl-2.0)
- <img src='./images/logo_python.png' width='14px'>  [EEG2BIDS](https://github.com/aces/EEG2BIDS): A tool for converting raw EEG and iEEG data into the BIDS standard data structure, prepared for LORIS (Longitudinal Online Research and Imaging System).
  <br>![](https://img.shields.io/badge/Javascript-yellow.svg?style=plastic)
- <img src='./images/logo_matlab.png' width='17px'>  [EEGLAB](https://eeglab.org/tutorials/04_Import/BIDS.html): <a href='https://github.com/arnodelorme/bids-MATLAB-tools'>See plugins</a>
  <br>
- <img src='./images/logo_matlab.png' width='17px'>  [FieldTrip - data2bids](https://www.fieldtriptoolbox.org/example/bids/):
  <br>[![License: GPL-3.0](https://img.shields.io/badge/License-GPLv3-blue.svg?style=plastic)](https://www.gnu.org/licenses/gpl-3.0)
- <img src='./images/logo_python.png' width='14px'>  [MNE-BIDS](https://mne.tools/mne-bids): MNE-BIDS is a Python package that allows you to read and write BIDS-compatible datasets with the help of MNE-Python.
  <br>[![PyPI version](https://badge.fury.io/py/mne-bids.svg)](https://pypi.org/project/mne-bids)[![License: BSD-3-Clause](https://img.shields.io/badge/License-BSD_3--Clause-blue.svg?style=plastic)](https://opensource.org/licenses/BSD-3-Clause)
- <img src='./images/logo_python.png' width='14px'>  [sovabids](https://sovabids.readthedocs.io/en/latest/): A Python package for the automatic conversion of EEG datasets to the BIDS standard, with a focus on making the most out of metadata.
  <br>

### MEG

- <img src='./images/logo_python.png' width='14px'>  [Biscuit](https://macquarie-meg-research.github.io/Biscuit/): GUI for easy MEG to BIDS conversion
  <br>[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=plastic)](https://opensource.org/licenses/MIT)
- <img src='./images/logo_matlab.png' width='17px'>  [EEGLAB](https://eeglab.org/tutorials/04_Import/BIDS.html): <a href='https://github.com/arnodelorme/bids-MATLAB-tools'>See plugins</a>
  <br>
- <img src='./images/logo_matlab.png' width='17px'>  [FieldTrip - data2bids](https://www.fieldtriptoolbox.org/example/bids/):
  <br>[![License: GPL-3.0](https://img.shields.io/badge/License-GPLv3-blue.svg?style=plastic)](https://www.gnu.org/licenses/gpl-3.0)
- <img src='./images/logo_python.png' width='14px'>  [MNE-BIDS](https://mne.tools/mne-bids): MNE-BIDS is a Python package that allows you to read and write BIDS-compatible datasets with the help of MNE-Python.
  <br>[![PyPI version](https://badge.fury.io/py/mne-bids.svg)](https://pypi.org/project/mne-bids)[![License: BSD-3-Clause](https://img.shields.io/badge/License-BSD_3--Clause-blue.svg?style=plastic)](https://opensource.org/licenses/BSD-3-Clause)

### MISC

- <img src='./images/logo_python.png' width='14px'>  [convert-eprime](https://github.com/tsalo/convert-eprime): Python functions to convert E-Prime files to CSVs. Not currently being developed.
  <br>[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=plastic)](https://opensource.org/licenses/MIT)
- <img src='./images/logo_python.png' width='14px'>  [sim2bids](https://github.com/dissagaliyeva/sim2bids): GUI to easily convert simulation results to BIDS format, according to <a href="https://bids.neuroimaging.io/bep034" target="_blank"> BEP 34 </a>.
  <br>[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=plastic)](https://opensource.org/licenses/MIT)

### MRI

- <img src='./images/logo_python.png' width='14px'>  [BIDScoin](https://bidscoin.readthedocs.io/en/stable/): BIDScoin is a flexible tool to convert (“coin”) source-level (raw) neuroimaging data sets to BIDS without needing to code anything. It features automatic data discovery based on header as well as filesystem information, and comes with a user-friendly GUI to add missing information and tweak the results. BIDScoin supports multiple source data formats with plugins (e.g. employing dcm2niix, spec2nii or nibabel) and allows customization of the prior knowledge about your data (allowing for fully automatic CLI data conversion if you like).
  <br>[![PyPI version](https://badge.fury.io/py/bidscoin.svg)](https://pypi.org/project/bidscoin)[![License: GPL-3.0](https://img.shields.io/badge/License-GPLv3-blue.svg?style=plastic)](https://www.gnu.org/licenses/gpl-3.0)
- <img src='./images/logo_R.png' width='18px'>  [BIDSconvertR](https://bidsconvertr.github.io/): The BIDSconvertR R package provides a user-friendly workflow with graphical user interfaces. It consists of the following steps: (i) convert DICOM data to NIfTI data using dcm2niix (ii) structure this data according to the BIDS specification (iii) provide the papayaWidget viewer for inspecting the images
  <br>[![License: GPL-3.0](https://img.shields.io/badge/License-GPLv3-blue.svg?style=plastic)](https://www.gnu.org/licenses/gpl-3.0)
- <img src='./images/logo_python.png' width='14px'>  [bidskit](https://github.com/jmtyszka/bidskit/blob/master/docs/QuickStart.md): Utility functions for working with DICOM and BIDS neuroimaging data.
  <br>[![PyPI version](https://badge.fury.io/py/bidskit.svg)](https://pypi.org/project/bidskit)[![Docker version](https://img.shields.io/docker/pulls/jmtyszka/bidskit.svg?style=plastic)](https://hub.docker.com/r/jmtyszka/bidskit)[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=plastic)](https://opensource.org/licenses/MIT)
- <img src='./images/logo_python.png' width='14px'>  [BIDSme](https://gitlab.uliege.be/CyclotronResearchCentre/Public/bidstools/bidsme/bidsme_example/-/tree/master/example1):
  <br>[![License: GPL-2.0](https://img.shields.io/badge/License-GPLv2-blue.svg?style=plastic)](https://www.gnu.org/licenses/gpl-2.0)
- <img src='./images/logo_python.png' width='14px'>  [BMAT](https://github.com/ColinVDB/BMAT):
  <br>[![Docker version](https://img.shields.io/docker/pulls/colinvdb/bmat-dcm2niix.svg?style=plastic)](https://hub.docker.com/r/colinvdb/bmat-dcm2niix)[![License: GPL-3.0](https://img.shields.io/badge/License-GPLv3-blue.svg?style=plastic)](https://www.gnu.org/licenses/gpl-3.0)
- <img src='./images/logo_python.png' width='14px'>  [BrkRaw](https://github.com/BrkRaw/brkraw): For a preclinical Bruker MRI scanner
  <br>[![License: GPL-3.0](https://img.shields.io/badge/License-GPLv3-blue.svg?style=plastic)](https://www.gnu.org/licenses/gpl-3.0)
- <img src='./images/logo_python.png' width='14px'>  [Clinica](https://aramislab.paris.inria.fr/clinica/docs/public/latest/):
  <br>[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=plastic)](https://opensource.org/licenses/MIT)
- <img src='./images/logo_python.png' width='14px'>  [dac2bids](https://github.com/dangom/dac2bids): Create a BIDS structure for a DICOM folder.
  <br>
- <img src='./images/logo_python.png' width='14px'>  [Data2Bids](https://github.com/SIMEXP/Data2Bids): Converts MRI files from extension supported by nibabel into NIfTI and convert them to BIDS
  <br>[![PyPI version](https://badge.fury.io/py/data2bids.svg)](https://pypi.org/project/data2bids)[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=plastic)](https://opensource.org/licenses/MIT)
- <img src='./images/logo_python.png' width='14px'>  [Dcm2Bids](https://unfmontreal.github.io/Dcm2Bids/): converts DICOM files using dcm2niix into BIDS
  <br>[![PyPI version](https://badge.fury.io/py/Dcm2Bids.svg)](https://pypi.org/project/Dcm2Bids)[![Docker version](https://img.shields.io/docker/pulls/unfmontreal/dcm2bids.svg?style=plastic)](https://hub.docker.com/r/unfmontreal/dcm2bids)[![License: GPL-3.0](https://img.shields.io/badge/License-GPLv3-blue.svg?style=plastic)](https://www.gnu.org/licenses/gpl-3.0)
- <img src='./images/logo_matlab.png' width='17px'>  [Explore ASL](https://exploreasl.github.io/Documentation/1.8.0/Tutorials-ASL-BIDS/): Convert DICOM and NIFTI data to the ASL-BIDS format.
  <br>
- <img src='./images/logo_python.png' width='14px'>  [ezBIDS](https://brainlife.io/docs/using_ezBIDS/): A web-based BIDS conversion tool with four unique features: (1) No installation or programming requirements. (2) Handling of both imaging and task events data and metadata. (3) Semi-automated inference and guidance for adherence to BIDS. (4) Multiple data management options, including download BIDS data to local system, or transfer to OpenNeuro.org or to brainlife.io.
  <br>![](https://img.shields.io/badge/Javascript-yellow.svg?style=plastic)![](https://img.shields.io/badge/shell-black.svg?style=plastic)[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=plastic)](https://opensource.org/licenses/MIT)
- <img src='./images/logo_matlab.png' width='17px'>  [FieldTrip - data2bids](https://www.fieldtriptoolbox.org/example/bids/):
  <br>[![License: GPL-3.0](https://img.shields.io/badge/License-GPLv3-blue.svg?style=plastic)](https://www.gnu.org/licenses/gpl-3.0)
- <img src='./images/logo_python.png' width='14px'>  [HeuDiConv](https://heudiconv.readthedocs.io/): A flexible DICOM converter for organizing brain imaging data into structured directory layouts
  <br>[![PyPI version](https://badge.fury.io/py/heudiconv.svg)](https://pypi.org/project/heudiconv)[![Docker version](https://img.shields.io/docker/pulls/nipy/heudiconv.svg?style=plastic)](https://hub.docker.com/r/nipy/heudiconv)[![License: Apache 2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg?style=plastic)](https://opensource.org/licenses/Apache-2.0)
-  [Horos (Osirix) export plugin](https://github.com/mslw/horos-bids-output): Horos plugin for BIDS output.
  <br>[![License: GPL-3.0](https://img.shields.io/badge/License-GPLv3-blue.svg?style=plastic)](https://www.gnu.org/licenses/gpl-3.0)
- <img src='./images/logo_python.png' width='14px'>  [mercure-dcm2bids](https://github.com/mercure-imaging/mercure-dcm2bids): A containerized app that can be used to perform BIDS conversion of DICOM studies sent directly to mercure from a scanner or PACS. mercure is an open-source DICOM orchestration platform that can integrate containerized apps into clinical workflows. It has a graphical user interface making it easy to setup and manage BIDS configurations for multiple protocols. The Dcm2Bids tool is used for conversion.
  <br>[![Docker version](https://img.shields.io/docker/pulls/mercureimaging/mercure-dcm2bids.svg?style=plastic)](https://hub.docker.com/r/mercureimaging/mercure-dcm2bids)[![License: GPL-3.0](https://img.shields.io/badge/License-GPLv3-blue.svg?style=plastic)](https://www.gnu.org/licenses/gpl-3.0)
- <img src='./images/logo_python.png' width='14px'>  [niix2bids](https://github.com/benoitberanger/niix2bids): Use this package as a command line to organize your Nifti dataset into BIDS.
  <br>[![License: GPL-3.0](https://img.shields.io/badge/License-GPLv3-blue.svg?style=plastic)](https://www.gnu.org/licenses/gpl-3.0)
-  [OpenfMRI2BIDS](https://github.com/bids-standard/openfmri2bids): Convert OpenfMRI dataset to BIDS
  <br>
- <img src='./images/logo_python.png' width='14px'>  [ReproIn](https://github.com/ReproNim/reproin): HeuDiConv-based turnkey solution: a setup for automatic generation of shareable, version-controlled BIDS datasets from MR scanners.
  <br>[![Docker version](https://img.shields.io/docker/pulls/repronim/reproin.svg?style=plastic)](https://hub.docker.com/r/repronim/reproin)[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=plastic)](https://opensource.org/licenses/MIT)
- <img src='./images/logo_python.png' width='14px'>  [SAMRI](https://github.com/IBT-FMI/SAMRI): Full stack Small Animal MRI data analysis package, including the `bru2bids` repositing pipeline, which can convert Bruker archives to the BIDS format. From the ETH and University of Zurich, with collaboration from MIT and Dartmouth College.
  <br>![](https://img.shields.io/badge/shell-black.svg?style=plastic)
-  [XNAT2BIDS](https://github.com/kamillipi/2bids): Simple xnat pipeline to convert DICOM scans to BIDS-compatible output (nii+json).
  <br>![](https://img.shields.io/badge/shell-black.svg?style=plastic)

### NIRS

- <img src='./images/logo_python.png' width='14px'>  [MNE-BIDS](https://mne.tools/mne-bids): MNE-BIDS is a Python package that allows you to read and write BIDS-compatible datasets with the help of MNE-Python.
  <br>[![PyPI version](https://badge.fury.io/py/mne-bids.svg)](https://pypi.org/project/mne-bids)[![License: BSD-3-Clause](https://img.shields.io/badge/License-BSD_3--Clause-blue.svg?style=plastic)](https://opensource.org/licenses/BSD-3-Clause)

### PET

- <img src='./images/logo_python.png' width='14px'>  [BIDScoin](https://bidscoin.readthedocs.io/en/stable/): BIDScoin is a flexible tool to convert (“coin”) source-level (raw) neuroimaging data sets to BIDS without needing to code anything. It features automatic data discovery based on header as well as filesystem information, and comes with a user-friendly GUI to add missing information and tweak the results. BIDScoin supports multiple source data formats with plugins (e.g. employing dcm2niix, spec2nii or nibabel) and allows customization of the prior knowledge about your data (allowing for fully automatic CLI data conversion if you like).
  <br>[![PyPI version](https://badge.fury.io/py/bidscoin.svg)](https://pypi.org/project/bidscoin)[![License: GPL-3.0](https://img.shields.io/badge/License-GPLv3-blue.svg?style=plastic)](https://www.gnu.org/licenses/gpl-3.0)
- <img src='./images/logo_matlab.png' width='17px'> <img src='./images/logo_python.png' width='14px'>  [PET2BIDS](https://github.com/openneuropet/PET2BIDS): Helps you convert your PET data! raw PET scanner files (for example ecat, dicom) and additional side file like excel sheets.
  <br>[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=plastic)](https://opensource.org/licenses/MIT)

### TSV

- <img src='./images/logo_python.png' width='14px'>  [BIDSto3col](https://github.com/bids-standard/bidsutils/tree/master/BIDSto3col): Reads BidsTSV and then creates 3 column event files, one per event type if a "trial_type" column is found.
  <br>![](https://img.shields.io/badge/shell-black.svg?style=plastic)

### behavioral

- <img src='./images/logo_python.png' width='14px'>  [convert-eprime](https://github.com/tsalo/convert-eprime): Python functions to convert E-Prime files to CSVs. Not currently being developed.
  <br>[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=plastic)](https://opensource.org/licenses/MIT)
- <img src='./images/logo_matlab.png' width='17px'>  [FieldTrip - data2bids](https://www.fieldtriptoolbox.org/example/bids/):
  <br>[![License: GPL-3.0](https://img.shields.io/badge/License-GPLv3-blue.svg?style=plastic)](https://www.gnu.org/licenses/gpl-3.0)

### computational model

- <img src='./images/logo_python.png' width='14px'>  [sim2bids](https://github.com/dissagaliyeva/sim2bids): GUI to easily convert simulation results to BIDS format, according to <a href="https://bids.neuroimaging.io/bep034" target="_blank"> BEP 34 </a>.
  <br>[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=plastic)](https://opensource.org/licenses/MIT)

### events

- <img src='./images/logo_python.png' width='14px'>  [ezBIDS](https://brainlife.io/docs/using_ezBIDS/): A web-based BIDS conversion tool with four unique features: (1) No installation or programming requirements. (2) Handling of both imaging and task events data and metadata. (3) Semi-automated inference and guidance for adherence to BIDS. (4) Multiple data management options, including download BIDS data to local system, or transfer to OpenNeuro.org or to brainlife.io.
  <br>![](https://img.shields.io/badge/Javascript-yellow.svg?style=plastic)![](https://img.shields.io/badge/shell-black.svg?style=plastic)[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=plastic)](https://opensource.org/licenses/MIT)

### iEEG

- <img src='./images/logo_matlab.png' width='17px'>  [FieldTrip - data2bids](https://www.fieldtriptoolbox.org/example/bids/):
  <br>[![License: GPL-3.0](https://img.shields.io/badge/License-GPLv3-blue.svg?style=plastic)](https://www.gnu.org/licenses/gpl-3.0)
- <img src='./images/logo_python.png' width='14px'>  [MNE-BIDS](https://mne.tools/mne-bids): MNE-BIDS is a Python package that allows you to read and write BIDS-compatible datasets with the help of MNE-Python.
  <br>[![PyPI version](https://badge.fury.io/py/mne-bids.svg)](https://pypi.org/project/mne-bids)[![License: BSD-3-Clause](https://img.shields.io/badge/License-BSD_3--Clause-blue.svg?style=plastic)](https://opensource.org/licenses/BSD-3-Clause)

### physiological

- <img src='./images/logo_python.png' width='14px'>  [BIDScoin](https://bidscoin.readthedocs.io/en/stable/): BIDScoin is a flexible tool to convert (“coin”) source-level (raw) neuroimaging data sets to BIDS without needing to code anything. It features automatic data discovery based on header as well as filesystem information, and comes with a user-friendly GUI to add missing information and tweak the results. BIDScoin supports multiple source data formats with plugins (e.g. employing dcm2niix, spec2nii or nibabel) and allows customization of the prior knowledge about your data (allowing for fully automatic CLI data conversion if you like).
  <br>[![PyPI version](https://badge.fury.io/py/bidscoin.svg)](https://pypi.org/project/bidscoin)[![License: GPL-3.0](https://img.shields.io/badge/License-GPLv3-blue.svg?style=plastic)](https://www.gnu.org/licenses/gpl-3.0)
- <img src='./images/logo_python.png' width='14px'>  [bidsphysio](None): Converts physio data to BIDS physiological recording
  <br>[![PyPI version](https://badge.fury.io/py/bidsphysio.svg)](https://pypi.org/project/bidsphysio/)[![Docker version](https://img.shields.io/docker/pulls/cbinyu/bidsphysio.svg?style=plastic)](https://hub.docker.com/r/cbinyu/bidsphysio/)
- <img src='./images/logo_python.png' width='14px'>  [phys2bids](https://phys2bids.readthedocs.io/en/latest/): Python3 library to format physiological files in BIDS.
  <br>[![PyPI version](https://badge.fury.io/py/phys2bids.svg)](https://pypi.org/project/phys2bids)
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
- [giga_connectome](https://github.com/bids-apps/giga_connectome): This is a BIDS-App to extract signal from a parcellation with nilearn, typically useful in a context of resting-state data processing.
  <br>[![Docker version](https://img.shields.io/docker/pulls/bids/giga_connectome.svg?style=plastic)](https://hub.docker.com/r/bids/giga_connectome)
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
- [BIBSnet](https://github.com/DCAN-Labs/BIBSnet): Utility for creating a nnU-Net anatomical MRI segmentation and mask with a infant brain trained model for the purposes of circumventing JLF within Nibabies.
  <br>[![Docker version](https://img.shields.io/docker/pulls/dcanumn/bibsnet.svg?style=plastic)](https://hub.docker.com/r/dcanumn/bibsnet)
- [fmriprep-fake](https://github.com/djarecka/fmriprep-fake): None
  <br>[![Docker version](https://img.shields.io/docker/pulls/djarecka/fmriprep_fake.svg?style=plastic)](https://hub.docker.com/r/djarecka/fmriprep_fake)
- [funcmasker-flex](https://github.com/khanlab/funcmasker-flex): BIDS App for U-net brain masking of fetal bold MRI
  <br>[![Docker version](https://img.shields.io/docker/pulls/khanlab/funcmasker-flex.svg?style=plastic)](https://hub.docker.com/r/khanlab/funcmasker-flex)
- [hippunfold](https://github.com/khanlab/hippunfold): BIDS App for Hippunfold (automated hippocampal unfolding and subfield segmentation)
  <br>[![Docker version](https://img.shields.io/docker/pulls/khanlab/hippunfold.svg?style=plastic)](https://hub.docker.com/r/khanlab/hippunfold)
- [mialsuperresolutiontoolkit](https://github.com/Medical-Image-Analysis-Laboratory/mialsuperresolutiontoolkit): The Medical Image Analysis Laboratory Super-Resolution ToolKit (MIALSRTK) consists of a set of C++ and Python processing and workflow tools necessary to perform motion-robust super-resolution fetal MRI reconstruction in the BIDS Apps framework.
  <br>[![Docker version](https://img.shields.io/docker/pulls/sebastientourbier/mialsuperresolutiontoolkit.svg?style=plastic)](https://hub.docker.com/r/sebastientourbier/mialsuperresolutiontoolkit)
- [micapipe](https://github.com/MICA-MNI/micapipe): micapipe from the Multimodal imaging and connectome analysis lab (https://mica-mni.github.io) at the Montreal Neurological Institute. Read The Docs documentation below
  <br>[![Docker version](https://img.shields.io/docker/pulls/micalab/micapipe.svg?style=plastic)](https://hub.docker.com/r/micalab/micapipe)
- [dmriprep](https://github.com/nipreps/dmriprep): dMRIPrep is a robust and easy-to-use pipeline for preprocessing of diverse dMRI data. The transparent workflow dispenses of manual intervention, thereby ensuring the reproducibility of the results.
  <br>[![Docker version](https://img.shields.io/docker/pulls/nipreps/dmriprep.svg?style=plastic)](https://hub.docker.com/r/nipreps/dmriprep)
- [fmripost-aroma](https://github.com/nipreps/fmripost-aroma): Functional MRI postprocessing with ICA-AROMA
  <br>[![Docker version](https://img.shields.io/docker/pulls/nipreps/fmripost-aroma.svg?style=plastic)](https://hub.docker.com/r/nipreps/fmripost-aroma)
- [fmripost-phase](https://github.com/nipreps/fmripost-phase): Postprocessing of complex-valued fMRI data
  <br>[![Docker version](https://img.shields.io/docker/pulls/nipreps/fmripost-phase.svg?style=plastic)](https://hub.docker.com/r/nipreps/fmripost-phase)
- [fmripost-rapidtide](https://github.com/nipreps/fmripost-rapidtide): Functional MRI postprocessing with Rapidtide
  <br>[![Docker version](https://img.shields.io/docker/pulls/nipreps/fmripost-rapidtide.svg?style=plastic)](https://hub.docker.com/r/nipreps/fmripost-rapidtide)
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
- [petdeface](https://github.com/openneuropet/petdeface): A nipype implementation of MiDeface used to deface PET and MR data as well as co-register the two modalities.
  <br>[![Docker version](https://img.shields.io/docker/pulls/openneuropet/petdeface.svg?style=plastic)](https://hub.docker.com/r/openneuropet/petdeface)
- [BIDSonym](https://github.com/PeerHerholz/BIDSonym): a BIDS app for pseudo-anonymization of neuroimaging data
  <br>[![Docker version](https://img.shields.io/docker/pulls/peerherholz/bidsonym.svg?style=plastic)](https://hub.docker.com/r/peerherholz/bidsonym)
- [aslprep](https://github.com/PennLINC/aslprep): Preprocessing of arterial spin labeling data
  <br>[![Docker version](https://img.shields.io/docker/pulls/pennlinc/aslprep.svg?style=plastic)](https://hub.docker.com/r/pennlinc/aslprep)
- [qsiprep](https://github.com/PennLINC/qsiprep): Preprocessing of diffusion MRI
  <br>[![Docker version](https://img.shields.io/docker/pulls/pennbbl/qsiprep.svg?style=plastic)](https://hub.docker.com/r/pennbbl/qsiprep)
- [qsirecon](https://github.com/PennLINC/qsirecon): Reconstruction of preprocessed diffusion MRI
  <br>[![Docker version](https://img.shields.io/docker/pulls/pennlinc/qsirecon.svg?style=plastic)](https://hub.docker.com/r/pennlinc/qsirecon)
- [xcp_d](https://github.com/PennLINC/xcp_d): Post-processing of fMRIPrep, nibabies, HCP, and DCAN BOLD derivatives for functional connectivity analysis
  <br>[![Docker version](https://img.shields.io/docker/pulls/pennlinc/xcp_d.svg?style=plastic)](https://hub.docker.com/r/pennlinc/xcp_d)
- [fitlins](https://github.com/poldracklab/fitlins): Fit Linear Models to BIDS Datasets
  <br>[![Docker version](https://img.shields.io/docker/pulls/poldracklab/fitlins.svg?style=plastic)](https://hub.docker.com/r/poldracklab/fitlins)
- [reproa](https://github.com/reprostat/reproa): BIDS App containing an instance of the ReproAnalysis (reproa) software (core only) running under Octave with minimum dependencies.
  <br>[![Docker version](https://img.shields.io/docker/pulls/reprostat/reproa.svg?style=plastic)](https://hub.docker.com/r/reprostat/reproa)
- [multiscalebrainparcellator](https://github.com/sebastientourbier/multiscalebrainparcellator): Multi-Scale Brain Parcellator, part of the Connectome Mapping Toolkit (CMTK), is a BIDS App that implements a full anatomical MRI processing pipeline, from raw T1w data to structural brain parcellation at five different scales.
  <br>[![Docker version](https://img.shields.io/docker/pulls/sebastientourbier/multiscalebrainparcellator.svg?style=plastic)](https://hub.docker.com/r/sebastientourbier/multiscalebrainparcellator)
- [gift-bids](https://github.com/trendscenter/gift-bids): None
  <br>[![Docker version](https://img.shields.io/docker/pulls/trends/gift-bids.svg?style=plastic)](https://hub.docker.com/r/trends/gift-bids)
<!-- APP ends -->

## Tools

Software packages for working with BIDS datasets.

<!-- TOOLS starts -->
- <img src='./images/logo_python.png' width='14px'> [ancp-bids](https://ancpbids.readthedocs.io/en/latest/): A Python package to read/write/query/validate BIDS datasets.
  <br> [![PyPI version](https://badge.fury.io/py/ancpbids.svg)](https://pypi.org/project/ancpbids/)
- <img src='./images/logo_python.png' width='14px'> [babs](https://pennlinc-babs.readthedocs.io/): BIDS App Bootstrap (BABS) is a reproducible, generalizable, and scalable Python package for BIDS App analysis of large datasets. It uses DataLad and adopts FAIRly big framework.
  <br> [![PyPI version](https://badge.fury.io/py/babs.svg)](https://pypi.org/project/babs/)
- <img src='./images/logo_python.png' width='14px'> [bids stats model](https://bids-standard.github.io/stats-models/index.html): Validate BIDS statistical model. To learn more the [BIDS stats model website](https://bids-standard.github.io/stats-models/index.html)
  <br> [![PyPI version](https://badge.fury.io/py/bsmschema.svg)](https://pypi.org/project/bsmschema/)
- <img src='./images/logo_python.png' width='14px'> [bids-cfood](https://gitlab.indiscale.com/caosdb/src/crawler-cfoods/bids-cfood): a module to handle BIDS dataset for the caosDB data crawler
- <img src='./images/logo_matlab.png' width='17px'> <img src='./images/logo_octave.png' width='16px'> [bids-matlab](https://bids-matlab.readthedocs.io/en/main/): MATLAB/Octave tools to interact with datasets conforming to the BIDS format
- <img src='./images/logo_python.png' width='14px'> [BIDS-pydantic](https://github.com/gold-standard-phantoms/bids-pydantic): Pulls a specified version of the BIDS schema and creates corresponding Pydantic models, which will provide BIDS data validation using Python type annotations. See also [BIDS-pydantic-models](https://pypi.org/project/BIDS-pydantic-models/).
  <br> [![PyPI version](https://badge.fury.io/py/BIDS-pydantic.svg)](https://pypi.org/project/BIDS-pydantic/)
- <img src='./images/logo_python.png' width='14px'> [bids2cite](https://bids2cite.readthedocs.io/en/latest/): package to interactively update `dataset_description.json` and generate citation files (for example `datacite.yml`) for BIDS datasets.
- <img src='./images/logo_python.png' width='14px'> [bids2table](https://childmindresearch.github.io/bids2table/bids2table.html): bids2table is a library for efficiently indexing and querying large-scale BIDS neuroimaging datasets and derivatives.
  <br> [![PyPI version](https://badge.fury.io/py/bids2table.svg)](https://pypi.org/project/bids2table/)
- <img src='./images/logo_R.png' width='18px'> [bidser](https://bbuchsbaum.github.io/bidser/): Working with Brain Imaging Data Structure in R
- <img src='./images/logo_python.png' width='14px'> [BIDSHandler](https://github.com/Macquarie-MEG-Research/BIDSHandler): Library for loading and manipulating BIDS compatible MEG data
- <img src='./images/logo_matlab.png' width='17px'> [Brainstorm](http://neuroimage.usc.edu/brainstorm/): MEG/EEG analysis package
- <img src='./images/logo_python.png' width='14px'> [clpipe](https://clpipe.readthedocs.io/en/latest/index.html): streamlined processing pipeline for MRI data centered around BIDS
- <img src='./images/logo_python.png' width='14px'> [cuBIDS](https://cubids.readthedocs.io/en/latest/): a Python package designed to facilitate reproducible curation of neuroimaging BIDS datasets
  <br> [![PyPI version](https://badge.fury.io/py/cubids.svg)](https://pypi.org/project/cubids/)
- <img src='./images/logo_python.png' width='14px'> [File mapper](https://github.com/DCAN-Labs/file-mapper): An easy tool to copy/move/symlink files from one directory to the other! Can be used to "convert" dataset to be BIDS compliant.
- <img src='./images/logo_python.png' width='14px'> [GUI dataset description generator](https://github.com/tolik-g/BIDS): GUI form that generates `dataset_description.json`
- <img src='./images/logo_python.png' width='14px'> [HALFpipe](https://github.com/HALFpipe/HALFpipe?tab=readme-ov-file#getting-started): wrapper for fmriprep and commong resting-stat and statistical analysis for fMRI
- [Hierarchical Event Descriptors (HED) online tools](https://www.hed-resources.org): Online tools for annotation, validation, summary, and assembly of event file contents and annotations.
- <img src='./images/logo_python.png' width='14px'> [Hierarchical Event Descriptors (HED) Python tools](https://www.hed-resources.org): HED libraries supporting schema development as well as annotation, validation, and analysis.
  <br> [![PyPI version](https://badge.fury.io/py/hedtools.svg)](https://pypi.org/project/hedtools/)
- <img src='./images/logo_matlab.png' width='17px'> [Lead-DBS](https://www.lead-dbs.org/): A toolbox facilitating Deep Brain Stimulation electrode reconstructions and computer simulations supports BIDS conversion and ingestion of BIDS datasets.
- <img src='./images/logo_python.png' width='14px'> [mne-bids](https://mne.tools/mne-bids/stable/index.html): collection of tools for converting magnetoencephalography (MEG) data into BIDS format, as well as some helper functions for creating the folders and metadata needed for a BIDS dataset.
- <img src='./images/logo_python.png' width='14px'> [mne-bids-pipeline](https://mne.tools/mne-bids-pipeline/stable/index.html): MNE-BIDS-Pipeline is a full-flegded processing pipeline for your MEG and EEG data. Under the hood, it uses MNE-Python.
- [neurobagel annotate](https://neurobagel.org/data_prep/): This tool allows you to create a machine readable data dictionary in .json format for a tabular phenotypic file in .tsv format ("Data table").
- [neurobagel query](https://neurobagel.org/public_nodes/): Neurobagel's query tool is a web interface for searching across a BIDS datasets based on various subject clinical-demographic and imaging parameters.
- <img src='./images/logo_python.png' width='14px'> [nipopy](https://nipoppy.readthedocs.io/en/latest/): Lightweight neuroimaging workflow manager to help with DICOM to BIDS conversion and running BIDS apps.
- [PRFmodel](https://github.com/vistalab/PRFmodel/wiki): a set of tools to fit population receptive field models to BIDS datasets
- <img src='./images/logo_python.png' width='14px'> [psychopy-bids](https://psychopy-bids.readthedocs.io/en/latest/): A psychopy plugin to help easily output a BIDS dataset, including `events.tsv` and `beh.tsv` files when running experiments with psychopy.
- <img src='./images/logo_python.png' width='14px'> [PyBIDS](https://bids-standard.github.io/pybids/): Python package to quickly parse / search the components of a BIDS dataset. It also contains functionality for running analyses on your data.
  <br> [![PyPI version](https://badge.fury.io/py/pybids.svg)](https://pypi.org/project/pybids/)
- <img src='./images/logo_R.png' width='18px'> [rbids](https://github.com/mathesong/rbids): aims to make BIDS datasets more easily accessible for packages written in R
- <img src='./images/logo_matlab.png' width='17px'> <img src='./images/logo_octave.png' width='16px'> [spm_2_bids](https://spm-2-bids.readthedocs.io/en/latest/): a tool convert SPM preprocessed output to BIDS derivatives (trying to follow [BEP12](https://bids.neuroimaging.io/bep012))
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

- [BEP004](https://bids.neuroimaging.io/bep004): Susceptibility Weighted Imaging
- [BEP020](https://bids.neuroimaging.io/bep020): Eye Tracking including Gaze Position and Pupil Size
- [BEP024](https://bids.neuroimaging.io/bep024): Computed Tomography scan
- [BEP026](https://bids.neuroimaging.io/bep026): Microelectrode Recordings
- [BEP032](https://bids.neuroimaging.io/bep032): Animal electrophysiology
- [BEP033](https://bids.neuroimaging.io/bep033): Advanced Diffusion Weighted Imaging
- [BEP036](https://bids.neuroimaging.io/bep036): Phenotypic Data Guidelines
- [BEP037](https://bids.neuroimaging.io/bep037): Non-Invasive Brain Stimulation
- [BEP038](https://bids.neuroimaging.io/bep038): Atlases
- [BEP039](https://bids.neuroimaging.io/bep039): Dimensionality reduction-based networks
- [BEP040](https://bids.neuroimaging.io/bep040): Functional Ultrasound
- [BEP042](https://bids.neuroimaging.io/bep042): Electromyography
- [BEP044](https://bids.neuroimaging.io/bep044): Stimuli

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
