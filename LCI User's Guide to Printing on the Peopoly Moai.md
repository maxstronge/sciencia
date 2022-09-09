# LCI User's Guide to Printing on the Peopoly Moai:
***
The **Peopoly Moai 130** is a bottom-up SLA printer. The Moai takes GCode files as input for printing, like FDM printers such as the Prusa Mk.III or the Ultimaker 3. However, many of the intuitions developed for FDM printing (eg. the largest flat side should be flat on the buildplate) are counterproductive for SLA printing, and as such SLA printers requrire unique considerations. The following is a brief guide to setup, support generation, slicing, and operation for the Moai, with troubleshooting for some common print errors. 

![[moai_pic.png]]

***
### I: Safety

Consult the MSDS for all materials prior to usage. The MSDS for the standard Peopoly Moai resin we have used to date is in the Prototyping folder on the server. The following is general advice, and not equivalent to reading the relevant safety documentation.

Avoid skin contact with resin. Always wear protective gloves when handling and when removing objects from the buildplate. If contact does occur, rinse the affected area as soon as possible. Slight irritation (acute contact dermatitis) may occur. Exposure to skin for several minutes may result in long-term irritation. 

The Moai uses a 405nm 140mW UV LED laser to cure the resin while printing. While in operation, ensure that the door is locked to avoid accidental exposure to the laser. The door panels block UV light, but watching the laser operate inside for extended periods of time may still cause damage. Use protective eyewear when appropriate. 

Once completed, prints are cured in isopropyl alcohol.  

### II: Software Requirements

Peopoly has its own slicing software, *Asura3D*, designed specifically for use with the Moai. Unfortunately, the software is poorly maintained, and requires manual registration and approval from the creator through a feature in the app which is currently broken. 

Until I can get in touch with said creator, there is an alternate workflow in place using several different programs (WIP as options are explored): 

- **Autodesk MeshMixer** - used to auto-orient the model for optimal adhesion, as well as autogeneration of SLA supports (needs very different support philosophy from FDM)
- **Ultimaker Cura** -  used to slice and produce .gcode, which the Moai also requires. Needs a very specific printer profile which can be downloaded from github, otherwise it will print in the FMD way (slight vertical motions in-between each line, will cause print to fail miserably)
- **Peopoly Moai 130 Printer Profile** -  found here: https://github.com/peopoly3d/moai-cura/tree/master contains all settings needed in Cura to slice for the Moai. Ensure that you do not change the infill - 70% or higher is mandatory for SLA, and has nothing to do with structural stability. Thus far we have used the $40 \ \mu\text{m}$ profile with moderate success (Cura version 3.5.1). 


### III: Orientation, Overhangs, and Slicing

Slicing and preparing models for SLA printing has a set of unique challenges and considerations, as mentioned above. Because the Moai is a bottom-up printer, the model will print upside-down, and care must be taken to ensure that the model is adequately supported during this process. 

The generation of these supports is handled by **Autodesk Meshmixer**. While Meshmixer is no longer actively maintained by Autodesk due to a number of its features overlapping with Fusion360, it's still available for Windows for free at https://www.meshmixer.com/, and makes the setup for SLA printing very easy.  Launching Meshmixer will result in this home screen:

![[Pasted image 20220902104458.png]]
1. Click the **Import** button to add your model to Meshmixer. Most of the time you'll want this to be a .STL file, but it can also open .OBJ and .PLY point cloud files. For the sake of this example I've imported the coupler from the NIV masking project.
2. Before we do anything with it, we'll need to add a printer profile to Meshmixer for the Moai.
   
	a. Click **File** > **Preferences**, then **Printers** > **Add**.
	
	   ![[Pasted image 20220902105036.png]]
	
	**b**. Enter the information for the printer as follows (adding a direct path to Cura is unnecessary, but will allow you to export and open in Cura in one click).
	
	   ![[Pasted image 20220902105228.png]]
	   No command line arguments are necessary, and the default .STL is a good format. Click **Apply** to return to the previous screen.

	**c**. Click on **Make None Visible** to hide all the printers currently active, then find the Moai profile in the list and click the checkmark next to it:
	
	   ![[Pasted image 20220902105421.png]]
	
	**d**. Click **Done**. The Moai profile should now be visible in the top-right corner of the Meshmixer window. 
	
![[Pasted image 20220902105536.png]]

3. We can now create a preset for the settings needed to create the necessary supports. With your model loaded, click on the **Analysis** button:
   
   ![[Pasted image 20220902113419.png]]
   This will bring up a series of menus on the left-hand side of the window. 
   
4. Select **Overhangs**. This section is responsible for generating supports.
   
   ![[Pasted image 20220902113716.png]]
   
   The following windows should appear:
   
   ![[Pasted image 20220902113856.png]]

5. Click the two arrow icons next to **Support Generator** and **Advanced Support** to view all the settings. Set them as indicated in the following screenshot:
   
   ![[Pasted image 20220902115109.png]]
   
   (For details regarding each setting and what it does, see the Appendix). 

6. Once all settings have been changed, click on the dialog box above *Angle Thresh*, then click **Save Current...**. Give this setting preset a name, like Moai. For future prints, this can be selected from the list instead of manually changing all settings. 
7. One last special consideration for SLA printing: the orientation of the model. Bottom-up printers lift the buildplate out of the resin vat layer by layer, and this creates a 'peel' force that can often cause layers of the model to split (this is referred to as *delamination*). The greater the flat surface area parallel to the build plate, the greater the peel force experienced by the model, and the more likely it is to delaminate. To prevent this, we print at an angle to minimize the amount of peel force experienced. For prints with large flat faces, 45 degrees usually does the trick. Some experimentation may be necessary as this is not consistent between models of different geometry. 
   
   To have Meshmixer automatically find the optimal orientation for your specific model, click on the **Orientation** button under **Analysis**, the same menu as the Overhang settings:
   
   ![[Pasted image 20220902122014.png]]
   
   You can change the angle as needed, and click **Update** to see the results. When you're satisfied with the orientation of the model, click **Accept**.

7. Now, return to the **Overhangs** menu, select the preset created earlier, and click **Generate Support**:
   
   ![[Pasted image 20220902122336.png]]
   
   The supports will be generated. This may take a few minutes. Click **Done** when satisfied.
   
   ![[Pasted image 20220902122656.png]]
   
8. We can now export the model with the supports included. If you included the path to Cura in the printer profile in step 2b, click the **Print** button at the bottom of the left-hand sidebar. This will automatically open Cura with your model imported. Otherwise, simply click **Export**, export as a .STL (binary, not ASCII), and open it in Cura normally. 
9. If this is the first time using Cura to slice for the Moai, you will need to set up a profile for the printer. Click **Preferences** on the top bar, then **Configure Cura...**:
   
   ![[Pasted image 20220902125127.png]]

10. Select **Printers** from the dialog on the left, then click **Add**:
    
    ![[Pasted image 20220902125306.png]]
11. Under *Add a non-networked printer*, scroll until you find Peopoly, then select the Moai. Give the printer profile a name, then click **Add**:
    
    ![[Pasted image 20220902125433.png]]
    
12. Once the printer profile has been created, activate it with the **Activate** button, then check the **Machine Settings**. Ensure they match the settings displayed in the following picture:
    
    ![[Pasted image 20220902125635.png]]

Click **Close** when finished. Cura should now show an annotated representation of the Moai buildplate, with the door, corners, and sides labelled:

![[Pasted image 20220902125831.png]]

Nearly ready for printing!

13. The final preparatory step is to import the Print Settings profile for the Moai into Cura. The link to the GitHub repo containing the settings were given above. First, click on the print settings bar (where it says *Extra High - 0.02mm* in the screenshot above.) 
14. Click on the **Extra High** profile to expand the drop-down dialog, then select **Manage Profiles...**
    ![[Pasted image 20220902130718.png]]
    
14. Click **Import**:
    
    ![[Pasted image 20220902130920.png]]
    
15. Navigate to the location of the .curaprofile downloaded from the GitHub, select it, then click **Open**. The Moai profile for Cura should now be visible. Select it, then click the **Activate** button to activate the profile:
    
    ![[Pasted image 20220902131205.png]]
    
Cura is now ready to slice models specifically for the SLA. Many of the settings may seem strange, but they are all optimized for SLA printing - for example, the infill must not be set to less than 70% in Cura, as this will cause leaking, even though the infill works differently on the Moai than on FDM printers. Just trust it!

16. If you haven't already, import your .STL that you generated from Meshmixer. Ensure that the new custom profile is activated, then click **Slice** in the lower right-hand corner (this might take a while):
    
    ![[Pasted image 20220902131810.png]]
    
    Note that Cura tells you that the print will require 0g of filament (which is true), and that it will take much longer than you expected (which is false). Typically the time shown in Cura is approximately 4x the duration it will actually take on the Moai, if not longer. For example, the print seen in the above screenshot took just over 4 hours to complete. 

17. Click **Save to File** to export a .gcode file which can be loaded onto an SD card and inserted into the Moai.

### IV: Printer Operation

![[Pasted image 20220902134755.png]]


The inside of the Moai looks like this:

![[20220902_133743.jpg]]

The silver object on the top is the build plate, which will lower into the resin contained in the vat below while printing. 

Before operating, ensure that there is enough resin in the tank, and give it a gentle stir with the plastic scraper. Take care not to apply too much pressure to the bottom of the tank, as this is where the special FEP layer is that enables printing, and it's a pain to replace.  Some air bubbles will be introduced - these will settle on their own in a couple of minutes. If you notice any lumps of partially cured resin in the tank, carefully remove them with forceps.

![[20220902_133748.jpg]]

Once the resin vat has been stirred and cleared of debris, ensure that the build plate is clean, using a microfiber cloth to avoid scratching the surface. It is important that no resin, cured or uncured, is left on the surface before printing. If needed, remove the tank for easier access. To do this, note the black knob on the top of the buildplate:

![[20220902_133753.jpg]]

Loosening this knob will allow you to carefully remove the buildplate by sliding it directly back, towards yourself. This allows for easier cleaning and is also useful for removing the completed print from the buildplate. To replace, simply slide the buildplate back on and hand-tighten the knob. 

The Moai does not have any USB ports or wireless capability - the only way to load files onto it is via SD card, as mentioned. Ensure your .gcode file has a readable, identifiable name, load it onto the SD card, and insert the SD into the slot in the printer, to the left of the power button. 

![[20220902_133722.jpg]]

Power on the Moai. Ensure that while the Moai is powered on and in operation, the door is closed and locked at all times, with the key removed from the lock. 

Use the wheel to select **Print**, navigate to the **gcode** folder, and select your model. Confirm if necessary, and the print will start. At this time, the UV light inside will activate - do **NOT** look inside through the door without protective eyewear. 

The screen underneath the power button will display the current layer, the total amount of layers, and the time elapsed. Unfortunately, it does not display an estimated time of completion - check in on it occasionally to get a sense of how close it is to being done, and try not to let it sit for too long on the buildplate once completed. 

When the print is complete, the buildplate will return to its position at the top of the chamber. At this time, it is safe to open the door, remove the buildplate, and gently detach the model from the surface with the plastic scraper. Do **NOT** use a metal one, as it will scratch the buildplate and cause complications. 


### V: Washing and Curing

Unlike FMD printers, SLA prints are not finished after the completion of the print. Immediately after printing, models retain a moderate amount of goopy uncured resin from the vat, and are not fully solidified, remaining somewhat soft and malleable until post-curing has taken place. The Prusa CW1 takes care of both the washing and the curing components of the SLA printing process. 

![[20220902_142247.jpg]]

Remove the lid of the isopropyl alcohol tank, and insert the tank onto the rails of the CW1. Place the mesh basket inside the tank, then carefully lower your model into the mesh basket. 

![[20220902_142138 (2).jpg]]

![[20220902_142208 (2).jpg]]
Close the lid of the CW1. It will detect that the tank has been inserted, and will give you the option to **Start washing**. Select this option and wait for the process to complete. A magnetic stir rod is included at the bottom of the tank to facilitate good coverage. 


![[20220902_142330.jpg]]

Once the wash has been completed, remove the model and carefully dry the model of excess IPA. 

This is a good time to remove supports with a pair of clippers, as the uncured resin has been removed, but the model is still malleable before the final curing process.

Once all supports are removed, remove the IPA tank from the CW1. Place the model in the center of the circular metal plate. Close the CW1, and the device will present you with an option to **Start curing**:

![[20220902_142318.jpg]]

Select this option and wait for the process to complete. Use caution and ensure that the CW1 is not opened during this procedure, as the curing process uses UV light as well. 

Once that timer expires, you are safe to remove your print - it's done! 

### VI: Troubleshooting

##### Levelling (model is skewed/does not stick):
If prints are not adhering to the plate properly, there may be an issue with the levelling. The SD card contains the test print for the levelling process detailed here: http://wiki.peopoly.net/doku.php?id=moai:leveling


##### Temperature (laser is running but resin doesn't seem to cure):

The resin for SLA printing needs to be maintained at a certain temperature, or it will not cure properly. Minimum temp: 25C. 30-35C ideal. Check this, especially in the winter -  many people have added a very simple heater to the inside of the printer that works quite well,.

##### Profile (miscellaneous errors):

Take extra care to ensure that you are using the very specific cura profile for the Moai, as downloaded from the github. If anything is changed it may cause very unpredictable errors. For example, default FDM printers have a little z-hop that they do in-between layers that will utterly ruin SLA prints. Speed, temperature, infill, everything is dialed in very specifically to work for the Moai. 


##### Delamination (parts of model fall off partway through):
Delamination is often caused by an insufficient amount of supports. Go back to meshmixer and add more by increasing the density, or, if it seems like the tips are very small, increase their diameter so there is more surface area for the model to attach to. 








### VII: Appendix

**Meshmixer Overhang Parameters:**

Meshmixer decides what constitutes an overhang by comparing a downward vector and the normal vector to faces of your model, as in the figure below:

![[Pasted image 20220902115737.png]]
- Angle Thresh:
	- Determines the angle between normal and down vectors that will be treated as an overhang. Any angle less than Angle Thresh will receive generated supports. 
- Contact Tol:
	- Tolerance for detecting whether the face is already resting on the ground plane. Keep this at zero for complicated shapes.
- Y-Offset: 
	- Distance from ground plane object. Very important - elevating off the bed and having the print rest on supports produces much more consistent results than having the object itself rest on the buildplate.
- Max Angle:
	- Maximum draft angle of the generated support posts
- Density:
	- adjusts spacing of support posts
- Layer height:
	- height of your printer
- Base, Post, Tip diameter:
	- self-explanatory. The support posts look like this:
	  
	  ![[Pasted image 20220902120139.png]]
- Allow Top Connections:
	- If checked, allows support bases to be printed on the model itself. If unchecked, all support bases will be on the ground plane. Similar to 'build plate only' for support locations in Cura.
- Optimization:
	- Controls how much optimization is done in terms of placing supports to minimize print time. 
- Solid Min Offset:
	- When performing the 'convert to solid' operation, which should be unnecessary if you've prepared your .STL correctly, sets a minimum 'buffer zone' around which no supports will be printed. 
- Tip Height / Base Height:
	- self-explanatory, no need to adjust 
- Strut Density:
	- Controls how many struts/forks are created on the same post
- Post Sides:
	- Number of sides the cylindrical post has. More = more cylindrical. 