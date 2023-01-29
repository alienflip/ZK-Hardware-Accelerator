
## PYNQ-Z2

> Use the Z2 with [chrome](https://www.google.com/intl/en_uk/chrome/)

> Get the disk image for the PYNQ-Z2 OS [here](http://www.pynq.io/board.html?_ga=2.95031516.1375262492.1660482686-74601426.1660347361), and burn it onto a MicroSD using, for example, [Win32DiskImager](https://wiki.ubuntu.com/Win32DiskImager)

> Follow the [Z2 get started guide](https://pynq.readthedocs.io/en/latest/getting_started/pynq_z2_setup.html)

> > Note: You may need to follow [this](https://discuss.pynq.io/t/static-ip-adress-configuration-issue/3259) debugging guide to run the PYNQ on Linux

### OOB Z2 Tests

> Go to `http://192.168.2.99:9090/lab` on Chrome, with your connected Z2

#### Host <-> FPGA file exchange

> Copy [Z2_Assets/server.ipynb](./Z2_Assets/server.ipynb) onto the PYNQ, and run it

> On the host, run:

```
python ~/zk/alienflip_release_0/HOST_Assets/server.py
```

> You should now see that there has been a file transferred to and from the PYNQ

### Z2 Bitstream Development

> Install [Vitis/Vivado 2022.1](https://www.xilinx.com/support/download.html)

> Remember to install build tools before compiling HLS:

```
sudo apt install build-essential
```

> > Note: the Z2 uses the part with code `xc7z020clg400-1`

> Now you can compile your C++ Vitis-HLS into Vivado-IP, and then use Vivado to generate `.hwh` and `.bit` files, which can be executed on silicon. Examples of this process can be seen below

> [These](https://www.youtube.com/channel/UCzBjN3CfLvZLRBoIwP5qZ_A/videos) [examples](https://pp4fpgas.readthedocs.io/en/latest/) help to get a feel for the Vitis/Vivado workflow

-----------
-----------
-----------