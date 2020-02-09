import re
from urllib.parse import urlparse

def scraper(url, resp):
    links = extract_next_links(url, resp)
    return [link for link in links if is_valid(link)]

def extract_next_links(url, resp):
    List = []
    #resp is the page itself to look at (response)
    html = lxml.html.fromstring(resp)#assuming resp is an html
    links = lxml.html.iterlinks()#i think this is getting all the links
    count = 0 
    for link in links:
        (element, attribute, link, pos) = link[count]#i think access url through link
        urldefrag(link)#have to defragment the link
        List.add(link)
        count += 1
    #list() is the list of URLs scrapped from resp
    #list must only contain defragmented urls
    #save URL and web page on local disk if you want?
    # Implementation required.
    
    return list()

def is_valid(url):
    try:
        parsed = urlparse(url)
        if parsed.scheme not in set(["http", "https"]):
            return False
        ##not sure if syntax correct here
        elif parsed.hostname not in set(["ics.uci.edu/", "cs.uci.edu/",
                                       "informatics.uci.edu/", "stat.uci.edu/",
                                        "today.uci.edu/"]):
            return False
        elif parsed.hostname == "today.uci.edu/":
            if parsed.path != "department/information_computer_sciences/":
                return False
        ##use urldefrag(original) to defragment urls for q1 on report
        return not re.match(
            r".*\.(css|js|bmp|gif|jpe?g|ico"
            + r"|png|tiff?|mid|mp2|mp3|mp4"
            + r"|wav|avi|mov|mpeg|ram|m4v|mkv|ogg|ogv|pdf"
            + r"|ps|eps|tex|ppt|pptx|doc|docx|xls|xlsx|names"
            + r"|data|dat|exe|bz2|tar|msi|bin|7z|psd|dmg|iso"
            + r"|epub|dll|cnf|tgz|sha1"
            + r"|thmx|mso|arff|rtf|jar|csv"
            + r"|rm|smil|wmv|swf|wma|zip|rar|gz)$", parsed.path.lower())

    except TypeError:
        print ("TypeError for ", parsed)
        raise
