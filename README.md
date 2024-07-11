<p align="center">
<img src="doc/YAMSteak.png" align="center" width="348" height="246"/> 
 </p>


# YAMSteak
This software is for generating YAML configuration file through a GUI.
You create a config.yml file and define which fields are needed and define what type of gui element it should be

``` YAML
GUI:
  height:
    type: entry
  width:
    type: entry
  border:
    type: dropdown
    options:
      - rounded
      - transparent
      - none
   buttons:
     type: subsection
     block:
       height:
         type: entry
       width:
         type: entry
       clickable:
         type: checkbox
      
```
<p align="left">
<img src="doc/example1.png" align="left" width="480" height="480"/> 
<img src="doc/example2.png" align="right" width="480" height="480"/> 
</p>
