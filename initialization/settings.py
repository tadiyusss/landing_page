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
                key="csr_email",
                name="Customer Support Email",
                value="",
                field=EmailField(
                    "Customer Support Email", 
                    description="The email address for customer support inquiries.",
                    render_kw={
                        "class": "fd-input"
                    }
                ),
                category_name="landing_page"
            ),
            SettingItem(
                key="facebook_url",
                name="Facebook URL",
                value="",
                field=StringField(
                    "Facebook URL",
                    description="The URL of the Facebook page for the landing page. e.g., https://www.facebook.com/yourpage",
                    render_kw={
                        "class": "fd-input"
                    }
                ),
                category_name="landing_page"
            ),
            SettingItem(
                key="tiktok_url",
                name="TikTok URL",
                value="",
                field=StringField(
                    "TikTok URL",
                    description="The URL of the TikTok page for the landing page. e.g., https://www.tiktok.com/@yourusername",
                    render_kw={
                        "class": "fd-input"
                    }
                ),
                category_name="landing_page"
            ),
            SettingItem(
                key="instagram_url",
                name="Instagram URL",
                value="",
                field=StringField(
                    "Instagram URL",
                    description="The URL of the Instagram page for the landing page. e.g., https://www.instagram.com/yourusername",
                    render_kw={
                        "class": "fd-input"
                    }
                ),
                category_name="landing_page"
            )
        ]
    )
]

def register_settings():
    for category in SETTINGS:
        register_category(category)
