import requests,datetime
pixela_endpoint = "https://pixe.la/v1/users"
TOKEN = ""#enter your token id (enter any character and number 0-9 but of length between 8-128)"
USER_NAME = ""#enter your user_name"
Graph_id = ""#enter the graph id"
graph_name = ""#"enter the graph name(like why r u using for cycling then type cycling graph)if u want to other  then update create a graph "
now = datetime.datetime.now()
# print(type(now.strftime("%Y%m%d")))
#---------------------------------------------------creating a user(POST)-----------------------------------------------------------------------------------------
user_parameter = {
    "token":TOKEN,
    "username" : USER_NAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}
response = requests.post(url=pixela_endpoint,json=user_parameter)
print(response.text)

#---------------------------------------------------------------create  a graph definition(POST)---------------------------------------------------------------------
graph_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs"
graph_config = {
    "id":Graph_id,
    "name":graph_name,
    "unit":"km",
    "type":"float",
    "color":"sora"
}
header = {
    "X-USER-TOKEN":TOKEN
}
response  = requests.post(url=graph_endpoint,json=graph_config,headers = header)
print(response.text)
#-------------------------------------------------------------todays work done (Post a Pixel)----------------------------------------------------------------------
pixel_endpoint = f"{graph_endpoint}/{graph_config['id']}"

print("not a user")
cycled_km = input("enter the km u cycled today ")
pixel_config = {
    "date":now.strftime("%Y%m%d"),
    "quantity":f"{cycled_km}"
}
response  = requests.post(url=pixel_endpoint,json=pixel_config,headers = header)
print(response.text)
#------------------------------------------------------------Update the pixel(Put)-------------------------------------------------------------------------------
#To update this comment out above both response
update_km = "enter the km u update today or enter no to not update"
update_endpoint = f"{pixel_endpoint}/{now.strftime('%Y%m%d')}"
update_config = {
    "quantity":update_km
}
response  = requests.put(url=update_endpoint,json=update_config,headers = header)
print(response.text)
#to delete
#-----------------------------------------------------------------Delete a pixel(delete)------------------------------------------------------------------------------------
#To delete this ...........comment out above both response
delete_endpoint = update_endpoint
response = requests.delete(url=delete_endpoint, headers=header)
print(response.text)
# visit here to see
# https://pixe.la/v1/users/{USER_NAME}/graphs/{Graph_id}.html

