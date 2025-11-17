import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICAgZGVmIG15QXRvaShzZWxmLCBzdHIpOgogICAgICAgICAiIiIKICAgICAgICAgOnR5cGUgc3RyOiBzdHIKICAgICAgICAgOnJ0eXBlOiBpbnQKICAgICAgICAgIiIiCiAgICAgICAgIGlmIGxlbihzdHIpID09IDAgOiByZXR1cm4gMAogICAgICAgICBscyA9IGxpc3Qoc3RyLnN0cmlwKCkpCiAgICAgICAgIAogICAgICAgICBzaWduID0gLTEgaWYgbHNbMF0gPT0gJy0nIGVsc2UgMQogICAgICAgICBpZiBsc1swXSBpbiBbJy0nLCcrJ10gOiBkZWwgbHNbMF0KICAgICAgICAgcmV0LCBpID0gMCwgMAogICAgICAgICB3aGlsZSBpIDwgbGVuKGxzKSBhbmQgbHNbaV0uaXNkaWdpdCgpIDoKICAgICAgICAgICAgIHJldCA9IHJldCoxMCArIG9yZChsc1tpXSkgLSBvcmQoJzAnKQogICAgICAgICAgICAgaSArPSAxCiAgICAgICAgIHJldHVybiBtYXgoLTIqKjMxLCBtaW4oc2lnbiAqIHJldCwyKiozMS0xKSk=").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
