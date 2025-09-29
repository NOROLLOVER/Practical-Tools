import re
import math

class ParseCsv:
    def parse_csv(self):
        total_tokens = 0
        pattern = r'completion_tokens: (\d+)'

        # 使用 readlines() 读取所有行，或者直接迭代文件对象
        with open(r"C:\JMeterLogs\jmeter.csv", "r", encoding="utf-8") as file:
            for line in file:  # 直接迭代文件对象更高效
                match = re.search(pattern, line)
                if match:
                    total_tokens += int(match.group(1))

        print(f"completion_tokens 总和: {total_tokens}")
        return total_tokens  # 添加返回值

if __name__ == '__main__':
    parser = ParseCsv()
    total = parser.parse_csv()
    # 现在可以使用 total 变量做其他处理
    avg_token = (total/(12*52.97))
    print(avg_token)