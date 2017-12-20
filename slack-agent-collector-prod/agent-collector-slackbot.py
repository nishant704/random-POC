import requests
import json
import sys
import os


IP=os.environ['NOMAD_CLIENT_IP_ADDRESS']
sys.stdout.write(str(IP))

list_mtcagent=requests.get('http://'+IP+':8500/v1/health/checks/mtcagent')
sys.stdout.write(str(list_mtcagent))
#print type(list_mtcagent)[

alive_agents=[]
for dicts in list_mtcagent.json():
    #print type(dicts)
    if dicts['Status'] == "passing":
        #print dicts['ServiceTags'][0]+'-'+dicts['ServiceTags'][1]
        alive_agents.append(dicts['ServiceTags'][0]+'-'+dicts['ServiceTags'][1])

#print alive_agents
sys.stdout.write(str(alive_agents))
print "-----------------------"

list_mtc_collector=requests.get('http://'+IP+':8500/v1/health/checks/mtcagent-collector')
sys.stdout.write(str(list_mtc_collector))

alive_collectors=[]
for collector in list_mtc_collector.json():
    if collector['Status'] == "passing":
        alive_collectors.append(collector['ServiceTags'][0])

    for agents in alive_agents:
        if  agents==collector["ServiceTags"][0] and collector['Status'] == "passing":
            print "Everything is Good with: "+agents
        elif agents==collector["ServiceTags"][0] and collector['Status'] == "critical":
            print "Bad-agents: "+agents
        else:
            pass

# print "Alive Agents with No Collectors ", set(alive_agents) - set(alive_collectors)

final = set()
final = set(alive_agents) - set(alive_collectors)

# print (str(final))

clean_final_list = map(str,final)


# print clean_final_list
sys.stdout.write(str(clean_final_list))

# str(final)[3:].encode('utf8'),

payload = {"text": "*Alive Agents with No Active Collectors ->*"+str(clean_final_list),"username": "Agent-Collector Bot"}

# print payload
post_to_channel=requests.post("https://hooks.slack.com/services/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",data=json.dumps(payload))
print "done"
