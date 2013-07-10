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
                    "title": "Evening Ladies",
                    "href": "/leagues/eveningladies/"
                },
                {
                    "title": "Evening Men",
                    "href": "/leagues/eveningmen/"
                },
                {
                    "title": "Weekend Mixed",
                    "href": "/leagues/weekendmixed/"
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
                    "title": "Sunday Open",
                    "href": "/leagues/sundayopen/"
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
        }
    ]
