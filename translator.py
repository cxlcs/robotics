from sys import argv
import requests


def translate(text, target="en", source="auto"):
    r = requests.post(
        "https://t.cxllm.uk/translate",
        json={
            "q": text,
            "source": source,
            "target": target,
            "format": "text",
            "api_key": "fac3533e-1c27-47fa-ab25-4f1b31a1b2f6",
        },
        timeout=None,
    )
    r = r.json()
    return r


if __name__ == "__main__":

    source = argv[1] if len(argv) >= 2 else "auto"
    target = argv[2] if len(argv) >= 3 else "en"
    text = " ".join(argv[3:]) if len(argv) >= 4 else input("Enter original text: ")
    r = translate(text, target, source)
    try:
        print("Detected Language:", r["detectedLanguage"]["language"])
        print("Confidence:", r["detectedLanguage"]["confidence"])
    except:
        pass

    print("Translation to", target + ":", r["translatedText"])
