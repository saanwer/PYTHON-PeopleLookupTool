#People Lookup
#Coded by | WarLord
#https://www.github.com/saanwer
import webbrowser
import os, time
from clint.textui import colored

os.system('title People Lookup')
os.system('color 0a')
os.system('cls') #Clear if Linux
search = raw_input("Input person's name to lookup : ")
print colored.yellow("[+] People search machine started! [+]")
print
time.sleep(1)
print colored.yellow("[+] Searching for "+search +" [+]")
print
#I've added some search engines and search sites
google = 'https://www.google.lk/?gfe_rd=cr&ei=5m_WWI-DJdTB2ASljIW4Aw#q='+search
zaba = 'http://www.zabasearch.com/people/'+search+'/'
switch = 'http://www.switchboard.com/name/'+search
whpages = 'http://www.whitepages.com/name/'+search
sprpages = 'http://www.superpages.com/listings.jsp?CS=L&MCBP=true&search=Find+It&STYPE=S&SCS=&C='+search
secsearch = 'https://secsearch.sec.gov/search?utf8=%3F&affiliate=secsearch&query='+search
ancestry = 'http://search.ancestry.com/cgi-bin/sse.dll?gss=rootsweb&gsfn='+search
yourfam = 'http://www.yourfamily.com/roots/yourfam.mv?qy='+search+'&xc=Query&xo=yfmsg&xn=202&xt=lost_bb'
dogpile = 'http://www.dogpile.com/search/web?fcoid=417&fcop=topnav&fpid=27&q='+search
peek = 'http://www.peekyou.com/'+search+'_'
yasni = 'http://www.yasni.com/'+search+'/free+people+search'
yatedo = 'http://www.yatedo.com/search/profil?q='+search
flickr = 'https://www.flickr.com/search/?text='+search
bing = 'https://www.bing.com/search?q='+search
wikimap = 'http://wikimapia.org/#lang=en&lat=6.931880&lon=79.847946&z=12&m=b&search='+search
yahoo = 'https://search.yahoo.com/search;_ylt=AwrTHRtzh9ZYlDkAGOKl87UF;_ylc=X1MDOTU4MTA0NjkEX3IDMgRmcgMEZ3ByaWQDdVMwcUltaUFUeFdfb0c0VlA0QXJNQQRuX3JzbHQDMARuX3N1Z2cDMARvcmlnaW4Dc2VhcmNoLnlhaG9vLmNvbQRwb3MDMARwcXN0cgMEcHFzdHJsAwRxc3RybAM2BHF1ZXJ5A3NhamphZAR0X3N0bXADMTQ5MDQ1NDM5MQ--?p='+search


print 'Random Information Lookup Of '+ search +' Initiated'
def Main():
    webbrowser.open(google) #Opens first tab
    print colored.blue('[+] Google lookup initiated [+]')
    webbrowser.open_new_tab(zaba) #Opens new tab
    print colored.blue('[+] Zabasearch initiated [+]')
    time.sleep(2)
    webbrowser.open_new_tab(switch)
    print colored.blue('[+] Switchboard lookup initiated [+]')
    time.sleep(2)
    webbrowser.open_new_tab(whpages)
    print colored.blue('[+] Whitepage lookup initiated [+]')
    time.sleep(2)
    webbrowser.open_new_tab(bing)
    print colored.blue('[+] Bing lookup initiated [+]')
    time.sleep(2)
    webbrowser.open_new_tab(yahoo)
    print colored.blue('[+] Yahoo search initiated [+]')
    print
    print colored.red('[*] Random Information Lookup Ended [*]')
    print
    print 'Business Information Lookup Of '+ search +' Initiated'
    time.sleep(2)
    webbrowser.open_new_tab(sprpages)
    print colored.blue('[+] Superpages lookup initiated [+]')
    time.sleep(2)
    webbrowser.open_new_tab(secsearch)
    print colored.blue('[+] U.S Security & Exchange lookup initiated [+]')
    print
    print colored.red('[*] Business Information Lookup Ended [*]')
    print
    print 'Death and Obituary Information Lookup Of '+ search +' Initiated'
    time.sleep(2)
    webbrowser.open_new_tab(ancestry)
    print colored.blue('[+] Ancestry lookup initiated [+]')
    print
    print colored.red('[*] Death and Obituary Information Lookup Ended [*]')
    print
    print 'General Information Lookup Of '+ search +' Initiated'
    time.sleep(2)
    webbrowser.open_new_tab(yourfam)
    print colored.blue('[+] Yourfamily lookup initiated [+]')
    time.sleep(2)
    webbrowser.open_new_tab(dogpile)
    print colored.blue('[+] Dogpile lookup initiated [+]')
    time.sleep(2)
    webbrowser.open_new_tab(peek)
    print colored.blue('[+] Peekyou lookup initiated [+]')
    time.sleep(2)
    webbrowser.open_new_tab(yasni)
    print colored.blue('[+] Yasni people search initiated [+]')
    time.sleep(2)
    webbrowser.open_new_tab(yatedo)
    print colored.blue('[+] Yatedo people search initiated [+]')
    print
    print colored.red('[*] General Information Lookup Ended [*]')
    print
    print 'Photos Lookup Of '+ search +' Initiated'
    time.sleep(2)
    webbrowser.open_new_tab(flickr)
    print colored.blue('[+] Flickr search initiated [+]')
    print
    print colored.red('[*] Photos Lookup Ended [*]')
    print
    print 'Locations Lookup Of '+ search +' Initiated'
    time.sleep(2)
    webbrowser.open_new_tab(wikimap)
    print colored.blue('[+] Wikimap search initiated [+]')
    print
    print colored.red('[*] Locations Lookup Ended [*]')
if __name__ == '__main__':
    Main()
