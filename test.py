"""from paddleocr import PaddleOCR, draw_ocr
from sys import argv

# Paddleocr supports Chinese, English, French, German, Korean and Japanese.
# You can set the parameter `lang` as `ch`, `en`, `fr`, `german`, `korean`, `japan`
# to switch the language model in order.
ocr = PaddleOCR(
    use_angle_cls=True, lang="en"
)  # need to run only once to download and load model into memory
photo = argv[1] if len(argv) >= 2 else "receipt.jpg"
img_path = "./photos/" + photo
result = ocr.ocr(img_path, cls=True)
for idx in range(len(result)):
    res = result[idx]
    for line in res:
        print(line)


# draw result
from PIL import Image

print(result)
image = Image.open(img_path).convert("RGB")
boxes = [line[0] for line in result]
txts = [line[1][0] for line in result]
scores = [line[1][1] for line in result]
im_show = draw_ocr(image, boxes, txts, scores, font_path="./roboto.ttf")
im_show = Image.fromarray(im_show)
im_show.save("result.jpg")
"""

import easyocr

reader = easyocr.Reader(["en"])
result = reader.readtext("./photos/mastermind.png", detail=0)
print(result)
