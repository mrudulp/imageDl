#! /usr/bin/env python
import urllib2 # required to parse source
import urllib
import os # required to check/create directory
import time # required to get current time
import datetime # required to convert time to datetime
from urlparse import urlparse # required to parse url path
from posixpath import basename, dirname # required to extract directory path
from HTMLParser import HTMLParser # required to parse html doc

class MyHtmlParser(HTMLParser):

    def __init__(self):
        # initialize the base class
        HTMLParser.__init__(self)
        # initialize member variables
        self._imgTagFound = False;
        self._server_addr = "";
        self._imgFiles = [];
        self._dirName = "";

    def handle_starttag(self, tag, attrs):
        
        if "img" in tag:
            self._imgTagFound = True;
        for attr in attrs:
            for att in attr:
                #ToDo: We need to ensure src was previous key.
                if "src" not in att: #Assuming value for src key
                    self._imgFiles.append(att); # append to the list
    
    def create_folder(self):
        try:
            ts = time.time()
            dirName = datetime.datetime.fromtimestamp(ts).strftime('%Y_%m_%d_%H_%M');
            if not os.path.exists(dirName): # Checking directory is not created earlier
                self._dirName = dirName;
                # print "Setting dirName:"+self._dirName;
                os.makedirs(dirName);
            elif os.path.exists(dirName):
                # print "directory exists:"+dirName;
                self._dirName = dirName;
        except OSError as exception:
            if exception.errno != errno.EEXIST:
                raise
    
    def download_img(self,imgFile):
        fetcher = urllib.URLopener();
        if not self._dirName:
            raise ValueError('Directory Name cannot be empty ')
        filename = self._dirName+"/"+imgFile;
        # print "filename:"+filename
        if not self._server_addr:
            raise ValueError('Server Name cannot be empty')
        srvaddr = self._server_addr+"/"+imgFile
        # print "SrvAddr:"+srvaddr
        fetcher.retrieve(srvaddr,filename);

    # expects url in http:// format
    def extract_basepath(self,url):
        if not "http" in url:
            raise ValueError('Specify address in http://<> format')
        parse_obj = urlparse(url)
        server_base_addr = parse_obj.netloc
        path = dirname(parse_obj.path)
        scheme = parse_obj.scheme
        l = [scheme,"://",server_base_addr,path];
        self._server_addr = ''.join(l);

    def start_parser(self,stringArg):
        self.create_folder();
        if "http" in stringArg:
            self.extract_basepath(stringArg); # Extract Server Path
            urlHandle = urllib2.urlopen(stringArg);
            htmlstr = urlHandle.read()
            self.feed(htmlstr.decode('utf-8')); #Start Parsing

        for imgFile in self._imgFiles:
            self.download_img(imgFile); #Download all files found
        if not self._imgTagFound:
            os.removedirs(self._dirName);

if __name__ == '__main__':
    import sys
    try:
        mhtp = MyHtmlParser();
        
        if not (sys.argv[1:]):
            print 'Usage:  %s <url>' % sys.argv[0]
        else:
            mhtp.start_parser(sys.argv[1]);
    except ValueError as err:
        print err;
    except AssertionError as err:
        print err;