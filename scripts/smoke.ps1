param(
  [Parameter(Mandatory=$true)][string]$Url,
  [int]$Tries = 20,
  [int]$DelaySeconds = 3
)

Write-Host "Smoke testing $Url ..."
for ($i=1; $i -le $Tries; $i++) {
  try {
    $res = Invoke-WebRequest -UseBasicParsing -TimeoutSec 5 -Uri $Url
    if ($res.StatusCode -ge 200 -and $res.StatusCode -lt 300) {
      Write-Host "OK ($($res.StatusCode))"
      $res.Content | Write-Output
      exit 0
    }
  } catch {}
  Start-Sleep -Seconds $DelaySeconds
  Write-Host "Retry $i/$Tries ..."
}
Write-Error "Smoke test failed for $Url"
exit 1

