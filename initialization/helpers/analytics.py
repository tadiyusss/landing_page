from extensions.landing_page.models.waitlist import Waitlist

def get_waitlist_count():
    return Waitlist.query.count()