def test_driver():
cases = [
("the human torch", "The Human Torch"),
("uatu the watcher", "Uatu The Watcher"),
("susan storm-richards", "Susan Storm-richards"),
]
for given, expected in cases:
got = my_title(given)
print(got == expected, repr(given), "->", repr(got))
