# LCI User's Guide to Printing on the Peopoly Moai:
***


*Stereolithography* (SLA) printing relies on a vastly different mechanism than the *Fused Deposit Modelling* (FDM) printers such as the Ultimaker 3 and the Prusa Mk. III, and thus requires a different workflow when preparing models for printing. Many of the intuitions developed for FDM printing (eg. the largest flat side should be flat on the buildplate) are counterproductive for bottom-up SLA printers such as the **Peopoly Moai 130**. The following is a brief guide to setup, slicing, and operation for the Moai, with troubleshooting for some common print errors. 

![[Pasted image 20220715122340.png|Peopoly Moai (130mm)]]

***
### I: Safety

Consult the MSDS for all materials prior to usage. The MSDS for the standard Peopoly Moai resin we have used to date is attached at the bottom of the document. The following is general advice, and not equivalent to reading the relevant safety documentation.

Avoid skin contact with resin. Wear protective gloves when handling and when removing objects from the buildplate. If contact does occur, rinse the affected area as soon as possible. Slight irritation (acute contact dermatitis) may occur. Exposure to skin for several minutes may result in long-term irritation. 

Please do not ingest the resin. 

The Moai uses a 405 nm UV LED laser to cure the resin while printing. While in operation, ensure that the door is locked to avoid accidental exposure to the laser. Use protective eyewear when appropriate. 

Once completed, prints are cured in isopropyl alcohol. Avoid leaving this container open for long periods of time as it is a respiratory hazard. 

### II: Software Requirements

Peopoly has its own slicing software, *Asura3D*, designed specifically for use with the Moai. Unfortunately, the software is poorly maintained, and requires manual registration and approval from the creator through a feature in the app which is currently broken. 

Until I can get in touch with said creator, there is an alternate workflow in place using several different programs (WIP as options are explored): 

- **Autodesk MeshMixer** - used to auto-orient the model for optimal adhesion, as well as autogeneration of SLA supports (needs very different support philosophy from FDM)
- **Ultimaker Cura** -  used to slice and produce .gcode, which the Moai also requires. Needs a very specific printer profile which can be downloaded from github, otherwise it will print in the FMD way (slight vertical motions in-between each line, will cause print to fail miserably)
- **Peopoly Moai 130 Printer Profile** -  found here: https://github.com/peopoly3d/moai-cura/tree/master contains all settings needed in Cura to slice for the Moai. Ensure that you do not change the infill - 70% or higher is mandatory for SLA, and has nothing to do with structural stability. Thus far we have used the $40 \ \mu\text{m}$ profile with moderate success (Cura version 3.5.1). 

p


### III: Slicing

### IV: Operation

### IV: Maintenance

### V: Troubleshooting

### VI: Appendix

Resin MSDS:
![[Peopoly Resin MSDS 2022.pdf]]