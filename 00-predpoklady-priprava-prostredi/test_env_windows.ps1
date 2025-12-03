# Skript pro kontrolu prostředí - Informatika 4 (Windows)
# Spouštějte v PowerShellu

Write-Host "--- KONTROLA PROSTŘEDÍ PRO INFORMATIKU 4 ---" -ForegroundColor Cyan
Write-Host ""

$all_ok = $true

# 1. Kontrola GIT
Write-Host "[1/4] Kontrola Git..." -NoNewline
try {
    $gitVersion = git --version 2>&1
    Write-Host " OK ($gitVersion)" -ForegroundColor Green
} catch {
    Write-Host " CHYBA! Git nebyl nalezen." -ForegroundColor Red
    Write-Host "      -> Nainstalujte Git z [https://git-scm.com/](https://git-scm.com/)" -ForegroundColor Yellow
    $all_ok = $false
}

# 2. Kontrola VS Code
Write-Host "[2/4] Kontrola VS Code..." -NoNewline
try {
    # code --version vrací více řádků, bereme první
    $codeVersion = (code --version)[0] 2>&1
    if ($LASTEXITCODE -eq 0) {
        Write-Host " OK ($codeVersion)" -ForegroundColor Green
    } else {
        throw
    }
} catch {
    Write-Host " VAROVÁNÍ." -ForegroundColor Yellow
    Write-Host "      -> Příkaz 'code' nebyl nalezen v PATH. Pokud máte VS Code nainstalovaný, je to v pořádku."
    Write-Host "      -> Doporučujeme při instalaci zaškrtnout 'Add to PATH'."
}

# 3. Kontrola Dockeru
Write-Host "[3/4] Kontrola Dockeru..." -NoNewline
try {
    $dockerVersion = docker --version 2>&1
    Write-Host " OK ($dockerVersion)" -ForegroundColor Green
    
    Write-Host "      Zkouším připojení k Docker Daemonovi..." -NoNewline
    $dockerInfo = docker info 2>&1
    if ($LASTEXITCODE -eq 0) {
        Write-Host " OK (Docker běží)" -ForegroundColor Green
    } else {
        Write-Host " CHYBA!" -ForegroundColor Red
        Write-Host "      -> Docker je nainstalovaný, ale neběží (Daemon not running)." -ForegroundColor Yellow
        Write-Host "      -> Spusťte aplikaci 'Docker Desktop'." -ForegroundColor Yellow
        $all_ok = $false
    }

} catch {
    Write-Host " CHYBA! Docker nebyl nalezen." -ForegroundColor Red
    Write-Host "      -> Nainstalujte Docker Desktop." -ForegroundColor Yellow
    $all_ok = $false
}

# 4. Kontrola VirtualBox (volitelné, těžko detekovatelné v PATH někdy)
Write-Host "[4/4] Kontrola VirtualBox..." -NoNewline
try {
    $vboxVersion = VBoxManage --version 2>&1
    Write-Host " OK ($vboxVersion)" -ForegroundColor Green
} catch {
    Write-Host " INFO" -ForegroundColor Gray
    Write-Host "      -> 'VBoxManage' není v PATH. Pokud máte VirtualBox nainstalovaný, je to OK."
}

Write-Host ""
if ($all_ok) {
    Write-Host "VŠE VYPADÁ V POŘÁDKU! JSTE PŘIPRAVENI. ✅" -ForegroundColor Green -BackgroundColor Black
} else {
    Write-Host "NĚKTERÉ NÁSTROJE CHYBÍ NEBO NEFUNGUJÍ. PROSÍM OPRAVTE JE. ❌" -ForegroundColor Red -BackgroundColor Black
}
Read-Host -Prompt "Stiskněte Enter pro ukončení"