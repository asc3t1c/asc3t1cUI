import requests
from urllib.parse import urlparse, parse_qs, urlencode, urlunparse
from colorama import Fore, Style, init
import datetime

init(autoreset=True)  # Automatically reset color after each print

def guess_params(params):
    if not params:
        common_params = [
            'id', 'page', 'user', 'search', 'q', 'searchTerm', 'item', 'category', 'cat', 'product',
            'prod', 'uid', 'name', 'email', 'token', 'lang', 'langue', 'langid', 'type', 'sort', 'order',
            'dir', 'filter', 'limit', 'offset', 'start', 'end', 'date', 'from', 'to', 'status', 'view',
            'mode', 'level', 'access', 'session', 'key', 'apikey', 'api_key', 'ref', 'referer', 'callback',
            'pageNo', 'pageNum', 'pageNumber', 'count', 'size', 'width', 'height', 'color', 'theme',
            'debug', 'test', 'admin', 'action', 'cmd', 'command', 'query', 'id_user', 'user_id', 'pass',
            'password', 'pwd', 'token_id', 'auth', 'auth_token', 'tokenkey', 'token_key', 'hash', 'signature',
            'sig', 'callback_url', 'redirect', 'return', 'url', 'next', 'prev', 'prevPage', 'prev_page',
            'nextPage', 'next_page', 'offset', 'limit', 'pageSize', 'page_size', 'orderBy', 'orderby', 'order_by',
            'sortBy', 'sortby', 'sort_by', 'filterBy', 'filterby', 'filter_by', 'categoryId', 'category_id',
            'subcategory', 'sub_category', 'subCategory', 'productId', 'product_id', 'productName', 'product_name',
            'price', 'minPrice', 'maxPrice', 'min_price', 'max_price', 'rating', 'review', 'reviews', 'tag',
            'tags', 'brand', 'manufacturer', 'colorId', 'color_id', 'sizeId', 'size_id', 'quantity', 'qty',
            'cart', 'basket', 'sessionId', 'session_id', 'userAgent', 'user_agent', 'device', 'deviceId',
            'device_id', 'platform', 'os', 'operatingSystem', 'operating_system', 'locale', 'region', 'country',
            'zip', 'zipcode', 'postal', 'postalcode', 'latitude', 'longitude', 'lat', 'lng', 'ip', 'ipAddress',
            'ip_address', 'mac', 'macAddress', 'mac_address', 'browser', 'version', 'browserVersion', 'browser_version',
            'language', 'acceptLanguage', 'accept_language', 'contentType', 'content_type', 'acceptEncoding',
            'accept_encoding', 'connection', 'cacheControl', 'cache_control', 'pragma', 'authorization', 'auth_type',
            'credentials', 'cookie', 'cookies', 'referer', 'origin', 'host', 'userId', 'user_id', 'emailId', 'email_id',
            'username', 'user_name', 'firstName', 'first_name', 'lastName', 'last_name', 'middleName', 'middle_name',
            'fullname', 'full_name', 'address', 'address1', 'address2', 'city', 'state', 'province', 'countryCode',
            'country_code', 'phone', 'phoneNumber', 'phone_number', 'fax', 'mobile', 'mobileNumber', 'mobile_number',
            'statusId', 'status_id', 'role', 'userRole', 'user_role', 'adminRole', 'admin_role', 'group', 'groupId',
            'group_id', 'permission', 'permissions', 'accessLevel', 'access_level', 'lastLogin', 'last_login',
            'createdAt', 'created_at', 'updatedAt', 'updated_at', 'deletedAt', 'deleted_at', 'active', 'enabled',
            'disabled', 'verified', 'verifiedAt', 'verified_at', 'resetToken', 'reset_token', 'activationToken',
            'activation_token', 'confirmationToken', 'confirmation_token', 'inviteToken', 'invite_token', 'apiVersion',
            'api_version', 'deviceType', 'device_type', 'appVersion', 'app_version', 'platformVersion', 'platform_version',
            'sdkVersion', 'sdk_version', 'buildNumber', 'build_number', 'release', 'releaseDate', 'release_date',
            'sessionToken', 'session_token', 'csrfToken', 'csrf_token', 'nonce', 'signatureVersion', 'signature_version',
            'authMethod', 'auth_method', 'loginMethod', 'login_method', 'logoutMethod', 'logout_method', 'referrer',
            'utm_source', 'utm_medium', 'utm_campaign', 'utm_term', 'utm_content', 'trackingId', 'tracking_id',
            'trackingCode', 'tracking_code', 'affiliateId', 'affiliate_id', 'partnerId', 'partner_id', 'campaignId',
            'campaign_id', 'sourceId', 'source_id', 'mediumId', 'medium_id', 'contentId', 'content_id', 'keyword',
            'keywords', 'searchTerm', 'search_terms', 'filterTerm', 'filter_term', 'sortTerm', 'sort_term', 'pageIndex',
            'page_index', 'pageOffset', 'page_offset', 'pageLimit', 'page_limit', 'loadMore', 'load_more', 'infiniteScroll',
            'infinite_scroll', 'lazyLoad', 'lazy_load', 'sessionId', 'session_id', 'tokenId', 'token_id', 'authToken',
            'auth_token', 'refreshToken', 'refresh_token', 'accessToken', 'access_token', 'idToken', 'id_token', 'grantType',
            'grant_type', 'scope', 'responseType', 'response_type', 'state', 'prompt', 'nonce', 'display', 'maxAge',
            'max_age', 'loginHint', 'login_hint', 'hd', 'codeChallenge', 'code_challenge', 'codeChallengeMethod',
            'code_challenge_method', 'redirectUri', 'redirect_uri', 'postLogoutRedirectUri', 'post_logout_redirect_uri'
        ]
        params = {p: [''] for p in common_params}
    return params

def run():
    print("Running XSS scan with automatic parameter detection...")
    url = input("Enter target URL (with or without parameters): ").strip()
    parsed = urlparse(url)
    params = parse_qs(parsed.query)
    params = guess_params(params)

    payloads = [
        '<a href="https://www.pornhub.com" target="_blank"><img src="https://el.phncdn.com/gif/45467111.gif" alt="STUPID" width="900" height="450"></a>',
        '<a href="https://www.pornhub.com" target="_blank"><img src="https://media1.tenor.com/m/sLjUbG5BVikAAAAd/trump-dance-trump-2024.gif" alt="STUPID" width="900" height="450"></a>',
        '<a href="https://pornhub.com/" target="_blank" rel="noopener nofollow ugc"><img src="https://media.tenor.com/-K9sHxXAb-cAAAAC/shame-on-you-patricia.gif" style="border:1px solid black;max-width:100%;" alt="We are in maintenance, please visit this web page!"></a>'
    ]

    vulnerable_params = []
    results = []

    for param in params:
        vulnerable = False
        for payload in payloads:
            test_params = params.copy()
            test_params[param] = payload
            test_url = urlunparse(parsed._replace(query=urlencode(test_params, doseq=True)))
            try:
                res = requests.get(test_url, timeout=5)
                if payload in res.text:
                    print(Fore.RED + f"[!] XSS vulnerability detected in parameter: {param} with payload: " 
                          + Fore.LIGHTYELLOW_EX + payload + Style.RESET_ALL)
                    vulnerable = True
                    vulnerable_params.append(param)
                    results.append((param, True, payload))
                    break
            except Exception as e:
                print(Fore.RED + f"[ERROR] {e}")
        if not vulnerable:
            print(Fore.YELLOW + f"[ ] No XSS detected in parameter: {param}")
            results.append((param, False, None))

    if not vulnerable_params:
        print(Fore.YELLOW + "[!] No vulnerable parameters detected for XSS.")

    # Prepare detailed HTML report
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    vuln_count = sum(1 for _, v, _ in results if v)
    safe_count = len(results) - vuln_count

    html_content = f"""
    <html>
    <head>
        <title>XSS Scan Report</title>
        <style>
            body {{ font-family: Arial, sans-serif; background-color: #f9f9f9; padding: 20px; }}
            h1 {{ color: #333; }}
            table {{ border-collapse: collapse; width: 100%; }}
            th, td {{ border: 1px solid #ccc; padding: 8px; text-align: left; }}
            th {{ background-color: #f2f2f2; }}
            tr.vulnerable {{ background-color: #f8d7da; }} /* light red */
            tr.safe {{ background-color: #d4edda; }} /* light green */
            .summary {{ margin-bottom: 20px; }}
            .payload {{ font-family: monospace; white-space: pre-wrap; max-width: 600px; word-break: break-all; }}
        </style>
    </head>
    <body>
        <h1>XSS Scan Report for {url}</h1>
        <p class="summary">
            Scan run at: <strong>{timestamp}</strong><br>
            Total parameters tested: <strong>{len(results)}</strong><br>
            Vulnerable parameters: <strong>{vuln_count}</strong><br>
            Safe parameters: <strong>{safe_count}</strong>
        </p>
        <table>
            <thead>
                <tr>
                    <th>Parameter</th>
                    <th>Vulnerable</th>
                    <th>Payload (if vulnerable)</th>
                </tr>
            </thead>
            <tbody>
    """

    for param, vulnerable, payload in results:
        row_class = "vulnerable" if vulnerable else "safe"
        vuln_text = "Yes" if vulnerable else "No"
        payload_html = f'<div class="payload">{payload}</div>' if vulnerable else "-"
        html_content += f'<tr class="{row_class}"><td>{param}</td><td>{vuln_text}</td><td>{payload_html}</td></tr>'

    html_content += """
            </tbody>
        </table>
    </body>
    </html>
    """

    with open("xss_scan_report.html", "w", encoding="utf-8") as f:
        f.write(html_content)

    print(Fore.GREEN + "\n[+] Detailed HTML report saved to xss_scan_report.html")

if __name__ == "__main__":
    run()
