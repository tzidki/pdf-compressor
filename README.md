# PDF Compressor

PDF Compressor is a simple tool to compress PDF files using Ghostscript. It checks if Ghostscript is installed and installs it if necessary, then processes all PDF files in the same directory as the executable.

## Features
- **Automatic Ghostscript Installation:** The tool checks if Ghostscript is installed and installs it if not.
- **PDF Compression:** Compresses PDF files to reduce their size while maintaining quality.
- **Progress Logging:** Logs the progress and any errors encountered during the process.

## Installation

1. **Download the Executable:**
   Download the latest version from the https://github.com/tzidki/pdf-compressor/releases page.

2. **Place PDF Files:**
   Place the PDF files you want to compress in the same directory as the executable.

## Usage

1. **Run the Application:**
   Right-click the executable `pdf-compressor.exe` and select "Run as administrator" to ensure the installation and compression processes have the necessary permissions.

2. **Monitor Progress:**
   The application will display progress and log details to the console and a log file `compress_pdfs_log.txt` in the same directory.

## Requirements

- **Windows OS**
- **Ghostscript:** The application will automatically install it if not already present.

## Contributing

If you would like to contribute, please fork the repository and use a feature branch. Pull requests are welcome.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements

- **Ghostscript:** For providing the core functionality for PDF compression.
- **PyInstaller:** For packaging the Python script into a standalone executable.

## Issues

Please report any issues or bugs you encounter [here](https://github.com/tzidki/pdf-compressor/issues).

## Contact

For any questions, feel free to reach out to etzidi@gmail.com.
