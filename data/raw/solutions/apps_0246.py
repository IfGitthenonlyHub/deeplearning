import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICAgZGVmIHJlcGxhY2VXb3JkcyhzZWxmLCBkaWN0LCBzZW50ZW5jZSk6CiAgICAgICAgIHRyaWVfdHJlZSA9IHsncm9vdCc6IHt9fQogICAgICAgICBmb3Igd29yZCBpbiBkaWN0OgogICAgICAgICAgICAgcGFyZW50ID0gdHJpZV90cmVlWydyb290J10KICAgICAgICAgICAgIGZvciBjIGluIHdvcmQgKyAnIyc6CiAgICAgICAgICAgICAgICAgcGFyZW50LnNldGRlZmF1bHQoYywge30pCiAgICAgICAgICAgICAgICAgcGFyZW50ID0gcGFyZW50W2NdCiAgICAgICAgIHNlbnRlbmNlLCByZXMgPSBzZW50ZW5jZS5zcGxpdCgpLCBbXQogICAgICAgICBmb3Igd29yZCBpbiBzZW50ZW5jZToKICAgICAgICAgICAgIHBhcmVudCA9IHRyaWVfdHJlZVsncm9vdCddCiAgICAgICAgICAgICBmb3IgaSwgYyBpbiBlbnVtZXJhdGUod29yZCArICcqJyk6CiAgICAgICAgICAgICAgICAgaWYgYyBub3QgaW4gcGFyZW50OgogICAgICAgICAgICAgICAgICAgICByZXMuYXBwZW5kKHdvcmQpCiAgICAgICAgICAgICAgICAgICAgIGJyZWFrCiAgICAgICAgICAgICAgICAgcGFyZW50ID0gcGFyZW50W2NdCiAgICAgICAgICAgICAgICAgaWYgJyMnIGluIHBhcmVudDoKICAgICAgICAgICAgICAgICAgICAgcmVzLmFwcGVuZCh3b3JkWzppICsgMV0pCiAgICAgICAgICAgICAgICAgICAgIGJyZWFrCiAgICAgICAgIHJldHVybiAnICcuam9pbihyZXMp").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
