import os
import requests
from backend.marketing.content_creator import generate_post

FB_TOKEN = os.getenv("FB_PAGE_ACCESS_TOKEN")
FB_PAGE_ID = os.getenv("FB_PAGE_ID")
IG_BUSINESS_ID = os.getenv("IG_BUSINESS_ACCOUNT_ID")
TIKTOK_TOKEN = os.getenv("TIKTOK_ACCESS_TOKEN")

MEDIA_URL = "https://via.placeholder.com/1080x1080.png?text=Atlantis+Jobs" # replace with real image/video URLs

def post_to_facebook(content):
    url = f"https://graph.facebook.com/{FB_PAGE_ID}/feed"
    payload = {"message": content, "access_token": FB_TOKEN}
    r = requests.post(url, data=payload)
    print("Facebook post status:", r.status_code, r.text)

def post_to_instagram(content):
    url = f"https://graph.facebook.com/{IG_BUSINESS_ID}/media"
    payload = {"caption": content, "image_url": MEDIA_URL, "access_token": IG_BUSINESS_ID}
    r = requests.post(url, data=payload)
    print("Instagram post status:", r.status_code, r.text)

def post_to_tiktok(content):
    url = "https://business-api.tiktokglobalshop.com/open_api/v1.0/post/create/"
    payload = {"text": content, "video_url": MEDIA_URL, "access_token": TIKTOK_TOKEN}
    r = requests.post(url, json=payload)
    print("TikTok post status:", r.status_code, r.text)

def auto_post():
    content = generate_post()
    post_to_facebook(content)
    post_to_instagram(content)
    post_to_tiktok(content)
