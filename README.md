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
| 0 | ![imagen](https://user-images.githubusercontent.com/64183934/137271752-903bb165-2a63-449f-ad76-adb0a122a2c8.png) |![imagen](https://user-images.githubusercontent.com/64183934/137271779-0966bba7-ab18-4091-b5eb-0e6ec1072749.png) |![imagen](https://user-images.githubusercontent.com/64183934/137271798-50332db2-a682-4a6d-b6b1-ed466efa048c.png) | ![imagen](https://user-images.githubusercontent.com/64183934/137271827-852ec96f-93d6-4005-a53a-4c345374a51d.png)
|45 | ![imagen](https://user-images.githubusercontent.com/64183934/137272136-f3641c7b-b934-48bc-beb7-be88509ba367.png) |![imagen](https://user-images.githubusercontent.com/64183934/137272178-05649540-abcd-4cb8-a445-75388eb2783d.png) |![imagen](https://user-images.githubusercontent.com/64183934/137272215-d9409cab-f37f-4e0e-837f-280e24ccdcd3.png)| ![imagen](https://user-images.githubusercontent.com/64183934/137272242-1a1d403b-332a-4fa7-92b0-478994acdc47.png)
|90 | ![imagen](https://user-images.githubusercontent.com/64183934/137272473-300bb16c-15a0-4711-9e1b-0c0bd4b5a487.png) |![imagen](https://user-images.githubusercontent.com/64183934/137272496-417ec018-c343-4946-bdcc-9372b56ca1d8.png) |![imagen](https://user-images.githubusercontent.com/64183934/137272518-b69f5069-ff69-4032-b96b-80593c20df2b.png) |![imagen](https://user-images.githubusercontent.com/64183934/137272545-bea51c0a-e235-4b91-a410-d698b0cbd9aa.png)
|135|![imagen](https://user-images.githubusercontent.com/64183934/137267535-71971f36-7c75-4d5b-8e28-de833066e801.png)








> Written with [StackEdit](https://stackedit.io/).
