def main_menu():
    """This function returns a data structure used to render the top
    level menu."""
    return [
        {
            "title": "Club information",
            "submenus": [
                {
                    "title": "About the club",
                    "href": "/info/about/"
                },
                {
                    "title": "Leagues",
                    "href": "/leagues/"
                },
                {
                    "title": "About the website",
                    "href": "/info/website/"
                },
                {
                    "title": "Contact us",
                    "href": "/info/contact/"
                }
            ]
        },
        {
            "title": "Membership",
            "submenus": [
                {
                    "title": "New member information",
                    "href": "/membership/new_member_info/"
                },
                {
                    "title": "Membership fees",
                    "href": "/membership/membership_fees/"
                },
                {
                    "title": "Member registration",
                    "href": "/membership/member_registration/"
                },
                {
                    "title": "divider",
                    "href": ""
                },
                {
                    "title": "Social activities",
                    "href": "/membership/social_activities/"
                },
                {
                    "title": "Curling information",
                    "href": "/membership/curling_information/"
                },
                {
                    "title": "Newsletter archives",
                    "href": "/membership/newsletter_archives/"
                },
                {
                    "title": "Subscribing to League Newsletters",
                    "href": "/membership/league_newsletters/"
                },
                {
                    "title": "Honourary Life Members",
                    "href": "/membership/life_members/"
                }
            ]
        },
        {
            "title": "Calendars",
            "submenus": [
                {
                    "title": "Events calendar",
                    "href": "#"
                },
                {
                    "title": "Ice allocation calendar",
                    "href": "#"
                }
            ]
        }
    ]

def base_processor(request):
    return dict(top_menus=main_menu())
