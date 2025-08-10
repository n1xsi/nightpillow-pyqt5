from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QGridLayout
from PyQt5.QtGui import QIcon, QImage, QPalette, QBrush
from PyQt5.QtCore import QSize, Qt
from qtwidgets import AnimatedToggle

from . import constants
from .utils import resource_path


class MainWindow(QWidget):
    """
    Главное окно приложения, отвечающее за отображение всех элементов UI.
    """

    def __init__(self):
        super().__init__()
        self._setup_ui()
        self._create_widgets()
        self._setup_layouts()
        self._apply_styles()

    def _setup_ui(self):
        """Инициализирует основные параметры окна."""
        self.setWindowTitle(constants.APP_TITLE)
        self.setWindowIcon(QIcon(resource_path(constants.ICON_PATH)))
        self.setFixedSize(QSize(constants.WINDOW_WIDTH, constants.WINDOW_HEIGHT))

        background = QImage(resource_path(constants.BG_PATH))
        scaled_bg = background.scaled(self.size(), Qt.IgnoreAspectRatio)
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(scaled_bg))
        self.setPalette(palette)

    def _create_widgets(self):
        """Создает все необходимые виджеты."""
        self.time_label = QLabel(constants.TIME_LABEL)
        self.toggle_label = QLabel(constants.TOGGLE_TEXT_WAKE_UP)

        self.time_input = QLineEdit()
        self.time_input.setPlaceholderText("23:00")

        self.toggle_switch = AnimatedToggle(
            pulse_unchecked_color=constants.SECONDARY_COLOR,
            checked_color=constants.SECONDARY_COLOR,
            pulse_checked_color=constants.TEXT_COLOR
        )

        self.calculate_button = QPushButton(constants.CALCULATE_BUTTON_TEXT)
        self.result_label = QLabel(constants.INITIAL_RESULT_TEXT)

    def _setup_layouts(self):
        """
        Размещает виджеты с помощью сеточного менеджера QGridLayout
        для точного выравнивания.
        """
        # Сеточный layout
        grid_layout = QGridLayout(self)

        # Отступы от краёв окна
        grid_layout.setContentsMargins(18, 55, 20, 20)
        
        # Расстояние между колонками и строками
        grid_layout.setHorizontalSpacing(15)
        grid_layout.setVerticalSpacing(12)

        # Размещение виджетов по сетке (строка, колонка)

        # Строка 0: Текстовые метки
        grid_layout.addWidget(self.time_label, 0, 0, Qt.AlignBottom)
        grid_layout.addWidget(self.toggle_label, 0, 1, Qt.AlignBottom)

        # Строка 1: Поле ввода и переключатель
        grid_layout.addWidget(self.time_input, 1, 0)
        # Выравнивание переключателя по верху его ячейки (чтобы он был на уровне с полем ввода)
        grid_layout.addWidget(self.toggle_switch, 1, 1, Qt.AlignTop)

        # Строка 2: Кнопка и результат
        grid_layout.addWidget(self.calculate_button, 2, 0)
        grid_layout.addWidget(self.result_label, 2, 1, 1, 2, Qt.AlignTop)

        # Настройка поведения сетки

        # Добавляем пустое растягивающееся пространство в последнюю колонку (индекс 2),
        # чтобы прижать все элементы влево и оставить место для картинки.
        grid_layout.setColumnStretch(2, 1)

        # Добавляем растягивающееся пространство в последнюю строку (индекс 3),
        # чтобы прижать все элементы вверх.
        grid_layout.setRowStretch(3, 1)

    def _apply_styles(self):
        """Применяет стили к виджетам."""
        base_text_style = f"font-family: {constants.FONT_FAMILY}; font-weight: bold; color: {constants.TEXT_COLOR};"

        self.time_label.setStyleSheet(f"{base_text_style} font-size: 16pt;")
        self.toggle_label.setStyleSheet(f"{base_text_style} font-size: 11pt; qproperty-alignment: AlignCenter;")
        self.result_label.setStyleSheet(f"{base_text_style} font-size: 12pt; qproperty-wordWrap: True;")

        # Установим минимальную высоту для метки результата, чтобы текст гарантированно поместился
        self.result_label.setMinimumHeight(60)

        self.time_input.setStyleSheet(f"""
            border: 2.5px solid {constants.PRIMARY_COLOR};
            font-family: {constants.FONT_FAMILY};
            font-weight: bold;
            font-size: 15pt;
        """)
        self.time_input.setAlignment(Qt.AlignCenter)
        self.time_input.setFixedSize(*constants.INPUT_SIZE)

        self.calculate_button.setStyleSheet(f"""
            background-color: {constants.PRIMARY_COLOR};
            {base_text_style}
            font-size: 12pt;
        """)
        self.calculate_button.setFixedSize(*constants.BUTTON_SIZE)

        self.toggle_switch.setFixedSize(*constants.TOGGLE_SIZE)
