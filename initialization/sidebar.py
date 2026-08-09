from core.utils.registry.side_navigation import register_category
from core.utils.dashboard import DashboardCategory, DashboardItem


SIDEBAR = [
    DashboardCategory(
        name="Landing Page",
        roles=["Administrator"],
        items=[
            DashboardItem(
                name="FAQs",
                icon_type="svg",
                icon="<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 20 20' fill='currentColor' class='fd-sidebar-item'><path fill-rule='evenodd' d='M18 10a8 8 0 1 1-16 0 8 8 0 0 1 16 0ZM8.94 6.94a.75.75 0 1 1-1.061-1.061 3 3 0 1 1 2.871 5.026v.345a.75.75 0 0 1-1.5 0v-.5c0-.72.57-1.172 1.081-1.287A1.5 1.5 0 1 0 8.94 6.94ZM10 15a1 1 0 1 0 0-2 1 1 0 0 0 0 2Z' clip-rule='evenodd' /></svg>",
                route="landing_page.manage_faqs",
                roles=["Administrator", "Support Agent"]
            ),
            DashboardItem(
                name="Inquiries",
                icon_type="svg",
                icon="<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 20 20' fill='currentColor' class='fd-sidebar-item'><path fill-rule='evenodd' d='M10 2c-2.236 0-4.43.18-6.57.524C1.993 2.755 1 4.014 1 5.426v5.148c0 1.413.993 2.67 2.43 2.902.848.137 1.705.248 2.57.331v3.443a.75.75 0 0 0 1.28.53l3.58-3.579a.78.78 0 0 1 .527-.224 41.202 41.202 0 0 0 5.183-.5c1.437-.232 2.43-1.49 2.43-2.903V5.426c0-1.413-.993-2.67-2.43-2.902A41.289 41.289 0 0 0 10 2Zm0 7a1 1 0 1 0 0-2 1 1 0 0 0 0 2ZM8 8a1 1 0 1 1-2 0 1 1 0 0 1 2 0Zm5 1a1 1 0 1 0 0-2 1 1 0 0 0 0 2Z' clip-rule='evenodd' /></svg>",
                route="landing_page.manage_inquiries",
                roles=["Administrator", "Support Agent"]
            )
            ,
            DashboardItem(
                name="Testimonials",
                icon_type="svg",
                icon="<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16' fill='currentColor' class='fd-sidebar-item'><path d='M1 8.849c0 1 .738 1.851 1.734 1.947L3 10.82v2.429a.75.75 0 0 0 1.28.53l1.82-1.82A3.484 3.484 0 0 1 5.5 10V9A3.5 3.5 0 0 1 9 5.5h4V4.151c0-1-.739-1.851-1.734-1.947a44.539 44.539 0 0 0-8.532 0C1.738 2.3 1 3.151 1 4.151V8.85Z' /><path d='M7 9a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v1a2 2 0 0 1-2 2h-.25v1.25a.75.75 0 0 1-1.28.53L9.69 12H9a2 2 0 0 1-2-2V9Z' /></svg>",
                route="landing_page.manage_testimonials",
                roles=["Administrator", "Support Agent"]
            ),
            DashboardItem(
                name="About Us",
                icon_type="svg",
                icon="<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16' fill='currentColor' class='fd-sidebar-item'><path fill-rule='evenodd' d='M3 3a2 2 0 0 0-2 2v6a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V5a2 2 0 0 0-2-2H3Zm2.5 5a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3ZM10 5.75a.75.75 0 0 1 .75-.75h1.5a.75.75 0 0 1 0 1.5h-1.5a.75.75 0 0 1-.75-.75Zm.75 3.75a.75.75 0 0 0 0 1.5h1.5a.75.75 0 0 0 0-1.5h-1.5ZM10 8a.75.75 0 0 1 .75-.75h1.5a.75.75 0 0 1 0 1.5h-1.5A.75.75 0 0 1 10 8Zm-2.378 3c.346 0 .583-.343.395-.633A2.998 2.998 0 0 0 5.5 9a2.998 2.998 0 0 0-2.517 1.367c-.188.29.05.633.395.633h4.244Z' clip-rule='evenodd' /></svg>",
                route="landing_page.manage_about_us",
                roles=["Administrator"]
            )
        ]
    )
]

def initialize_sidebar():
    for category in SIDEBAR:
        register_category(category)