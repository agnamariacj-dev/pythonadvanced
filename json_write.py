#json read/write
#json write
f=open("data.json",'w')
content=[{"name":"arun","age":23},
         {"name":"amal","age":25}]
import json
json.dump(content,f)
f.close()
