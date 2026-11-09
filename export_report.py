"""Сборка отчета через nbconvert с учетом запуска Chromium в Windows."""

import asyncio
import sys
from pathlib import Path
from nbconvert.nbconvertapp import NbConvertApp

folder = Path(__file__).resolve().parent
app = NbConvertApp()
app.initialize([
    "--to", "webpdf", "--no-input", "--execute", str(folder / "02_report.ipynb"),
    "--output", "report.pdf", "--output-dir", str(folder)
])

# В Windows стандартный цикл nbconvert не поддерживает запуск Chromium.
if sys.platform == "win32":
    asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())

app.start()
