import scraperwiki
import lxml.html
import sys

def get_dif(name):
    #name = raw_input('What material are you interested in? ')
    #name = 'Achavalite'
    # Achavalite
    # Actinium
    
    html = scraperwiki.scrape('http://rruff.geo.arizona.edu/AMS/minerals/{0}'.format(name))
    
    root = lxml.html.fromstring(html)
    # get the links
    hrefs = root.xpath('//a/@href')
    
    iid = ''
    
    for href in hrefs:
       # print 'http://ahr13.mapyourshow.com' + href.attrib['href'] 
        if 'javascript' in href:
           fid = href.split("(")[-1].replace("'", '').strip(')')
           iid = fid
           break
    ###
    
    # xray_html = scraperwiki.scrape('http://rruff.geo.arizona.edu/AMS/xtal_data/DIFfiles/.txt'.format(iid))
    # xray_root = lxml.html.fromstring(xray_html)
    # print xray_root:wq
    
    import urllib2
    xray_response = urllib2.urlopen('http://rruff.geo.arizona.edu/AMS/xtal_data/DIFfiles/{0}.txt'.format(iid))
    # fooline = [ item for item in response.readlines() if 'href' in item and 'diffraction' in item]
    # for item in fooline:
    #     print item
    fl= xray_response.readlines()
    print_flag = False
    two_theta = []
    intensity = []
    for item in fl:
        if '=====' in item:
            print_flag = False
        if print_flag:
            fooline = item.split()
            two_theta.append(float(fooline[0]))
            intensity.append(float(fooline[1]))
        if '2-THETA' in item:
            print_flag = True
    ####
    #print('XRD data points of ' + name)
    #print('Two Theta : ' + str(two_theta[:10]))
    #print('Intensity : ' + str(intensity[:10]))
    
    #writing_file = open('xray.csv', 'a')
    #writing_file.write(name + ',' + repr(two_theta) + ',' + repr(intensity) + '\n')
    #writing_file.close()
    
    return two_theta, intensity
