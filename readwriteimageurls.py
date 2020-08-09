# Import the libraries
import requests
import shutil
import wget
import urllib.request
from logging_ import setup_logger
import logging
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
log_error = setup_logger(name ='error', log_file = 'debug.log', level=logging.ERROR,formatter=formatter)
log_info = setup_logger(name ='info', log_file = 'info.log', level=logging.INFO,formatter=formatter)

class UrlImage(object):

    def __init__(self,url,path):
        self.url_ = url
        self.path = path


    def file_name(self):
        """
        :return:  filename of the image
        """
        filename = self.url_.split('/')[-1]

        return filename


    def open_url(self):

        """
        :return: Saves file once status code is 200
        """
        try:
            r = requests.get(self.url_,stream =True)
        except Exception as e:
            log_error.error('url image error {0} '.format(e))


        if r.status_code == 200:
            r.raw.decode_content = True

            with open(self.path + self.file_name(), 'wb') as f:

                shutil.copyfileobj(r.raw, f)

                log_info.info('Image save {}'.format(self.path + self.file_name()))
        else :
            log_error.error('url image could not be saved status code {}'.format(r.status_code))




    def wget_image(self):
        """
        :wget image - downloads the image given url
        """
        try:
            image_file = wget.download(self.url_,self.path+self.file_name())
            log_info.info("Image Successfully Downloaded: {0}".format(image_file))
        except Exception as e:
            log_error.error("url image could not be saved {}".format(e))



    def urllib_request(self):
        """
       :urllib - downloads images from url
       """
        try:
            opener = urllib.request.build_opener()
            opener.addheaders = [('User-Agent',
                                  'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
            urllib.request.install_opener(opener)

            urllib.request.urlretrieve(self.url_, self.path+self.file_name())
            log_info.info("Image Successfully Downloaded: {0}".format(self.path+self.file_name()))
        except Exception as e:
            log_error.error("url image could not be saved {}".format(e))






