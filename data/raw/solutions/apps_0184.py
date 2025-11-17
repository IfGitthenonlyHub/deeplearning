import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICBkZWYgbWF4UmVwT3B0MShzZWxmLCB0ZXh0OiBzdHIpIC0+IGludDoKICAgICAgICBmb3IgayxnIGluIGl0ZXJ0b29scy5ncm91cGJ5KHRleHQpOgogICAgICAgICAgICBwcmludChnKQogICAgICAgIEcgPSBbW2ssbGVuKGxpc3QoZykpXSBmb3IgayxnIGluIGl0ZXJ0b29scy5ncm91cGJ5KHRleHQpXQogICAgICAgIGMgPSBjb2xsZWN0aW9ucy5Db3VudGVyKHRleHQpCiAgICAgICAgCiAgICAgICAgcmVzID0gbWF4KG1pbihuKzEsIGNba10pIGZvciBrLG4gaW4gRykKICAgICAgICAKICAgICAgICBmb3IgaSBpbiByYW5nZSgxLGxlbihHKS0xKToKICAgICAgICAgICAgaWYgR1tpLTFdWzBdID09IEdbaSsxXVswXSBhbmQgR1tpXVsxXSA9PSAxOgogICAgICAgICAgICAgICAgcmVzID0gbWF4KG1pbihHW2ktMV1bMV0rR1tpKzFdWzFdKzEsIGNbR1tpLTFdWzBdXSksIHJlcykKICAgICAgICByZXR1cm4gcmVz").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
