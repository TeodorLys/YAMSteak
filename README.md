<p align="center">
<img src="doc/YAMSteak.png" align="center" width="348" height="246"/> 
 </p>


# YAMSteak
This software is for generating YAML configuration file through a GUI.
You create a config.yml file and define which fields are needed and define what type of gui element it should be
## Example
##### Config.yml
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
