# A360 Assistant Engine 서버 시작 스크립트
# 실행: .\start.ps1

# 기존 프로세스 정리
Write-Host "기존 프로세스 정리 중..."
Get-NetTCPConnection -LocalPort 8000 -State Listen -ErrorAction SilentlyContinue |
    Select-Object -ExpandProperty OwningProcess | Sort-Object -Unique |
    ForEach-Object { Stop-Process -Id $_ -Force -ErrorAction SilentlyContinue }

Get-NetTCPConnection -LocalPort 8501 -State Listen -ErrorAction SilentlyContinue |
    Select-Object -ExpandProperty OwningProcess | Sort-Object -Unique |
    ForEach-Object { Stop-Process -Id $_ -Force -ErrorAction SilentlyContinue }

Start-Sleep -Seconds 1

# 백엔드 시작 (포트 8000)
Write-Host "백엔드 시작 중 (포트 8000)..."
$backendDir = "$PSScriptRoot\backend"
Start-Process -FilePath "uvicorn" -ArgumentList "main:app --host 0.0.0.0 --port 8000" `
    -WorkingDirectory $backendDir -WindowStyle Normal

Start-Sleep -Seconds 3

# 프론트엔드 시작 (포트 8501)
Write-Host "프론트엔드 시작 중 (포트 8501)..."
$frontendDir = "$PSScriptRoot\frontend"
Start-Process -FilePath "streamlit" -ArgumentList "run app.py --server.port 8501" `
    -WorkingDirectory $frontendDir -WindowStyle Normal

Start-Sleep -Seconds 4

# 상태 확인
try {
    $health = (Invoke-WebRequest -Uri "http://localhost:8000/health" -UseBasicParsing -TimeoutSec 5).Content
    Write-Host "백엔드: $health" -ForegroundColor Green
} catch {
    Write-Host "백엔드 응답 없음" -ForegroundColor Red
}

try {
    $streamlit = (Invoke-WebRequest -Uri "http://localhost:8501/healthz" -UseBasicParsing -TimeoutSec 5).StatusCode
    Write-Host "Streamlit: HTTP $streamlit" -ForegroundColor Green
} catch {
    Write-Host "Streamlit 응답 없음" -ForegroundColor Red
}

Write-Host ""
Write-Host "서버 시작 완료. Extension 재로드: chrome://extensions/" -ForegroundColor Cyan
