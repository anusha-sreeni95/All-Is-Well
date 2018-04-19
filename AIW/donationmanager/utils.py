from donationmanager.models import DonationBox

def create_donation(donation_title, donation_item_description, ngo_name, location, creation_date, ngo_email):
    row = DonationBox(donation_title = donation_title,
                donation_item_description = donation_item_description,
                ngo_name = ngo_name,
                location = location,
                creation_date = creation_date,
                ngo_email = ngo_email)
    row.save()
