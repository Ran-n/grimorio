$Flag = $args[0]
$File = $args[1]

if (-not $Flag) {
    $Flag = '-h'
}

$action = @{ '-v' = 'show'; '-m' = 'edit'; '-c' = 'create'; '-d' = 'remove' }[$Flag]

if ($Flag -eq '-h') {
    $action = 'help'
} elseif (-not $action) {
    Write-Error "Unknown flag: $Flag"
    exit 1
} elseif (-not $File) {
    Write-Error "Missing file argument"
    exit 1
}


# the logic lives in metadata_core.py beside this script (shared with metadata.bat)
python (Join-Path $PSScriptRoot "metadata_core.py") $action $File
