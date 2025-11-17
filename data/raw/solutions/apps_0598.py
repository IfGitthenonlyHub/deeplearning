import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("ZGVmIFR1cm4oYSwgbik6CiBtID0gbWF4KGEpCiBmb3IgaSBpbiByYW5nZShuKToKICBhW2ldID0gbSAtIGFbaV0KCm4sIGsgPSBsaXN0KG1hcChpbnQsIGlucHV0KCkuc3BsaXQoKSkpCmEgPSBsaXN0KG1hcChpbnQsIGlucHV0KCkuc3BsaXQoKSkpCmlmIGsgPiAwOgogVHVybihhLCBuKQogayAtPSAxCiBpZiBrICYgMSA9PSAxOgogIFR1cm4oYSwgbikKcHJpbnQoJyAnLmpvaW4obWFwKHN0cixhKSkp").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
