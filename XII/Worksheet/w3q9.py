def LongToShort():
    with open("message.txt", "r") as file:
        with open("sms.txt", "w") as sms:
            content = file.read()[:151]
            sms.write(content)
            print("150 leading characters from message.txt written to sms.txt")


LongToShort()
