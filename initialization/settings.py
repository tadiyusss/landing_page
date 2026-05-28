from core.utils.settings import SettingCategory, SettingItem
from wtforms import StringField, EmailField
from ..forms.validators import validate_telegram_username
from core.utils.registry.settings import register_setting, register_category

SETTINGS = [
    SettingCategory(
        name="landing_page",
        nice_name="Landing Page",
        description="Settings related to the landing page extension.",
        settings=[
            SettingItem(
                key="csr_telegram_username",
                name="Customer Support Telegram Username",
                value="",
                field=StringField(
                    "Customer Support Telegram Username", 
                    description="The Telegram username (without @) for customer support inquiries.",
                    validators=[validate_telegram_username]
                ),
                category_name="landing_page"
            ),
            SettingItem(
                key="csr_email",
                name="Customer Support Email",
                value="",
                field=EmailField(
                    "Customer Support Email", 
                    description="The email address for customer support inquiries.",
                ),
                category_name="landing_page"
            )
        ]
    )
]


def register_settings():
    for category in SETTINGS:
        register_category(category)
