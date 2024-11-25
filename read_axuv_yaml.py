import yaml
import numpy as np
import matplotlib.pyplot as plt
import math

def read_yaml(yaml_file):
  #yaml_file='/vac-runs/lm26c/lm26c-107/AXUV_Specs_LM120_7-Nov-2024.yaml'
  with open(yaml_file, 'r') as file:
     axuv_struct=yaml.safe_load(file)
  #print(chord['name'])
  #orientation=-1
  #for chordname in chord['chords']:
  #  if chordname[0:2]=='PV':
  #    print(chordname)
  #    r=[chord['chords'][chordname]['r1'],chord['chords'][chordname]['r2']]
  #    z=np.multiply([chord['chords'][chordname]['z1'],chord['chords'][chordname]['z2']],orientation)
  #    plt.plot(r,z,label=chord['name'])

  return axuv_struct


def radius(z, r1,r2, theta1, theta2, z1, z2):
    s=(z-z2)/(z1-z2)
    r_sq=r1**2*s**2+ r2**2*(1-s)**2+ 2*r1*r2*s*(1-s)*math.cos(math.pi*(theta1-theta2)/180.0)
    return math.sqrt(r_sq)


def slopes_inter(r1,r2,z1,z2,theta):
  m0=(r2-r1)/(z2-z1)
  tan_theta=math.tan(theta)
  mp=(m0-tan_theta)/(1+m0*tan_theta)
  mm=(m0+tan_theta)/(1-m0*tan_theta)
  cp=-mp*z1+r1
  cm=-mm*z1+r1
  c0=-m0*z1+r1
  return mp,mm, cp, cm, m0, c0

def cal_r_edge(z,x1,x2,y1,y2,z1,z2,hangle):
  s=(z-z2)/(z1-z2)
  x=s*x1+(1-s)*x2
  y=s*y1+(1-s)*y2
  #t2p=math.atan(y/x)*180/math.pi
  #chord length
  R0=math.sqrt((x1-x)**2+(y1-y)**2+(z1-z)**2)
  #angle between (-x,-y2,0) and (x1-x,y1-y, vz1-z)
  cos_alpha=(-x*(x1-x)-y*(y1-y))/(math.sqrt(x**2+y**2)*R0)
  sin_alpha=math.sqrt(1-cos_alpha**2)
  #outer edge of the beam
  r2p=R0*sin_alpha*(cos_alpha+sin_alpha*math.tan(hangle))/(sin_alpha-cos_alpha*math.tan(hangle))-R0*cos_alpha+math.sqrt(x**2+y**2)
  return r2p#, t2p 



