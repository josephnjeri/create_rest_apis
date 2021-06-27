from meeting import Meeting
name = "Dr. Joseph Njeri"
Interviewer = "Mr Steven Njoroge"
profession = "Data Science"
company = "EDI GmbH"
city = "Karlsruhe"
country = "Deutschland"

obj = Meeting(name, Interviewer, profession, company, city, country)

print(obj.ask_name())
print(obj.say_name())
print(obj.greet())
print(obj.respond())
print(obj.ask_profession())
print(obj.admit_profession())