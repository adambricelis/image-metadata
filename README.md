# Image Metadata

Python scripts to read and edit image metadata in bulk.

When a photographer takes pictures of my family, they often forget to set the date and time on their camera. If I import those pictures into Google Photos, they show up at the wrong date and time because their timestamps are incorrect. I created these scripts to fix the timestamps on a set of photos from a photoshoot.

## Getting started

1. Install prerequisites:
    * [Python 3](https://www.python.org/downloads/)
    * [pip](https://pip.pypa.io/en/stable/installation/)
1. Clone this repository
1. Create virtual environment: `python3 -m venv venv`
1. Activate virtual environment: `source venv/bin/activate`
1. Install Python packages: `pip3 install -r requirements.txt`
1. Create .env file
    1. Copy [example.env](example.env) to .env
    1. (Optional) Modify environment variables to suit your use case

## Usage guide

Run `python <script> -h` for help

## Contribution Policy

This project is closed to outside contributions.
