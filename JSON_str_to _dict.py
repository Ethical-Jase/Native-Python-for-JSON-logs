import json

# enter own string path / ID
logstr1 = '{"_index": ".ds-logs-elastic_agent.endpoint_security-default-2023.08.18-000002","_id": "M82oJYoBdNYBaOvRrqci","_version": 1,"_score": 0,  "_source": {    "agent": {      "name": "DESKTOP-C2SGOOT",      "id": "2e068a13-dea5-4331-b275-f56c179fec00",      "type": "endpoint",      "ephemeral_id": "8883aa22-2d06-4bd6-afce-f1456b0d9a4f",      "version": "8.9.1"    }  }}'
logstr2 = '{"_index": ".ds-logs-elastic_agent.endpoint_security-default-2023.08.18-000002","_id": "M82oJYoBdNYBaOvRrqch","_version": 1,"_score": 0,  "_source": {    "agent": {      "name": "DESKTOP-C2SGOOT",      "id": "2e068a13-dea5-4331-b275-f56c179fec00",      "type": "endpoint",      "ephemeral_id": "8883aa22-2d06-4bd6-afce-f1456b0d9a4f",      "version": "8.9.1"    }  }}'

#list1 = []

dict1 = json.loads(logstr1)
dict2 = json.loads(logstr2)

list1 = [dict1,dict2]
print(" {0} {1}".format(list1[0]["_index"], list1[1]["_score"]))

for x in list1:
    
#example to print all ids
    print(x["_id"])

#example to print specific id
    if x["_id"] == "M82oJYoBdNYBaOvRrqch" :
     print(x["_id"])

#example to print whole dict if specific id is found
    if x["_id"] == "M82oJYoBdNYBaOvRrqch" :
     print(x)
