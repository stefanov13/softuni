text_ = input()

symbols_count = {}
for symbol_ in text_:
    if symbol_ in symbols_count:
        symbols_count[symbol_] += 1
    else:
        symbols_count[symbol_] = 1

ordered_symbols_count = dict(sorted(symbols_count.items()))

for symb, count_ in ordered_symbols_count.items():
    print(f"{symb}: {count_} time/s")
