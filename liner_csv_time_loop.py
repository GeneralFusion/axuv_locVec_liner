import csv
import numpy as np
import matplotlib.pyplot as plt
import math

#version to address the situation t1=/=t2

# assume in t1=t2 (in this case it is)
import read_axuv_yaml
yaml_file='./AXUV_Specs_LM120_7-Nov-2024.yaml'
axuv=read_axuv_yaml.read_yaml(yaml_file)

nchord=0
for chordname in axuv:
  if chordname[0:4]=='AXUV':
    nchord=nchord+1
simOriginZm = -2.401;
simOrientation=1;

num_ratio=np.zeros(nchord)  
mchord=0
for chordname in axuv:
  if chordname[0:4]=='AXUV':
    nratio=0
    for ratio in axuv[chordname]['ratios']:
      nratio=nratio+1
      axuv[chordname]['ratios'][ratio]['block_start']=0
      axuv[chordname]['ratios'][ratio]['block_mid']=0
      axuv[chordname]['ratios'][ratio]['block_all']=0
    num_ratio[mchord]=nratio
    print(chordname)
    print('num ratios=', round(num_ratio[mchord]))
    mchord=mchord+1

file_dir='./liner_trajectory_csim_1005D/timesliced/'
t_us_start=0
dt_us=10
t_us_end=3000

for t_us in range(t_us_start, t_us_end, dt_us):
  t_string='0.'+str(t_us).zfill(6)
  filename=file_dir+t_string+'/liner_trajectory.csv'
  num_lines = sum(1 for _ in open(filename))
  npoints=num_lines
#  print('npoints=', npoints)
  r=np.zeros(npoints)
  z=np.zeros(npoints)
  k=0
  with open(filename, mode='r') as file:
    test=csv.reader(file)
    for lines in test:
      r[k]=lines[0]
      z[k]=lines[1]
      k=k+1



  for chordname in axuv:
    if chordname[0:4]=='AXUV':
      for ratio in axuv[chordname]['ratios']:
        vr1=axuv[chordname]['ratios'][ratio]['effective_location_vector']['r1']*1e-3
        vr2=axuv[chordname]['ratios'][ratio]['effective_location_vector']['r2']*1e-3
        vz1=axuv[chordname]['ratios'][ratio]['effective_location_vector']['z1']*1e-3*simOrientation+simOriginZm
        vz2=axuv[chordname]['ratios'][ratio]['effective_location_vector']['z2']*1e-3*simOrientation+simOriginZm
        vt1=axuv[chordname]['ratios'][ratio]['effective_location_vector']['t1']
        vt2=axuv[chordname]['ratios'][ratio]['effective_location_vector']['t2']
        hangle=0.5*axuv[chordname]['ratios'][ratio]['cone_angle_deg']*math.pi/180.0
        x1=vr1*math.cos(vt1*math.pi/180.0)
        x2=vr2*math.cos(vt2*math.pi/180.0)
        y1=vr1*math.sin(vt1*math.pi/180.0)
        y2=vr2*math.sin(vt2*math.pi/180.0)
        flag=0
        i=npoints-1
        if axuv[chordname]['ratios'][ratio]['block_start']==0:
          while (flag==0 and z[i]>0.0):
            r2p=read_axuv_yaml.cal_r_edge(z[i],x1,x2,y1,y2,vz1,vz2,hangle)
            if r[i]<r2p:
                flag=1 
                axuv[chordname]['ratios'][ratio]['block_start']=1
                axuv[chordname]['ratios'][ratio]['block_start_t_us']=t_us
            i=i-1
        #if (flag==1):
        #   print(chordname,ratio,'upper blocked')
        flag=0
        i=npoints-1
        if axuv[chordname]['ratios'][ratio]['block_mid']==0:
          while (flag==0 and z[i]>0.0):
            if r[i]<read_axuv_yaml.radius(z[i], vr1,vr2, vt1, vt2, vz1, vz2):
                flag=1 
                axuv[chordname]['ratios'][ratio]['block_mid']=1
                axuv[chordname]['ratios'][ratio]['block_mid_t_us']=t_us
            i=i-1
        flag=0
        i=npoints-1
        if axuv[chordname]['ratios'][ratio]['block_all']==0:
          while (flag==0 and z[i]>0.0):
             r2m=read_axuv_yaml.cal_r_edge(z[i],x1,x2,y1,y2,vz1,vz2,-hangle)
             if r[i]<r2m:
                flag=1 
                axuv[chordname]['ratios'][ratio]['block_all']=1
                axuv[chordname]['ratios'][ratio]['block_all_t_us']=t_us
             i=i-1
        #if (flag==1):
        #   print(chordname,ratio,'lower blocked')
        

for chordname in axuv:
  if chordname[0:4]=='AXUV':
    for ratio in axuv[chordname]['ratios']:
      nratio=nratio+1
      #axuv[chordname]['ratios'][ratio]['block_start']=0
      #axuv[chordname]['ratios'][ratio]['block_all']=0
      print(chordname, ' with ' , ratio, 'block start at ', axuv[chordname]['ratios'][ratio]['block_start_t_us'], ' us')
      print(chordname, ' with ' , ratio, 'block mid at ', axuv[chordname]['ratios'][ratio]['block_mid_t_us'], ' us')
      print(chordname, ' with ' , ratio, 'block all at ', axuv[chordname]['ratios'][ratio]['block_all_t_us'], ' us')
     
#plt.plot(z,r)
#plt.plot(z[0:30],r[0:30], color='r')


#plt.show()


