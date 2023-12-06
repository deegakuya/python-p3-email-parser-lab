# your code goes here!
import re

class EmailAddressParser:
    def __init__(self, email_addresses):
        self.email_addresses = email_addresses

    def parse(self):
        # Split string based on commas or spaces
        addresses = re.split(r'[,\s]+', self.email_addresses)

        # Filter out non-email strings
        valid_addresses = [address for address in addresses if re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', address)]

        # Use a set to store unique email addresses
        unique_addresses = set(valid_addresses)

        # Sort the addresses alphabetically and convert back to a list
        sorted_addresses = sorted(unique_addresses)

        return sorted_addresses
