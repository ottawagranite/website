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
            "title": "League information",
            "submenus": [
                {
                    "title": "General information",
                    "href": "/leagues/general/"
                },
                {
                    "title": "Looking for curlers",
                    "href": "/leagues/looking/"
                },
                {
                    "title": "divider",
                    "href": ""
                },
                {
                    "title": "Day Ladies",
                    "href": "/leagues/dayladies/"
                },
                {
                    "title": "Day Men",
                    "href": "/leagues/daymen/"
                },
                {
                    "title": "Day Mixed",
                    "href": "/leagues/daymixed/"
                },
                {
                    "title": "divider",
                    "href": ""
                },
                {
                    "title": "Evening Ladies",
                    "href": "/leagues/eveningladies/"
                },
                {
                    "title": "Evening Men",
                    "href": "/leagues/eveningmen/"
                },
                {
                    "title": "divider",
                    "href": ""
                },
                {
                    "title": "Weekend Mixed",
                    "href": "/leagues/weekendmixed/"
                },
                {
                    "title": "Sunday Open",
                    "href": "/leagues/sundayopen/"
                },
                {
                    "title": "Monday Open Fixed",
                    "href": "/leagues/mondayopenfixed/"
                },
                {
                    "title": "Wednesday Open",
                    "href": "/leagues/wednesdayopen/"
                },
                {
                    "title": "divider",
                    "href": ""
                },
                {
                    "title": "Little Rocks",
                    "href": "/leagues/littlerocks/"
                },
                {
                    "title": "Bantam / Juniors",
                    "href": "/leagues/bantamjuniors/"
                },
                {
                    "title": "Rookies Rock",
                    "href": "/leagues/rookiesrock/"
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
