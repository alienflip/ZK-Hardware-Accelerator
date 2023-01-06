# MINA: SNARK-Worker FPGA-Acceleration

> This guide consists of three parts, they cover: 

- [Developing on a MINA Node, locally](#mina)
- [Developing on the PYNQ-Z2 FPGA](#pynq-z2)
- [Integrating and running the full system (WIP)](#mina-z2-accelerator)

-----------
-----------
-----------
-----------

## MINA

> For this system, your host machine should be running [Ubuntu-18.04](https://ubuntu.com/tutorials/create-a-usb-stick-on-ubuntu#1-overview). I have not tested it on other distros / OS's

> On installation, remember to run:

```
sudo apt upgrade
sudo apt update
```

### Install and build dev environment

> The following roughly follows [this guide](https://github.com/MinaProtocol/mina/tree/develop/nix)

> From you console:

```
git clone git@github.com:MinaProtocol/mina.git
cd mina
git submodule sync
git submodule update --init --recursive
sh <(curl -L https://nixos.org/nix/install) --daemon
mkdir -p "${XDG_CONFIG_HOME-${HOME}/.config}/nix"
```

> Now change the file `/etc/nix/nix.conf`; it should look like this:

```
trusted-substituters = "https://storage.googleapis.com/mina-nix-cache"
trusted-public-keys = "nix-cache.minaprotocol.org:D3B1W+V7ND1Fmfii8EhbAbF1JXoe2Ct4N34OKChwk2c= nix-cache.minaprotocol.org:fdcuDzmnM0Kbf7yU4yywBuUEJWClySc1WIF6t6Mm8h4= nix-cache.minaprotocol.org:D3B1W+V7ND1Fmfii8EhbAbF1JXoe2Ct4N34OKChwk2c="
build-users-group = nixbld
```

> Now close the console, then open again, and run:

```
cd mina
echo 'experimental-features = nix-command flakes' > "${XDG_CONFIG_HOME-${HOME}/.config}/nix/nix.conf"
./nix/pin.sh
```

### Fast Iteration

```
chmod a+x ~/zk/alienflip_release_0/HOST_Assets/runDemo.sh
mv ~/zk/alienflip_release_0/HOST_Assets/runDemo.sh ~/mina
```

> Navigate to, for example, `mina/src/lib/snark_worker/functor.ml`, and make changes for testing; then build and test as done below

### Test changes live, locally

> Make changes to a mina file, then run the following to build and test the changes:

```
cd mina
nix build mina
nix develop mina
```

```
dune build src/app/cli/src/mina.exe
eval "$buildPhase"
sudo ./runDemo.sh
```

-----------
-----------
-----------

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

## MINA-Z2 Accelerator 

> This will consist of connecting the above two dev-environments; it will also require some deep dives into the MINA OCaml and Rust tech stack, and some experiments with the limitations of the PYNQ

-----------
-----------
-----------
-----------