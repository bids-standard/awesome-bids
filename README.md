# Awesome BIDS [![Awesome](https://awesome.re/badge.svg)](https://github.com/sindresorhus/awesome#readme)

<img src="https://raw.githubusercontent.com/bids-standard/bids-specification/master/BIDS_logo/BIDS_logo_white_transparent_background_crop.png#gh-dark-mode-only" alt="bids-logo" width="600"/>
<img src="https://raw.githubusercontent.com/bids-standard/bids-specification/master/BIDS_logo//BIDS_logo_black_transparent_background_crop.png#gh-light-mode-only" alt="bids-logo" width="600"/>

A curated list of awesome BIDS projects, proposals, apps and resources

## Contents

- [Apps](#apps)
- [Converters](#converters)
- [Documentation](#documentation)
- [Extension proposals](#extension-proposals)
- [Libraries](#libraries)


## Apps

BIDS Apps are also announced on [BIDS Apps](https://bids-apps.neuroimaging.io/apps/).

- [aa](http://github.com/BIDS-Apps/aa) (Automatic Analysis)
- [afni_proc](https://github.com/BIDS-Apps/afni_proc)
- ...

## Converters

Tools for converting data to/from BIDS from other standard or custom formats and layouts.

<!-- Converters starts -->

 ### MRI

- [Autobids](https://github.com/khanlab/autobids): Automated Dicom to BIDS and pipelines using compute canada. From the Center for Functional and Metabolic Mapping (CFMM) at Western’s Robarts Research Institute.
  [![Last commit](https://img.shields.io/github/last-commit/khanlab/autobids?style=plastic)](https://github.com/khanlab/autobids)
- [BIDScoin](https://bidscoin.readthedocs.io/en/stable/): BIDScoin converts your source-level neuroimaging data to BIDS
  ![](https://img.shields.io/badge/Python-blue.svg?style=plastic)[![Last commit](https://img.shields.io/github/last-commit/Donders-Institute/bidscoin?style=plastic)](https://github.com/Donders-Institute/bidscoin)[![PyPI version](https://badge.fury.io/py/bidscoin.svg)](https://pypi.org/project/bidscoin)[![License: GPL-3.0](https://img.shields.io/badge/License-GPLv3-blue.svg?style=plastic)](https://www.gnu.org/licenses/gpl-3.0)
- [BIDSconvertR](https://bidsconvertr.github.io/): The BIDSconvertR R package provides a user-friendly workflow with graphical user interfaces. It consists of the following steps: (i) convert DICOM data to NIfTI data using dcm2niix (ii) structure this data according to the BIDS specification (iii) provide the papayaWidget viewer for inspecting the images
  ![](https://img.shields.io/badge/R-grey.svg?style=plastic)[![Last commit](https://img.shields.io/github/last-commit/bidsconvertr/bidsconvertr?style=plastic)](https://github.com/bidsconvertr/bidsconvertr)[![License: GPL-3.0](https://img.shields.io/badge/License-GPLv3-blue.svg?style=plastic)](https://www.gnu.org/licenses/gpl-3.0)
- [bidsify](https://github.com/NILAB-UvA/bidsify): Tool to convert source MRI datasets to BIDS-compatible datasets.
  ![](https://img.shields.io/badge/Python-blue.svg?style=plastic)[![Last commit](https://img.shields.io/github/last-commit/NILAB-UvA/bidsify?style=plastic)](https://github.com/NILAB-UvA/bidsify)[![PyPI version](https://badge.fury.io/py/bidsify.svg)](https://pypi.org/project/bidsify)[![Docker version](https://img.shields.io/docker/pulls/lukassnoek/bidsify.svg?style=plastic)](https://hub.docker.com/r/lukassnoek/bidsify)
- [bidskit](https://github.com/jmtyszka/bidskit/blob/master/docs/QuickStart.md): Utility functions for working with DICOM and BIDS neuroimaging data.
  ![](https://img.shields.io/badge/Python-blue.svg?style=plastic)[![Last commit](https://img.shields.io/github/last-commit/jmtyszka/bidskit?style=plastic)](https://github.com/jmtyszka/bidskit)[![PyPI version](https://badge.fury.io/py/bidskit.svg)](https://pypi.org/project/bidskit)[![Docker version](https://img.shields.io/docker/pulls/jmtyszka/bidskit.svg?style=plastic)](https://hub.docker.com/r/jmtyszka/bidskit)[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=plastic)](https://opensource.org/licenses/MIT)
- [BIDSme](https://gitlab.uliege.be/CyclotronResearchCentre/Public/bidstools/bidsme/bidsme_example/-/tree/master/example1):
  ![](https://img.shields.io/badge/Python-blue.svg?style=plastic)[![Last commit](https://img.shields.io/github/last-commit/nbeliy/bidsme?style=plastic)](https://github.com/nbeliy/bidsme)[![License: GPL-2.0](https://img.shields.io/badge/License-GPLv2-blue.svg?style=plastic)](https://www.gnu.org/licenses/gpl-2.0)
- [BMAT](https://github.com/ColinVDB/BMAT):
  ![](https://img.shields.io/badge/Python-blue.svg?style=plastic)[![Last commit](https://img.shields.io/github/last-commit/ColinVDB/BMAT?style=plastic)](https://github.com/ColinVDB/BMAT)[![Docker version](https://img.shields.io/docker/pulls/colinvdb/bmat-dcm2niix.svg?style=plastic)](https://hub.docker.com/r/colinvdb/bmat-dcm2niix)[![License: GPL-3.0](https://img.shields.io/badge/License-GPLv3-blue.svg?style=plastic)](https://www.gnu.org/licenses/gpl-3.0)
- [BrkRaw](https://github.com/BrkRaw/brkraw): For a preclinical Bruker MRI scanner
  ![](https://img.shields.io/badge/Python-blue.svg?style=plastic)[![Last commit](https://img.shields.io/github/last-commit/BrkRaw/brkraw?style=plastic)](https://github.com/BrkRaw/brkraw)[![License: GPL-3.0](https://img.shields.io/badge/License-GPLv3-blue.svg?style=plastic)](https://www.gnu.org/licenses/gpl-3.0)
- [Clinica](https://aramislab.paris.inria.fr/clinica/docs/public/latest/):
  ![](https://img.shields.io/badge/Python-blue.svg?style=plastic)[![Last commit](https://img.shields.io/github/last-commit/aramis-lab/clinica?style=plastic)](https://github.com/aramis-lab/clinica)[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=plastic)](https://opensource.org/licenses/MIT)
- [dac2bids](https://github.com/dangom/dac2bids): Create a BIDS structure for a DICOM folder.
  ![](https://img.shields.io/badge/Python-blue.svg?style=plastic)[![Last commit](https://img.shields.io/github/last-commit/dangom/dac2bids?style=plastic)](https://github.com/dangom/dac2bids)
- [Data2Bids](https://github.com/SIMEXP/Data2Bids): Converts MRI files from extension supported by nibabel into NIfTI and convert them to BIDS
  ![](https://img.shields.io/badge/Python-blue.svg?style=plastic)[![Last commit](https://img.shields.io/github/last-commit/SIMEXP/Data2Bids?style=plastic)](https://github.com/SIMEXP/Data2Bids)[![PyPI version](https://badge.fury.io/py/data2bids.svg)](https://pypi.org/project/data2bids)[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=plastic)](https://opensource.org/licenses/MIT)
- [Dcm2Bids](https://unfmontreal.github.io/Dcm2Bids/): converts DICOM files using dcm2niix into BIDS
  ![](https://img.shields.io/badge/Python-blue.svg?style=plastic)[![Last commit](https://img.shields.io/github/last-commit/cbedetti/Dcm2Bids?style=plastic)](https://github.com/cbedetti/Dcm2Bids)[![PyPI version](https://badge.fury.io/py/Dcm2Bids.svg)](https://pypi.org/project/Dcm2Bids)[![Docker version](https://img.shields.io/docker/pulls/unfmontreal/dcm2bids.svg?style=plastic)](https://hub.docker.com/r/unfmontreal/dcm2bids)[![License: GPL-3.0](https://img.shields.io/badge/License-GPLv3-blue.svg?style=plastic)](https://www.gnu.org/licenses/gpl-3.0)
- [Explore ASL](https://exploreasl.github.io/Documentation/1.8.0/Tutorials-ASL-BIDS/): Convert DICOM and NIFTI data to the ASL-BIDS format.
  ![](https://img.shields.io/badge/MATLAB-orange.svg?style=plastic)[![Last commit](https://img.shields.io/github/last-commit/ExploreASL/ExploreASL?style=plastic)](https://github.com/ExploreASL/ExploreASL)
- [HeuDiConv](https://heudiconv.readthedocs.io/): A flexible DICOM converter for organizing brain imaging data into structured directory layouts
  ![](https://img.shields.io/badge/Python-blue.svg?style=plastic)[![Last commit](https://img.shields.io/github/last-commit/nipy/heudiconv?style=plastic)](https://github.com/nipy/heudiconv)[![PyPI version](https://badge.fury.io/py/heudiconv.svg)](https://pypi.org/project/heudiconv)[![Docker version](https://img.shields.io/docker/pulls/nipy/heudiconv.svg?style=plastic)](https://hub.docker.com/r/nipy/heudiconv)[![License: Apache 2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg?style=plastic)](https://opensource.org/licenses/Apache-2.0)
- [Horos (Osirix) export plugin](https://github.com/mslw/horos-bids-output): Horos plugin for BIDS output.
  [![Last commit](https://img.shields.io/github/last-commit/mslw/horos-bids-output?style=plastic)](https://github.com/mslw/horos-bids-output)[![License: GPL-3.0](https://img.shields.io/badge/License-GPLv3-blue.svg?style=plastic)](https://www.gnu.org/licenses/gpl-3.0)
- [niix2bids](https://github.com/benoitberanger/niix2bids): Use this package as a command line to organize your Nifti dataset into BIDS.
  ![](https://img.shields.io/badge/Python-blue.svg?style=plastic)[![Last commit](https://img.shields.io/github/last-commit/benoitberanger/niix2bids?style=plastic)](https://github.com/benoitberanger/niix2bids)[![License: GPL-3.0](https://img.shields.io/badge/License-GPLv3-blue.svg?style=plastic)](https://www.gnu.org/licenses/gpl-3.0)
- [OpenfMRI2BIDS](https://github.com/bids-standard/openfmri2bids): Convert OpenfMRI dataset to BIDS
  [![Last commit](https://img.shields.io/github/last-commit/bids-standard/openfmri2bids?style=plastic)](https://github.com/bids-standard/openfmri2bids)
- [PET2BIDS](https://github.com/openneuropet/PET2BIDS): Helps you convert your PET data! raw PET scanner files (for example ecat, dicom) and additional side file like excel sheets.
  ![](https://img.shields.io/badge/MATLAB-orange.svg?style=plastic)![](https://img.shields.io/badge/Python-blue.svg?style=plastic)[![Last commit](https://img.shields.io/github/last-commit/openneuropet/PET2BIDS?style=plastic)](https://github.com/openneuropet/PET2BIDS)[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=plastic)](https://opensource.org/licenses/MIT)
- [ReproIn](https://github.com/ReproNim/reproin): HeuDiConv-based turnkey solution: a setup for automatic generation of shareable, version-controlled BIDS datasets from MR scanners.
  ![](https://img.shields.io/badge/Python-blue.svg?style=plastic)[![Last commit](https://img.shields.io/github/last-commit/ReproNim/reproin?style=plastic)](https://github.com/ReproNim/reproin)[![Docker version](https://img.shields.io/docker/pulls/repronim/reproin.svg?style=plastic)](https://hub.docker.com/r/repronim/reproin)[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=plastic)](https://opensource.org/licenses/MIT)
- [SAMRI](https://doi.org/10.3389/fninf.2020.00005): Full stack Small Animal MRI data analysis package, including the `bru2bids` repositing pipeline, which can convert Bruker archives to the BIDS format. From the ETH and University of Zurich, with collaboration from MIT and Dartmouth College.
  ![](https://img.shields.io/badge/Python-blue.svg?style=plastic)![](https://img.shields.io/badge/shell-black.svg?style=plastic)[![Last commit](https://img.shields.io/github/last-commit/IBT-FMI/SAMRI?style=plastic)](https://github.com/IBT-FMI/SAMRI)
- [XNAT2BIDS](https://github.com/kamillipi/2bids): Simple xnat pipeline to convert DICOM scans to BIDS-compatible output (nii+json).
  ![](https://img.shields.io/badge/shell-black.svg?style=plastic)[![Last commit](https://img.shields.io/github/last-commit/kamillipi/2bids?style=plastic)](https://github.com/kamillipi/2bids)

 ### MEEG

- [BIDSme](https://gitlab.uliege.be/CyclotronResearchCentre/Public/bidstools/bidsme/bidsme_example/-/tree/master/example1):
  ![](https://img.shields.io/badge/Python-blue.svg?style=plastic)[![Last commit](https://img.shields.io/github/last-commit/nbeliy/bidsme?style=plastic)](https://github.com/nbeliy/bidsme)[![License: GPL-2.0](https://img.shields.io/badge/License-GPLv2-blue.svg?style=plastic)](https://www.gnu.org/licenses/gpl-2.0)
- [Biscuit](https://macquarie-meg-research.github.io/Biscuit/): GUI for easy MEG to BIDS conversion
  ![](https://img.shields.io/badge/Python-blue.svg?style=plastic)[![Last commit](https://img.shields.io/github/last-commit/Macquarie-MEG-Research/Biscuit?style=plastic)](https://github.com/Macquarie-MEG-Research/Biscuit)[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=plastic)](https://opensource.org/licenses/MIT)
- [EEG2BIDS](None): A tool for converting raw EEG and iEEG data into the BIDS standard data structure, prepared for LORIS (Longitudinal Online Research and Imaging System).
  ![](https://img.shields.io/badge/Javascript-yellow.svg?style=plastic)![](https://img.shields.io/badge/Python-blue.svg?style=plastic)[![Last commit](https://img.shields.io/github/last-commit/aces/EEG2BIDS?style=plastic)](https://github.com/aces/EEG2BIDS)
- [EEGLAB](https://eeglab.org/tutorials/04_Import/BIDS.html): <a href='https://github.com/arnodelorme/bids-MATLAB-tools'>See plugins</a>
  ![](https://img.shields.io/badge/MATLAB-orange.svg?style=plastic)[![Last commit](https://img.shields.io/github/last-commit/sccn/eeglab?style=plastic)](https://github.com/sccn/eeglab)
- [FieldTrip - data2bids](https://www.fieldtriptoolbox.org/example/bids/):
  ![](https://img.shields.io/badge/MATLAB-orange.svg?style=plastic)[![Last commit](https://img.shields.io/github/last-commit/fieldtrip/fieldtrip?style=plastic)](https://github.com/fieldtrip/fieldtrip)[![License: GPL-3.0](https://img.shields.io/badge/License-GPLv3-blue.svg?style=plastic)](https://www.gnu.org/licenses/gpl-3.0)
- [MNE-BIDS](https://mne.tools/mne-bids): MNE-BIDS is a Python package that allows you to read and write BIDS-compatible datasets with the help of MNE-Python.
  ![](https://img.shields.io/badge/Python-blue.svg?style=plastic)[![Last commit](https://img.shields.io/github/last-commit/mne-tools/mne-bids?style=plastic)](https://github.com/mne-tools/mne-bids)[![PyPI version](https://badge.fury.io/py/mne-bids.svg)](https://pypi.org/project/mne-bids)[![License: BSD-3-Clause](https://img.shields.io/badge/License-BSD_3--Clause-blue.svg?style=plastic)](https://opensource.org/licenses/BSD-3-Clause)
- [sovabids](https://sovabids.readthedocs.io/en/latest/): A Python package for the automatic conversion of EEG datasets to the BIDS standard, with a focus on making the most out of metadata.
  ![](https://img.shields.io/badge/Python-blue.svg?style=plastic)[![Last commit](https://img.shields.io/github/last-commit/yjmantilla/sovabids?style=plastic)](https://github.com/yjmantilla/sovabids)

 ### physiological

- [BIDScoin](https://bidscoin.readthedocs.io/en/stable/): BIDScoin converts your source-level neuroimaging data to BIDS
  ![](https://img.shields.io/badge/Python-blue.svg?style=plastic)[![Last commit](https://img.shields.io/github/last-commit/Donders-Institute/bidscoin?style=plastic)](https://github.com/Donders-Institute/bidscoin)[![PyPI version](https://badge.fury.io/py/bidscoin.svg)](https://pypi.org/project/bidscoin)
- [bidsphysio](None): Converts physio data (CMRR, AcqKnowledge, Siemens PMU) to BIDS physiological recording
  ![](https://img.shields.io/badge/Python-blue.svg?style=plastic)[![Last commit](https://img.shields.io/github/last-commit/cbinyu/bidsphysio?style=plastic)](https://github.com/cbinyu/bidsphysio)[![PyPI version](https://badge.fury.io/py/bidsphysio.svg)](https://pypi.org/project/bidsphysio/)[![Docker version](https://img.shields.io/docker/pulls/cbinyu/bidsphysio.svg?style=plastic)](https://hub.docker.com/r/cbinyu/bidsphysio/)
- [phys2bids](https://phys2bids.readthedocs.io/en/latest/): Python3 library to format physiological files in BIDS.
  ![](https://img.shields.io/badge/Python-blue.svg?style=plastic)[![Last commit](https://img.shields.io/github/last-commit/physiopy/phys2bids?style=plastic)](https://github.com/physiopy/phys2bids)[![PyPI version](https://badge.fury.io/py/phys2bids.svg)](https://pypi.org/project/phys2bids)

 ### others

- [convert-eprime](https://github.com/tsalo/convert-eprime): Python functions to convert E-Prime files to csvs. Not currently being developed.
  ![](https://img.shields.io/badge/Python-blue.svg?style=plastic)[![Last commit](https://img.shields.io/github/last-commit/tsalo/convert-eprime?style=plastic)](https://github.com/tsalo/convert-eprime)[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=plastic)](https://opensource.org/licenses/MIT)
- [DCM2NIIx](https://github.com/neurolabusc/dcm2niix): dcm2nii DICOM to NIfTI converter
  [![Last commit](https://img.shields.io/github/last-commit/neurolabusc/dcm2niix?style=plastic)](https://github.com/neurolabusc/dcm2niix)
- [DICM2NII](https://github.com/xiangruili/dicm2nii): dcm2nii DICOM to NIfTI converter
  ![](https://img.shields.io/badge/MATLAB-orange.svg?style=plastic)[![Last commit](https://img.shields.io/github/last-commit/xiangruili/dicm2nii?style=plastic)](https://github.com/xiangruili/dicm2nii)
- [sim2bids](https://github.com/dissagaliyeva/sim2bids): GUI to easily convert simulation results to BIDS format, according to <a herf="https://bids.neuroimaging.io/bep034" target="_blank">   BEP 34 </a>.
  ![](https://img.shields.io/badge/Python-blue.svg?style=plastic)[![Last commit](https://img.shields.io/github/last-commit/dissagaliyeva/sim2bids?style=plastic)](https://github.com/dissagaliyeva/sim2bids)[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=plastic)](https://opensource.org/licenses/MIT)
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

- [BIDS-MATLAB](https://github.com/bids-standard/BIDS-MATLAB)
- [PyBIDS](https://github.com/bids-standard/pybids)
- ...

<!-- TOOLS starts -->
<!-- TOOLS ends -->

## Contribute

Contributions welcome! Read the [contribution guidelines](contributing.md) first.
