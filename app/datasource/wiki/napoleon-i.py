import re

import requests
import wikipedia
from opencc import OpenCC

wikipedia.set_lang("zh")
cc = OpenCC("t2s")

page = wikipedia.page("拿破仑一世")

content = cc.convert(page.content)

segments = [
    segment.replace("\n", "").replace("\r", "")
    for segment in re.split(r"\n==+ (.*?) ==+\n", content)
    if segment != "\n" and segment != "\r"
]

sections = requests.get(
    "https://zh.wikipedia.org/w/api.php?action=parse&page=%E6%8B%BF%E7%A0%B4%E4%BB%91%E4%B8%80%E4%B8%96&prop=sections&format=json"
).json()

sections_level = {}

for section in sections["parse"]["sections"]:
    sections_level[cc.convert(section["line"])] = int(section["level"]) - 1

print(sections_level)
