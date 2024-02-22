from supabase_py import create_client, Client
##################################
# INSTALL SUPABASE: pip install supabase-py
##################################

# xZmV05zR7JaK9N8u DO NOT DELETE

#URL & Key to connect with Supabase
url = "https://gntzynfeplzsjtwuzwpb.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImdudHp5bmZlcGx6c2p0d3V6d3BiIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MDcyNzAyMDMsImV4cCI6MjAyMjg0NjIwM30.WBravl32P51EEqg-BykO2QyUoxgfINwCpvnVGXIbazM"
print("Supabase URL:", url)

#Printing contents of the database
supabase: Client = create_client(url, key)
response = supabase.table('Users').select("*").execute()
print(response)

response = {'data': [{'id': 2, 'Name': 'OPUS'}, {'id': 10, 'Name': 'Reese'}, {'id': 11, 'Name': 'Josh'}, {'id': 25, 'Name': 'Javi'}, {'id': 26, 'Name': 'Josh(again)'}, {'id': 28, 'Name': 'im_sorry_im_testing'}, {'id': 29, 'Name': 'test'}], 'status_code': 200}

target_id = 11  # replace with the ID you want to compare
target_name = 'TEST'  # replace with the Name you want to compare

for entry in response['data']:
    if entry['id'] == target_id:
        print(f"Match found for ID: {target_id} and Name: {target_name}")
        # Update the fields in the data
        target_id= entry['id']
        target_name = entry['Name']
        print("{} and {}".format(target_id, target_name))
        break
else:
    print(f"No match found for ID: {target_id} and Name: {target_name}")

print("Updated data:", response['data'])


#Adding data to database
#user_name = input("Enter your name: ")
#supabase.table("Users").insert({"Name": user_name}).execute()
print(response)



          
