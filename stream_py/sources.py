from io import BytesIO

from PIL import ImageGrab


class ImageSource(object):

    pass


class ScreenSource(ImageSource):

    @staticmethod
    def get_frame():
        image = ImageGrab.grab()
        _ = BytesIO()
        image.save(_, format="JPEG")
        _.seek(0)
        frame = _.getvalue()
        return (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

    def __iter__(self):
        return self

    def __next__(self):
        return self.get_frame()
