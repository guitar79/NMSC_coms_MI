#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 03:03:20 2017

@author: guitar79
"""

import os
from pathlib import Path
from PIL import Image

from datetime import datetime
from dateutil.relativedelta import relativedelta

start_time=str(datetime.now())

#area = [cf, cn, a, k, lk]
area = "cn"
chl = ['vis', 'ir1', 'ir2', 'swir', 'wv', 'com']
#chl = "ir1"
year = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017]
#year = [2014, 2015, 2016, 2017]
#yr = "2016"

dr_out = '/media/guitar79/6T/COMS_MI/le1b'
dr_base = '/run/user/1000/gvfs/smb-share:server=parksrne,share=coms_mi/le1b'

dummy_im = Image.open('dummy.png');

#for yr in sorted(os.listdir('%s/%s/%s' %(dr_base, area, chl[1]))):
for yr in year:
	dr_read = '%s/%s/%s/%s' %(dr_base, area, chl[1], yr)
	for i in sorted(os.listdir(dr_read)):
		if i[-4:] == '.png':
			im_list = ['%s/%s/%s/%s/coms_mi_le1b_%s_%s_%s' %(dr_base, area, chl[0], yr, chl[0], area, i[-16:]),\
			    '%s/%s/%s/%s/coms_mi_le1b_%s_%s_%s' %(dr_base, area, chl[1], yr, chl[1], area, i[-16:]),\
			    '%s/%s/%s/%s/coms_mi_le1b_%s_%s_%s' %(dr_base, area, chl[2], yr, chl[2], area, i[-16:]),\
			    '%s/%s/%s/%s/coms_mi_le1b_%s_%s_%s' %(dr_base, area, chl[3], yr, chl[3], area, i[-16:]),\
			    '%s/%s/%s/%s/coms_mi_le1b_%s_%s_%s' %(dr_base, area, chl[4], yr, chl[4], area, i[-16:]),\
			    '%s/%s/%s/%s/coms_mi_le1b_%s_%s_%s' %(dr_base, area, chl[5], yr, chl[5], area, i[-16:]),\
			    '%s/%s/all/%s/coms_mi_le1b_all_%s_%s' %(dr_out, area, yr, area, i[-16:])]
			file_all = Path(im_list[6])
		if file_all.is_file(): # image file already exists in my folder
			print ('File exists %s' %(im_list[6]))
		else :
			try : 
				im_ir1 = Image.open(im_list[1])
				width_ir1, height_ir1 = im_ir1.size
				im_new=Image.new('RGB', (width_ir1*3, height_ir1*2)) #creates a new empty image, RGB mode, 3x2

				print('starting %s' %(im_list[1]))
				for j in range(0,2):
					for k in range(0,3):
						t=3*j+k;
						if (os.path.isfile(im_list[t])):
							im=Image.open(im_list[t])
							im_new.paste(im, (width_ir1*k, height_ir1*j))
						else:
							im_new.paste(dummy_im, (width_ir1*k, height_ir1*j))
				if not os.path.exists('%s/%s/all/%s/' %(dr_out, area, yr)):
					os.makedirs('%s/%s/all/%s/' %(dr_out, area, yr))
				im_new.save(im_list[6])
				print('creating...... %s' %(im_list[6]))
				print('-'*30)
			except : 
				with open('%s/%s/merge_error_log'%(dr_base, area), 'a')  as f:
					f.write('error...... %s\n' %(im_list[6]))
				print('error...... %s' %(im_list[6]))
				print('='*30)
end_time = str(datetime.now())
print("start : "+ start_time+" end: "+end_time)
