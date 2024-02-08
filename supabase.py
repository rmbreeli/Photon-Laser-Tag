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

#Adding data to database
supabase.table("Users").insert({"Name": "Gashler"}).execute()
response = supabase.table('Users').select("*").execute()
print(response)



          
