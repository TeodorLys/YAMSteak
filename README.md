<p align="center">
<img src="doc/YAMSteak.png" align="center" width="348" height="246"/> 
 </p>


# YAMSteak
This software is for generating YAML configuration file through a GUI.
You create a config.yml file and define which fields are needed and define what type of gui element it should be. 

Super janky, thrown together in about 3 days but it works! 
Quick fix FTW

## Example
##### Config.yml
``` YAML
GUI:
  height:
    type: entry
    description: "The height of the main window" # Generates a tooltip
                                                 # when hovering over the height entrybox
  width:
    type: entry
  border:
    type: dropdown
    options:
      - rounded
      - transparent
      - none
  buttons:
    type: listblock
    block:
      height:
        type: entry
      width:
        type: entry
      clickable:
        type: checkbox
      
```


<p align="center">
<img src="doc/example.png" align="center" width="800" height="400"/> 
</p>


##### Output
``` YAML
GUI:
  border: transparent
  buttons:
  - clickable: true
    height: '15'
    width: '20'
  height: '150'
  width: '200'

```
