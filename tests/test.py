import email
import email.iterators
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from muttdown import config
from muttdown import main

def plain_test():
    """Bare text/plain is passed through unchanged"""
    message = email.message.Message()
    message.set_payload("This is plain text.")

    converted, did_convert = main.convert_tree(message, config.Config())

    assert did_convert == False
    assert message.as_string() == converted.as_string()

def plain_marked_test():
    """text/plain marked with !m is converted to multipart/alternative"""
    message = email.message.Message()
    message.set_payload("!m\n# This is a md header.\n")

    converted, did_convert = main.convert_tree(message, config.Config())

    assert did_convert == True
    assert converted.get_content_type() == "multipart/alternative"
