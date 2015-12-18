# -*- coding: utf-8 -*-
"""
Created on Thu Dec 03 20:02:56 2015

@author: Tonnam
"""
# pip install scraperwiki

import amcsd_list
import ams_lxml

# Get list of crystal structure names
name_list = amcsd_list.get_list()

# Formatting strings of .csv file for DIF files scraping
doi = '10.1130/2006.2397(06)'
sub_citation_1 = 'American Mineralogist Crystal Structure Database'
url = 'http://rruff.geo.arizona.edu/AMS/amcsd.php'
m_name = 'X-ray diffraction'
unit_intensity = 'Arb. units'
unit_two_theta = '$^{\circ}$'
unit_wavelength = '$\AA$'

list_two_theta = []
list_intensity = []

# Write .csv file in appropriate format
with open('xray_diffraction.csv', 'w') as fout:
    fout.write('Citation,Sub citation,Sub citation,Sub url,Common name,Measurement method,'+\
    'Measurement name,Measurement value,Measurement units,'+\
    'Measurement condition name,Measurement condition value,Measurement condition units,'+\
    'Measurement condition name,Measurement condition value,Measurement condition units\n')
    for name in name_list[:5]:
        print name
        xray_info = ams_lxml.get_xray_info(name)
        list_two_theta.append(xray_info.two_theta)
        list_intensity.append(xray_info.intensity)
        ref_format = xray_info.author+'. '+xray_info.journal+'. '+xray_info.title
        fout.write(doi+','+sub_citation_1+',\"'+ref_format+'\",'+url+','+name+',' \
        +m_name+',Intensity,\"'+repr(intensity)+'\",'+unit_intensity \
        +',2$\Theta$,\"'+repr(two_theta)+'\",'+unit_two_theta \
        +',X-ray wavelength,'+str(xray_info.wavelength)+','+unit_wavelength+'\n')
fout.close()