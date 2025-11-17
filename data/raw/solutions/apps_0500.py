import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICAgZGVmIGNhbGN1bGF0ZShzZWxmLCBzKToKICAgICAgICAgaWYgbm90IHM6IHJldHVybiAwCiAgICAgICAgIGxlbmd0aCA9IGxlbihzKQogICAgICAgICBzdGFjayA9IFtdCiAgICAgICAgIG51bSA9IDAKICAgICAgICAgc2lnbiA9ICcrJwogICAgICAgICBmb3IgaWR4LCBjIGluIGVudW1lcmF0ZShzKToKICAgICAgICAgICAgIGlmIGMuaXNkaWdpdCgpOgogICAgICAgICAgICAgICAgIG51bSA9IG51bSoxMCArIG9yZChjKSAtIG9yZCgnMCcpCiAgICAgICAgICAgICBpZiBjIGluIFsnKycsJy0nLCcqJywnLyddIG9yIGlkeCA9PSBsZW5ndGggLSAxOgogICAgICAgICAgICAgICAgIGlmIHNpZ24gPT0gJysnOgogICAgICAgICAgICAgICAgICAgICBzdGFjay5hcHBlbmQobnVtKQogICAgICAgICAgICAgICAgIGVsaWYgc2lnbiA9PSAnLSc6CiAgICAgICAgICAgICAgICAgICAgIHN0YWNrLmFwcGVuZCgtbnVtKQogICAgICAgICAgICAgICAgIGVsaWYgc2lnbiA9PSAnKic6CiAgICAgICAgICAgICAgICAgICAgIHN0YWNrLmFwcGVuZChzdGFjay5wb3AoKSAqIG51bSkKICAgICAgICAgICAgICAgICBlbGlmIHNpZ24gPT0gJy8nOgogICAgICAgICAgICAgICAgICAgICBzdGFjay5hcHBlbmQoaW50KHN0YWNrLnBvcCgpIC8gbnVtKSkKICAgICAgICAgICAgICAgICBzaWduID0gYwogICAgICAgICAgICAgICAgIG51bSA9IDAKICAgICAgICAgCiAgICAgICAgIHJldHVybiBzdW0oc3RhY2spCiAgICAgICAgICIiIgogICAgICAgICA6dHlwZSBzOiBzdHIKICAgICAgICAgOnJ0eXBlOiBpbnQKICAgICAgICAgIiIi").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
