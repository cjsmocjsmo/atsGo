#!/usr/bin/python3

import re
import os
import requests
import logging
import feedparser
import eztvlib as ez

LOWERDECKS       = re.compile(r"S03E01")
DISCOVERY        = re.compile(r"S04E08")
MANDALORIAN      = re.compile(r"S03E01")
LOSTINSPACE      = re.compile(r"S03E01")
ORVILLE          = re.compile(r"S03E01")
PICARD           = re.compile(r"S02E01")
RAISEDBYWOLVES   = re.compile(r"S02E01")
FORALLMANKIND    = re.compile(r"S03E01")
BADBATCH         = re.compile(r"S02E01")
LOKI             = re.compile(r"S02E01")
STRANGENEWWORLDS = re.compile(r"S01E01")
STARTREKPRODIGY  = re.compile(r"S01E08")
ACOLYTE          = re.compile(r"S01E01")
LANDO            = re.compile(r"S01E01")
AHSOKA           = re.compile(r"S01E01")
OBIWANDENOBI     = re.compile(r"S01E01")
DROIDSTORY       = re.compile(r"S01E01")
GROOT            = re.compile(r"S01E01")
WHATIF           = re.compile(r"S02E01")
WAKANDA          = re.compile(r"S01E01")
HAWKEYE          = re.compile(r"S02E01")
YTHELASTMAN      = re.compile(r'S02E01')
FOUNDATION       = re.compile(r'S02E01')
WHEELOFTIME      = re.compile(r"S02E01")
BOOKOFBOBAFETT   = re.compile(r"S01E05")

class CheckForNewEpisodes:
    def __init__(self):
        self.masterMagnet = []
        self.tgxreq = requests.get("https://torrentgalaxy.mx/latest")
        self.feed = feedparser.parse('https://torrentgalaxy.mx/rss')
        try:
            os.stat('/home/logs/EZtv.log')
        except FileNotFoundError:
            with open('/home/logs/EZtv.log', 'w') as newfile:
                newfile.write("Log created")
        
        logging.basicConfig(
            filename ='/home/logs/EZtv.log',
            level = logging.DEBUG,
            format = '%(levelname)s:%(asctime)s:%(message)s',
        )

    def search_lower_decks(self):
        logging.debug("Searching Lower Decks")
        print("\nSearching Lower Decks")
        r = requests.get('https://eztv.re/search/star-trek-lower-decks')
        llist = ez.search_for_new_episode(r.text, LOWERDECKS)
        self.masterMagnet.extend(llist)
        lll = len(llist)
        logging.debug("Found: {}".format(lll))
        print("Found: {}".format(lll))
        return lll

    def search_discovery(self):
        logging.debug("Searchng Discovery")
        print("\nSearchng Discovery")
        r = requests.get('https://eztv.re/search/discovery')
        llist = ez.search_for_new_episode(r.text, DISCOVERY)
        self.masterMagnet.extend(llist)
        lll = len(llist)
        logging.debug("Found: {}".format(lll))
        print("Found: {}".format(lll))
        return lll

    def search_mando(self):
        logging.debug("Searching Mandalorian")
        print("\nSearching Mandalorian")
        r = requests.get('https://eztv.re/search/mandalorian')
        llist = ez.search_for_new_episode(r.text, MANDALORIAN)
        self.masterMagnet.extend(llist)
        lll = len(llist)
        logging.debug("Found: {}".format(lll))
        print("Found: {}".format(lll))
        return lll
        
    def search_lost_in_space(self):
        logging.debug("Searching Lost In Space")
        print("\nSearching Lost In Space")
        r = requests.get('https://eztv.re/search/lost-in-space')
        llist = ez.search_for_new_episode(r.text, LOSTINSPACE)
        self.masterMagnet.extend(llist)
        lll = len(llist)
        logging.debug("Found: {}".format(lll))
        print("Found: {}".format(lll))
        return lll

    def search_orville(self):
        logging.debug("Searching The Orville")
        print("\nSearching The Orville")
        r = requests.get('https://eztv.re/search/orville')
        llist = ez.search_for_new_episode(r.text, ORVILLE)
        self.masterMagnet.extend(llist)
        lll = len(llist)
        logging.debug("Found: {}".format(lll))
        print("Found: {}".format(lll))
        return lll

    def search_picard(self):
        logging.debug("Searching Picard")
        print("\nSearching Picard")
        r = requests.get('https://eztv.re/search/picard')
        llist = ez.search_for_new_episode(r.text, PICARD)
        self.masterMagnet.extend(llist)
        lll = len(llist)
        logging.debug("Found: {}".format(lll))
        print("Found: {}".format(lll))
        return lll

    def search_raised_by_wolves(self):
        logging.debug("Searching Raised by Wolves")
        print("\nSearching Raised by Wolves")
        r = requests.get('https://eztv.re/search/raised-by-wolves')
        llist = ez.search_for_new_episode(r.text, RAISEDBYWOLVES)
        self.masterMagnet.extend(llist)
        lll = len(llist)
        logging.debug("Found: {}".format(lll))
        print("Found: {}".format(lll))
        return lll

    def search_for_all_man_kind(self):
        logging.debug('Searching For All Man Kind')
        print("\nSearching For All Man Kind")
        r = requests.get('https://eztv.re/search/for-all-mankind')
        llist = ez.search_for_new_episode(r.text, FORALLMANKIND)
        self.masterMagnet.extend(llist)
        lll = len(llist)
        logging.debug("Found: {}".format(lll))
        print("Found: {}".format(lll))
        return lll

    def search_bad_batch(self):
        logging.debug("Searching Bad Batch")
        print("\nSearching Bad Batch")
        r = requests.get('https://eztv.re/search/star-wars-bad-batch')
        llist = ez.search_for_new_episode(r.text, BADBATCH)
        self.masterMagnet.extend(llist)
        lll = len(llist)
        logging.debug("Found: {}".format(lll))
        print("Found: {}".format(lll))
        return lll

    def search_loki(self):
        logging.debug("Searching Loki")
        print("\nSearching Loki")
        r = requests.get('https://eztv.re/search/loki')
        llist = ez.search_for_new_episode(r.text, LOKI)
        self.masterMagnet.extend(llist)
        lll = len(llist)
        logging.debug("Found: {}".format(lll))
        print("Found: {}".format(lll))
        return lll

    def search_ythelastman(self):
        logging.debug("Searching y the last man")
        print("\nSearching y the last man")
        r = requests.get('https://eztv.re/search/y-the-last-man')
        llist = ez.search_for_new_episode(r.text, YTHELASTMAN)
        self.masterMagnet.extend(llist)
        lll = len(llist)
        logging.debug("Found: {}".format(lll))
        print("Found: {}".format(lll))
        return lll

    def search_wheeloftime(self):
        logging.debug("Searching wheeloftime")
        print("\nSearching wheeloftime")
        r = requests.get('https://eztv.re/search/wheel-of-time')
        llist = ez.search_for_new_episode(r.text, WHEELOFTIME)
        self.masterMagnet.extend(llist)
        lll = len(llist)
        logging.debug("Found: {}".format(lll))
        print("Found: {}".format(lll))
        return lll

    def search_foundation(self):
        logging.debug("Searching foundation")
        print("\nSearching foundation")
        r = requests.get('https://eztv.re/search/foundation')
        llist = ez.search_for_new_episode(r.text, FOUNDATION)
        self.masterMagnet.extend(llist)
        lll = len(llist)
        logging.debug("Found: {}".format(lll))
        print("Found: {}".format(lll))
        return lll

    def search_marvel_what_if(self):
        logging.debug("Searching what_if")
        print("\nSearching what_if")
        r = requests.get('https://eztv.re/search/what-if')
        llist = ez.search_for_new_episode(r.text, WHATIF)
        self.masterMagnet.extend(llist)
        lll = len(llist)
        logging.debug("Found: {}".format(lll))
        print("Found: {}".format(lll))
        return lll

    def search_star_trek_prodigy(self):
        logging.debug("Searching star_trek_prodigy")
        print("\nSearching star_trek_prodigy")
        r = requests.get('https://eztv.re/search/star-trek-prodigy')
        llist = ez.search_for_new_episode(r.text, STARTREKPRODIGY)
        self.masterMagnet.extend(llist)
        lll = len(llist)
        logging.debug("Found: {}".format(lll))
        print("Found: {}".format(lll))
        return lll


    def search_hawkeye(self):
        logging.debug("Searching hawkeye")
        print("\nSearching hawkeye")
        r = requests.get('https://eztv.re/search/hawkeye-2021')
        llist = ez.search_for_new_episode(r.text, HAWKEYE)
        self.masterMagnet.extend(llist)
        lll = len(llist)
        logging.debug("Found: {}".format(lll))
        print("Found: {}".format(lll))
        return lll

    def search_book_of_boba_fett(self):
        logging.debug("Searching book_of_boba")
        print("\nSearching book_of_boba")
        r = requests.get('https://eztv.re/search/the-book-of-boba-fett')
        llist = ez.search_for_new_episode(r.text, BOOKOFBOBAFETT)
        self.masterMagnet.extend(llist)
        lll = len(llist)
        logging.debug("Found: {}".format(lll))
        print("Found: {}".format(lll))
        return lll


    
























    def search_star_trek_strange_new_worlds(self):
        logging.debug("Searching Star Trek Strange New Worlds")
        print("\nSearching Star Trek Strange New Worlds")
        mastermeta = []

        s1 = re.compile(r"Strange New Worlds")
        s2 = re.compile(r"Star Trek Strange New Worlds")
        s3 = re.compile(r"Strange.New.Worlds")
        s4 = re.compile(r"Star.Trek.Strange.New.Worlds")
        slist = [s1, s2, s3, s4]
        
        r1 = requests.get('https://eztv.re/search/star-trek-strange-new-worlds')
        meta1 = ez.search_entry_for_title(r1.text, slist)
        if len(meta1) != 0:
            mastermeta.extend(meta1)
        else:
            pass

        r2 = requests.get('https://eztv.re/search/strange-new-worlds')
        meta2 = ez.search_entry_for_title(r2.text, slist)
        if len(meta2) != 0:
            mastermeta.extend(meta2)
        else:
            pass

        meta4 = ez.tgx_search_entry_for_title(self.tgxreq.text, slist)
        if len(meta4) != 0:
            mastermeta.extend(meta4)
        else:
            pass

        meta5 = ez.tgx_search_rss(self.feed, slist)
        if meta5 != None:
            mastermeta.extend(meta5)
        else:
            pass

        if len(mastermeta) != 0:
            llist = ez.newnew_search_for_new_episode(mastermeta, STRANGENEWWORLDS)
            self.masterMagnet.extend(llist)
            logging.debug("Found: {}".format(len(llist)))
            print("Found: {}".format(len(llist)))
            return len(llist)
        else:
            logging.debug("Found: 0")
            print("Found: 0")
            return 0

    def search_acolyte(self):
        logging.debug("Searching Acolyte")
        print("\nSearching Acolyte")
        mastermeta = []

        s1 = re.compile(r'Acolyte')
        s2 = re.compile(r"The Acolyte")
        s3 = re.compile(r"Star Wars Acolyte")
        s4 = re.compile(r"Star Wars The Acolyte")
        s5 = re.compile(r"The.Acolyte")
        s6 = re.compile(r"Star.Wars.Acolyte")
        s7 = re.compile(r"Star.Wars.The.Acolyte")
        slist = [s1, s2, s3, s4, s5, s6, s7]

        r1 = requests.get('https://eztv.re/search/star-wars-the-acolyte')
        metadata1 = ez.search_entry_for_title(r1.text, slist)
        if len(metadata1) != 0:
            mastermeta.extend(metadata1)
        else:
            pass

        r2 = requests.get('https://eztv.re/search/star-wars-acolyte')
        metadata2 = ez.search_entry_for_title(r2.text, slist)
        if len(metadata2) != 0:
            mastermeta.extend(metadata2)
        else:
            pass

        r3 = requests.get('https://eztv.re/search/acolyte')
        metadata3 = ez.search_entry_for_title(r3.text, slist)
        if len(metadata3) != 0:
            mastermeta.extend(metadata3)
        else:
            pass

        meta4 = ez.tgx_search_entry_for_title(self.tgxreq.text, slist)
        if len(meta4) != 0:
            mastermeta.extend(meta4)
        else:
            pass

        meta5 = ez.tgx_search_rss(self.feed, slist)
        if meta5 != None:
            mastermeta.extend(meta5)
        else:
            pass

        if len(mastermeta) != 0:
            llist = ez.newnew_search_for_new_episode(mastermeta, ACOLYTE)
            [logging.debug(ll) for ll in llist]
            self.masterMagnet.extend(llist)
            lll = len(llist)
            logging.debug("Found: {}".format(lll))
            print("Found: {}".format(lll))
            return lll
        else:
            logging.debug("Found: 0")
            print("Found: 0")
            return 0

    

    def search_lando(self):
        logging.debug("Searching Lando")
        print("\nSearching Lando")
        mastermeta = []

        s1 = re.compile(r"Lando")
        s2 = re.compile(r"Star Wars Lando")
        s3 = re.compile(r"Star.Wars.Lando")
        slist = [s1, s2, s3]

        r1 = requests.get('https://eztv.re/search/star-wars-lando')
        metadata1 = ez.search_entry_for_title(r1.text, slist)
        if len(metadata1) != 0:
            mastermeta.extend(metadata1)
        else:
            pass

        r2 = requests.get('https://eztv.re/search/lando')
        metadata2 = ez.search_entry_for_title(r2.text, slist)
        if len(metadata2) != 0:
            mastermeta.extend(metadata2)
        else:
            pass

        meta4 = ez.tgx_search_entry_for_title(self.tgxreq.text, slist)
        if len(meta4) != 0:
            mastermeta.extend(meta4)
        else:
            pass

        meta5 = ez.tgx_search_rss(self.feed, slist)
        if meta5 != None:
            mastermeta.extend(meta5)
        else:
            pass

        if len(mastermeta) != 0:
            llist = ez.newnew_search_for_new_episode(mastermeta, LANDO)
            [logging.debug(ll) for ll in llist]
            self.masterMagnet.extend(llist)
            lll = len(llist)
            logging.debug("Found: {}".format(lll))
            print("Found: {}".format(lll))
            return lll
        else:
            logging.debug("Found: 0")
            print("Found: 0")
            return 0

    def search_ahsoka(self):
        logging.debug("Searching Ahsoka")
        print("\nSearching Ahsoka")
        mastermeta = []

        s1 = re.compile(r"Ahsoka")
        s2 = re.compile(r"Star Wars Ahsoka")
        s3 = re.compile(r'Star.Wars.Ahsoka')
        slist = [s1, s2, s3]

        r1 = requests.get('https://eztv.re/search/star-wars-ahsoka')
        metadata1 = ez.search_entry_for_title(r1.text, slist)
        if len(metadata1) != 0:
            mastermeta.extend(metadata1)
        else:
            pass

        r2 = requests.get('https://eztv.re/search/ahsoka')
        metadata2 = ez.search_entry_for_title(r2.text, slist)
        if len(metadata2) != 0:
            mastermeta.extend(metadata2)
        else:
            pass

        meta4 = ez.tgx_search_entry_for_title(self.tgxreq.text, slist)
        if len(meta4) != 0:
            mastermeta.extend(meta4)
        else:
            pass

        meta5 = ez.tgx_search_rss(self.feed, slist)
        if meta5 != None:
            mastermeta.extend(meta5)
        else:
            pass

        if len(mastermeta) != 0:
            llist = ez.newnew_search_for_new_episode(mastermeta, AHSOKA)
            [logging.debug(ll) for ll in llist]
            self.masterMagnet.extend(llist)
            lll = len(llist)
            logging.debug("Found: {}".format(lll))
            print("Found: {}".format(lll))
            return lll
        else:
            logging.debug("Found: 0")
            print("Found: 0")
            return 0

    def search_obi_wan_kenobi(self):
        logging.debug("Searching Obi Wan Kenobi")
        print("\nSearching Obi Wan Kenobi")
        mastermeta = []

        s1 = re.compile(r"Obi Wan Kenobi")
        s2 = re.compile(r"Star Wars Obi Wan Kenobi")
        s1 = re.compile(r"Obi.Wan.Kenobi")
        s3 = re.compile(r"Star.Wars.Obi.Wan.Kenobi")
        slist = [s1, s2, s3]

        r1 = requests.get('https://eztv.re/search/star-wars-obi-wan-kenobi')
        metadata1 = ez.search_entry_for_title(r1.text, slist)
        if len(metadata1) != 0:
            mastermeta.extend(metadata1)
        else:
            pass

        r2 = requests.get('https://eztv.re/search/obi-wan-kenobi')
        metadata2 = ez.search_entry_for_title(r2.text, slist)
        if len(metadata2) != 0:
            mastermeta.extend(metadata2)
        else:
            pass

        meta4 = ez.tgx_search_entry_for_title(self.tgxreq.text, slist)
        if len(meta4) != 0:
            mastermeta.extend(meta4)
        else:
            pass

        meta5 = ez.tgx_search_rss(self.feed, slist)
        if meta5 != None:
            mastermeta.extend(meta5)
        else:
            pass

        if len(mastermeta) != 0:
            llist = ez.newnew_search_for_new_episode(mastermeta, OBIWANDENOBI)
            [logging.debug(ll) for ll in llist]
            self.masterMagnet.extend(llist)
            lll = len(llist)
            logging.debug("Found: {}".format(lll))
            print("Found: {}".format(lll))
            return lll
        else:
            logging.debug("Found: 0")
            print("Found: 0")
            return 0

    def search_droid_story(self):
        logging.debug("Searching A Droid Story")
        print("\nSearching A Droid Story")
        mastermeta = []

        s1 = re.compile(r"Droid Story")
        s2 = re.compile(r"A Droid Story")
        s3 = re.compile(r"Star Wars Droid Story")
        s4 = re.compile(r'Star Wars A Droid Story')
        s5 = re.compile(r"Droid.Story")
        s6 = re.compile(r"A.Droid.Story")
        s7 = re.compile(r"Star.Wars.Droid.Story")
        s8 = re.compile(r'Star.Wars.A.Droid.Story')
        slist = [s1, s2, s3, s4, s5, s6, s7, s8]

        r1 = requests.get('https://eztv.re/search/star-wars-a-droid-story')
        metadata1 = ez.search_entry_for_title(r1.text, slist)
        if len(metadata1) != 0:
            mastermeta.extend(metadata1)
        else:
            pass

        r2 = requests.get('https://eztv.re/search/a-droid-story')
        metadata2 = ez.search_entry_for_title(r2.text, slist)
        if len(metadata2) != 0:
            mastermeta.extend(metadata2)
        else:
            pass

        r3 = requests.get('https://eztv.re/search/droid-story')
        metadata3 = ez.search_entry_for_title(r3.text, slist)
        if len(metadata3) != 0:
            mastermeta.extend(metadata3)
        else:
            pass

        meta4 = ez.tgx_search_entry_for_title(self.tgxreq.text, slist)
        if len(meta4) != 0:
            mastermeta.extend(meta4)
        else:
            pass

        meta5 = ez.tgx_search_rss(self.feed, slist)
        if meta5 != None:
            mastermeta.extend(meta5)
        else:
            pass

        if len(mastermeta) != 0:
            llist = ez.newnew_search_for_new_episode(mastermeta, DROIDSTORY)
            [logging.debug(ll) for ll in llist]
            self.masterMagnet.extend(llist)
            lll = len(llist)
            logging.debug("Found: {}".format(lll))
            print("Found: {}".format(lll))
            return lll
        else:
            logging.debug("Found: 0")
            print("Found: 0")
            return 0

    def search_groot(self):
        logging.debug("Searching Groot")
        print("\nSearching Groot")
        mastermeta = []
        s1 = re.compile(r'Groot')
        s2 = re.compile(r"Marvel Groot")
        s3 = re.compile(r"Marvel.Groot")
        slist = [s1, s2, s3]

        r1 = requests.get('https://eztv.re/search/groot')
        metadata1 = ez.search_entry_for_title(r1.text, slist)
        if len(metadata1) != 0:
            mastermeta.extend(metadata1)
        else:
            pass

        r2 = requests.get('https://eztv.re/search/marvel-groot')
        metadata2 = ez.search_entry_for_title(r2.text, slist)
        if len(metadata2) != 0:
            mastermeta.extend(metadata2)
        else:
            pass

        meta4 = ez.tgx_search_entry_for_title(self.tgxreq.text, slist)
        if len(meta4) != 0:
            mastermeta.extend(meta4)
        else:
            pass

        meta5 = ez.tgx_search_rss(self.feed, slist)
        if meta5 != None:
            mastermeta.extend(meta5)
        else:
            pass

        if len(mastermeta) != 0:
            llist = ez.newnew_search_for_new_episode(mastermeta, GROOT)
            [logging.debug(ll) for ll in llist]
            self.masterMagnet.extend(llist)
            lll = len(llist)
            logging.debug("Found: {}".format(lll))
            print("Found: {}".format(lll))
            return lll
        else:
            logging.debug("Found: 0")
            print("Found: 0")
            return 0

    def search_marvel_wakanda(self):
        logging.debug("Searching Marvel Wakanda")
        print("\nSearching Marvel Wakanda")
        mastermeta = []
        s1  = re.compile(r'Wakanda')
        s2  = re.compile(r'Marvel Wakanda')
        s3  = re.compile(r'Marvel.Wakanda')
        slist = [s1, s2, s3]

        r1 = requests.get('https://eztv.re/search/marvel-wakanda')
        metadata1 = ez.search_entry_for_title(r1.text, slist)
        if len(metadata1) != 0:
            mastermeta.extend(metadata1)
        else:
            pass

        r2 = requests.get('https://eztv.re/search/wakanda')
        metadata2 = ez.search_entry_for_title(r2.text, slist)
        if len(metadata2) != 0:
            mastermeta.extend(metadata2)
        else:
            pass

        meta4 = ez.tgx_search_entry_for_title(self.tgxreq.text, slist)
        if len(meta4) != 0:
            mastermeta.extend(meta4)
        else:
            pass

        meta5 = ez.tgx_search_rss(self.feed, slist)
        if meta5 != None:
            mastermeta.extend(meta5)
        else:
            pass

        if len(mastermeta) != 0:
            llist = ez.newnew_search_for_new_episode(mastermeta, WAKANDA)
            [logging.debug(ll) for ll in llist]
            self.masterMagnet.extend(llist)
            lll = len(llist)
            logging.debug("Found: {}".format(lll))
            print("Found: {}".format(lll))
            return lll
        else:
            logging.debug("Found: 0")
            print("Found: 0")
            return 0


    # def downloadTorrents(self):
    #     for mag in self.masterMagnet:
    #         print("Downloading: {}".format(mag[0]))
    #         dl = TM.DownloadTor(mag[1])
    #         dl.startDownload()

    def main(self):
        # os.system("expressvpn connect")
        a = self.search_lower_decks()
        b = self.search_discovery()
        c = self.search_mando()
        d = self.search_lost_in_space()
        e = self.search_orville()
        f = self.search_picard()
        g = self.search_raised_by_wolves()
        h = self.search_for_all_man_kind()
        i = self.search_bad_batch()
        j = self.search_loki()
        k = self.search_star_trek_prodigy()
        t = self.search_marvel_what_if()
        w = self.search_ythelastman()
        y = self.search_foundation()
        z = self.search_wheeloftime()
        v = self.search_hawkeye()
        l = self.search_star_trek_strange_new_worlds()
        m = self.search_acolyte()
        n = self.search_book_of_boba_fett()
        o = self.search_lando()
        p = self.search_ahsoka()
        q = self.search_obi_wan_kenobi()
        r = self.search_droid_story()
        s = self.search_groot()
        u = self.search_marvel_wakanda()
        print("Total Number Of Episodes")
        sum1 = sum([a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p])
        sum2 = sum([q, r, s, t, u, v, w, y, z])
        totalfound = sum1 + sum2
        if totalfound > 0:
            print(self.masterMagnet)
            print(totalfound)
            tf = str(totalfound)
            ez.email_list3("EZtv", tf)
        else:
            print("0")
            pass
        # if a, b, c, d, e, p, q, m, n, wv, bb, l > 0:
        #     self.downloadTorrents()
        #     bar = RN.RenameFiles()
        #     bar.renameFiles()
        # else:
        #     print("No New Episodes found check episode list")

if __name__ == "__main__":
    foo = CheckForNewEpisodes()
    foo.main()
    
