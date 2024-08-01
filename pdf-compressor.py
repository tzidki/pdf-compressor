import os
import subprocess
import sys
import urllib.request
import logging

# הגדרת קובץ יומן (log file) ורמת הדיווח
logging.basicConfig(filename='compress_pdfs_log.txt', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def check_ghostscript_installed():
    try:
        result = subprocess.run(['gswin64c', '--version'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        logging.info('Ghostscript check output: ' + result.stdout.decode())
        return result.returncode == 0
    except FileNotFoundError:
        logging.error('Ghostscript not found.')
        return False

def install_ghostscript():
    gs_download_url = "https://github.com/ArtifexSoftware/ghostpdl-downloads/releases/download/gs951/gs951w64.exe"
    local_file_path = os.path.join(os.getcwd(), "gswin64_installer.exe")

    try:
        # הורדת קובץ ההתקנה
        logging.info("Downloading Ghostscript...")
        urllib.request.urlretrieve(gs_download_url, local_file_path)
        logging.info("Ghostscript downloaded.")

        # הרצת קובץ ההתקנה
        logging.info("Installing Ghostscript...")
        subprocess.run(local_file_path, check=True)
        logging.info("Ghostscript installed.")

        # הוספת Ghostscript ל-PATH
        gs_path = r'C:\Program Files\gs\gs9.51\bin'
        if gs_path not in os.environ['PATH']:
            os.environ['PATH'] += os.pathsep + gs_path
            logging.info(f"Added {gs_path} to PATH")

        os.remove(local_file_path)
    except Exception as e:
        logging.error(f"Failed to install Ghostscript: {e}")

def main():
    if not check_ghostscript_installed():
        print("Ghostscript is not installed. Installing now...")
        logging.info("Ghostscript is not installed. Installing now...")
        install_ghostscript()
    else:
        print("Ghostscript is already installed.")
        logging.info("Ghostscript is already installed.")

    # תיקון נתיב הסקריפט
    if getattr(sys, 'frozen', False):
        # אם הקוד מופעל מקובץ EXE שנוצר על ידי PyInstaller
        script_dir = os.path.dirname(sys.executable)
    else:
        script_dir = os.path.dirname(os.path.abspath(__file__))

    folder_path = script_dir
    output_folder = os.path.join(folder_path, 'compressed')
    os.makedirs(output_folder, exist_ok=True)
    print(f"Created output folder at {output_folder}")
    logging.info(f"Created output folder at {output_folder}")

    all_files = os.listdir(folder_path)
    logging.info(f"All files in directory: {all_files}")

    pdf_files = [f for f in all_files if f.lower().endswith('.pdf')]
    total_files = len(pdf_files)
    successful_conversions = 0

    print(f"Found {total_files} PDF files.")
    logging.info(f"Found {total_files} PDF files.")

    for i, filename in enumerate(pdf_files):
        input_path = os.path.join(folder_path, filename)
        output_path = os.path.join(output_folder, filename)
        
        print(f"Processing file: {input_path}")
        logging.info(f"Processing file: {input_path}")

        try:
            ghostscript_path = 'gswin64c.exe'  # מניחים שהפקודה ב-PATH
            command = [
                ghostscript_path,
                '-sDEVICE=pdfwrite',
                '-dCompatibilityLevel=1.4',
                '-dPDFSETTINGS=/screen',  # דחיסה מקסימלית
                '-dNOPAUSE',
                '-dQUIET',
                '-dBATCH',
                f'-sOutputFile={output_path}',
                input_path
            ]
            subprocess.run(command, check=True)
            successful_conversions += 1
            print(f"Compressed {filename}")
            logging.info(f"Compressed {filename}")
        except subprocess.CalledProcessError as e:
            print(f"Error compressing {filename}: {e}")
            logging.error(f"Error compressing {filename}: {e}")
        except FileNotFoundError as fnf_error:
            print(f"File not found error: {fnf_error}")
            logging.error(f"File not found error: {fnf_error}")
        except Exception as e:
            print(f"Unexpected error: {e}")
            logging.error(f"Unexpected error: {e}")

        progress = (i + 1) / total_files * 100
        print(f"Progress: {progress:.2f}% ({i + 1}/{total_files} files)")
        logging.info(f"Progress: {progress:.2f}% ({i + 1}/{total_files} files)")

    print(f"Successfully compressed {successful_conversions}/{total_files} files.")
    logging.info(f"Successfully compressed {successful_conversions}/{total_files} files.")

if __name__ == "__main__":
    main()
