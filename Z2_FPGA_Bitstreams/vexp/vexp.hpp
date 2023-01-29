#include "ap_axi_sdata.h"
#include "hls_stream.h"
#include "hls_math.h"

#define N 16

typedef hls::axis<float, 0, 0, 0> pkt;
typedef hls::stream< pkt > strm;

typedef float DataType;

template <typename T> void test_kernel(T in[N], T out[N]);
