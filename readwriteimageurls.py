# Import the libraries
import requests
import shutil
from logging_ import setup_logger
import logging
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
log_error = setup_logger(name ='error', log_file = 'debug.log', level=logging.ERROR,formatter=formatter)
log_info = setup_logger(name ='info', log_file = 'info.log', level=logging.ERROR,formatter=formatter)

class UrlImage(object):

    def __init__(self,url,path):
        self.url_ = url
        self.path = path


    def file_name(self):

        filename = self.url_.split(',')[-1]

        return filename


    def open_url(self):
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






if __name__ == '__main__' :


    u = UrlImage(url="http://com.dataturks.a96-i23.open.s3.amazonaws.com/2c9fafb06477f4cb0164895548a600a3/dd0c53fe-8300-4422-80e2-7d446ae4a329___STR838.jpg",
                 path='/home/amogh/Pictures/image_url/')

    u.open_url()



