# ESL AI Feedback Analysis 项目

这是一个简单的学习分析项目，用Python语言分析高中学生如何使用ChatGPT生成的英语作文反馈。

## 为什么做这个项目？
想要了解不同英语水平的学生如何与AI反馈互动，是否能改善他们的英语写作水平。

## 数据与工具
- Google Docs版本历史记录
- Coh-Metrix (文本分析工具)
- PM4Py (过程分析工具)

## 项目结构说明
- `cohmetrix_analysis.py`：计算文本的Coh-Metrix指标
- `pm4py_process.py`：分析学生修改作文的过程

## 怎么使用？
下载代码到你电脑，然后运行:
```bash
pip install -r requirements.txt
python cohmetrix_analysis.py
