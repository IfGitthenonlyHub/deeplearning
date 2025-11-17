import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("aW1wb3J0IHN5cwoKaW5wdXQgPSBzeXMuc3RkaW4ucmVhZGxpbmUKCmZvciBfIGluIHJhbmdlKGludChpbnB1dCgpKSk6CiAgICBuLCBrID0gbGlzdChtYXAoaW50LCBpbnB1dCgpLnNwbGl0KCkpKQogICAgYSA9IGxpc3QobWFwKGludCwgaW5wdXQoKS5zcGxpdCgpKSkKICAgIGlmIGxlbihzZXQoYSkpID4gazoKICAgICAgICBwcmludCgtMSkKICAgICAgICBjb250aW51ZQogICAgYSA9IGxpc3Qoc2V0KGEpKQogICAgYSArPSBbMV0gKiAoayAtIGxlbihhKSkKICAgIHByaW50KGsgKiBuKQogICAgcHJpbnQoKihhICogbikp").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
