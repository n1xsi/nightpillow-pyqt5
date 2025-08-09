from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout, QApplication
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
        """Размещает виджеты с помощью менеджеров компоновки."""
        # Левая колонка с контролами
        controls_layout = QVBoxLayout()
        controls_layout.setSpacing(10)
        controls_layout.addWidget(self.time_label)
        controls_layout.addWidget(self.time_input)
        controls_layout.addWidget(self.calculate_button)
        controls_layout.addStretch()  # Добавляет пустое растягивающееся пространство снизу

        # Центральная колонка с переключателем
        toggle_layout = QVBoxLayout()
        toggle_layout.addWidget(self.toggle_label)
        toggle_layout.addWidget(self.toggle_switch)
        toggle_layout.addStretch()

        # Правая колонка с результатом
        result_layout = QVBoxLayout()
        result_layout.addSpacing(125)  # Отступ сверху для выравнивания
        result_layout.addWidget(self.result_label)
        result_layout.addStretch()

        # Главный горизонтальный layout
        main_layout = QHBoxLayout(self)
        main_layout.setContentsMargins(20, 50, 20, 20)
        main_layout.addLayout(controls_layout)
        main_layout.addSpacing(20)
        main_layout.addLayout(toggle_layout)
        main_layout.addSpacing(20)
        # stretch=1 заставляет этот layout занять всё доступное место
        main_layout.addLayout(result_layout, stretch=1)

    def _apply_styles(self):
        """Применяет стили к виджетам."""
        # Общие стили для текста
        base_text_style = f"font-family: {constants.FONT_FAMILY}; font-weight: bold; color: {constants.TEXT_COLOR};"

        self.time_label.setStyleSheet(f"{base_text_style} font-size: 16pt;")
        self.toggle_label.setStyleSheet(f"{base_text_style} font-size: 11pt; qproperty-alignment: AlignCenter;")
        self.result_label.setStyleSheet(
            f"{base_text_style} font-size: 12pt; qproperty-alignment: AlignLeft; qproperty-wordWrap: True;")

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
        self.result_label.setFixedWidth(250)
