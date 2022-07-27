from pyrock import Client

client = Client()

rock = client.get_random_rock()

print(rock.name)

newrock = client.get_rock("glow rock")

print(newrock.description)