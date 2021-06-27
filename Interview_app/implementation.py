from meeting import Meeting
name = "Everline  Ogola"
profession = "Surveryor"
company = "JOOS engineering company"
city = "Karlsruhe"
country = "Deutschland"


obj = Meeting(name, profession, company, city, country)

print(obj.ask_name())
print(obj.say_name())
print(obj.greet())
print(obj.respond())
print(obj.ask_profession())
print(obj.admit_profession())