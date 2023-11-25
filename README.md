# GAOKAO-Bench-2023

GAOKAO-Bench-2023将中国2023年高考选择题作为数据集,是对[GAOKAO-Bench](https://github.com/OpenLMLab/GAOKAO-Bench)(包含2010-2022年高考题)测评框架的补充.我们希望将GAOKAO-Bench打造成可持续的大模型测评框架,见证中文大语言模型的不断发展.

## 数据集

GAOKAO-Bench-2023的数据类型如下表所示,具体数据格式可参见[GAOKAO-Bench](https://github.com/OpenLMLab/GAOKAO-Bench#json%E6%A0%BC%E5%BC%8F%E8%AF%B4%E6%98%8E).

| 名称                             | 类型                  | 选择题数量 |
| -------------------------------- | --------------------- | ---------- |
| 2023_Math_MCQs                   | single_choice         | 49         |
| 2023_History_MCQs                | single_choice         | 33         |
| 2023_Biology_MCQs                | single_choice         | 15         |
| 2023_Political_Science_MCQs      | single_choice         | 29         |
| 2023_Physics_MCQs                | multi_choice          | 11         |
| 2023_Chemistry_MCQs              | single_choice         | 9          |
| 2023_Chinese_Modern_Lit          | multi_question_choice | 12         |
| 2023_English_Fill_in_Blanks      | multi_question_choice | 70         |
| 2023_English_Cloze_Test          | five_out_of_seven     | 20         |
| 2023_Geography_MCQs              | multi_question_choice | 17         |
| 2023_English_Reading_Comp        | multi_question_choice | 60         |
| 2023_Chinese_Lang_and_Usage_MCQs | multi_question_choice | 4          |
| Total                            |                       | 329        |

## 评测

评测框架和GAOKAO-Bench相同,具体文件见下表:

| 文件名                      | 功能                       |
| --------------------------- | -------------------------- |
| /Bench/objective_bench      | 生成客观题(选择题)答案     |
| /Bench/bench_function       | 测试相关函数               |
| /Bench/2023_Obj_Prompt.json | 2023年客观题(选择题)Prompt |

具体测评方式可以参考[GAOKAO-Bench](https://github.com/OpenLMLab/GAOKAO-Bench#%E7%AE%80%E5%8D%95%E7%A4%BA%E4%BE%8B).
