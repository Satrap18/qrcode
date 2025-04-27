# QR Code Generator - پروژه تولید کیوآر کد

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-green.svg)
![QRCode](https://img.shields.io/badge/QR-Code-red.svg)

یک برنامه ساده برای تولید و ذخیره کیوآر کد با استفاده از پایتون و کتابخانه Tkinter.

## ویژگی‌های پروژه

- رابط کاربری ساده و intuitive
- امکان وارد کردن متن یا لینک برای تولید کیوآر کد
- قابلیت ذخیره کیوآر کد تولید شده در سیستم
- استفاده از کتابخانه qrcode برای تولید کیوآر کد
- طراحی شده با Tkinter برای رابط گرافیکی

## نحوه استفاده

1. متن یا URL مورد نظر خود را در فیلد وارد کنید
2. روی دکمه "Generate QR Code" کلیک کنید
3. کیوآر کد تولید شده را مشاهده خواهید کرد
4. برای ذخیره کیوآر کد، روی دکمه "Save QR Code" کلیک کنید
5. محل ذخیره‌سازی و نام فایل را انتخاب کنید (پیشفرض: .png)

## نیازمندی‌ها

- Python 3.x
- کتابخانه‌های مورد نیاز:
  ```
  tkinter
  qrcode
  ```

## نصب

1. ابتدا مخزن را کلون کنید:
   ```bash
   git clone https://github.com/yourusername/qr-code-generator.git
   cd qr-code-generator
   ```

2. کتابخانه‌های مورد نیاز را نصب کنید:
   ```bash
   pip install qrcode[pil]
   ```

3. برنامه را اجرا کنید:
   ```bash
   python QRCode.py
   ```

## تصاویر از برنامه

![Screenshot 1](screenshots/screenshot1.png) *(نمونه از رابط کاربری)*

## مشارکت

مشارکت‌ها، پیشنهادات و گزارش مشکلات از طریق Issues و Pull Requests پذیرفته می‌شوند.

## لایسنس

این پروژه تحت لایسنس [MIT](LICENSE) منتشر شده است.

---

با تشکر از استفاده از این پروژه! برای هر سوال یا مشکل می‌توانید Issue ایجاد کنید.