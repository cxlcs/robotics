from paddleocr import PaddleOCR, draw_ocr
from sys import argv
from translator import translate
from speech import tts

photo = argv[1] if len(argv) >= 2 else "receipt.jpg"
lang = argv[2] if len(argv) >= 3 else "en"
# Paddleocr supports Chinese, English, French, German, Korean and Japanese.
# You can set the parameter `lang` as `ch`, `en`, `fr`, `german`, `korean`, `japan`
# to switch the language model in order.
ocr = PaddleOCR(
    use_angle_cls=True, lang=lang
)  # need to run only once to download and load model into memory
img_path = "./photos/" + photo
result = ocr.ocr(img_path, cls=True)
text = ""
for idx in range(len(result)):
    res = result[idx]
    for r in res:
        print(r[-1][0])
        text += r[-1][0] + " "
print(text)
t = translate(text, "en", "fr")
print(t)
tts(t["translatedText"], "en", "co.uk")

"""# draw result
from PIL import Image

result = result[0]
image = Image.open(img_path).convert("RGB")
boxes = [line[0] for line in result]
txts = [line[1][0] for line in result]
scores = [line[1][1] for line in result]
im_show = draw_ocr(
    image,
    boxes,
    txts,
    scores,
)
im_show = Image.fromarray(im_show)
im_show.save("result.jpg")
"""
