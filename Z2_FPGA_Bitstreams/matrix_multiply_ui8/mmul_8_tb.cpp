#include "mmul_p.hpp"

void mmul_sw(DataType in0[NN], DataType in1[NN], DataType out[NN]) {
	for(int k = 0; k < N; k++){
		for(int i = 0; i < N; i++){
			int index = N*i+(i+k)%N;
			for(int j = 0; j < N; j++){
				out[index] = out[index] + in0[i*N+j]*in1[j*N+(i+k)%N];
			}
		}
	}
}

int main(void) {
  int i, j, err;

  DataType in0[NN];
  DataType in1[NN];
  DataType out_sw[NN];
  DataType out_hw[NN];

  /* initiation */
  for (i = 0; i < NN; i++) {
	  in0[i] = i;
	  in1[i] = i;
	  out_sw[i] = 0;
	  out_hw[i] = 0;
  }

  /* hardware execute */
  test_kernel<DataType>(in0, in1, out_hw);
  printf("hardware kernel complete\n");

  /* software execute */
  mmul_sw(in0, in1, out_sw);
  printf("software kernel complete\n");

  /* comparison */
  err = 1;
  for(i = 0; i < NN; i++){
	  if(out_sw[i] != out_hw[i]){
		  err = 0;
	  }
  }

  if (err == 1) {
	  printf("Test successful!\r\n");
  	  return 0;
  }
  printf("Test failed!\r\n");
  return 1;
}
