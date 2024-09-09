# 💫🌟 Physics Master's Project - Data Analysis of a Simulation

## Objective

In this project, I analysed data from the IllustrisTNG simulation to validate a contested theory:
* The collapsar model predicts that long gamma-ray bursts (LGRBs) require a local metallicity       of  less than 30% solar metallicity.
* LGRBs are mostly observed from host galaxies with metallicity greater than this limit. 
* This discrepancy means the collapsar model could be wrong!
* Due to technological constraints, we cannot currently measure the local metallicity of LGRBs.
* I aimed to analyse data from an advanced cosmological simulation to decide the validity of the collapsar model.

The sections below will explain additional details on the data and technologies utilized.

## Dataset Used

This project used the TNG50-1 simulation thanks to its superior mass resolution, making it useful for investigating small-scale processes, which LGRBs are: they're on the stellar scale as opposed to the galaxy scale.
The data is organised into one hundred snapshots at different redshifts (used to measure distance of astronomical objects, also can be related to the age of an observed object, so can be thought of simulation-time snapshots).
Each snapshot has a set of attributes, such as redshift, number of each type of particle, and a catalogue of subhalos (galaxies) and halos (galaxy clusters). Each subhalo has a long list of attributes, including an associated star formation rate (SFR), mass and metallicity. The mass and metallicity are both divided into different components such as gas and stars. This information is also present at the particle-level, for intra-galaxy analysis.

More info about the simulation can be found on the website: https://www.tng-project.org

## Technologies

The following technologies are used to build this project:
- Language: Python
- Libraries: illustris_python, numpy, matplotlib, scipy
- IDE: Spyder 
- Storage: University Servers

## Outcome



***
