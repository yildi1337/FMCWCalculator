# FMCWCalculator
A simple Python tool for calculating between basic FMCW radar parameters

# Screenshot
![](https://github.com/yildi1337/FMCWCalculator/blob/main/screenshot/screenshot.png)

# Further information
The tool is based on the [PySimpleGUI](https://pypi.org/project/PySimpleGUI/) library and simply allows to determine a missing parameter of the FMCW radar equation:
$$d = \frac{c_0~\Delta f}{2} \frac{\mathrm{d}t}{\mathrm{d}f}$$
where $$d$$ is the distance between the antenna and the reflecting object, <img src="https://render.githubusercontent.com/render/math?math=c_0"> is the speed of light, $$\Delta f$$ is the resulting difference frequency, $$\mathrm{d}t$$ is the sweep time, and $$\mathrm{d}f$$ is the sweep bandwidth. In addition, the tool calculates the resolution which is given by:
$$r = \frac{c_0}{2~\mathrm{d}f}$$
