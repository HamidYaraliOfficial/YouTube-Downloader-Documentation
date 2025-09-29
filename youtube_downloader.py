import sys
import os
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit,
    QPushButton, QComboBox, QProgressBar, QTextEdit, QLabel, QStyleFactory,
    QTabWidget, QGridLayout, QScrollArea, QMenuBar, QMenu, QFileDialog
)
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QIcon, QPalette, QColor, QFont
from pytube import YouTube
import datetime
import json
from pathlib import Path

# Developed by Hamid Yarali
# GitHub: https://github.com/HamidYaraliOfficial
# Instagram: https://www.instagram.com/hamidyaraliofficial?igsh=MWpxZjhhMHZuNnlpYQ==
# Telegram: @Hamid_Yarali

class YouTubeDownloader(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("YouTube Downloader")
        self.setGeometry(100, 100, 900, 600)
        self.setWindowIcon(QIcon('icon.ico'))  # Assuming an icon file exists
        
        # Language and theme settings
        self.current_lang = 'en'
        self.current_theme = 'Windows'
        self.download_history = []
        self.load_history()
        
        # Language dictionaries
        self.texts = {
            'en': {
                'title': 'YouTube Downloader',
                'url_label': 'Enter YouTube URL:',
                'download_btn': 'Download',
                'quality_label': 'Select Quality:',
                'history_tab': 'Download History',
                'settings_tab': 'Settings',
                'language_label': 'Language:',
                'theme_label': 'Theme:',
                'clear_history': 'Clear History',
                'status_idle': 'Ready to download...',
                'status_downloading': 'Downloading: {title}',
                'status_complete': 'Download completed: {title}',
                'status_error': 'Error: {error}',
                'history_title': 'Title',
                'history_url': 'URL',
                'history_date': 'Date',
                'history_path': 'Path',
                'select_folder': 'Select Download Folder',
                'default_folder': 'Default Download Folder',
                'apply': 'Apply',
                'file_menu': 'File',
                'exit_action': 'Exit',
                'about': 'About',
                'about_text': 'YouTube Downloader\nVersion 1.0\nDeveloped by Hamid Yarali\nGitHub: https://github.com/HamidYaraliOfficial\nInstagram: https://www.instagram.com/hamidyaraliofficial\nTelegram: @Hamid_Yarali'
            },
            'fa': {
                'title': 'دانلودکننده یوتیوب',
                'url_label': 'لینک یوتیوب را وارد کنید:',
                'download_btn': 'دانلود',
                'quality_label': 'انتخاب کیفیت:',
                'history_tab': 'تاریخچه دانلود',
                'settings_tab': 'تنظیمات',
                'language_label': 'زبان:',
                'theme_label': 'تم:',
                'clear_history': 'پاک کردن تاریخچه',
                'status_idle': 'آماده برای دانلود...',
                'status_downloading': 'در حال دانلود: {title}',
                'status_complete': 'دانلود کامل شد: {title}',
                'status_error': 'خطا: {error}',
                'history_title': 'عنوان',
                'history_url': 'لینک',
                'history_date': 'تاریخ',
                'history_path': 'مسیر',
                'select_folder': 'انتخاب پوشه دانلود',
                'default_folder': 'پوشه پیش‌فرض دانلود',
                'apply': 'اعمال',
                'file_menu': 'فایل',
                'exit_action': 'خروج',
                'about': 'درباره',
                'about_text': 'دانلودکننده یوتیوب\nنسخه 1.0\nتوسعه‌یافته توسط حمید یارعلی\nگیت‌هاب: https://github.com/HamidYaraliOfficial\nاینستاگرام: https://www.instagram.com/hamidyaraliofficial\nتلگرام: @Hamid_Yarali'
            },
            'zh': {
                'title': 'YouTube 下载器',
                'url_label': '请输入 YouTube 链接：',
                'download_btn': '下载',
                'quality_label': '选择质量：',
                'history_tab': '下载历史',
                'settings_tab': '设置',
                'language_label': '语言：',
                'theme_label': '主题：',
                'clear_history': '清除历史记录',
                'status_idle': '准备下载...',
                'status_downloading': '正在下载：{title}',
                'status_complete': '下载完成：{title}',
                'status_error': '错误：{error}',
                'history_title': '标题',
                'history_url': '链接',
                'history_date': '日期',
                'history_path': '路径',
                'select_folder': '选择下载文件夹',
                'default_folder': '默认下载文件夹',
                'apply': '应用',
                'file_menu': '文件',
                'exit_action': '退出',
                'about': '关于',
                'about_text': 'YouTube 下载器\n版本 1.0\n由 Hamid Yarali 开发\nGitHub: https://github.com/HamidYaraliOfficial\nInstagram: https://www.instagram.com/hamidyaraliofficial\nTelegram: @Hamid_Yarali'
            },
            'ru': {
                'title': 'Загрузчик YouTube',
                'url_label': 'Введите URL YouTube:',
                'download_btn': 'Скачать',
                'quality_label': 'Выберите качество:',
                'history_tab': 'История загрузок',
                'settings_tab': 'Настройки',
                'language_label': 'Язык:',
                'theme_label': 'Тема:',
                'clear_history': 'Очистить историю',
                'status_idle': 'Готово к загрузке...',
                'status_downloading': 'Загрузка: {title}',
                'status_complete': 'Загрузка завершена: {title}',
                'status_error': 'Ошибка: {error}',
                'history_title': 'Название',
                'history_url': 'URL',
                'history_date': 'Дата',
                'history_path': 'Путь',
                'select_folder': 'Выберите папку для загрузки',
                'default_folder': 'Папка для загрузки по умолчанию',
                'apply': 'Применить',
                'file_menu': 'Файл',
                'exit_action': 'Выход',
                'about': 'О программе',
                'about_text': 'Загрузчик YouTube\nВерсия 1.0\nРазработано Hamid Yarali\nGitHub: https://github.com/HamidYaraliOfficial\nInstagram: https://www.instagram.com/hamidyaraliofficial\nTelegram: @Hamid_Yarali'
            }
        }

        # Theme dictionaries with improved contrast
        self.themes = {
            'Windows': {
                'background': QColor(245, 245, 245),  # Light gray
                'text': QColor(0, 0, 0),  # Black
                'button': QColor(230, 230, 230),  # Light gray button
                'button_text': QColor(0, 0, 0),  # Black
                'button_hover': QColor(200, 200, 200),  # Slightly darker gray
                'accent': QColor(0, 120, 212),  # Windows blue
                'border': QColor(180, 180, 180),  # Medium gray
                'header': QColor(220, 220, 220)  # Light gray header
            },
            'Dark': {
                'background': QColor(32, 32, 32),  # Dark gray
                'text': QColor(230, 230, 230),  # Light gray
                'button': QColor(50, 50, 50),  # Darker gray
                'button_text': QColor(230, 230, 230),  # Light gray
                'button_hover': QColor(70, 70, 70),  # Slightly lighter dark
                'accent': QColor(0, 120, 212),  # Blue accent
                'border': QColor(80, 80, 80),  # Dark gray border
                'header': QColor(40, 40, 40)  # Darker gray header
            },
            'Red': {
                'background': QColor(255, 235, 235),  # Light red
                'text': QColor(80, 0, 0),  # Dark red
                'button': QColor(255, 200, 200),  # Light red button
                'button_text': QColor(80, 0, 0),  # Dark red
                'button_hover': QColor(255, 180, 180),  # Slightly darker red
                'accent': QColor(200, 0, 0),  # Red accent
                'border': QColor(220, 150, 150),  # Medium red
                'header': QColor(255, 220, 220)  # Light red header
            },
            'Blue': {
                'background': QColor(235, 245, 255),  # Light blue
                'text': QColor(0, 0, 80),  # Dark blue
                'button': QColor(200, 220, 255),  # Light blue button
                'button_text': QColor(0, 0, 80),  # Dark blue
                'button_hover': QColor(180, 200, 255),  # Slightly darker blue
                'accent': QColor(0, 0, 200),  # Blue accent
                'border': QColor(150, 180, 220),  # Medium blue
                'header': QColor(220, 235, 255)  # Light blue header
            }
        }

        # Initialize UI
        self.init_ui()
        self.apply_theme(self.current_theme)
        self.update_texts()

    def init_ui(self):
        # Main widget and layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.main_layout = QVBoxLayout(self.central_widget)
        self.main_layout.setContentsMargins(20, 20, 20, 20)
        self.main_layout.setSpacing(15)

        # Menu bar
        self.menu_bar = QMenuBar()
        self.file_menu = QMenu(self.texts['en']['file_menu'])
        self.exit_action = self.file_menu.addAction(self.texts['en']['exit_action'])
        self.exit_action.triggered.connect(self.close)
        self.about_action = self.file_menu.addAction(self.texts['en']['about'])
        self.about_action.triggered.connect(self.show_about)
        self.menu_bar.addMenu(self.file_menu)
        self.main_layout.addWidget(self.menu_bar)

        # Tab widget
        self.tabs = QTabWidget()
        self.tabs.setStyleSheet("""
            QTabWidget::pane {
                border: 1px solid rgba(0, 0, 0, 0.1);
                border-radius: 8px;
                background: rgba(255, 255, 255, 0.95);
            }
            QTabBar::tab {
                padding: 10px 20px;
                margin-right: 5px;
                border-top-left-radius: 8px;
                border-top-right-radius: 8px;
                background: rgba(0, 0, 0, 0.05);
                color: black;
            }
            QTabBar::tab:selected {
                background: rgba(0, 120, 212, 0.3);
                font-weight: bold;
                color: black;
            }
        """)
        self.main_layout.addWidget(self.tabs)

        # Download tab
        self.download_tab = QWidget()
        self.download_layout = QVBoxLayout(self.download_tab)
        self.download_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.download_layout.setSpacing(10)

        # URL input
        self.url_label = QLabel()
        self.url_label.setFont(QFont("Segoe UI", 12))
        self.url_input = QLineEdit()
        self.url_input.setPlaceholderText("https://www.youtube.com/watch?v=...")
        self.url_input.setFixedHeight(40)
        self.url_input.setStyleSheet("""
            QLineEdit {
                border-radius: 8px;
                padding: 8px;
                font-size: 14px;
                border: 1px solid rgba(0, 0, 0, 0.2);
                background: rgba(255, 255, 255, 0.95);
                color: black;
            }
        """)

        # Quality selection
        self.quality_label = QLabel()
        self.quality_label.setFont(QFont("Segoe UI", 12))
        self.quality_combo = QComboBox()
        self.quality_combo.setFixedHeight(40)
        self.quality_combo.setStyleSheet("""
            QComboBox {
                border-radius: 8px;
                padding: 8px;
                font-size: 14px;
                border: 1px solid rgba(0, 0, 0, 0.2);
                background: rgba(255, 255, 255, 0.95);
                color: black;
            }
            QComboBox::drop-down {
                border: none;
            }
        """)

        # Download button
        self.download_btn = QPushButton()
        self.download_btn.setFixedHeight(50)
        self.download_btn.setFont(QFont("Segoe UI", 12, QFont.Weight.Bold))
        self.download_btn.setStyleSheet("""
            QPushButton {
                border-radius: 10px;
                font-size: 16px;
                font-weight: bold;
                border: 1px solid rgba(0, 0, 0, 0.1);
                background: rgba(0, 120, 212, 0.8);
                color: white;
            }
            QPushButton:hover {
                background: rgba(0, 120, 212, 1.0);
            }
            QPushButton:disabled {
                background: rgba(0, 120, 212, 0.5);
                color: rgba(255, 255, 255, 0.7);
            }
        """)
        self.download_btn.clicked.connect(self.start_download)

        # Progress bar
        self.progress_bar = QProgressBar()
        self.progress_bar.setTextVisible(True)
        self.progress_bar.setFixedHeight(30)
        self.progress_bar.setStyleSheet("""
            QProgressBar {
                border-radius: 8px;
                text-align: center;
                font-size: 12px;
                background: rgba(0, 0, 0, 0.1);
                color: black;
            }
            QProgressBar::chunk {
                background: rgba(0, 120, 212, 0.8);
                border-radius: 8px;
            }
        """)

        # Status text
        self.status_text = QTextEdit()
        self.status_text.setReadOnly(True)
        self.status_text.setFixedHeight(120)
        self.status_text.setStyleSheet("""
            QTextEdit {
                border-radius: 8px;
                font-size: 14px;
                border: 1px solid rgba(0, 0, 0, 0.2);
                background: rgba(255, 255, 255, 0.95);
                color: black;
            }
        """)

        # Folder selection
        self.folder_label = QLabel()
        self.folder_label.setFont(QFont("Segoe UI", 12))
        self.folder_input = QLineEdit()
        self.folder_input.setPlaceholderText(self.texts['en']['default_folder'])
        self.folder_input.setFixedHeight(40)
        self.folder_input.setStyleSheet("""
            QLineEdit {
                border-radius: 8px;
                padding: 8px;
                font-size: 14px;
                border: 1px solid rgba(0, 0, 0, 0.2);
                background: rgba(255, 255, 255, 0.95);
                color: black;
            }
        """)
        self.folder_btn = QPushButton()
        self.folder_btn.setFixedHeight(40)
        self.folder_btn.setFont(QFont("Segoe UI", 12))
        self.folder_btn.setStyleSheet("""
            QPushButton {
                border-radius: 8px;
                font-size: 14px;
                border: 1px solid rgba(0, 0, 0, 0.1);
                background: rgba(0, 120, 212, 0.8);
                color: white;
            }
            QPushButton:hover {
                background: rgba(0, 120, 212, 1.0);
            }
        """)
        self.folder_btn.clicked.connect(self.select_folder)

        # Layout for download tab
        folder_layout = QHBoxLayout()
        folder_layout.addWidget(self.folder_input)
        folder_layout.addWidget(self.folder_btn)
        self.download_layout.addWidget(self.url_label)
        self.download_layout.addWidget(self.url_input)
        self.download_layout.addWidget(self.quality_label)
        self.download_layout.addWidget(self.quality_combo)
        self.download_layout.addWidget(self.download_btn)
        self.download_layout.addWidget(self.folder_label)
        self.download_layout.addLayout(folder_layout)
        self.download_layout.addWidget(self.progress_bar)
        self.download_layout.addWidget(self.status_text)

        # History tab
        self.history_tab = QWidget()
        self.history_layout = QVBoxLayout(self.history_tab)
        self.history_scroll = QScrollArea()
        self.history_scroll.setWidgetResizable(True)
        self.history_content = QWidget()
        self.history_grid = QGridLayout(self.history_content)
        self.history_grid.setSpacing(10)
        self.history_scroll.setWidget(self.history_content)
        self.history_scroll.setStyleSheet("""
            QScrollArea {
                border: 1px solid rgba(0, 0, 0, 0.1);
                border-radius: 8px;
                background: rgba(255, 255, 255, 0.95);
            }
        """)
        self.clear_history_btn = QPushButton()
        self.clear_history_btn.setFixedHeight(40)
        self.clear_history_btn.setFont(QFont("Segoe UI", 12))
        self.clear_history_btn.setStyleSheet("""
            QPushButton {
                border-radius: 8px;
                font-size: 14px;
                border: 1px solid rgba(0, 0, 0, 0.1);
                background: rgba(200, 0, 0, 0.8);
                color: white;
            }
            QPushButton:hover {
                background: rgba(200, 0, 0, 1.0);
            }
        """)
        self.clear_history_btn.clicked.connect(self.clear_history)
        self.history_layout.addWidget(self.history_scroll)
        self.history_layout.addWidget(self.clear_history_btn)

        # Settings tab
        self.settings_tab = QWidget()
        self.settings_layout = QVBoxLayout(self.settings_tab)
        self.settings_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.settings_layout.setSpacing(10)

        self.language_label = QLabel()
        self.language_label.setFont(QFont("Segoe UI", 12))
        self.language_combo = QComboBox()
        self.language_combo.addItems(['English', 'فارسی', '中文', 'Русский'])
        self.language_combo.setFixedHeight(40)
        self.language_combo.setStyleSheet("""
            QComboBox {
                border-radius: 8px;
                padding: 8px;
                font-size: 14px;
                border: 1px solid rgba(0, 0, 0, 0.2);
                background: rgba(255, 255, 255, 0.95);
                color: black;
            }
            QComboBox::drop-down {
                border: none;
            }
        """)
        self.language_combo.currentIndexChanged.connect(self.change_language)

        self.theme_label = QLabel()
        self.theme_label.setFont(QFont("Segoe UI", 12))
        self.theme_combo = QComboBox()
        self.theme_combo.addItems(['Windows', 'Dark', 'Red', 'Blue'])
        self.theme_combo.setFixedHeight(40)
        self.theme_combo.setStyleSheet("""
            QComboBox {
                border-radius: 8px;
                padding: 8px;
                font-size: 14px;
                border: 1px solid rgba(0, 0, 0, 0.2);
                background: rgba(255, 255, 255, 0.95);
                color: black;
            }
            QComboBox::drop-down {
                border: none;
            }
        """)
        self.theme_combo.currentIndexChanged.connect(self.change_theme)

        self.apply_btn = QPushButton()
        self.apply_btn.setFixedHeight(40)
        self.apply_btn.setFont(QFont("Segoe UI", 12))
        self.apply_btn.setStyleSheet("""
            QPushButton {
                border-radius: 8px;
                font-size: 14px;
                border: 1px solid rgba(0, 0, 0, 0.1);
                background: rgba(0, 120, 212, 0.8);
                color: white;
            }
            QPushButton:hover {
                background: rgba(0, 120, 212, 1.0);
            }
        """)
        self.apply_btn.clicked.connect(self.apply_settings)

        self.settings_layout.addWidget(self.language_label)
        self.settings_layout.addWidget(self.language_combo)
        self.settings_layout.addWidget(self.theme_label)
        self.settings_layout.addWidget(self.theme_combo)
        self.settings_layout.addWidget(self.apply_btn)
        self.settings_layout.addStretch()

        # Add tabs
        self.tabs.addTab(self.download_tab, self.texts['en']['history_tab'])
        self.tabs.addTab(self.history_tab, self.texts['en']['history_tab'])
        self.tabs.addTab(self.settings_tab, self.texts['en']['settings_tab'])

        # Load history to UI
        self.update_history_ui()

    def apply_theme(self, theme_name):
        palette = QPalette()
        theme = self.themes.get(theme_name, self.themes['Windows'])
        palette.setColor(QPalette.ColorRole.Window, theme['background'])
        palette.setColor(QPalette.ColorRole.WindowText, theme['text'])
        palette.setColor(QPalette.ColorRole.Button, theme['button'])
        palette.setColor(QPalette.ColorRole.ButtonText, theme['button_text'])
        palette.setColor(QPalette.ColorRole.Highlight, theme['accent'])
        palette.setColor(QPalette.ColorRole.Base, theme['background'])
        palette.setColor(QPalette.ColorRole.AlternateBase, theme['header'])
        palette.setColor(QPalette.ColorRole.Text, theme['text'])
        self.setPalette(palette)
        self.setStyle(QStyleFactory.create('WindowsVista' if theme_name == 'Windows' else 'Fusion'))

    def update_texts(self):
        lang = self.current_lang
        self.setWindowTitle(self.texts[lang]['title'])
        self.url_label.setText(self.texts[lang]['url_label'])
        self.quality_label.setText(self.texts[lang]['quality_label'])
        self.download_btn.setText(self.texts[lang]['download_btn'])
        self.folder_label.setText(self.texts[lang]['default_folder'])
        self.folder_btn.setText(self.texts[lang]['select_folder'])
        self.status_text.setText(self.texts[lang]['status_idle'])
        self.clear_history_btn.setText(self.texts[lang]['clear_history'])
        self.language_label.setText(self.texts[lang]['language_label'])
        self.theme_label.setText(self.texts[lang]['theme_label'])
        self.apply_btn.setText(self.texts[lang]['apply'])
        self.file_menu.setTitle(self.texts[lang]['file_menu'])
        self.exit_action.setText(self.texts[lang]['exit_action'])
        self.about_action.setText(self.texts[lang]['about'])
        self.tabs.setTabText(0, self.texts[lang]['history_tab'])
        self.tabs.setTabText(1, self.texts[lang]['history_tab'])
        self.tabs.setTabText(2, self.texts[lang]['settings_tab'])
        
        # Set text alignment
        alignment = Qt.AlignmentFlag.AlignRight if lang == 'fa' else Qt.AlignmentFlag.AlignLeft
        self.url_label.setAlignment(alignment)
        self.quality_label.setAlignment(alignment)
        self.folder_label.setAlignment(alignment)
        self.language_label.setAlignment(alignment)
        self.theme_label.setAlignment(alignment)

    def change_language(self, index):
        langs = ['en', 'fa', 'zh', 'ru']
        self.current_lang = langs[index]
        self.update_texts()
        self.update_history_ui()

    def change_theme(self, index):
        themes = ['Windows', 'Dark', 'Red', 'Blue']
        self.current_theme = themes[index]
        self.apply_theme(self.current_theme)

    def apply_settings(self):
        self.update_texts()
        self.apply_theme(self.current_theme)

    def show_about(self):
        from PyQt6.QtWidgets import QMessageBox
        QMessageBox.information(self, self.texts[self.current_lang]['about'], 
                               self.texts[self.current_lang]['about_text'])

    def select_folder(self):
        folder = QFileDialog.getExistingDirectory(self, self.texts[self.current_lang]['select_folder'])
        if folder:
            self.folder_input.setText(folder)

    def start_download(self):
        url = self.url_input.text().strip()
        if not url:
            self.status_text.setText(self.texts[self.current_lang]['status_error'].format(error="No URL provided"))
            return

        try:
            yt = YouTube(url, on_progress_callback=self.on_progress)
            self.quality_combo.clear()
            streams = yt.streams.filter(progressive=True, file_extension='mp4')
            for stream in streams:
                self.quality_combo.addItem(f"{stream.resolution} - {stream.mime_type}")
            
            if self.quality_combo.count() == 0:
                self.status_text.setText(self.texts[self.current_lang]['status_error'].format(error="No valid streams found"))
                return

            self.download_btn.setEnabled(False)
            self.folder_btn.setEnabled(False)
            QTimer.singleShot(100, self.download_video)
        except Exception as e:
            self.status_text.setText(self.texts[self.current_lang]['status_error'].format(error=str(e)))
            self.download_btn.setEnabled(True)
            self.folder_btn.setEnabled(True)

    def on_progress(self, stream, chunk, bytes_remaining):
        total_size = stream.filesize
        bytes_downloaded = total_size - bytes_remaining
        percentage = (bytes_downloaded / total_size) * 100
        self.progress_bar.setValue(int(percentage))
        self.status_text.setText(self.texts[self.current_lang]['status_downloading'].format(title=stream.title))

    def download_video(self):
        try:
            yt = YouTube(self.url_input.text().strip())
            stream = yt.streams.filter(progressive=True, file_extension='mp4')[self.quality_combo.currentIndex()]
            folder = self.folder_input.text() or os.path.expanduser("~/Downloads")
            filename = self.sanitize_filename(yt.title) + ".mp4"
            output_path = os.path.join(folder, filename)
            stream.download(output_path=folder, filename=filename)
            self.status_text.setText(self.texts[self.current_lang]['status_complete'].format(title=yt.title))
            self.add_to_history(yt.title, self.url_input.text(), output_path)
            self.download_btn.setEnabled(True)
            self.folder_btn.setEnabled(True)
        except Exception as e:
            self.status_text.setText(self.texts[self.current_lang]['status_error'].format(error=str(e)))
            self.download_btn.setEnabled(True)
            self.folder_btn.setEnabled(True)

    def sanitize_filename(self, filename):
        invalid_chars = '<>:"/\\|?*'
        for char in invalid_chars:
            filename = filename.replace(char, '')
        return filename[:200]  # Limit filename length

    def add_to_history(self, title, url, path):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.download_history.append({
            'title': title,
            'url': url,
            'date': timestamp,
            'path': path
        })
        self.save_history()
        self.update_history_ui()

    def save_history(self):
        with open('download_history.json', 'w', encoding='utf-8') as f:
            json.dump(self.download_history, f, ensure_ascii=False, indent=4)

    def load_history(self):
        try:
            with open('download_history.json', 'r', encoding='utf-8') as f:
                self.download_history = json.load(f)
        except FileNotFoundError:
            self.download_history = []

    def update_history_ui(self):
        # Clear existing widgets
        for i in reversed(range(self.history_grid.count())):
            self.history_grid.itemAt(i).widget().setParent(None)

        # Add headers
        headers = [
            self.texts[self.current_lang]['history_title'],
            self.texts[self.current_lang]['history_url'],
            self.texts[self.current_lang]['history_date'],
            self.texts[self.current_lang]['history_path']
        ]
        for col, header in enumerate(headers):
            label = QLabel(header)
            label.setStyleSheet("font-weight: bold; font-size: 14px; padding: 5px; color: black;")
            label.setAlignment(Qt.AlignmentFlag.AlignRight if self.current_lang == 'fa' else Qt.AlignmentFlag.AlignLeft)
            self.history_grid.addWidget(label, 0, col)

        # Add history items
        for row, item in enumerate(self.download_history, 1):
            title_label = QLabel(item['title'][:50] + ('...' if len(item['title']) > 50 else ''))
            url_label = QLabel(f"<a href='{item['url']}'>{item['url'][:30]}</a>")
            url_label.setOpenExternalLinks(True)
            date_label = QLabel(item['date'])
            path_label = QLabel(item['path'])
            
            for label in [title_label, url_label, date_label, path_label]:
                label.setStyleSheet("font-size: 12px; padding: 5px; border-bottom: 1px solid rgba(0, 0, 0, 0.1); color: black;")
                label.setWordWrap(True)
                label.setAlignment(Qt.AlignmentFlag.AlignRight if self.current_lang == 'fa' else Qt.AlignmentFlag.AlignLeft)
            
            self.history_grid.addWidget(title_label, row, 0)
            self.history_grid.addWidget(url_label, row, 1)
            self.history_grid.addWidget(date_label, row, 2)
            self.history_grid.addWidget(path_label, row, 3)

    def clear_history(self):
        self.download_history = []
        self.save_history()
        self.update_history_ui()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('Windows')
    window = YouTubeDownloader()
    window.show()
    sys.exit(app.exec())