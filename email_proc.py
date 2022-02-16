def email_Process(email):
    username = email[0:email.index("@")]
    email_domain = email[email.index("@")+1:]
    return [username, email_domain]

def printMsg(username, email_domain):
    print(f"Username is {username}; Email Domain is {email_domain}")

def main():
    email = input("plese enter your email address: ").strip()
    username, email_domain = email_Process(email)
    printMsg(username, email_domain)

if __name__ == "__main__":
    main()