<!-----

Yay, no errors, warnings, or alerts!

Conversion time: 0.416 seconds.


Using this Markdown file:

1. Paste this output into your source file.
2. See the notes and action items below regarding this conversion run.
3. Check the rendered output (headings, lists, code blocks, tables) for proper
   formatting and use a linkchecker before you publish this page.

Conversion notes:

* Docs to Markdown version 1.0β34
* Thu Apr 13 2023 00:28:25 GMT-0700 (PDT)
* Source doc: MDC_EdgeStore_README-md
----->



# **MDC_EdgeStore**

This Blender Addon will allow you to store and restore the Edge Selection for each object. 


## 
**Description**

In this first version you will find the Menu Items in 3DView for Object & Edit Modes at the button of the Menu under a submenu EdgeStore. Both ‘Save/Store’ and ‘Set/Restore’ actions are available. 

This functionality is supposed to be available in an upcoming update and should be redundant. It should work in all versions but being new as of Blender version 3.5.0 this first version 1.0 is coded for that version so you would need to update blender to that version or above.


## 
**Getting Started**

### 
**Dependencies**



* Blender Version 3.5.0


### 
**Installing**

* From the Blender Market for donations if useful to you
* You can also download from this github repository to try it.
* The release section will have a proper zip file which you can add through the Preferences of Blender.
* Install Blender addon through Preferences via this [V1.0 release link](https://github.com/MasterJames/MDC_EdgeStore/releases/download/v1.0/MDC_EdgeStore.zip)



### 
**Alternate Usages**

* The main function saveSetObjEdges was originally part of just a script and includes redundant arguments for calling from different code-bases. It is relatively simple to call it from your own script if you wish to use it in your own way or projects.

## 
**Help/Warning**


It is new and relatively untested so you should always save when testing it out or for your usage and workflow. Please feel free to report issues here at its GitHub repository. 


## 
**Authors**

Master Domain Corporation is a private company that does many seemingly unrelated things. This simple Blender addon is an attempt to add the community transitioning to Blender.

The only current Author is 

**Master James** 	_@MasterJames_  	masterjames@master-domain.net


## 
**Version History**



* 1.0
    * Initial release version 1.0 2023-04-14 (only one storage space per object with Menu item only actions)
    * A future version will likely try to provide a similar panel like those that exists for Vertex and Face Selection Groups.

## 
**License**


This project is licensed under the Master Domain Corporation as a privately held entity.


## 
**Acknowledgments**

It was inspired by a Blender Discord Community user and new user of the wonders of Blender.org, and someone coming from a more traditional background with industry standard solutions. During their inquiry into how it might be possible to select and recall Edge Selection, as an attempt to provide community support for Blender as it is still clearly in need of some seemingly obvious abilities, the initially seemingly easy solution was better for the community to wrap it up in an official Addon.
