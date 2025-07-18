
---

## پروژه 2: تبدیل دما (Temperature Converter)

### کد Python (`temp_converter.py`):

```python
def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def main():
    print("تبدیل دما بین سلسیوس و فارنهایت")
    while True:
        print("\nانتخاب تبدیل:")
        print("1. سلسیوس به فارنهایت")
        print("2. فارنهایت به سلسیوس")
        print("3. خروج")

        choice = input("انتخاب کنید (1/2/3): ")

        if choice == "3":
            print("خداحافظ!")
            break

        if choice not in ["1", "2"]:
            print("گزینه نامعتبر است.")
            continue

        try:
            temp = float(input("دمای ورودی را وارد کنید: "))
        except ValueError:
            print("لطفاً عدد معتبر وارد کنید.")
            continue

        if choice == "1":
            result = celsius_to_fahrenheit(temp)
            print(f"{temp} درجه سلسیوس برابر است با {result:.2f} درجه فارنهایت.")
        elif choice == "2":
            result = fahrenheit_to_celsius(temp)
            print(f"{temp} درجه فارنهایت برابر است با {result:.2f} درجه سلسیوس.")

if __name__ == "__main__":
    main()
