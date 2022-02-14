import os
import tornado.ioloop
import tornado.web
import tornado.httpserver
from tornado.escape import json_decode, json_encode, utf8
from paddleocr import PaddleOCR

file_name = "uuid.txt"
# if not os.path.exists(file_name):
#     os.(file_name)

with open("uuid.txt", 'r') as f:
    uuids = f.read().split(',')
f.close()

ocr = PaddleOCR(use_angle_cls=True, lang="ch")  # need to run only once to download and load model into memory


class IndexHandler(tornado.web.RequestHandler):
    def get_photo_ret(path):
        img_path = path
        imgs_val = ""
        try:
            result = ocr.ocr(img_path, cls=True)
        except:
            imgs_val = "ERROR_IMG_NOT_FOUND"
            return imgs_val
        for line in result:
            if line[1][1] > 0.98:
                imgs_val = line[1][0]
            else:
                imgs_val = "ERROR_IMG_REC_ERROR"
        return imgs_val

    def post(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
        path = self.get_body_argument("path")
        author_key = self.get_body_argument("key")
        if author_key in uuids:
            ret_val = IndexHandler.get_photo_ret(path=path)
        else:
            ret_val = "user does not exist"
        self.write(json_encode(ret_val))

    def get(self):
        self.write("get method is not available")


def make_app():
    return tornado.web.Application([
        (r"/api/v1/vin-rec", IndexHandler),
    ])


if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    print("Server Start Ok.....")
    tornado.ioloop.IOLoop.current().start()
