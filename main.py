import requests
from datetime import datetime as dt


today = dt.now()
date = today.strftime("%Y%m%d")
q=input("How many Hours Did You Work on Azure Today?")

username = "promit"
token = "FlipFlop123"
pixela_endpoint = "https://pixe.la/v1/users"
graph_endpoint = "https://pixe.la/v1/users/promit/graphs"
graph_post_api = "https://pixe.la/v1/users/promit/graphs/promit-graph1"
graph_put_api = f"https://pixe.la/v1/users/promit/graphs/promit-graph1/{date}"

graph_params = {
    "X-USER-TOKEN": token}

user_params = {
    "token": token,
    "username": "promit",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

graph_config = {
    "id": "promit-graph1",
    "name": "Programming",
    "unit": "hr",
    "type": "float",
    "color": "sora"
}


graph_post = {
    "date": date,
    "quantity": q,
}

graph_update = {
    "name": "Azure-Everyday",
    "unit":"hrs",
    "timezone":"Asia/Kolkata"

}

# response=requests.post(url=pixela_endpoint,json=user_params)
# print(response.text)

# response = requests.post(url=graph_endpoint,json=graph_config,headers=graph_params)
# print(response.text)

response = requests.post(url=graph_post_api, json=graph_post, headers=graph_params)
print(response.text)

# update=requests.put(url=graph_post_api,headers=graph_params,json=graph_update)
# print(update.text)

# update = requests.delete(url=graph_put_api,headers=graph_params)
# print(update.text)


