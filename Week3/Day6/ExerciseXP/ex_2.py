import json

json_string = """
{
    "company": {
        "name": "TechCorp",
        "employee": {
            "name": "Alex",
            "payable": {
                "salary": 5000,
                "currency": "USD"
            }
        }
    }
}
"""

def main():
    data = json.loads(json_string)
    current_salary = data["company"]["employee"]["payable"]["salary"]
    print(f"Current salary: {current_salary}")

    data["company"]["employee"]["birth_date"] = "1812-05-15"

    with open("modified_data.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

    print("The file is saves as 'modified_data.json'")


main()