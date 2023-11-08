class Employee:
    def __init__(self, name, address, salary):
        self.name = name
        self.address = address
        self.salary = salary
        self.bonus_hours = 0
        self.skills_learned = []

    def calculate_bonus(self):
        return self.salary * (self.bonus_hours / 8*20)

    def add_skill(self, skill):
        self.skills_learned.append(skill)


class Manager(Employee):
    def __init__(self, name, address, salary, team_size, team_members):
        super().__init__(name, address, salary)
        self.team_size = team_size
        self.team_members = team_members

    def add_member(self, member):
        self.team_members.append(member)
        self.team_size = len(self.team_members)
        return f"{self.name} team is {self.team_members} ({self.team_size} members)"

    def remove_member(self, member):
        self.team_members.remove(member)
        self.team_size = len(self.team_members)
        return f"{self.name} team is {self.team_members} ({self.team_size} members)"

    def calculate_bonus(self):
        return super().calculate_bonus() + 1000


class Engineer(Employee):
    def __init__(self, name, address, salary, programming_languages):
        super().__init__(name, address, salary)
        self.programming_languages = programming_languages

    def add_language(self, language):
        self.programming_languages.append(language)
        return f"{self.name} is writing code in {self.programming_languages}"

    def remove_language(self, language):
        self.programming_languages.remove(language)
        return f"{self.name} is writing code in {self.programming_languages}"

    def write_code(self):
        return f"{self.name} is writing code in {self.programming_languages}."


class Salesperson(Employee):
    def __init__(self, name, address, salary, sales_target):
        super().__init__(name, address, salary)
        self.sales_target = sales_target

    def meet_sales_target(self):
        if self.sales_target >= 100000:
            return f"{self.name} exceeded the sales target!"
        else:
            return f"{self.name} needs to work harder to meet the sales target."


manager = Manager("John", "123 Main St", 80000, 10, ["Alice", "Bob"])
print(manager.add_member("Charlie"))
print(manager.remove_member("Alice"))
print(f"Bonus for {manager.name}: ${manager.calculate_bonus()}")

engineer = Engineer("Alice", "456 Elm St", 70000, ["Python", "Java"])
print(engineer.add_language("JavaScript"))
print(engineer.remove_language("Java"))

salesperson = Salesperson("Bob", "789 Oak St", 60000, 500000)
salesperson.bonus_hours = 20
print(salesperson.meet_sales_target())
print(f"Bonus for {salesperson.name}: ${salesperson.calculate_bonus()}")
