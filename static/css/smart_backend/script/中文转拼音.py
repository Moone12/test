# pip install pypinyin
from pypinyin import lazy_pinyin, Style
style = Style.TONE3
name_list=lazy_pinyin('李思贤', style=style)
print(''.join(name_list))