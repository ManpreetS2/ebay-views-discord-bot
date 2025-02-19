import os
import json
import requests
import discord
from datetime import datetime

# Get the token and channel ID from environment variables
TOKEN = os.getenv('DISCORD_TOKEN')  # Discord bot token from environment variable
CHANNEL_ID = int(os.getenv('CHANNEL_ID'))  # Channel ID from environment variable
MAX_VIEWS = int(os.getenv('MAX_VIEWS', 100))  # Max views, default 100 if not set

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-GB,en;q=0.9',
    'dnt': '1',
    'referer': 'https://www.ebay.co.uk/',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
    'sec-ch-ua-full-version': '"102.0.5005.63"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Windows"',
    'sec-ch-ua-platform-version': '"10.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
}

def lambda_handler(event, context):
    """AWS Lambda function to handle eBay view requests."""
    try:
        body = json.loads(event['body'])
        number_of_views = int(float(body['views']))
        link = body['link']

        if number_of_views > MAX_VIEWS:
            return {
                "statusCode": 400,
                "body": json.dumps(f"You can only have a maximum of {MAX_VIEWS} views")
            }

        # Simulate views by sending requests
        for _ in range(number_of_views):
            requests.get(link, headers=headers)

        return {
            "statusCode": 200,
            "body": json.dumps(f"Successfully added {number_of_views} views to {link}")
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps(f"Error: {str(e)}")
        }
