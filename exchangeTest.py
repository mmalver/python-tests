from datetime import datetime, timedelta
import pytz
from exchangelib import DELEGATE, IMPERSONATION, Account, Credentials, ServiceAccount, \
	EWSDateTime, EWSTimeZone, Configuration, NTLM, GSSAPI, CalendarItem, Message, \
	Mailbox, Attendee, Q, ExtendedProperty, FileAttachment, ItemAttachment, \
	HTMLBody, Build, Version, FolderCollection


def getMessage():
	"""This method asks for a message body, builds it in an array, and returns a list."""
	mBody = [];
	m = raw_input("enter a message body")
	while len(m) != 0:
		mBody.append(m)
		m = raw_input()
	returnMessage = ""
	
	for m in mBody:
		returnMessage = returnMessage + m + "\n"
	return returnMessage


credentials = Credentials(username='testexchange@alticomcti.com',password='Mm6126730064m$')
my_account = Account(primary_smtp_address='testexchange@alticomti.com',credentials=credentials,autodiscover=True, access_type=DELEGATE)
print "blablabla"
