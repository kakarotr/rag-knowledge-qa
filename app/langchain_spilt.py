from langchain.text_splitter import CharacterTextSplitter

text = "1812年，俄罗斯违抗“大陆封锁”政策，拿破仑发兵伐俄，意图歼灭俄军主力，但最终因战略失败，无功而返。1813年，各国缔结第六次反法同盟；拿破仑虽在春季战局逼和联军，然秋季遭遇多面夹击陷入劣势，至莱比锡战役大败后被迫撤回本土。1814年，他以机动战术屡挫敌军，然联军大举犯境之际攻入巴黎，终使其宣告退位，遭流放至意大利厄尔巴岛。1815年，拿破仑一度返回法国，重建百日王朝，但于滑铁卢战役再度败北，并远囚于大西洋圣赫勒拿岛，至1821年病逝。"

text_splitter = CharacterTextSplitter(separator="。", chunk_size=200, chunk_overlap=50)

chunks = text_splitter.split_text(text)

for i, chunk in enumerate(chunks):
    print(i, chunk)
