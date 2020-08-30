from cx_Freeze import setup, Executable

setup( name='Voice-Assistant News bot setup',
       version='3.0',
       author='SANJAY KUMAR',
       description='This application only operates through voice-commands.',
       executables=[Executable(r'C:\Users\sanju\OneDrive\Desktop\IIC contest\news_feeder.py',
                                icon=r'C:\Users\sanju\OneDrive\Desktop\IIC contest\favicon2.ico',
                                shortcutName="Voice-Assistant News Bot",shortcutDir='DesktopFolder')]
    )