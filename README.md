# YouTube Downloader Documentation

## Persian (فارسی)

### معرفی پروژه
این پروژه یک اپلیکیشن دانلود ویدیو از یوتیوب است که با استفاده از پایتون و کتابخانه PyQt6 برای رابط گرافیکی توسعه یافته است. این برنامه امکان دانلود ویدیو یا صوت از یوتیوب را با انتخاب کیفیت و ذخیره در مسیر دلخواه فراهم می‌کند. رابط کاربری حرفه‌ای با تم‌های ویندوز 11، تاریک، قرمز و آبی طراحی شده و از چهار زبان (فارسی، انگلیسی، چینی و روسی) پشتیبانی می‌کند. این اپلیکیشن دارای قابلیت‌هایی مانند نمایش درصد پیشرفت دانلود، تاریخچه دانلود و تنظیمات زبان و تم است.

### ویژگی‌ها
- **دانلود ویدیو و صوت**: دانلود ویدیوهای یوتیوب با انتخاب کیفیت‌های مختلف.
- **رابط کاربری چندزبانه**: پشتیبانی از زبان‌های فارسی، انگلیسی، چینی و روسی با چیدمان راست‌چین و چپ‌چین.
- **تم‌های متنوع**: شامل تم‌های ویندوز 11، تاریک، قرمز و آبی با طراحی مدرن و جذاب.
- **تاریخچه دانلود**: نمایش و مدیریت تاریخچه دانلودها با جزئیات (عنوان، لینک، تاریخ و مسیر فایل).
- **پیشرفت دانلود**: نمایش درصد پیشرفت دانلود با نوار پیشرفت.
- **انتخاب پوشه**: امکان انتخاب مسیر ذخیره‌سازی فایل‌های دانلودشده.
- **طراحی حرفه‌ای**: رابط کاربری مشابه ویندوز 11 با انیمیشن‌ها و افکت‌های بصری زیبا.

### پیش‌نیازها
- پایتون 3.8 یا بالاتر
- کتابخانه‌های مورد نیاز:
  - PyQt6 (`pip install PyQt6`)
  - pytube (`pip install pytube`)
- سیستم‌عامل: ویندوز یا لینوکس
- دسترسی به اینترنت برای دانلود ویدیوها

### نصب و راه‌اندازی
1. فایل `youtube_downloader.py` را در یک پوشه ذخیره کنید.
2. کتابخانه‌های مورد نیاز را با استفاده از دستورات زیر نصب کنید:
   ```bash
   pip install PyQt6
   pip install pytube
   ```
3. فایل را اجرا کنید:
   ```bash
   python youtube_downloader.py
   ```
4. در رابط کاربری، لینک یوتیوب را وارد کنید، کیفیت را انتخاب کنید و دکمه دانلود را فشار دهید.

### ساختار فایل‌ها
- `youtube_downloader.py`: فایل اصلی حاوی کد پایتون و رابط گرافیکی.
- `download_history.json`: فایل ذخیره‌سازی تاریخچه دانلودها (به‌صورت خودکار ایجاد می‌شود).
- `icon.ico` (اختیاری): فایل آیکون برنامه برای نمایش در نوار عنوان.

### توسعه‌دهنده
توسعه‌یافته توسط حمید یارعلی  
- گیت‌هاب: [HamidYaraliOfficial](https://github.com/HamidYaraliOfficial)  
- اینستاگرام: [hamidyaraliofficial](https://www.instagram.com/hamidyaraliofficial?igsh=MWpxZjhhMHZuNnlpYQ==)  
- تلگرام: [@Hamid_Yarali](https://t.me/Hamid_Yarali)

---

## English

### Project Overview
This project is a YouTube video downloader application developed using Python and the PyQt6 library for its graphical user interface. It allows users to download videos or audio from YouTube with selectable quality and save them to a desired location. The application features a professional interface inspired by Windows 11, with support for Windows, Dark, Red, and Blue themes, and four languages (Persian, English, Chinese, and Russian). It includes functionalities such as download progress tracking, download history, and customizable language and theme settings.

### Features
- **Video and Audio Download**: Download YouTube videos with various quality options.
- **Multilingual Interface**: Supports Persian, English, Chinese, and Russian with proper right-to-left and left-to-right layouts.
- **Multiple Themes**: Includes Windows 11, Dark, Red, and Blue themes with a modern and appealing design.
- **Download History**: View and manage download history with details (title, URL, date, and file path).
- **Download Progress**: Displays download progress with a progress bar.
- **Folder Selection**: Choose custom directories for saving downloaded files.
- **Professional Design**: Windows 11-inspired interface with smooth animations and visual effects.

### Requirements
- Python 3.8 or higher
- Required libraries:
  - PyQt6 (`pip install PyQt6`)
  - pytube (`pip install pytube`)
- Operating System: Windows or Linux
- Internet connection for downloading videos

### Installation and Setup
1. Save the `youtube_downloader.py` file in a directory.
2. Install the required libraries using the following commands:
   ```bash
   pip install PyQt6
   pip install pytube
   ```
3. Run the file:
   ```bash
   python youtube_downloader.py
   ```
4. In the interface, enter a YouTube URL, select a quality, and click the download button.

### File Structure
- `youtube_downloader.py`: Main file containing the Python code and GUI.
- `download_history.json`: File for storing download history (automatically created).
- `icon.ico` (optional): Application icon file for the title bar.

### Developer
Developed by Hamid Yarali  
- GitHub: [HamidYaraliOfficial](https://github.com/HamidYaraliOfficial)  
- Instagram: [hamidyaraliofficial](https://www.instagram.com/hamidyaraliofficial?igsh=MWpxZjhhMHZuNnlpYQ==)  
- Telegram: [@Hamid_Yarali](https://t.me/Hamid_Yarali)

---

## Chinese (中文)

### 项目简介
该项目是一个使用 Python 和 PyQt6 库开发的 YouTube 视频下载器应用程序。它允许用户从 YouTube 下载视频或音频，并支持选择不同质量和保存路径。该应用程序具有专业的用户界面，灵感来源于 Windows 11，支持 Windows、暗色、红色和蓝色四种主题，并支持四种语言（波斯语、英语、中文和俄语）。其功能包括下载进度跟踪、下载历史记录以及语言和主题的自定义设置。

### 功能
- **视频和音频下载**：支持以多种质量下载 YouTube 视频。
- **多语言界面**：支持波斯语、英语、中文和俄语，适配右到左和左到右布局。
- **多种主题**：包括 Windows 11、暗色、红色和蓝色主题，设计现代且吸引人。
- **下载历史**：查看和管理下载历史，包含详细信息（标题、URL、日期和文件路径）。
- **下载进度**：通过进度条显示下载进度。
- **文件夹选择**：支持选择自定义保存下载文件的目录。
- **专业设计**：灵感来源于 Windows 11 的界面，带有流畅的动画和视觉效果。

### 要求
- Python 3.8 或更高版本
- 所需库：
  - PyQt6 (`pip install PyQt6`)
  - pytube (`pip install pytube`)
- 操作系统：Windows 或 Linux
- 互联网连接用于下载视频

### 安装和设置
1. 将 `youtube_downloader.py` 文件保存在一个目录中。
2. 使用以下命令安装所需库：
   ```bash
   pip install PyQt6
   pip install pytube
   ```
3. 运行文件：
   ```bash
   python youtube_downloader.py
   ```
4. 在界面中输入 YouTube 链接，选择质量，然后点击下载按钮。

### 文件结构
- `youtube_downloader.py`：包含 Python 代码和图形用户界面的主文件。
- `download_history.json`：用于存储下载历史的文件（自动创建）。
- `icon.ico`（可选）：应用程序标题栏的图标文件。

### 开发者
由 Hamid Yarali 开发  
- GitHub: [HamidYaraliOfficial](https://github.com/HamidYaraliOfficial)  
- Instagram: [hamidyaraliofficial](https://www.instagram.com/hamidyaraliofficial?igsh=MWpxZjhhMHZuNnlpYQ==)  
- Telegram: [@Hamid_Yarali](https://t.me/Hamid_Yarali)