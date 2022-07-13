import subprocess

subprocess.call(r"pyInstaller --onefile --name Projectile_Sim --add-data source.exe;. --icon=cannon_ball.ico --clean main.py")
