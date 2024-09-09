# 💫🌟 Physics Master's Project - Data Analysis of a Cosmological Simulation

## Objective

In this project, I analysed data from the IllustrisTNG simulation to validate a contested theory:
* The collapsar model predicts that long gamma-ray bursts (LGRBs) require a local metallicity of less than 30% solar metallicity.
* LGRBs are mostly observed from host galaxies with metallicity greater than this limit. 
* This discrepancy means the collapsar model could be wrong!
* Due to technological constraints, we cannot currently measure the local metallicity of LGRBs.
* I aimed to analyse data from an advanced cosmological simulation to decide the validity of the collapsar model.

The sections below will explain additional details on the data and technologies utilized.

## Table of Contents

- [Dataset Used](#dataset-used)
- [Technologies](#technologies)
- [Methods](#methods)
- [Results](#results)
- [Still interested?](#still_interested)

## Dataset Used

* This project used the TNG50-1 simulation thanks to its superior mass resolution, making it useful for investigating small-scale processes, which LGRBs are: they're on the stellar scale as opposed to the galaxy scale.
* The data is organised into one hundred snapshots at different redshifts (used to measure distance of astronomical objects, also can be related to the age of an observed object, so can be thought of simulation-time snapshots).
* Each snapshot has a set of attributes, such as redshift, number of each type of particle, and a catalogue of subhalos (galaxies) and halos (galaxy clusters).
* Each subhalo has a long list of attributes, including an associated star formation rate (SFR), mass and metallicity. The mass and metallicity are both divided into different components such as gas and stars.
* This information is also present at the "cell"-level, for intra-galaxy analysis.

More info about the simulation can be found on the website: https://www.tng-project.org

## Technologies

The following technologies are used to build this project:
- Language: Python
- Libraries: illustris_python, numpy, matplotlib, scipy
- IDE: Spyder 
- Storage: University Servers

## Methods

* The objective was to obtain the necessary data from TNG, using a model to select galaxies likely to be GRB hosts, and compare this data with observations. 
* Out of the hundred available snapshots, snapshot 33 (at redshift z ~ 2), was chosen for it being the most common redshift for observed LGRBs.
* No GRBs have been observed from galaxies with very low stellar mass or from low SFR (passive) galaxies so these were filtered out of the data.
* Within each galaxy remaining in the data, the cells were also filtered to only keep the star-forming cells.
* Two variables were calculated:
    - F = Fraction of star-forming cells with metallicity below the collapsar model limit
    - T = Total star formation rate in these low-metallicity cells
* The product of these variables was used as the weighting for the random selection of 1000 galaxies as GRB hosts, to match the collapsar model's predictions.

## Results

* The metallicities, star formation rates, and stellar masses of the randomly selected galaxy sample were plotted as cumulative distribution functions to be compared with observation.
* The model that best-matched the observational data, had a metallicity limit of 30% solar (just like the collapsar model) and had a greater weighting on F, so it was more likely to select galaxies with a high fraction of star-forming cells below the metallicity limit.
* Basically, the model most like the collapsar model selected simulation data most comparable to real-life observations, and hence, **the collapsar model was validated, as it agreed with real-life observational data.**

| Observation | Simulation (Collapsar Model) |
| ------------- | ------------- |
| ![image](https://github.com/user-attachments/assets/07604a85-6f4a-47c2-ac87-15a518d8e7f5) | ![image](https://github.com/user-attachments/assets/f9eb33fd-eeea-4bdd-b3a6-295656f1efbc) |
| ![image](https://github.com/user-attachments/assets/e84ad3f5-e329-413a-a670-88a843552f4e) | ![image](https://github.com/user-attachments/assets/3c8fcb77-52cc-4481-af16-dca5a75b70a3) |
| ![image](https://github.com/user-attachments/assets/59e92a35-a9ac-42b3-9833-667c4703fb50) | ![image](https://github.com/user-attachments/assets/3807eecc-c3a8-4e71-91f4-81d6edadee01) |

The observational data was taken from: Palmerio JT, et al. Are long gamma-ray bursts biased tracers of star formation? Clues from the host galaxies of the Swift/BAT6 complete sample of bright LGRBs. Astron Astrophys. 2019 Mar;623(A26):1-18.

## Still interested?

* For as many details as possible on this project, read the [report](Report.pdf).
* For more details, but in a less wordy format, view the [PowerPoint presentation](Presentation.pptx).
* For a look into the type of python code written for this project, see the [code example](code_example.py).

***
