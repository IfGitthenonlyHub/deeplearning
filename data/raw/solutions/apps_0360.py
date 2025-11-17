import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgZGVmIHNoaXBXaXRoaW5EYXlzKHNlbGYsIHdlaWdodHM6IExpc3RbaW50XSwgRDogaW50KSAtPiBpbnQ6CiAgICBsZWZ0LCByaWdodCA9IG1heCh3ZWlnaHRzKSwgc3VtKHdlaWdodHMpCiAgICB3aGlsZSBsZWZ0IDwgcmlnaHQ6CiAgICAgIG1pZCwgbmVlZCwgY3VyID0gbGVmdCArIChyaWdodCAtIGxlZnQpIC8vIDIsIDEsIDAKICAgICAgZm9yIHcgaW4gd2VpZ2h0czoKICAgICAgICBpZiBjdXIgKyB3ID4gbWlkOgogICAgICAgICAgbmVlZCArPSAxCiAgICAgICAgICBjdXIgPSAwCiAgICAgICAgY3VyICs9IHcKICAgICAgaWYgbmVlZCA+IEQ6IGxlZnQgPSBtaWQgKyAxCiAgICAgIGVsc2UgOiByaWdodCA9IG1pZAogICAgcmV0dXJuIGxlZnQ=").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
