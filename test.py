import requests
new_url ="https://api-test.orderhandler.com/admin/manage/sp/query-simple"
params ={"Cookie":"SESSION=NzM1OGU1MTUtZjBlZS00YTk3LWE4M2QtZDU1MTI3NjQzYWE0"}
payload = {
    "status": 1,
    "paging": "false"
}

result = requests.post(new_url,params=params,json=payload)

print(result)
