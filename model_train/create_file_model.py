import yaml
from yaml.loader import SafeLoader, BaseLoader, FullLoader
import json
# Open the file and load the file
arrfile = ["chitchat.yml", "faq.yml",
           "general.yml", "nlu.yml", "out_of_scope.yml"]
path_data ="" # data/nlu/
for files in arrfile:
    with open("autobot.json", "a", encoding='utf-8') as f:
        with open(path_data+files, "r+", encoding='utf-8') as f0:
            data = yaml.load(f0, Loader=SafeLoader)
            for nl in data['nlu']:
                if list(nl.keys())[0] == 'intent':
                    text = str(nl['examples']).split("-")
                    for te in text:
                        if te != "":
                            ob = {}
                            ob['prompt'] = te+" -->"
                            ob["completion"] = " "+nl['intent']+" .END"
                            json_object = json.dumps(ob, ensure_ascii=False)
                            f.write(json_object)
                            f.write(",")

with open('autobot.json', 'rb+') as fh:
    fh.seek(-1, 2)
    fh.truncate()
