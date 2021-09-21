# FMCWCalculator
A simple Python tool for calculating between basic FMCW radar parameters

# Screenshot
![](https://github.com/yildi1337/FMCWCalculator/blob/main/screenshot/screenshot.png)

# Further information
The tool is based on the [PySimpleGUI](https://pypi.org/project/PySimpleGUI/) library and simply allows to determine a missing parameter of the FMCW radar equation:

<img src="https://render.githubusercontent.com/render/math?math=d = \frac{c_0~\Delta f}{2} \frac{\mathrm{d}t}{\mathrm{d}f}">

where <img src="https://render.githubusercontent.com/render/math?math=d"> is the distance between the antenna and the reflecting object, <img src="https://render.githubusercontent.com/render/math?math=c_0"> is the speed of light, <img src="https://render.githubusercontent.com/render/math?math=\Delta f"> is the resulting difference frequency, <img src="https://render.githubusercontent.com/render/math?math=\mathrm{d}t"> is the sweep time, and <img src="https://render.githubusercontent.com/render/math?math=\mathrm{d}f"> is the sweep bandwidth. In addition, the tool calculates the resolution which is given by:

<img src="https://render.githubusercontent.com/render/math?math=r = \frac{c_0}{2~\mathrm{d}f}">
