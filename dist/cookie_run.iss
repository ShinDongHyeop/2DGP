; Script generated by the Inno Setup Script Wizard.
; SEE THE DOCUMENTATION FOR DETAILS ON CREATING INNO SETUP SCRIPT FILES!

[Setup]
; NOTE: The value of AppId uniquely identifies this application.
; Do not use the same AppId value in installers for other applications.
; (To generate a new GUID, click Tools | Generate GUID inside the IDE.)
AppId={{7320C56F-81C6-41D5-BDE3-C994633545B8}
AppName=Cookie_Run
AppVersion=1.5
;AppVerName=Cookie_Run 1.5
AppPublisher=KPU
AppPublisherURL=http://www.kpu.ac.kr
AppSupportURL=http://www.kpu.ac.kr
AppUpdatesURL=http://www.kpu.ac.kr
DefaultDirName={pf}\Cookie_Run
DisableProgramGroupPage=yes
OutputDir=C:\Users\1\Desktop
OutputBaseFilename=setup
Compression=lzma
SolidCompression=yes

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

[Files]
Source: "C:\Users\1\Documents\GitHub\2DGP\dist\mygame.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\1\Documents\GitHub\2DGP\dist\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs
; NOTE: Don't use "Flags: ignoreversion" on any shared system files

[Icons]
Name: "{commonprograms}\Cookie_Run"; Filename: "{app}\mygame.exe"
Name: "{commondesktop}\Cookie_Run"; Filename: "{app}\mygame.exe"; Tasks: desktopicon

[Run]
Filename: "{app}\mygame.exe"; Description: "{cm:LaunchProgram,Cookie_Run}"; Flags: nowait postinstall skipifsilent
