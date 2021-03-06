class Meeting:
    def __init__(self, name, interviewer, profession, company, city, country):
        self.name = name
        self.interviewer = interviewer
        self.profession = profession
        self.company = company
        self.city = city
        self.country = country

    
    def ask_name(self):
        return f'{self.interviewer}: what is your name?'
    
    def say_name(self):
        return f'{self.name}: My name is {self.name}'

    def greet(self):
            return f'{self.interviewer}: How are you {self.name}?'
    
    def respond(self):
        return f'{self.name}: I am very fine'
    
    def ask_profession(self):
        return f'{self.interviewer}: What is your profession {self.name}?'
    
    def admit_profession(self):
        return f'{self.name}: I work mainly as a {self.profession} at the {self.company} in {self.city}, {self.country}'
    
    

    

