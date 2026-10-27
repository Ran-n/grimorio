$state = "$env:TEMP\claude_working.txt"
$frames = @('⠋','⠙','⠹','⠸','⠼','⠴','⠦','⠧','⠇','⠏')

if (Test-Path $state) {
    $tick = [int]((Get-Date).TimeOfDay.TotalMilliseconds / 120) % $frames.Length
    $label = Get-Content $state -Raw 2>$null
    $label = if ($label) { $label.Trim() } else { "Working" }
    Write-Output "$($frames[$tick]) $label"
} else {
    Write-Output ""
}
