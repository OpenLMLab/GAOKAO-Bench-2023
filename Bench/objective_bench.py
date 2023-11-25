import sys
import os
import codecs

parent_path = os.path.dirname(sys.path[0])
if parent_path not in sys.path:
    sys.path.append(parent_path)

from models.openai_gpt4 import OpenaiAPI

from bench_function import get_api_key, export_distribute_json, export_union_json
import os
import json
import time


if __name__ == "__main__":
    # Load the MCQ_prompt.json file
    with open("./2023_Obj_Prompt.json", "r") as f:
        data = json.load(f)['examples']
    f.close()

# get the model_name and instantiate model_api
model_api = OpenaiAPI([""])
model_name = "gpt-4"
    
for i in range(len(data)):
    directory = "../Data"

    keyword = data[i]['keyword']
    question_type = data[i]['type']
    zero_shot_prompt_text = data[i]['prefix_prompt']
    print(model_name)
    print(keyword)
    print(question_type)

    export_distribute_json(
        model_api, 
        model_name, 
        directory, 
        keyword, 
        zero_shot_prompt_text, 
        question_type, 
        parallel_num=1, 
    )

    export_union_json(
        directory, 
        model_name, 
        keyword,
        zero_shot_prompt_text,
        question_type
    )
    


