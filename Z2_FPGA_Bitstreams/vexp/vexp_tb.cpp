#include "vexp.hpp"

void vexp_sw(DataType in[N], DataType out[N]) {
	for(int i = 0; i < N; i++){
		out[i] = hls::exp(in[i]);
	}
}

int main(void) {
  int i, j, err;

  DataType in[N];
  DataType out_sw[N];
  DataType out_hw[N];

  /* initiation */
  for (i = 0; i < N; i++) {
	  in[i] = DataType(i);
	  out_sw[i] = DataType(0);
	  out_hw[i] = DataType(0);
  }

  /* hardware execute */
  test_kernel<DataType>(in, out_hw);
  printf("\nHardware kernel complete\n");

  /* software execute */
  vexp_sw(in, out_sw);
  printf("\nSoftware kernel complete\n");

  err = 1;
  for(int i = 0; i < N; i++) {
	  err = out_sw[i] == out_hw[i];
	  printf("%f, %f \n", out_sw[i], out_hw[i]);
  }
  printf("\n");

  if (err == 1) {
	  printf("\nTest successful!\r\n");
  	  return 0;
  }
  printf("\nTest failed!\r\n");
  return 1;
}
