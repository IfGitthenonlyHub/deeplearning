import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICAgZGVmIGZpbmRMZW5ndGgoc2VsZiwgQSwgQik6CiAgICAgICAgIGRlZiBjaGVjayhsZW5ndGgpOgogICAgICAgICAgICAgc2VlbiA9IHtBW2k6aStsZW5ndGhdCiAgICAgICAgICAgICAgICAgICAgIGZvciBpIGluIHJhbmdlKGxlbihBKSAtIGxlbmd0aCArIDEpfQogICAgICAgICAgICAgcmV0dXJuIGFueShCW2o6aitsZW5ndGhdIGluIHNlZW4KICAgICAgICAgICAgICAgICAgICAgICAgZm9yIGogaW4gcmFuZ2UobGVuKEIpIC0gbGVuZ3RoICsgMSkpCiAKICAgICAgICAgQSA9ICcnLmpvaW4obWFwKGNociwgQSkpCiAgICAgICAgIEIgPSAnJy5qb2luKG1hcChjaHIsIEIpKQogICAgICAgICBsbywgaGkgPSAwLCBtaW4obGVuKEEpLCBsZW4oQikpICsgMQogICAgICAgICB3aGlsZSBsbyA8IGhpOgogICAgICAgICAgICAgbWkgPSBpbnQoKGxvICsgaGkpIC8gMikKICAgICAgICAgICAgIGlmIGNoZWNrKG1pKToKICAgICAgICAgICAgICAgICBsbyA9IG1pICsgMQogICAgICAgICAgICAgZWxzZToKICAgICAgICAgICAgICAgICBoaSA9IG1pCiAgICAgICAgIHJldHVybiBsbyAtIDE=").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
