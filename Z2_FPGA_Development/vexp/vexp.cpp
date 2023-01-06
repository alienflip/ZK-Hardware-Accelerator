#include "vexp.hpp"

template <typename T> void test_kernel(T in[N], T out[N]) {
	for(int i = 0; i < N; i++){
		out[i] = hls::exp(in[i]);
	}
}

void vexp
(
	strm &INPUT,
	strm &OUTPUT
)
{
#pragma HLS INTERFACE ap_ctrl_none port=return
#pragma HLS INTERFACE axis port=INPUT
#pragma HLS INTERFACE axis port=OUTPUT

	DataType l_0[N];
	DataType out[N];

load_A:
	  for (int i = 0; i < N; i++) {
		pkt temp = INPUT.read();
		l_0[i] = temp.data;
	  }

	  test_kernel<DataType>(l_0, out);

write_C:
	for (int i = 0; i < N; i++) {
		pkt temp;
		temp.data = out[i];
		ap_uint<1> last = 0;
		if (i == N - 1) {
			last = 1;
		}
		temp.last = last;
		temp.keep = -1;
		OUTPUT.write(temp);
	}
}
