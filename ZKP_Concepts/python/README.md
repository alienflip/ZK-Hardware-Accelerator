# Usage

```
chmod a+x initRun.sh
```

## Install

> > Follow [this guide](https://docs.docker.com/desktop/install/linux-install/) to set-up docker

## Build and run

> Build the environment image:

```
sudo docker build -t zk_python_initial_explorations .
```

> > Note: `IMAGE ID` can be seen (then copied manually to the following commands) by using the following command:

```
sudo docker images
```

> Copy the relevant `IMAGE ID` into the following command to run the container:

```

sudo docker run --rm -it <IMAGE ID>
```

> To delete image:

```
sudo docker rmi -f <IMAGE ID>
```

--------

# Examples

## [ff.py](./ff.py)

> Exploration in Finite Field Arithmetic

## [fft.py](./fft.py)

> Exploration in Fast Fourier Transform

## [msm.py](./msm.py)

> Exploration in Multi Scalar Multiplication (Multi Exponentiation)

--------

## Further work here

> exploration in the Finite Field Fast Fourier Transform