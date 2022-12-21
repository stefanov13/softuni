def check_percent(num):
    bar = num // 10
    if num == 100:
        print(f"{num}% Complete!")
        print(f"[{bar * '%'}]")
    else:
        print(f"{num}% [{bar * '%'}{(10 - bar) * '.'}]")
        print("Still loading...")


loading_percent = int(input())
check_percent(loading_percent)
