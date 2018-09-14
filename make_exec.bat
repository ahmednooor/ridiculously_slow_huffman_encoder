pyinstaller gui_main.pyw ^
    --clean ^
    --windowed --noconsole --onefile ^
    --name "File_Compression_Tool" ^
    --icon "./assets/icon.ico" ^
    --paths "C:/Users/Ahmed Noor/AppData/Local/Programs/Python/Python36-32/" ^
    --add-data "huffman_encoder;./huffman_encoder/" ^
    --add-data "assets;./assets/"