from core.utils.registry.side_navigation import register_category
from core.utils.dashboard import DashboardCategory, DashboardItem


SIDEBAR = [
    DashboardCategory(
        name="Landing Page",
        roles=["Administrator"],
        items=[
            DashboardItem(
                name="Waitlist",
                icon_type="svg",
                icon="<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 20 20' fill='currentColor' class='sidenav-item'><path fill-rule='evenodd' d='M5.404 14.596A6.5 6.5 0 1 1 16.5 10a1.25 1.25 0 0 1-2.5 0 4 4 0 1 0-.571 2.06A2.75 2.75 0 0 0 18 10a8 8 0 1 0-2.343 5.657.75.75 0 0 0-1.06-1.06 6.5 6.5 0 0 1-9.193 0ZM10 7.5a2.5 2.5 0 1 0 0 5 2.5 2.5 0 0 0 0-5Z' clip-rule='evenodd' /></svg>",
                route="landing_page.waitlist",
                roles=["Administrator"]
            ),
            DashboardItem(
                name="FAQs",
                icon_type="svg",
                icon="<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 20 20' fill='currentColor' class='sidenav-item'><path fill-rule='evenodd' d='M18 10a8 8 0 1 1-16 0 8 8 0 0 1 16 0ZM8.94 6.94a.75.75 0 1 1-1.061-1.061 3 3 0 1 1 2.871 5.026v.345a.75.75 0 0 1-1.5 0v-.5c0-.72.57-1.172 1.081-1.287A1.5 1.5 0 1 0 8.94 6.94ZM10 15a1 1 0 1 0 0-2 1 1 0 0 0 0 2Z' clip-rule='evenodd' /></svg>",
                route="landing_page.manage_faqs",
                roles=["Administrator"]
            )
        ]
    )
]

def initialize_sidebar():
    for category in SIDEBAR:
        register_category(category)