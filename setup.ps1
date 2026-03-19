$main_folder = "C:\Program Files\Dart Applications"
$dart_application_launcher_folder = "C:\Program Files\Dart Applications\Dart Application Launcher"
$dart_application_launcher_assets_folder = "C:\Program Files\Dart Applications\Dart Application Launcher\assets"
$dart_applications_start_menu_folder = "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Dart Applications"

$source_ps2exe_executables_path = "./ps2exe_executables/*"
$source_start_menu_shortcuts = "./start_menu_shortcuts/*"
$source_assets_path = "./dart_app_launcher/assets/*"
$source_application_launcher_exe = "./dart_app_launcher/dist/dart_application_launcher.exe"

$shortcut = "./Dart Application Launcher.lnk"

$desktop = "C:\Users\Public\Desktop"
$startup = "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup"
$start_menu = "C:\ProgramData\Microsoft\Windows\Start Menu\Programs"

if (-not (Test-Path -Path $main_folder)) { New-Item -Path $main_folder -ItemType Directory -Force}

if (-not (Test-Path -Path $dart_application_launcher_folder)) { New-Item -Path $dart_application_launcher_folder -ItemType Directory -Force}

if (-not (Test-Path -Path $dart_application_launcher_assets_folder)) { New-Item -Path $dart_application_launcher_assets_folder -ItemType Directory -Force}

if (-not (Test-Path -Path $dart_applications_start_menu_folder)) {New-Item -Path $dart_applications_start_menu_folder -ItemType Directory -Force}

Copy-Item $source_ps2exe_executables_path $main_folder -Force

Copy-Item $source_assets_path $dart_application_launcher_assets_folder -Force

Copy-Item $source_application_launcher_exe $dart_application_launcher_folder -Force

Copy-Item $source_start_menu_shortcuts $dart_applications_start_menu_folder -Force

Copy-Item $shortcut $desktop -Force
Copy-Item $shortcut $startup -Force