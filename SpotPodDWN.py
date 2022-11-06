#!/usr/bin/python3
import os
import requests as r
import re
import sys
from bs4 import BeautifulSoup
import json

if len(sys.argv) == 1:
    os.system("cls")
    print("SPOTIFY PODCAST DOWNLOADER")
    print("   [*] py SpotyPodDWN.py LINK")
    print("   [-] Vai su https://open.spotify.com")
    print("   [-] Cerca il tuo PODCAST preferito")
    print("   [-] Anziche PLAY clicca sui \"..\"")
    print("   [-] Clicca su \"Copia Link Episodio\"")
    exit()
#episode = input("Inserisci link episodio: ")

def single_pod():
    episode = sys.argv[1]


    split = episode.split("/")
    split2 = split[4].split("?")
    split3 = split2[0]

    url = f"https://spclient.wg.spotify.com/soundfinder/v1/unauth/episode/{split3}/com.widevine.alpha?market=IT"
    res = r.get(url)
    link = res.json()

    pod_link = link['passthroughUrl']
    podcast = r.get(pod_link, stream=True)

    #extract title from main request

    source_title = r.get(episode).text
    titolo = re.search("data-testid=\"episodeTitle\">(.*?)</span>", source_title).group(1)
    print(f"Sto caricando l'episodio:  *{titolo}*")
    filename = f"{titolo}.mp3".replace(":"," -")

    with open(filename, 'wb') as f:
        f.write(podcast.content)
        f.close()
    print(" [+] Finito! Goditi il tuo Podcast :D")
    print(" [+] Lo trovi nella cartella corrente")
    print(f" [+] Filename: {filename}")

single_pod()
#multi_pod()