from core.utils.settings import SettingCategory, SettingItem
from wtforms import StringField
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
                )
            )
        ]
    )
]


def register_settings():
    print(f"[Landing Page] Registering settings...")
    for category in SETTINGS:
        register_category(
            name=category.name,
            nice_name=category.nice_name,
            description=category.description
        )
        for setting in category.settings:
            register_setting(
                key=setting.key,
                name=setting.name,
                value=setting.value,
                category_name=category.name,
                field=setting.field
            )
    print(f"[Landing Page] Settings registered.")