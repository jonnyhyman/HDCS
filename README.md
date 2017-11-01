**Human Digital Control Station [HDCS]**
----------
![View](https://photos-4.dropbox.com/t/2/AADOTByn3Gc_uAQeEVfd4g9bEARQ9L2q0yWo9NMQgamDQw/12/9419831/png/32x32/1/_/1/2/hdcs.png/EJLXggcYm_YOIAcoBw/4bCbrWV41BHylh2dO5toJZT6UY5ltV0EtUFjWbhFklQ?size=1600x1200&size_mode=3)

**HDCS is a command, control, and instrumentation interface.**

*Designed initially for use with testing small hybrid rockets, it can be expanded or reduced to fit the needs of many other instrumentation and control applications.*

**Check out the video demo at this link!**
[![Demo Video](https://img.youtube.com/vi/-lvVTYNzDvo/0.jpg)](https://www.youtube.com/watch?v=-lvVTYNzDvo)

To run, clone the git repository on your local machine, then in a command line :

    python __HDCS__.py

You may find you are missing the **dependencies**: 

* Python 3.6.2+
* PyQt5
   * pyqtgraph
   * numpy
* Installed fonts found in /fonts folder

**Architecture**
----------
This code is intimately intertwined with a number of other systems, chief of which is ADCS. The [ADCS code can be found here](https://github.com/jonnyhyman/ADCS/).

![Structure](https://photos-2.dropbox.com/t/2/AAAR0l0M-Gal1o5NNPScqEbjMYxzwnbddSYxf0zj3ZARug/12/9419831/png/32x32/1/_/1/2/arch.png/EJLXggcYm_YOIAcoBw/2W07iQ74YkNBXnlrxBmlB6-t9DTfnCTmYhg4UvuL_KM?size=1600x1200&size_mode=3)

Ultimately, the micro-controllers (far right of diagram) take the majority of the data in, and actuate the commands.

*Note: One can definitely separate each module of HDCS from the ADCS / Micro grand scheme. Modules each continue to be written to be as portable as possible.*

**UI Design & Automatic Refactoring Features**
----------
**The ([Qt Creator](https://www1.qt.io/download/)) program is used to add features to the GUI,** and also to signal to the program which variables should be shown on screen - in "displays" - and which should not.

**A key finding in the creation of HDCS** is that updating Qt Stylesheets to reflect the state of a variable (in limits, or out of limits), is seriously too slow for the scale of QLabels on-screen. Because of this, we refactor the GUI on each startup.

**UI refactoring** refers to the conversion of all the QLabels which are automatically *identified* as "color-able" (see definitions below), *into highly efficient* **QGraphicsItems**. 

In addition to the performance improvements, this also allows us to drag and drop any displays as we wish.

---

The creation of a new instrumentation variable into the interface is very simple.
---

1. Open the MainWindow GUI file (mainwindow.ui) found in the "design_files" folder. *Note that this is a Qt Creator / Qt Designer file, so get that program first to edit it.*

2. Add the new display window as a QLabel object
3. Change the ObjectName to exactly the same as the "key" it will have in the state variable dictionary, for example: *'countdown_time'*

3.  Pick which display style you would like to have
	* Color-State Display ***"csd"*** (color **text** to reflect if in or out of limits)
		* csd0 : do not display numeric state in text
		* csd1 : display numeric state in text
	
	* Background-color-State Display ***"bsd"*** (color **background** to reflect if in or out of limits)
		* bsd0 : do not display numeric state in text
		* bsd1 : display numeric state in text
		
4. Save the file and convert to .py with the Qt -> PyQt utility (see .bat files in design_files folder)

5.  Add the instrumentation variable to Definitions.State as a new key, value pair in the dictionary.
6. Add the instrumentation's safe limits in State_Limits if needed
7. Add the key to the Definitions.Control_Keys variable (if the key is not instrumentation)


More documentation coming soon!

> Written with [StackEdit](https://stackedit.io/).
