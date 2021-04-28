clear = "\033[0m"

def title(f):
  print("\033[1;33m" + f"=== TESTING {f.__name__} ===" + clear)

def test(expected, f, *args):
  red = "\033[31m"
  green = "\033[32m"
  actual = f(*args)
  print(f"[{green + 'SUCCESS' + clear if actual == expected else red + 'FAIL' + clear}] {f.__name__}{args} = {actual}")
