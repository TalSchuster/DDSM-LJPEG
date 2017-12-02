# DDSM-LJPEG
This repository is created for converting Mammography of [Digital Database for Screening Mammography (DDSM)](http://marathon.csee.usf.edu/Mammography/Database.html) form LJPEG to more ordinary format.

## Prerequisite
[ImageMagick](http://www.imagemagick.org/) is a great tool for image processing. We use it for converting from .pnm to .png.


## Install
1\. Download the resources.
```
# make sure to clone with --recursive
git clone --recursive git@github.com:TalSchuster/DDSM-LJPEG.git
```

2\. ljpeg
```
cd ljpeg/jpegdir
make
```

3\. ddsm
```
cd ddsm/ddsm-software
g++ -Wall -O2 ddsmraw2pnm.c -o ddsmraw2pnm
```

## Usage

```
python convert.py --path_to_cases <Path to cases dir containing noramls/ cancers/ etc..>
```
