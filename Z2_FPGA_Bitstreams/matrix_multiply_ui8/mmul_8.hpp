#include <cstdio>
#include <cinttypes>

#include "ap_axi_sdata.h"
#include "hls_stream.h"

#define N 32
#define NN 1024

typedef ap_axiu<8, 1, 1, 1> pkt;
typedef hls::stream< pkt > strm;
typedef ap_int<8> int_x;

typedef std::uint8_t DataType;

template <typename T> void test_kernel(T in0[NN], T in1[NN], T out[NN]);
