# Smart manufacturing LAB - AVATAR
### Practical guide for the development of a VR manufacturing system - A.Y. 2022/2023
#### Contents


    1. Introduction
    2. Digital tools
        MS Excel
        GitHub
        Autodesk Inventor
        Notepad++
        VEB.js
        JSON
    3. General scheme – IDEF0 diagram
    4. Creation of an online repository or a local folder
    5. Definition and creation of the 3D models
        How to obtain the 3D models
        Conventions
        Shaping the models
    6. Generation of the 3D environment
    7. Visualization of the 3D environment
    8. Moving the robot - animations

#### Introduction
The aim of this project is to provide a practical guide defining all the steps necessary for the creation of a learning workflow based on VR technologies. All the technical steps are defined, from the creation of a 3D environment to the robot movement. The 3D environment in our case is the CNR laboratory where two COMAU robots are available for testing.
Before starting with the description of the activities, a brief description of the utilized digital tools used in the examples is previously done.
#### Digital tools
### MS Excel
Excel is one of the most know software and thanks to his capabilities we can directly generate a text that will become the .json file. A template of the Excel is provided and the instructions to fill all the cells are provided in the document.
### GitHub (https://github.com/)
GitHub is a web and cloud-based service and was born to helps developers store and manage their code and track and control changes. GitHub is used in this project as if it is an online public cloud. This way more people can make changes to the project and VEB.js will be able to access the files online. Using a public repository is free of charge.
### Autodesk Inventor (https://www.autodesk.it/products/inventor/overview)
Inventor is a software for 3D modelling. Any kind of 3D modelling software can be used for our purpose (e.g. SketchUp, Solidworks). The software must be able to save files in GLTF/GLB format.  
### Notepad++ (https://notepad-plus-plus.org/downloads/)
Notepad++ is a text editor. It is used in this guide since it facilitates the visualization of the elements during programming json files can be opened with notepad++ so that the all the elements of the code can be better understood. This is a free software.
### VEB.js (https://virtualfactory.gitbook.io/vlft/tools/vebjs)
VEB.js (Virtual Environment based on Babylon.js) is a reconfigurable model-driven virtual environment application. On this application is possible to read and visualize our json files so the factory environment with its assets and animations. Babylon.js library is free to use.
### JSON
JSON is an open standard file format and data interchange format that uses human-readable text to store and transmit data objects consisting of attribute-value pairs and arrays (or other serializable values). It is a common data format with diverse uses in electronic data interchange, including that of web applications with servers. JSON is a language-independent data format. It was derived from JavaScript.
## General scheme – IDEF0 diagram
The workflow for creating an XR environment turns out to be much broader than what we will focus on. The complete scheme is shown below. More details can be found at the following link: Avatar workflows - AVATAR (univ-grenoble-alpes.fr).
**insert image 1!!!**

We now focus on the IDEF0 diagram of A4 step. It is a tool developed to describe any kind of workflows. It is composed by different elements described below:
* The square is representing an activity that must be completed. Each square is associated with input/output, digital tools and learning objectives.
* The I/O represent the necessary materials needed to complete the activity and the expected outcome after completing it.
* Digital tools are the software that allow the completion of the activity.

The following image is schematizing the whole process:
**insert image 2!!!**

Meanwhile, this is specific for the software used in the examples:
**insert image 3!!!**

Each chapter of this guide describes all the activities shown in the diagram with the relative input/outputs and necessary digital tools. For each of the activities is described the procedure with input/outputs, mechanisms, and the activities necessary to complete them. A practical example is then explained to facilitate the comprehension of the specific argument.

## Creation of an online repository or a local folder
There are 2 ways to work with the files that you are going to create: locally or online. The online repository you can use is provided by GitHub, this is necessary to store our files and access to them when required from the activities. Online repository is not mandatory, all the files can be also created locally. Anyway, we strongly recommend creating it so the whole team will be able to access it and work simultaneously. Here are the steps to create it:
1.	First is necessary to Sign Up at the following link: Join GitHub · GitHub
2.	Once registered click, on the top left of the page the green button “New”. 
3.	Insert the repository name and a description. Make it public and leave the other options as default.	
4.	It is now possible to upload the files by clicking on “Add file” and  “Upload files”.
Here is an example of an already existing repository (is recommended not to modify any file in this repository): savixy/AVATARrepository: This is a repository for 3D models of the Erasmus+ project AVATAR

## Definition and creation of the 3D models
The 3D environment must contain all the models that will be involved in the manufacturing process. It is also good to integrate furniture and other elements to make the scene more complete. The objects that will be in the 3D environment are:
*	2 COMAU robots
*	2 robot bases
*	1 conveyor
*	1 tool
*	the robot controller

## How to obtain the 3D models
Once we have the list of all the necessary objects, we’re going to find them 2 possible ways.
1.	First, is possible to exploit existing models provided or in online libraries (those can be free to download or with a fee). It is important to mention that the file format of the 3D models must be available in a neutral format (e.g. .STEP or .IGES) so that they can be modified.
The final format to be used in the VR environment must be a .GLB or .GLTF.
2.	The 3D models can be created from scratch using any CAD software (e.g. Inventor, SketchUP, Solidworks) able to export the files in the previous mentioned formats. This is a more time-consuming way that must be used to create specific models for our environment.

#### Conventions
Before going on, be aware that the orientation of each single component must be coherent with the other objects in the scene. In many CAD environments, it is possible to specify the convention used for the orientation of the z-axis (z-up option). The z-up convention is the one that will be also used in our examples (it is anyway possible to use other conventions, be coherent). 
As example, the URDF files uses the following conventions:
*	z-up
*	Euler angles XYZ extrinsic (corresponding to ZYX intrinsic)

That are different from VEB.js conventions:
*	Yup
*	Euler angles YXZ intrinsic

More details about the 3D models can be found here: https://virtualfactory.gitbook.io/vlft/kb/instantiation/3d-models. 

## Shaping the models
The laboratory structure and the robot already exist, the files are provided in the attached folder “3D models”.
The base of the robot, the conveyor and the robot tool must be generated manually. All the measurement necessary to shape the models; controller, conveyor, robot base, tool and their placement in the environment [Zmap] (the unit of measure is millimetres) are in the folder “Drawings”. For each of them you can find the dwg files, a PNG file with the measurements and a picture of the robot base and the tool. It is not necessary to define every single detail of the models.

## Generation of the 3D environment
Once you have all the models, we can start creating the 3D environment. The steps consist in:
1.	Import the files.
2.	Place the models in the correct position and orientation depending on the “zmap”. The aim is to: add the base of the robot, under it, add the conveyor in the correct position and attach the tool to the robot.

In the example, this work is supported with the use of an Excel sheet able to generate the .json file that can be read by VEB.js or any other software mentioned in the IDEF0 diagram (e.g. Unreal Engine, Unity).
There is another way that avoid the use of the Excel file that consists in directly modifying the .json file.

**Excel file template**
The file template can be found in the folder “” and is named “Excel_Template”. The sheet “assets” have all the details about the single 3D models in the environment. The sheet “context” has 4 cells of our interest:
* JSON file text: the text inside this cell is providing us the code for the .json file. By copying it in a .txt file and changing the format in .json we are able to create our .json file.
* UnitOfMeasureScale: this is the unit of measure 0,01 for centimetres, 1 for meters.
* Zup convention: VEB.js use the Yup convention. It is important to be aware of the convention used in the 3D visualizer.
* Repository location: path where the 3D models can be found. This is not mandatory since in the VEB.js link we are going to refer again to this repository.

More details can be found at the following link: https://virtualfactory.gitbook.io/vlft/kb/instantiation/assets/spreadsheet
Once the Excel file is completed with all the details, the json file can be created by copying the B1 cell of the sheet “context”.

**Json code**
The modifying of the .json code is a bit more complex than the use of the Excel file but allow to have a higher control over the written code. This can be done using any text software.
An already existing .json file with the laboratory structure and the robot can be found in the folder “files” and is named “Original.json”. 
It is important to mention that the position and orientation must be checked multiple times in the 3d environment to be sure the model is in the expected place (the way to visualize the online environment is described in the next chapter).
Let’s see the new code defined for adding the conveyor:
**Insert image 5!!!**

## Visualization of the 3D environment
This chapter of the document is extremely important since it allow us to check visually if the models are positioned correctly and if the robot is working as expected. 
**Creating a scene**
Before importing the models, it is possible to define the environment. The latter consist in adding cameras and lights. More information can be found at the following link: https://virtualfactory.gitbook.io/vlft/tools/vebjs/input-output. To automatically import the environment the relative file name must "*nameofthescenefile_env.json*" be and must be in the same folder of the scene file.
Once you have created the online repository with the scene (.json) file and the environment file, or you have them locally you are ready to visualize it in the 3D VEB.js (or any other software) environment.

In case you have them **locally**, open VEB.js (link: https://ec2-54-174-51-194.compute-1.amazonaws.com/vebjs/?inputscene=&repoMod3d=) and click on import scene, select your .json file. You should now be able to see the 3D environment.
If you’re using VEB.js you can move the camera using “q-w-e-a-s-d” buttons.

If you have them **online**, you need to modify the following link accordingly to your username and the name of the repository:
http://ec2-54-174-51-194.compute-1.amazonaws.com/vebjs/?inputscene=https://raw.githubusercontent.com/
**username**/**name-of-the-repository**/main/scenes/**name-of-the-json-file.json**
&repoMod3d=https://raw.githubusercontent.com/*username**/**name-of-the-repository**
/main/models/
The words in bold must be modified with the respective reference words.
