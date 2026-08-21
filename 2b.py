from experta import *
class StudentFacts(Fact):
    pass
class CareerExpertSystem(KnowledgeEngine):
    @Rule(StudentFacts(likes='Maths'), StudentFacts(likes='Physics'))
    def mechanical(self):
        print("Suggested Career Path: Mechanical Engineering")
    @Rule(StudentFacts(likes='Programming'), StudentFacts(likes='Maths'))
    def computer(self):
        print("Suggested Career Path: Computer Engineering")
    @Rule(StudentFacts(likes='Biology'), StudentFacts(likes='Chemistry'))
    def biotech(self):
        print("Suggested Career Path: Biotechnology")
    @Rule(StudentFacts(likes='Circuits'), StudentFacts(likes='Maths'))
    def electronics(self):
        print("Suggested Career Path: Electronics Engineering")
    @Rule(StudentFacts(likes='Chemistry '), StudentFacts(likes='physics'))
    def chemical_eng(self):
        print("Suggested Career Path: Chemical engineering")
    @Rule(StudentFacts(likes='History'), StudentFacts(likes='English'))
    def civil_services(self):
        print("Suggested Career Path: Law / Civil Services")
    @Rule(StudentFacts(likes='Economics'), StudentFacts(likes='Maths'))
    def data_analyst(self):
        print("Suggested Career Path: Data Analyst / Actuarial Science")
    @Rule(StudentFacts(likes='Psychology'), StudentFacts(likes='Biology'))
    def neuroscientist(self):
        print("Suggested Career Path: Neuroscience / Cognitive Science")
    @Rule(StudentFacts(likes='Business'), StudentFacts(likes='Maths'))
    def finance(self):
        print("Suggested Career Path: Financial Engineering / Investment Banking")
    @Rule(StudentFacts(likes='Political_Science'), StudentFacts(likes='History'))
    def public_policy(self):
        print("Suggested Career Path: Public Policy / International Relations")
    @Rule(StudentFacts(likes='Art'), StudentFacts(likes='Programming'))
    def ui_ux_designer(self):
        print("Suggested Career Path: UI/UX Design / Interactive Media")
    @Rule(StudentFacts(likes='Environmental_Science'), StudentFacts(likes='Chemistry'))
    def env_engineer(self):
        print("Suggested Career Path: Environmental Engineering")

     

def main():
    engine = CareerExpertSystem()
    engine.reset()
    print("Welcome to the Career Path Expert System!")
    interests = input("Enter your interests separated by commas (e.g., Maths, Physics, Programming,biology,chemistry,art,environmental_science ): ").split(',')
    for interest in interests:
        engine.declare(StudentFacts(likes=interest.strip()))
    engine.run()
if __name__ == "__main__":
    main()
