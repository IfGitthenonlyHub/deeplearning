import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICAgZGVmIGNhbGN1bGF0ZShzZWxmLCBzKToKICAgICAgICAgIiIiCiAgICAgICAgIDp0eXBlIHM6IHN0cgogICAgICAgICA6cnR5cGU6IGludAogICAgICAgICAiIiIKICAgICAgICAgc2lnbj1bMV0KICAgICAgICAgbnVtcz0wCiAgICAgICAgIHRvdGFsPTAKICAgICAgICAgbGF0ZXN0c2lnbj0xCiAgICAgICAgIGZvciBjIGluIHM6CiAgICAgICAgICAgICAKICAgICAgICAgICAgIGlmIGMuaXNkaWdpdCgpOgogICAgICAgICAgICAgICAgIG51bXM9MTAqbnVtcytpbnQoYykKICAgICAgICAgICAgIGVsaWYgYz09JygnOgogICAgICAgICAgICAgICAgIG51bXM9MAogICAgICAgICAgICAgICAgIHNpZ24uYXBwZW5kKGxhdGVzdHNpZ24pCiAgICAgICAgICAgICBlbGlmIGM9PScpJzoKICAgICAgICAgICAgICAgICB0b3RhbD10b3RhbCtsYXRlc3RzaWduKm51bXMKICAgICAgICAgICAgICAgICBzaWduLnBvcCgpCiAgICAgICAgICAgICAgICAgbnVtcz0wCiAgICAgICAgICAgICBlbGlmIGMgaW4gWycrJywnLSddOgogICAgICAgICAgICAgICAgIHRvdGFsPXRvdGFsK2xhdGVzdHNpZ24qbnVtcwogICAgICAgICAgICAgICAgIGxhdGVzdHNpZ249c2lnblstMV0qKCsxIGlmIGM9PScrJyBlbHNlIC0xKQogICAgICAgICAgICAgICAgIG51bXM9MAogICAgICAgICAKICAgICAgICAgcmV0dXJuIHRvdGFsK2xhdGVzdHNpZ24qbnVtcw==").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
