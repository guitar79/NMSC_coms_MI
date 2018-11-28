# -*- coding: utf-8 -*-
"""
@author: guitar79@naver.com, yyyyy@snu.ac.kr
#http://nmsc.kma.go.kr/emcoms/BIMG/COMS/Y2017/M08/D24/coms_mi_le1b_ir1_a_201708240545.png # east asia
#http://nmsc.kma.go.kr/emcoms/BIMG/COMS/Y2017/M08/D26/coms_mi_le1b_ir1_cf_201708260215.png # fulldisk asia
#http://nmsc.kma.go.kr/emcoms/BIMG/COMS/Y2017/M09/D15/coms_mi_le1b_ir1_cn_201709152200.png # 북반구확장 asia
"""
#chl = ['vis', 'ir1', 'ir2', 'swir', 'wv', 'com']
chl = ['wv', 'com']
#area = [cf, cn, a, k, lk]
area = "cn"
import urllib.request
from pathlib import Path
import os
for i in range(0,len(chl)):
    for year in range(2010,2019):
        	if not os.path.exists('%s/%d/' %(chl[i], year)):
        		os.makedirs('%s/%d/' %(chl[i], year))
        	for Mo in range(1,13):
        		for Da in range(1,32):
        			for Ho in range(1,25):
        				for Mn in range(0,60,15): # looks like the interval is 5min. often omitted.
        					url = "http://nmsc.kma.go.kr/emcoms/BIMG/COMS/Y%d/M%02d/D%02d/coms_mi_le1b_%s_%s_%d%02d%02d%02d%02d.png" \
        					% (year, Mo, Da, chl[i], area, year, Mo, Da, Ho, Mn)
        					filename = url.split('/')[-1]
        					my_file = Path('%s/%d/%s' % (chl[i],year,filename))
        					if my_file.is_file(): # image file already exists in my folder
        					    print ('File exists %s' % filename)
        					else:
        					    try:
        					        print ('Trying %s' % filename)
        					        urllib.request.urlretrieve(url, '%s/%d/%s' % (chl[i],year,filename))
        					        print ('Downloaded %s' % url)
        					    except  urllib.error.HTTPError: # image file doesn't exists in the server
        					        print ('Error %s' % filename)
