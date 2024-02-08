#!/usr/bin/python3
"""Defines an obj attribute lookup function."""


def lookup(obj):
    """Return a list of an obj's available attributes."""
    return (dir(obj))
