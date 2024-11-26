Nov 26 2024
This is a piece of work requested by Curtis to estimate the time 
an axuv beam will be blocked by the liner.
In this case presented, the location vector and liner trajectory used
is from M3V3.


read_axuv_yaml.py          read location vector yaml file and locate the edge of beam
liner_csv_time_loop.py     read JSD liner traj. and check the time for blocking of the beam


Sample output for csim1005D and the loc vector file included:

$python3 liner_csv_time_loop.py
AXUV_A
num ratios= 3
AXUV_B
num ratios= 3
AXUV_C
num ratios= 2
AXUV_D
num ratios= 2
AXUV_A  with  ratio_1 block start at  1590  us
AXUV_A  with  ratio_1 block mid at  1700  us
AXUV_A  with  ratio_1 block all at  1730  us
AXUV_A  with  ratio_2 block start at  1590  us
AXUV_A  with  ratio_2 block mid at  1700  us
AXUV_A  with  ratio_2 block all at  1730  us
AXUV_A  with  ratio_3 block start at  1590  us
AXUV_A  with  ratio_3 block mid at  1700  us
AXUV_A  with  ratio_3 block all at  1730  us
AXUV_B  with  ratio_1 block start at  2380  us
AXUV_B  with  ratio_1 block mid at  2430  us
AXUV_B  with  ratio_1 block all at  2480  us
AXUV_B  with  ratio_2 block start at  2380  us
AXUV_B  with  ratio_2 block mid at  2430  us
AXUV_B  with  ratio_2 block all at  2480  us
AXUV_B  with  ratio_3 block start at  2380  us
AXUV_B  with  ratio_3 block mid at  2430  us
AXUV_B  with  ratio_3 block all at  2480  us
AXUV_C  with  ratio_1 block start at  2610  us
AXUV_C  with  ratio_1 block mid at  2690  us
AXUV_C  with  ratio_1 block all at  2750  us
AXUV_C  with  ratio_2 block start at  2630  us
AXUV_C  with  ratio_2 block mid at  2690  us
AXUV_C  with  ratio_2 block all at  2740  us
AXUV_D  with  ratio_1 block start at  2790  us
AXUV_D  with  ratio_1 block mid at  2850  us
AXUV_D  with  ratio_1 block all at  2900  us
AXUV_D  with  ratio_2 block start at  2820  us
AXUV_D  with  ratio_2 block mid at  2850  us
AXUV_D  with  ratio_2 block all at  2870  us

