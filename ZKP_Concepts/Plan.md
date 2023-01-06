# What constitutes a first demo

- Port of simple but heavy function from MINA Node (OCaml) onto PYNQ-Z2 Overlay
- MINA node with OCaml drivers connecting the Node to PYNQ-Z2, which calls the function with its data, and returns correct calculation to the nde

## Execution particulars for first demo

0. Pick a function in the OCaml [Prover file](https://github.com/MinaProtocol/mina/tree/develop/src/lib/snark_worker) to put onto the PYNQ-Z2
1. Use logger to record the inputs and outputs of the function on a live MINA node
2. Write the function in C++ using HLS, and use the inputs and outputs to test the Z2 implimentation 
3. Once the Z2 implimentation is correct, begin working on the OCaml networking module for the MINA node. This should be a group of files and a header file in the OCaml node
4. This driver should ping the FPGA with data, then await and return the FPGA results

# What consititutes an MVP

-  Port of MINA/0(1)-labs Rust Finite Field Fast Fourier Transform (FFTFF) and Multi-Exponentiation (MSM) onto PYNQ-Z2 Overlay
- MINA node with OCaml drivers connecting the Node to PYNQ-Z2, which calls the FFTFF and MSM

## Execution particulars for an MVP

Same as execution particulars for a first demo, except with with the following differences:

0. A deep dive into the MINA implimentation of Rust version of the MSM and FFTFF (located in the `proof systems` sub-directory [here](https://github.com/MinaProtocol/mina/tree/develop/src/lib/crypto)):
1. How does the node call it?
2. Is it compiled at runtime, or is it all precompiled?
3. How can we log the I/O?
4. How large are the I/O?
5. Can the Z2 handle the I/O size? 

- HLS physical implimentation on Z2 for MSM and FFTFF: same as for the ‘first demo’.
- Networking module: same as for the ‘first demo’.