import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("ZnJvbSBzeXMgaW1wb3J0IHN0ZGluLHN0ZG91dAp0PWludChzdGRpbi5yZWFkbGluZSgpKQp3aGlsZSh0KToKIG4scT1saXN0KG1hcChpbnQsc3RkaW4ucmVhZGxpbmUoKS5yc3RyaXAoKS5zcGxpdCgpKSkKIGFycj1saXN0KG1hcChpbnQsc3RkaW4ucmVhZGxpbmUoKS5yc3RyaXAoKS5zcGxpdCgpKSkKIGQ9e30KIGQxPXt9CiBhPWFyci5jb3B5KCkKIGEuc29ydCgpCiBmb3IgaSBpbiByYW5nZShuKToKICBkMVthW2ldXT1pCiAgZFthcnJbaV1dPWkKIHdoaWxlKHEpOgogIHY9aW50KHN0ZGluLnJlYWRsaW5lKCkucnN0cmlwKCkpCiAgaW5kZXg9ZFt2XQogIHNtYWxsZXI9ZDFbdl0KICBiaWdnZXI9bi1zbWFsbGVyLTEKICBsb3csaGlnaD0wLG4tMQogIGMxLGMyPTAsMAogIHdoaWxlKGhpZ2g+PWxvdyk6CiAgIG1pZD0oaGlnaCtsb3cpLy8yCiAgIGlmIG1pZD09aW5kZXg6CiAgICBicmVhawogICBlbGlmIGluZGV4Pm1pZDoKICAgIGlmIGFyclttaWRdPnY6CiAgICAgYzErPTEKICAgIGVsc2U6CiAgICAgc21hbGxlci09MQogICAgbG93PW1pZCsxCiAgIGVsc2U6CiAgICBpZiB2PmFyclttaWRdOgogICAgIGMyKz0xCiAgICBlbHNlOgogICAgIGJpZ2dlci09MQogICAgaGlnaD1taWQtMQogIGlmIGMyPmMxOgogICBpZiBiaWdnZXI+PShjMi1jMSk6CiAgICBwcmludChjMikKICAgZWxzZToKICAgIHByaW50KC0xKQogIGVsaWYgYzE+YzI6CiAgIGlmIHNtYWxsZXI+PShjMS1jMik6CiAgICBwcmludChjMSkKICAgZWxzZToKICAgIHByaW50KC0xKQogIGVsc2U6CiAgIHByaW50KGMxKQogIHEtPTEKIHQtPTE=").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
