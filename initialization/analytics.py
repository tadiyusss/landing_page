from core.utils.analytics import Grid, LargeAnalyticsCardData, MediumAnalyticsCardData, SmallAnalyticsCardData
from .helpers.analytics import get_pending_inquiries_count, get_total_visitors, get_new_visitors, get_returning_visitors, get_total_visits, get_unread_inquiries_count
from core.utils.registry.analytics import register_analytics, register_analytics_item

ANALYTICS = [
    Grid(
        title="Landing Page Analytics",
        contents=[
            SmallAnalyticsCardData(
                title="Total Visitors",
                value_function=lambda: get_total_visitors(),
                roles=["Administrator"],
                icon="<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 20 20' fill='currentColor' class='analytics-icon'><path d='M10 12.5a2.5 2.5 0 1 0 0-5 2.5 2.5 0 0 0 0 5Z' /><path fill-rule='evenodd' d='M.664 10.59a1.651 1.651 0 0 1 0-1.186A10.004 10.004 0 0 1 10 3c4.257 0 7.893 2.66 9.336 6.41.147.381.146.804 0 1.186A10.004 10.004 0 0 1 10 17c-4.257 0-7.893-2.66-9.336-6.41ZM14 10a4 4 0 1 1-8 0 4 4 0 0 1 8 0Z' clip-rule='evenodd' /></svg>"
            ),
            SmallAnalyticsCardData(
                title="New Visitors",
                value_function=lambda: get_new_visitors(),
                roles=["Administrator"],
                icon="<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 20 20' fill='currentColor' class='analytics-icon'><path d='M10 12.5a2.5 2.5 0 1 0 0-5 2.5 2.5 0 0 0 0 5Z' /><path fill-rule='evenodd' d='M.664 10.59a1.651 1.651 0 0 1 0-1.186A10.004 10.004 0 0 1 10 3c4.257 0 7.893 2.66 9.336 6.41.147.381.146.804 0 1.186A10.004 10.004 0 0 1 10 17c-4.257 0-7.893-2.66-9.336-6.41ZM14 10a4 4 0 1 1-8 0 4 4 0 0 1 8 0Z' clip-rule='evenodd' /></svg>"
            ),
            SmallAnalyticsCardData(
                title="Total Visits",
                value_function=lambda: get_total_visits(),
                roles=["Administrator"],
                icon="<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 20 20' fill='currentColor' class='analytics-icon'><path d='M10 12.5a2.5 2.5 0 1 0 0-5 2.5 2.5 0 0 0 0 5Z' /><path fill-rule='evenodd' d='M.664 10.59a1.651 1.651 0 0 1 0-1.186A10.004 10.004 0 0 1 10 3c4.257 0 7.893 2.66 9.336 6.41.147.381.146.804 0 1.186A10.004 10.004 0 0 1 10 17c-4.257 0-7.893-2.66-9.336-6.41ZM14 10a4 4 0 1 1-8 0 4 4 0 0 1 8 0Z' clip-rule='evenodd' /></svg>"
            ),
            SmallAnalyticsCardData(
                title="Unread Inquiries",
                value_function=lambda: get_unread_inquiries_count(),
                roles=["Administrator"],
                icon="<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 20 20' fill='currentColor' class='analytics-icon'><path d='M2.003 5.884L10 9.882l7.997-3.998A2 2 0 0 0 16 4H4a2 2 0 0 0-1.997 1.884ZM18 8.118l-8 4-8-4V14a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8.118Z' /></svg>"
            ),
            SmallAnalyticsCardData(
                title="Pending Inquiries",
                value_function=lambda: get_pending_inquiries_count(),
                roles=["Administrator"],
                icon="<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 20 20' fill='currentColor' class='analytics-icon'><path d='M2.003 5.884L10 9.882l7.997-3.998A2 2 0 0 0 16 4H4a2 2 0 0 0-1.997 1.884ZM18 8.118l-8 4-8-4V14a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8.118Z' /></svg>"
            ),
        ],
        roles=["Administrator"],
    )
]


def initialize_analytics():
    for item in ANALYTICS:
        register_analytics(item)