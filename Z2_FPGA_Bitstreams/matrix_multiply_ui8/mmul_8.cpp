#include "mmul_p.hpp"

template <typename T> void test_kernel(T in0[NN], T in1[NN], T out[NN]) {
	for(int k = 0; k < N; k++){
		for(int i = 0; i < N; i++){
#pragma HLS PIPELINE II=1
			int index = N*i+(i+k)%N;
			for(int j = 0; j < N; j++){
				out[index] = out[index] + in0[i*N+j]*in1[j*N+(i+k)%N];
			}
		}
	}
	return;
}

void mmul_p
(
	strm &INPUT0,
	strm &INPUT1,
	strm &OUTPUT
)
{
#pragma HLS INTERFACE axis port=INPUT0
#pragma HLS INTERFACE axis port=INPUT1
#pragma HLS INTERFACE axis port=OUTPUT

	DataType l_0[NN];
	DataType l_1[NN];
	DataType out[NN];

load_A:
	  for (int i = 0; i < NN; i++) {
		pkt temp = INPUT0.read();
		l_0[i] = temp.data;
	  }
load_B:
	  for (int i = 0; i < NN; i++) {
		pkt temp = INPUT1.read();
		l_1[i] = temp.data;
	  }

	  test_kernel<DataType>(l_0, l_1, out);

write_C:
	for (int i = 0; i < NN; i++) {
		pkt temp;
		temp.data = out[i];
		ap_uint<1> last = 0;
		if (i == NN - 1) {
			last = 1;
		}
		temp.last = last;
		temp.keep = -1;
		OUTPUT.write(temp);
	}
}
