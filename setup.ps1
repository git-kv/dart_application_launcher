$main_folder = "C:\Program Files\Dart Applications"
$dart_application_launcher_folder = "C:\Program Files\Dart Applications\Dart Application Launcher"
$dart_application_launcher_assets_folder = "C:\Program Files\Dart Applications\Dart Application Launcher\assets"

$source_ps2exe_executables_path = "./ps2exe_executables/*"
$source_assets_path = "./dart_app_launcher/assets/*"
$source_application_launcher_exe = "./dart_app_launcher/dist/dart_application_launcher.exe"

if (-not (Test-Path -Path $main_folder)) { New-Item -Path $main_folder -ItemType Directory -Force}

if (-not (Test-Path -Path $dart_application_launcher_folder)) { New-Item -Path $dart_application_launcher_folder -ItemType Directory -Force}

if (-not (Test-Path -Path $dart_application_launcher_assets_folder)) { New-Item -Path $dart_application_launcher_assets_folder -ItemType Directory -Force}

Copy-Item $source_ps2exe_executables_path $main_folder

Copy-Item $source_assets_path $dart_application_launcher_assets_folder

Copy-Item $source_application_launcher_exe $dart_application_launcher_folder