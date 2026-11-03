# Developer: Hamdy Abou El Anein
# Contact: hamdy.aea@protonmail.com
import os
os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")
import unittest
from unittest.mock import patch
from PyQt6.QtWidgets import QApplication
from PyQt6.QtTest import QTest
from Chapitre13.threadSimple import MainWindow
from Chapitre13.threadsCommunication import MyWidget
from Chapitre15.toDoList import MainWindow as Tasks


class WidgetTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = QApplication.instance() or QApplication([])

    def test_blank_task_ignored(self):
        window = Tasks()
        self.addCleanup(window.close)
        window.task_input.setText("  ")
        window.add_task()
        self.assertEqual(window.task_list.count(), 0)
        window.task_input.setText(" example ")
        window.add_task()
        self.assertEqual(window.task_list.item(0).text(), "example")

    def test_simple_worker_can_close_while_running(self):
        window = MainWindow()
        window.lancer_thread()
        window.close()
        self.assertFalse(window.mon_thread.isRunning())

    def test_worker_can_restart(self):
        window = MyWidget()
        self.addCleanup(window.close)
        with patch("Chapitre13.threadsCommunication.time.sleep", return_value=None):
            for _ in range(2):
                window.start_thread()
                for tick in range(200):
                    QTest.qWait(5)
                    if not window.thread.isRunning():
                        break
                self.assertFalse(window.thread.isRunning())
                self.assertTrue(window.button.isEnabled())
                self.assertEqual(window.label.text(), "100%")

    def test_communication_worker_can_close(self):
        window = MyWidget()
        window.start_thread()
        window.close()
        self.assertFalse(window.thread.isRunning())


if __name__ == "__main__":
    unittest.main()
