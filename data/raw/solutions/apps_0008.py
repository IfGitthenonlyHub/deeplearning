import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Zm9yIF8gaW4gcmFuZ2UoaW50KGlucHV0KCkpKToKICAgIG4sIGsgPSBsaXN0KG1hcChpbnQsIGlucHV0KCkuc3BsaXQoKSkpCiAgICBpbnAgPSBpbnB1dCgpLmxvd2VyKCkKICAgIGsgPSBtaW4oaywgaW5wLmNvdW50KCdsJykpCiAgICBhbnMgPSBpbnAuY291bnQoJ3cnKSArIHR1cGxlKHppcChpbnAsICdsJyArIGlucCkpLmNvdW50KCd3dycpICsgayAqIDIKICAgIGlmICd3JyBpbiBpbnA6CiAgICAgICAgaW5wMiA9IFtdCiAgICAgICAgY3VyID0gLTEKICAgICAgICBmb3IgYyBpbiBpbnA6CiAgICAgICAgICAgIGlmIGN1ciAhPSAtMToKICAgICAgICAgICAgICAgIGlmIGMgPT0gJ2wnOgogICAgICAgICAgICAgICAgICAgIGN1ciArPSAxCiAgICAgICAgICAgICAgICBlbHNlOgogICAgICAgICAgICAgICAgICAgIGlucDIuYXBwZW5kKGN1cikKICAgICAgICAgICAgaWYgYyA9PSAndyc6CiAgICAgICAgICAgICAgICBjdXIgPSAwCiAgICAgICAgaW5wMi5zb3J0KCkKICAgICAgICBmb3IgaW5wMmkgaW4gaW5wMjoKICAgICAgICAgICAgaWYgaW5wMmkgPiBrOgogICAgICAgICAgICAgICAgYnJlYWsKICAgICAgICAgICAgayAtPSBpbnAyaQogICAgICAgICAgICBhbnMgKz0gMQogICAgZWxzZToKICAgICAgICBhbnMgPSBtYXgoYW5zIC0gMSwgMCkKICAgIHByaW50KGFucyk=").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
