from extensions.landing_page.models.waitlist import Waitlist
from extensions.landing_page.models.visitors import Visitor, Visit
from extensions.landing_page.models.contact_us import ContactUs

def get_waitlist_count():
    return Waitlist.query.count()

def get_total_visitors():
    return Visitor.query.count()

def get_new_visitors():
    return Visitor.query.filter_by(is_new=True).count()

def get_returning_visitors():
    return Visitor.query.filter_by(is_new=False).count()

def get_total_visits():
    return Visit.query.count()

def get_unread_inquiries_count():
    return ContactUs.query.filter_by(status='new').count()

def get_pending_inquiries_count():
    return ContactUs.query.filter_by(status='pending').count()