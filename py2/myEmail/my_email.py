import smtplib

def sendEmail(fromAddr, toAddr, subject, msg, serverAddr, password, username=None, inPort=25, outPort=587):
    # Sets username
    if username is None:
        username = fromAddr
    
    # Creates message with header
    header = 'FROM: %s\nTO: %s\nSUBJECT: %s\n' % (fromAddr, toAddr, subject)
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