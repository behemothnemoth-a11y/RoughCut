$ErrorActionPreference = "Stop"
$Repo = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)
$Release = Join-Path $Repo "release"
New-Item -ItemType Directory -Force -Path $Release | Out-Null
$Out = Join-Path $Release "RoughCut_26.2_DROP_0003_pack.zip"
if (Test-Path $Out) { Remove-Item $Out -Force }
Compress-Archive -Path (Join-Path $Repo "pack.mcmeta"), (Join-Path $Repo "pack.png"), (Join-Path $Repo "assets") -DestinationPath $Out -Force
Write-Host "Created $Out" -ForegroundColor Green
