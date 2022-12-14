convert_digit = float(input())
input_metric = input()
output_metric = input()
result = 0

if input_metric == "mm":
    if output_metric == "m":
        result = convert_digit * 0.001
    elif output_metric == "cm":
        result = convert_digit * 0.1
elif input_metric == "cm":
    if output_metric == "m":
        result = convert_digit * 0.01
    elif output_metric == "mm":
        result = convert_digit * 10
elif input_metric == "m":
    if output_metric == "cm":
        result = convert_digit * 100
    elif output_metric == "mm":
        result = convert_digit * 1000

print (f"{result:.3f}")
