import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICBkZWYgbWluU3dhcHMoc2VsZiwgZ3JpZDogTGlzdFtMaXN0W2ludF1dKSAtPiBpbnQ6CiAgICAgICAgc3RhcnQ9MQogICAgICAgIHN3YXA9MAogICAgICAgIG49bGVuKGdyaWQpCiAgICAgICAgemVyb3NfaW5ncmlkPW4tMQogICAgICAgIHdoaWxlIHplcm9zX2luZ3JpZD4wOgogICAgICAgICAgICBzd2FwcGVkX2dyaWQ9RmFsc2UKICAgICAgICAgICAgZm9yIGkgaW4gcmFuZ2UobGVuKGdyaWQpKToKICAgICAgICAgICAgICAgIGlmIHN1bShncmlkW2ldW3N0YXJ0Ol0pPT0wOgogICAgICAgICAgICAgICAgICAgIHN3YXArPWkKICAgICAgICAgICAgICAgICAgICBncmlkLnJlbW92ZShncmlkW2ldKQogICAgICAgICAgICAgICAgICAgIHN3YXBwZWRfZ3JpZD1UcnVlCiAgICAgICAgICAgICAgICAgICAgemVyb3NfaW5ncmlkLT0xCiAgICAgICAgICAgICAgICAgICAgc3RhcnQrPTEKICAgICAgICAgICAgICAgICAgICBicmVhawogICAgICAgICAgICBpZiBub3Qgc3dhcHBlZF9ncmlkOgogICAgICAgICAgICAgICAgcmV0dXJuIC0xCiAgICAgICAgcmV0dXJuIHN3YXA=").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
