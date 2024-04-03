from django.shortcuts import render, redirect
import os, requests
from django.contrib import messages
from instalooter import looters
from instalooter.looters import InstaLooter
from instalooter.looters import PostLooter
from .models import InstagramDownload
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_argument("--headless")


def index(request):
    return render(request, "tubeloader/index.html")


def is_valid_instagram_url(url):
    try:
        response = requests.get(url)
        return response.status_code == 200 and "instagram.com" in response.url
    except Exception as e:
        print(f"Error checking URL validity: {e}")
        return False


def extract_content(url):
    driver = webdriver.Chrome(options=options)
    driver.get(url)

    # Wait for the page to load
    time.sleep(5)

    caption = driver.find_element(
        By.XPATH,
        "//div[@class='_a9zn _a9zo']/div[@class='_a9zr']/div[@class='_a9zs']/h1[@class='_ap3a _aaco _aacu _aacx _aad7 _aade']",
    ).text
    like = driver.find_element(
        By.XPATH,
        "//div[@class='x9f619 xjbqb8w x78zum5 x168nmei x13lgxp2 x5pf9jr xo71vjh xr1yuqi xkrivgy x4ii5y1 x1gryazu x1n2onr6 x1plvlek xryxfnj x1iyjqo2 x2lwn1j xeuugli xdt5ytf x1a02dak xqjyukv x1cy8zhl x1oa3qoh x1nhvcw1']",
    ).text
    username = driver.find_element(
        By.XPATH,
        "//a[@class='x1i10hfl xjbqb8w x1ejq31n xd10rxx x1sy0etr x17r0tee x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz  _acan _acao _acat _acaw _aj1- _ap30 _a6hd']",
    ).text
    date = driver.find_element(
        By.XPATH,
        "//div[@class='x1yztbdb x1h3rv7z x1swvt13']/div[@class='x9f619 xjbqb8w x78zum5 x168nmei x13lgxp2 x5pf9jr xo71vjh x1n2onr6 x1plvlek xryxfnj x1c4vz4f x2lah0s x1q0g3np xqjyukv x6s0dn4 x1oa3qoh x1nhvcw1']",
    ).text

    driver.quit()
    return caption, like, username, date


def get_insta(request):
    homedir = os.path.expanduser("~")
    dirs = homedir + "/Downloads"
    if request.method == "POST":
        link = request.POST.get("links")
        is_valid_instagram_url(link)
        caption, like, username, date = extract_content(link)

        r = InstagramDownload(
            link=link, caption=caption, like=like, username=username, date=date
        )
        r.save()

        # p = InstaLooter.get_post_info(link)
        # print(p)

        # if "get_video" in request.POST:
        #     print("if")
        #     l = "nathiyarajendiran_nathiiiii"
        #     PostLooter(l).download_videos(dirs, media_count=50)
        # elif "get_photo" in request.POST:
        #     l = "nathiyarajendiran_nathiiiii"
        #     PostLooter(1).download(dirs, media_count=50)

    return index(request)
