# Interactive visualization of simple closed curves on torus representing different homotopy classes

## Description
Interactive visualization: possible to choose radiuses for torus;  p,q parameters for curves; opacity level; draw an arbitrary curve using mouse as a brush. Made using MayaVi library. 

## Requirements
```
(which were hard to satisfy actually)

Python 2.7
Numpy
Mayavi + Vtk
Traits
Tkinter
```

## How to start
shapes.py contains hyperparameters for torus and parameters for everything.

visual.py actually performs drawing and interactions.

Therefore just enter
```
python visual.py
```
in command-line and hope it works.


## How it looks like

Intitial position             |  You can rotate torus freely with a mouse
:-------------------------:|:-------------------------:
![](https://github.com/ttaggg/torus/blob/master/images/snapshot.png)  |  ![](https://github.com/ttaggg/torus/blob/master/images/snapshot1.png)


## Parameters

Changing parameters of the curves             |  Changing opacity
:-------------------------:|:-------------------------:
![](https://github.com/ttaggg/torus/blob/master/images/snapshot2.png)  |  ![](https://github.com/ttaggg/torus/blob/master/images/snapshot3.png)


## Adding curve manually

  Drawing the curve    |  Result (blue curve)
:-------------------------:|:-------------------------:
![](https://github.com/ttaggg/torus/blob/master/images/tksnap1.png)  |  ![](https://github.com/ttaggg/torus/blob/master/images/snapshot5.png)


  Drawing the curve    |  Not-So-Good-Result (blue curve)
:-------------------------:|:-------------------------:
![](https://github.com/ttaggg/torus/blob/master/images/tksnap2.png)  |  ![](https://github.com/ttaggg/torus/blob/master/images/snapshot6.png)


## Disclaimer
I hope I did not mess this up, however I am not that sure.
