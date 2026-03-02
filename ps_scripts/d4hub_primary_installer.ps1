<#
    .SYNOPSIS
    This script simply copies D4K Primary files into a location in the
    user's local appdata so that D4K can be rapidly updated and allows
    D4K's files to be quickly updated by rerunning this script.
#>

# Get user's username
$username = $env:USERNAME

# Declare source and destination directories
$source = "\\eocservices.dartadvantage.com\apps$\programs\d4hub\pb22\primary\push"
$destination = "C:\Users\$username\AppData\Local\Dart Applications\D4Hub\PB22\Primary"
$app_path = "C:\Users\$username\AppData\Local\Dart Applications\D4Hub\PB22\Primary\d4hub.exe"

# Mirror files in source to destination
robocopy $source $destination /MIR

# Launch application after install
Start-Process -FilePath $app_path