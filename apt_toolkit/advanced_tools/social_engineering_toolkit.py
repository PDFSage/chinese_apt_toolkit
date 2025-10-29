def generate_pretext(target_name, target_company):
    pretext = f"Hello {target_name}, this is John from the IT department at {target_company}. We're having some issues with your account and need you to verify some information."
    return pretext

def main():
    target_name = input("Enter target name: ")
    target_company = input("Enter target company: ")
    pretext = generate_pretext(target_name, target_company)
    print(pretext)

if __name__ == "__main__":
    main()
