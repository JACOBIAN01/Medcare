import datetime
import random
import string

def generate_room_id(doctor_initials):
    date_part = datetime.datetime.now().strftime("%Y%m%d")
    random_part = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
    return f"CR-{doctor_initials}-{date_part}-{random_part}"

# Example
room_id = generate_room_id("JD")  # Doctor's initials: JD
print("Consultation Room ID:", room_id)
