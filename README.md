# CRT (Cathode-ray tube) Simulator
By **TheJPMZ**

This program simulates how a Cathode-ray tube (CRT) should work and provides an easy way to tinker with voltages and see the results. 

A CRT was a machine capable of displaying images from various voltage signals, they were used mainly for oscilloscopes and televisions.
![imagen](https://user-images.githubusercontent.com/64183934/137262036-cd78e342-70db-46d2-ac0d-38b864be256e.png)

## How to run?
On CMD/Console:
- To install dependencies ```pip install -r requirements.txt```
- After that, to run the simulation ```python CRTSimulator.py```


## Functionality
There are two modes, which can be switched at any moment.
On the first mode, you can select the voltage of the vertical and horizontal plates changing the electron's position. 
On the second mode, changing the gap between the plates and a relation of frequencies the trajectory of the electron is displayed automatically.

## Options
- Acceleration voltage 
	- It effectively makes the electron travel faster, making the image brighter.
- Latency
	- How fast is the window refreshed this can lead to quality images but slower drawing time, or a short drawing time but poor image quality.
- Vertical and Horizontal plate voltage
	- Change the voltage of the corresponding pair of plates moving the electron.
- Phase shift between both oscillators
	- Move the plates in relation to each other in an angle from 0 to 180 degrees.
- Frequency
	- Choose between some plate frequency relations optimized for Lissajous curves ( 1:1 | 1:2 | 1:3 | 2:3 )

## Demonstration

Using all the tools provided you can make some images like this ones:

![imagen](https://user-images.githubusercontent.com/64183934/137262036-cd78e342-70db-46d2-ac0d-38b864be256e.png)
![imagen](https://user-images.githubusercontent.com/64183934/137265998-5786ea3a-9e3f-4abd-98cc-063c3f62969b.png)

As the program's main focus is rendering Lissajous curves:
|   |1:1|1:2|1:3|2:3
|-- |--|--|--|--|

![imagen](https://user-images.githubusercontent.com/64183934/137271779-0966bba7-ab18-4091-b5eb-0e6ec1072749.png)
![imagen](https://user-images.githubusercontent.com/64183934/137271798-50332db2-a682-4a6d-b6b1-ed466efa048c.png)
![imagen](https://user-images.githubusercontent.com/64183934/137271827-852ec96f-93d6-4005-a53a-4c345374a51d.png)

| 0 | ![imagen](https://user-images.githubusercontent.com/64183934/137271752-903bb165-2a63-449f-ad76-adb0a122a2c8.png)|![imagen](https://user-images.githubusercontent.com/64183934/137271779-0966bba7-ab18-4091-b5eb-0e6ec1072749.png) |![imagen](https://user-images.githubusercontent.com/64183934/137271798-50332db2-a682-4a6d-b6b1-ed466efa048c.png) | ![imagen](https://user-images.githubusercontent.com/64183934/137271827-852ec96f-93d6-4005-a53a-4c345374a51d.png)
|45 |![imagen](https://user-images.githubusercontent.com/64183934/137267000-09098f10-6f65-46b0-a27e-3b06ca005d23.png)
|90 |
![imagen](https://user-images.githubusercontent.com/64183934/137267242-b98d7139-481e-4a2a-8a2c-9e66a9db0756.png)
|135|![imagen](https://user-images.githubusercontent.com/64183934/137267535-71971f36-7c75-4d5b-8e28-de833066e801.png)




> Written with [StackEdit](https://stackedit.io/).
