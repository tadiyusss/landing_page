from core.utils.analytics import Grid, LargeAnalyticsCardData, MediumAnalyticsCardData, SmallAnalyticsCardData
from .helpers.analytics import get_waitlist_count
from core.utils.registry.analytics import register_analytics

ANALYTICS = [
    Grid(
        title="Landing Page Analytics",
        contents=[
            SmallAnalyticsCardData(
                title="Waitlist Count",
                value_function=lambda: get_waitlist_count(),
                roles=["Administrator"],
                icon="<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 20 20' fill='currentColor' class='analytics-icon'><path d='M7 8a3 3 0 1 0 0-6 3 3 0 0 0 0 6ZM14.5 9a2.5 2.5 0 1 0 0-5 2.5 2.5 0 0 0 0 5ZM1.615 16.428a1.224 1.224 0 0 1-.569-1.175 6.002 6.002 0 0 1 11.908 0c.058.467-.172.92-.57 1.174A9.953 9.953 0 0 1 7 18a9.953 9.953 0 0 1-5.385-1.572ZM14.5 16h-.106c.07-.297.088-.611.048-.933a7.47 7.47 0 0 0-1.588-3.755 4.502 4.502 0 0 1 5.874 2.636.818.818 0 0 1-.36.98A7.465 7.465 0 0 1 14.5 16Z' /></svg>"
            )
        ],
        roles=["Administrator"],
    )
]


def initialize_analytics():
    for item in ANALYTICS:
        register_analytics(item)