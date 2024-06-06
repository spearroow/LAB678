if (-not (Get-Command python -ErrorAction SilentlyContinue)) {
    Write-Host "Python nie jest zainstalowany. Instalacja..."
    Invoke-WebRequest -Uri https://www.python.org/ftp/python/3.9.5/python-3.9.5-amd64.exe -OutFile python-installer.exe
    Start-Process -FilePath python-installer.exe -ArgumentList '/quiet InstallAllUsers=1 PrependPath=1' -Wait
    Remove-Item -Force python-installer.exe
} else {
    Write-Host "Python jest już zainstalowany."
}

if (-not (Get-Command pip -ErrorAction SilentlyContinue)) {
    Write-Host "pip nie jest zainstalowany. Instalacja..."
    Invoke-WebRequest -Uri https://bootstrap.pypa.io/get-pip.py -OutFile get-pip.py
    python get-pip.py
    Remove-Item -Force get-pip.py
} else {
    Write-Host "pip jest już zainstalowany."
}

Write-Host "Instalacja PyInstaller..."
pip install pyinstaller

Write-Host "Budowanie pliku .exe..."
pyinstaller --onefile main.py

