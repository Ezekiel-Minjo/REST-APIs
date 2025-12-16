"""
blocklist.py

This file just contains the blocklist of the JWT tokens. It wil be imported by app and the Logout resource so that tokens can be added to the blocklist when the user logs out and checked against the blocklist when a protected endpoint is accessed.
"""


BLOCKLIST = set()