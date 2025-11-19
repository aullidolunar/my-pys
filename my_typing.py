import time

def type_writing(t_nfo):
    delay=float(t_nfo.get("delay", 0.25))
    text=t_nfo.get("text", "no-string")
    for ch in text:
        print(ch, end='', flush=True)
        time.sleep(delay)

nfo = {
    "delay": 0.25,
    "text": "Hello world! :)"
}

type_writing(nfo)