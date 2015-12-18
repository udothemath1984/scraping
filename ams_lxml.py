import scraperwiki
import lxml.html as lxml
import sys

class XrayInfo:
    #
    # just for convenience
    def __init__(self):
        self.two_theta = []
        self.intensity = []
        self.author = ''
        self.journal = ''
        self.title = ''
        self.wavelength = 0.0
    #
####

def get_mineral_id( name='' ):
    #
    # check user input
    if not name:
        sys.exit(".... User please input a mineral name....")
    # 
    AMS_URL_BASE = 'http://rruff.geo.arizona.edu/AMS/'
    #
    html = scraperwiki.scrape( AMS_URL_BASE + 'minerals/{0}'.format(name))
    # 
    root = lxml.fromstring(html)
    #
    # get the links; I actually have no idea what exactly xpath do, nor about the expression pattern
    #
    hrefs = root.xpath('//a/@href')
    # 
    # NEED FIX!
    # only take the first entry on the linked webpage
    #    this is actually problematic in many case... 
    #
    iid = 0 # id of a mineral name; only take the first entry on the linked webpage
    # 
    for href in hrefs:
        #
        if 'javascript' in href:
           # 
           # haven't checked the generity of the pattern!
           #
           fid = href.split("(")[-1].replace("'", '').strip(')')
           iid = fid
           break # break after first hit of finding the mineral name and its id
    ###
    return iid
####

def get_xray_info( name = '' ):
    #    
    import urllib2
    #
    iid = get_mineral_id( name=name )
    # 
    xray_response = urllib2.urlopen('http://rruff.geo.arizona.edu/AMS/xtal_data/DIFfiles/{0}.txt'.format(iid))
    fl = xray_response.readlines() # all text file in read into this; Enshi's poor choice of variable name...
    #
    xray_info = XrayInfo()
    #
    print_flag = False
    two_theta = []
    intensity = []
    #
    # Reference information from Xray Text page
    #
    xray_info.author = fl[1]
    xray_info.journal = fl[2]
    xray_info.title = fl[3]
    #
    for item in fl:
        if 'WAVELENGTH' in item:
            xray_info.wavelength = float(item.split()[-1])
        #
        if '=====' in item:
            print_flag = False
        if print_flag:
            fooline = item.split()
            two_theta.append(float(fooline[0]))
            intensity.append(float(fooline[1]))
        if '2-THETA' in item:
            print_flag = True
       
    ####
    #
    # printing and debugging session
    #
    #print('XRD data points of ' + name)
    #print('Two Theta : ' + str(two_theta[:10]))
    #print('Intensity : ' + str(intensity[:10]))
    # 
    #writing_file = open('xray.csv', 'a')
    #writing_file.write(name + ',' + repr(two_theta) + ',' + repr(intensity) + '\n')
    #writing_file.close()
    # 
    # END printing session
    #
    return xray_info
####

if __name__ == '__main__':
    #
    get_xray_info( name='' )
