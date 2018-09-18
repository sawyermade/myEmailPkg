import smtplib, ssl, requests

def smcEmail(toAddr, subject, msg, password, username=None, inPort=25, outPort=587):
    # From addr
    fromAddr = 'smc@sawyer0.com'

    # Sets username
    if username is None:
        username = fromAddr
    else:
        fromAddr = username

    # Gets server addr
    serverAddr = fromAddr.split('@')[-1]
    
    # Creates message with header
    header = 'FROM: {}\nTO: {}\nSUBJECT: {}\n'.format(fromAddr, toAddr, subject)
    msg = header + msg

    try:
        # Connects to server and sends mail
        context = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
        server = smtplib.SMTP_SSL(serverAddr, inPort)
        server.set_debuglevel(1)
        print('DEBUG')        
        server.connect(serverAddr, inPort)
        print('DEBUG')
        server.ehlo()
        server.starttls(context=context)
        server.ehlo()
        server.login(username, password)
        server.sendmail(fromAddr, toAddr, msg)

        # Returns true if complete
        return True

    except Exception as e:
        # Prints exception and returns false
        print(e)
        return False

def sendEmail(fromAddr, toAddr, subject, msg, password, serverAddr=None, username=None, inPort=25, outPort=587):
    # Sets username
    if username is None:
        username = fromAddr

    # Sets serverAddr
    if serverAddr is None:
        serverAddr = fromAddr.split('@')[-1]
    
    # Creates message with header
    header = 'FROM: {}\nTO: {}\nSUBJECT: {}\n'.format(fromAddr, toAddr, subject)
    msg = header + msg

    try:
        # Connects to server and sends mail
        server = smtplib.SMTP(serverAddr, inPort)
        server.connect(serverAddr, outPort)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(username, password)
        server.sendmail(fromAddr, toAddr, msg)

        # Returns true if complete
        return True

    except Exception as e:
        # Prints exception and returns false
        print(e)
        return False

def main():
    # Sets up arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-fe', '--fromEmail', help='Email to send from')
    parser.add_argument('-te', '--toEmail', help='Email to send to')
    parser.add_argument('-pe', '--passEmail', help='Email password')
    parser.add_argument('-se', '--serverEmail', help='Server address')
    args = parser.parse_args()

    # Checks required args are there
    if not args.fromEmail or not args.toEmail or not args.passEmail:
        print('\n*** Error: Must pass required arguments, check run_examples ***\n')
        parser.print_help()
        sys.exit(1)

    # Sets server address
    if args.serverEmail:
        server = args.serverEmail
    else:
        server = 'mail.sawyer0.com'

    # Sends message
    msg = 'You Suck bro!\n'
    subject = 'You Suck!'
    sendEmail(args.fromEmail, args.toEmail, subject, msg, server, args.passEmail)

if __name__ == '__main__':
    main()