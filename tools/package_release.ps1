$ErrorActionPreference = 'Stop'
$RepoRoot = Split-Path -Parent $PSScriptRoot
$ReleaseDir = Join-Path $RepoRoot 'release'
$OutZip = Join-Path $ReleaseDir 'RoughCut_26.2_DROP_0001_pack.zip'

New-Item -ItemType Directory -Force -Path $ReleaseDir | Out-Null

if (Get-Command python -ErrorAction SilentlyContinue) {
    & python (Join-Path $PSScriptRoot 'validate_pack.py')
    if ($LASTEXITCODE -ne 0) { throw 'Validation failed.' }
}

if (Test-Path $OutZip) { Remove-Item $OutZip -Force }
Compress-Archive -Path `
    (Join-Path $RepoRoot 'pack.mcmeta'), `
    (Join-Path $RepoRoot 'pack.png'), `
    (Join-Path $RepoRoot 'assets') `
    -DestinationPath $OutZip -CompressionLevel Optimal

Write-Host "Created: $OutZip" -ForegroundColor Green
