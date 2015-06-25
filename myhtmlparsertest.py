import unittest
import myhtmlparser
import time
import os

'''Base Class for Unit Test'''
class MyHtmlParserTest(unittest.TestCase):
	def setUp(self):
		# print "Setting up :::"
		self._mhtp = myhtmlparser.MyHtmlParser()

		self._download_test_dir = "download_test_dir";
		self._create_folder_dir = "create_folder_dir";

		#create new directory
		if not os.path.exists(self._download_test_dir):
			os.makedirs(self._download_test_dir);

		if not os.path.exists(self._create_folder_dir):
			os.makedirs(self._create_folder_dir)

	def tearDown(self):
		# print "Tearing Down :::"
		self._mhtp = None

		#clean all directories
		if os.path.exists(self._download_test_dir):
			self.removeDir(self._download_test_dir);
			os.removedirs(self._download_test_dir);
		if os.path.exists(self._create_folder_dir):
			self.removeDir(self._create_folder_dir);
			os.removedirs(self._create_folder_dir);

	def removeDir(self,dirName):
		for root, dirs, files in os.walk(dirName, topdown=False):
		    for name in files:
		        os.remove(os.path.join(root, name))
		    for name in dirs:
		        os.removedirs(os.path.join(root, name))

	# Valid url test
	@unittest.expectedFailure
	def test_bad_address(self):
		self._mhtp.start_parser('http://www.elizabethcastro.com/html5ed/examples/create_images/dithersafe.htm');

	def test_valid_address(self):
		self._mhtp.start_parser('http://www.elizabethcastro.com/html5ed/examples/create_images/dithersafe.html');
	
	# Download address test
	@unittest.expectedFailure
	def test_bad_download_address(self):
		self._mhtp._server_addr = 'http://www.elizabethcastro.com/html5ed/examples/create_images';
		self._mhtp._dirName = self._download_test_dir;
		self._mhtp.download_img('diter.gif');

	def test_valid_download_address(self):
		self._mhtp._server_addr = 'http://www.elizabethcastro.com/html5ed/examples/create_images';
		self._mhtp._dirName = self._download_test_dir;
		imgName = 'dither.gif'
		self._mhtp.download_img(imgName);
		print os.listdir(self._download_test_dir);
		if not imgName in os.listdir(self._download_test_dir):
			raise ValueError('file not downloaded')
	
	@unittest.expectedFailure
	def test_empty_server_address_when_downloading(self):
		self._mhtp._dirName = self._download_test_dir;
		self._mhtp.download_img('dither.gif');

	@unittest.expectedFailure
	def test_empty_dirName_when_downloading(self):
		self._mhtp._server_addr = 'http://www.elizabethcastro.com/html5ed/examples/create_images';
		self._mhtp.download_img('dither.gif');

	# Base address test
	@unittest.expectedFailure
	def test_bad_base_address(self):
		self._mhtp.extract_basepath('www.elizabethcastro.com/html5ed/examples/create_images');

	def test_valid_base_address(self):
		self._mhtp.extract_basepath('http://www.elizabethcastro.com/html5ed/examples/create_images');

	# Start Tag tests
	def test_empty_attribute_start_tag(self):
		self._mhtp.handle_starttag('img',())

	def test_valid_start_tag(self):
		self._mhtp.handle_starttag('img',["src","dither.gif"])

if __name__ == '__main__':
    unittest.main()
		