# positional and keyword arguments
def introduce(name, age, country):
    print(f"My name is {name}, I am {age} years old from {country}.")

introduce("Alikhan", 20, "Kazakhstan")  # positional
introduce(age=25, name="Samet", country="Kazakhstan")  # keyword

# mixed arguments
def describe(name, country="Kazakhstan"):
    print(f"{name} lives in {country}.")

describe("Alikhan")
describe("Samet", "USA")