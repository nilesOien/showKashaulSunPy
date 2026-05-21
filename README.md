
# Showing a silly SunPy demo

Basically installs SunPy using uv and then does something from
[https://docs.sunpy.org](https://docs.sunpy.org).

I use the uv python package manager rather than pip, so uv has to be installed.

I had to :
```
uv python pin 3.14
```
in order to get a remotely recent version of SunPy.

Then run :
```
./installPackages.sh
```
to init a uv project. If you use pip and a reasonably recent version of python then you can :
```
pip install sunpy[all]
```
I just use uv here to get a recent python version (and hence a recent SunPy version).

Then run :
```
./Runner.sh
```
to run the python in showKashaulSunPy.py

The first run may take time since it needs to initialize everything.

