# PYNQ-Z2 Primitives

> To use the following, use a [correctly set-up Z2 environment](https://pynq.readthedocs.io/en/latest/getting_started/pynq_z2_setup.html) in chrome; and with a running Z2, drag the `.hwh`, `.bit` and `.ipynb` files in this repo into the Z2 environment, and run the notebook

> > This follows from the `PYNQ-Z2` section of `alienflip_release_0`

----------------

## [Matrix Multiplication](./matrix_multiply_ui8/)

> `A` and `B` are `32x32 uint_8 matrixes`

> >  Notebook output:

```
OUT = AB
```

----------------

## [Vector Exponentiation](./vexp/)

> `A` is a `16 element float array`

> >  Notebook output:

```
OUT = [exp(A[i]) for i in range(len(A))]
```