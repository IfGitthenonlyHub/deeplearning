import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICAgZGVmIHByZWRpY3RQYXJ0eVZpY3Rvcnkoc2VsZiwgc2VuYXRlKToKICAgICAgICAgIiIiCiAgICAgICAgIDp0eXBlIHNlbmF0ZTogc3RyCiAgICAgICAgIDpydHlwZTogc3RyCiAgICAgICAgICIiIgogICAgICAgICBudW0gPSAwICAjIG51bSBvZiBSZWVkaW5nIFIKICAgICAgICAgd2hpbGUgKCdSJyBpbiBzZW5hdGUgYW5kICdEJyBpbiBzZW5hdGUpOgogICAgICAgICAgICAgcmVzID0gW10KICAgICAgICAgICAgIGZvciBpIGluIHNlbmF0ZToKICAgICAgICAgICAgICAgICBpZiBpPT0nUic6CiAgICAgICAgICAgICAgICAgICAgIGlmIG51bT49MDoKICAgICAgICAgICAgICAgICAgICAgICAgIHJlcy5hcHBlbmQoaSkKICAgICAgICAgICAgICAgICAgICAgbnVtKz0xCiAgICAgICAgICAgICAgICAgZWxzZToKICAgICAgICAgICAgICAgICAgICAgaWYgbnVtPD0wOgogICAgICAgICAgICAgICAgICAgICAgICAgcmVzLmFwcGVuZChpKQogICAgICAgICAgICAgICAgICAgICBudW0tPTEKICAgICAgICAgICAgIHNlbmF0ZSA9IHJlcwogICAgICAgICByZXR1cm4gJ1JhZGlhbnQnIGlmICdSJyBpbiBzZW5hdGUgZWxzZSAnRGlyZSc=").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
