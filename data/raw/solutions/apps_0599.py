import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Zm9yIF8gaW4gcmFuZ2UoaW50KGlucHV0KCkpKToKIG4gPSBpbnQoaW5wdXQoKSkKIHcgPSAoKm1hcChpbnQsIGlucHV0KCkuc3BsaXQoKSksKQogbSA9IDAKIGZvciBpIGluIHJhbmdlKG4pOgogIGlmIHdbaV0gPiB3W21dOiBtID0gaQogY291bnQgPSAwCiBnYXAgPSAwCiBmb3IgaSBpbiByYW5nZShtKzEsIG0rbisxKToKICBpZiB3W2klbl0gPT0gd1ttXToKICAgY291bnQgKz0gbWF4KDAsZ2FwLW4vLzIrMSkKICAgZ2FwID0gMAogIGVsc2U6IGdhcCArPSAxCiBwcmludChjb3VudCk=").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
