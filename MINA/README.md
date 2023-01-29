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

## MINA-Z2 Accelerator 

> This will consist of connecting the above dev-environment with the [Z2](../Z2_Workflow/) dev-environment; it will also require some deep dives into the MINA OCaml and Rust tech stack, and some experiments with the limitations of the PYNQ

-----------
-----------
-----------
-----------