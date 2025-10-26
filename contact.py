class Contact:
    """Represents a contact entry with name, phone number, and email."""

    def __init__(self, name, phone, email):
        """Initialize a new contact with a name, phone number, and email."""
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        """Return a formatted string representation of the contact."""
        return f"Name: {self.name}, Phone: {self.phone}, Email: {self.email}"
