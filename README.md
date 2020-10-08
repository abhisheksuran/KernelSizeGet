# KernelSizeGet
This contains script that outputs different kernel size, stride and padding that can be use to transform input image size into desired output shape. 
This script works for tensorflow, you can try this for other frameworks.
Will be improving script in future.

NOTE:
  1. This script assumes that user is using Maxpool2d layer with default parameters after every convolution layer.
  2. Depth of image is equal to number of kernel used, so depth is not in script's output
```
usage: shaper.py [-h] -l integer_value -ih integer_value -iw integer_value -oh integer_value -ow integer_value
                 [-vs integer_value] [-hs integer_value] [-k True/False]

THIS SCRIPT IS USEFUL TO GET KERNEL SIZE, STRIDES AND PADDING FOR EACH CONV LAYER IN CONVOLUTION NETWORK TO GET DESIER
OUTPUT SHAPE FROM A GIVEN INPUT IMAGE SHAPE

optional arguments:
  -h, --help         show this help message and exit
  -l integer_value   Number of convolution layers in your network(only integer values accepted)
  -ih integer_value  Height of input image (only integer values accepted)
  -iw integer_value  Width of input image (only integer values accepted)
  -oh integer_value  Height of output image (only integer values accepted)
  -ow integer_value  Width of output image (only integer values accepted)
  -vs integer_value  (optional)vertical stride for image (only integer values accepted)
  -hs integer_value  (optional)horizontal stride for image (only integer values accepted)
  -k True/False      set True if you only want to try kernels with equal height and width (False is by default)
```
