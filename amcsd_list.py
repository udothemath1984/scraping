import scraperwiki
import lxml.html

def get_list():
    html = scraperwiki.scrape('http://rruff.geo.arizona.edu/AMS/all_minerals.php')
    
    root = lxml.html.fromstring(html)
    # get the links
    hrefs = root.xpath('//a/@href')
    
    # iid = ''
    
    data_name = []
    
    for href in hrefs:
       # print 'http://ahr13.mapyourshow.com' + href.attrib['href'] 
       # if 'javascript' in href:
       #    fid = href.split("(")[-1].replace("'", '').strip(')')
       #    iid = fid
       #    break
       if 'mineral' in href:
           data_name.append( href.split('/')[-1] )
    
    return data_name
###

# for item in data_name:
#    print item

# 
# # xray_html = scraperwiki.scrape('http://rruff.geo.arizona.edu/AMS/xtal_data/DIFfiles/.txt'.format(iid))
# # xray_root = lxml.html.fromstring(xray_html)
# # print xray_root:wq
# 
# import urllib2
# xray_response = urllib2.urlopen('http://rruff.geo.arizona.edu/AMS/xtal_data/DIFfiles/{0}.txt'.format(iid))
# # fooline = [ item for item in response.readlines() if 'href' in item and 'diffraction' in item]
# # for item in fooline:
# #     print item
# fl= xray_response.readlines()
# print_flag = False
# for item in fl:
#     if '=====' in item:
#         print_flag = False
#     if print_flag:
#         print item
#     if '2-THETA' in item:
#         print_flag = True
