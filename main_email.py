from email_proc import email_Process, printMsg
def main():
    emails = ['qud@gmail.com', 'youtune@codexplore.dev', 'face@gmail.com']
    for email in emails:
        username, email_domain = email_Process(email)
        printMsg(username, email_domain)
if __name__ == "__main__":
    main()
