# -*- coding: utf-8 -*-
"""
Created on Thu Dec 03 20:02:56 2015

@author: Tonnam
"""
# pip install scraperwiki

import amcsd_list
import ams_lxml

name_list = amcsd_list.get_list()

doi = '10.1130/2006.2397(06)'
sub_citation_1 = 'American Mineralogist Crystal Structure Database'
url = 'http://rruff.geo.arizona.edu/AMS/amcsd.php'
m_name = 'X-ray diffraction'
unit_intensity = 'Arb. units'
unit_two_theta = '$^{\circ}$'


list_two_theta = []
list_intensity = []

with open('xray_diffraction.csv', 'w') as fout:
    fout.write('Citation,Sub citation,Sub url,Common name,Measurement method,Measurement name,Measurement value,Measurement units,Measurement condition name,Measurement condition value,Measurement condition units\n')
    for name in name_list[:5]:
        print name
        two_theta, intensity = ams_lxml.get_dif(name)
        list_two_theta.append(two_theta)
        list_intensity.append(intensity)
        fout.write(doi+','+sub_citation_1+','+url+','+name+','+m_name+',Intensity,\"'+repr(intensity)+'\",'+unit_intensity+',2$\Theta$,\"'+repr(two_theta)+'\",'+unit_two_theta+'\n')
fout.close()