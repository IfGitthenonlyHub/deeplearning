import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Zm9yIF8gaW4gcmFuZ2UoaW50KGlucHV0KCkpKToKIGEsYj1saXN0KG1hcChpbnQsaW5wdXQoKS5zcGxpdCgpKSkKIGFiPWJpbihhKVsyOl0KIGJiPWJpbihiKVsyOl0KIG49YWJzKGxlbihiYiktbGVuKGFiKSkKIGlmIG4+MDoKICBpZiBsZW4oYmIpPmxlbihhYik6CiAgIGFiID0gIjAiKm4gKyBhYgogIGVsc2U6CiAgIGJiID0gIjAiKm4gKyBiYgogbT0wCiBjb3VudD0wCiBmb3IgaSBpbiByYW5nZShsZW4oYmIpKToKICBsPWludChhYiwyKV5pbnQoYmIsMikKICBpZiBsPm06CiAgIG09bAogICBjb3VudD1pCiAgYmIgPWJiWy0xXSArIGJiCiAgYmI9YmJbOi0xXQogIAogcHJpbnQoY291bnQsbSk=").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
