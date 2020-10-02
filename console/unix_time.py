#!/usr/bin/python3

from PyQt5.QtCore import QDateTime, Qt

now = QDateTime.currentDateTime()

unix_time = now.toSecsSinceEpoch()
print(f"unix_time = {unix_time}")

d = QDateTime.fromSecsSinceEpoch(unix_time)
print(f"QDateTime.fromSecsSinceEpoch {d.toString(Qt.ISODate)}")