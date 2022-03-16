from pyrock import Client

client = Client()

rock = client.get_random_rock()

print(rock.name)

newrock = client.get_rock("glow roeck")

print(newrock.description)