# -*- coding: utf-8 -*-
"""
Created on Thu Dec 03 20:02:56 2015

@author: Tonnam
"""
# pip install scraperwiki

import amcsd_list
import ams_lxml

name_list = amcsd_list.get_list()

doi = 'http://dx.doi.org/10.1130/2006.2397(06)'
url = 'http://rruff.geo.arizona.edu/AMS/amcsd.php'
m_name = 'X-ray diffraction pattern'

list_two_theta = []
list_intensity = []

with open('xray_diffraction.csv', 'w') as fout:
    fout.write('Citation,URL,Common name,Measurement name,Two theta,Intensity\n')
    for name in name_list:
        print name
        two_theta, intensity = ams_lxml.get_dif(name)
        list_two_theta.append(two_theta)
        list_intensity.append(intensity)
        fout.write(doi+','+url+','+name+','+m_name+','+repr(two_theta)+','+repr(intensity)+'\n')
fout.close()