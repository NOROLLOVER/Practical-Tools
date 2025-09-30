import re
from datetime import datetime

r"""
“.”:匹配单个字符；“*”:匹配前一个字符的0次或多次；
“+”：匹配前一个字符的1次或多次；“？”匹配前一个字符的0次或1次
“^”：匹配字符串开头；“$”匹配字符串结尾
“[]”字符集，匹配其中任意一个字符，“（）”分组，将一部分正则作为整体
“|”或操作，匹配两边任意一个模式

\w：匹配字母、数字或下划线（等价于 [a-zA-Z0-9_]）
\d：匹配任意数字（等价于 [0-9]）
\s：匹配空白字符（空格、制表符、换行等）
\b：匹配单词边界
"""

# 从字符串开头匹配
# re.match()
# 在整个字符串中搜索第一个匹配
# re.search()
# 找到所有匹配的子串，返回列表
# re.findall()
# 替换匹配的子串
# re.sub()


if __name__ == '__main__':
    text = "Hello, my email is example@domain.com and another is test123@gmail.com"
    email_pattern = r"(\w+@\w+\.\w+)"
    # 查找第一个匹配
    first_email = re.search(email_pattern,text)
    print(first_email.group(1))
    print("\t")

    # 查找所有匹配，返回的是一个列表
    all_email = re.findall(email_pattern,text)
    for email in all_email:
        print(email)

    #匹配连在一起的数字
    numbers = "Age: 25, Height: 180cm, Weight: 75kg"
    numbers_pattern = r"\d+"
    print(re.findall(numbers_pattern, numbers))

    # 字符串替换
    text_with_links = "Visit https://www.baidu.com and http://www.text.org"
    place_pattern = r"\w+://\w+\.\w+\.\w+"
    print(re.sub(place_pattern, "[***]", text_with_links))

    # 4. 分组匹配
    date = datetime.now().date()
    date_text = f"今天是 {date}"
    print(date_text)
    now_date_pattern = r"(\d+)-(\d+)-(\d+)"
    print(re.findall(now_date_pattern, date_text))
    for now_date in re.findall(now_date_pattern, date_text):
        year,month,day = now_date
        print(f"明天是{year}-{month}-{int(day)+1}")



    date_pattern = r"(\d{4})-(\d{2})-(\d{2})"

    print(re.findall(date_pattern,date_text))

    # 查找所有日期并提取年、月、日
    matches = re.findall(date_pattern, date_text)
    for match in matches:
        year, month, day = match
        print(f"日期: {year}年{month}月{day}日")



