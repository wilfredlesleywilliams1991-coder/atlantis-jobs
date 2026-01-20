import os, requests
from backend.marketing.content_creator import generate_post

FB_TOKEN = os.getenv("FB_PAGE_ACCESS_TOKEN")
FB_PAGE_ID = os.getenv("FB_PAGE_ID")
IG_BUSINESS_ID = os.getenv("IG_BUSINESS_ACCOUNT_ID")
TIKTOK_TOKEN = os.getenv("TIKTOK_ACCESS_TOKEN")
MEDIA_URL = "https://via.placeholder.com/1080x1080.png?text=Atlantis+Jobs"

def post_to_facebook(content):
    r=requests.post(f"https://graph.facebook.com/{FB_PAGE_ID}/feed",data={"message":content,"access_token":FB_TOKEN})
    print("Facebook:",r.status_code)

def post_to_instagram(content):
    r=requests.post(f"https://graph.facebook.com/{IG_BUSINESS_ID}/media",data={"caption":content,"image_url":MEDIA_URL,"access_token":IG_BUSINESS_ID})
    print("Instagram:",r.status_code)

def post_to_tiktok(content):
    r=requests.post("https://business-api.tiktokglobalshop.com/open_api/v1.0/post/create/",json={"text":content,"video_url":MEDIA_URL,"access_token":TIKTOK_TOKEN})
    print("TikTok:",r.status_code)

def auto_post():
    content=generate_post()
    post_to_facebook(content)
    post_to_instagram(content)
    post_to_tiktok(content)
