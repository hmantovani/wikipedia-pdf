import customtkinter as ctk
import os
import pyperclip
import urllib.parse
import threading
from tkinter import filedialog, messagebox
from playwright.sync_api import sync_playwright
from PIL import Image

class WikiPDFDownloaderApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Configurações da Janela
        self.title("Wikipedia PDF Downloader")
        self.geometry("650x600")
        self.is_english = True
        
        self.translations = {
            "en": {
                "title": "Wikipedia to PDF",
                "inst": "1. Paste Wiki links below (one per line)\n2. Or import CSV/TXT files\n3. PDFs save to 'downloads' folder",
                "btn_csv": "Import CSV",
                "btn_txt": "Import TXT",
                "btn_paste": "Paste Clipboard",
                "btn_main": "GENERATE PDFs",
                "status_wait": "Status: Waiting...",
                "status_done": "Success! {} PDF(s) saved.",
                "msg_empty": "Please enter at least one link!",
                "lang_btn": "PT/BR"
            },
            "pt": {
                "title": "Wikipedia para PDF",
                "inst": "1. Cole os links da Wiki abaixo (um por linha)\n2. Ou importe arquivos CSV/TXT\n3. PDFs salvos na pasta 'downloads'",
                "btn_csv": "Importar CSV",
                "btn_txt": "Importar TXT",
                "btn_paste": "Colar Clipboard",
                "btn_main": "GERAR PDFs",
                "status_wait": "Status: Aguardando...",
                "status_done": "Sucesso! {} PDF(s) salvos.",
                "msg_empty": "Por favor, insira pelo menos um link!",
                "lang_btn": "EN/US"
            }
        }

        # Caminho dos Assets (Bandeiras)
        self.base_path = os.path.dirname(os.path.abspath(__file__))
        asset_path = os.path.join(self.base_path, "assets")
        
        try:
            self.img_us = ctk.CTkImage(light_image=Image.open(os.path.join(asset_path, "us.png")), size=(20, 20))
            self.img_br = ctk.CTkImage(light_image=Image.open(os.path.join(asset_path, "br.png")), size=(20, 20))
        except:
            self.img_us = None
            self.img_br = None

        # Interface
        self.lang_button = ctk.CTkButton(self, text="PT/BR", image=self.img_br, compound="right", width=100, command=self.toggle_language)
        self.lang_button.pack(pady=10, padx=20, anchor="ne")

        self.main_label = ctk.CTkLabel(self, text="", font=("Roboto", 24, "bold"))
        self.main_label.pack(pady=10)

        self.inst_label = ctk.CTkLabel(self, text="", font=("Roboto", 12), justify="left")
        self.inst_label.pack(pady=5)

        self.url_textbox = ctk.CTkTextbox(self, width=550, height=200)
        self.url_textbox.pack(pady=10)

        self.file_frame = ctk.CTkFrame(self)
        self.file_frame.pack(pady=10)

        self.btn_csv = ctk.CTkButton(self.file_frame, text="", command=lambda: self.import_file("csv"))
        self.btn_csv.grid(row=0, column=0, padx=10)

        self.btn_txt = ctk.CTkButton(self.file_frame, text="", command=lambda: self.import_file("txt"))
        self.btn_txt.grid(row=0, column=1, padx=10)

        self.btn_paste = ctk.CTkButton(self.file_frame, text="", fg_color="gray", command=self.paste_from_clipboard)
        self.btn_paste.grid(row=0, column=2, padx=10)

        self.download_btn = ctk.CTkButton(self, text="", fg_color="#c92a2a", font=("Roboto", 16, "bold"), height=45, command=self.start_download_thread)
        self.download_btn.pack(pady=20)

        self.status_label = ctk.CTkLabel(self, text="", text_color="gray")
        self.status_label.pack(pady=5)

        self.update_ui_text()

    def toggle_language(self):
        self.is_english = not self.is_english
        self.update_ui_text()

    def update_ui_text(self):
        lang = "en" if self.is_english else "pt"
        data = self.translations[lang]
        self.main_label.configure(text=data["title"])
        self.inst_label.configure(text=data["inst"])
        self.btn_csv.configure(text=data["btn_csv"])
        self.btn_txt.configure(text=data["btn_txt"])
        self.btn_paste.configure(text=data["btn_paste"])
        self.download_btn.configure(text=data["btn_main"])
        self.status_label.configure(text=data["status_wait"])
        self.lang_button.configure(text=data["lang_btn"], image=self.img_br if self.is_english else self.img_us)

    def paste_from_clipboard(self):
        try:
            self.url_textbox.insert("end", pyperclip.paste() + "\n")
        except:
            pass

    def import_file(self, extension):
        file_path = filedialog.askopenfilename(filetypes=[(f"{extension.upper()} files", f"*.{extension}")])
        if file_path:
            with open(file_path, 'r', encoding='utf-8') as f:
                self.url_textbox.insert("end", f.read() + "\n")

    def start_download_thread(self):
        raw_text = self.url_textbox.get("1.0", "end-1c")
        links = [line.strip() for line in raw_text.split('\n') if line.strip()]

        if not links:
            lang = "en" if self.is_english else "pt"
            messagebox.showwarning("Warning", self.translations[lang]["msg_empty"])
            return

        # Desabilita o botão para evitar múltiplos cliques
        self.download_btn.configure(state="disabled")
        threading.Thread(target=self.download_logic, args=(links,), daemon=True).start()

    def download_logic(self, links):
            # Cria a pasta downloads absoluta
            download_folder = os.path.join(self.base_path, "downloads")
            if not os.path.exists(download_folder):
                os.makedirs(download_folder)

            total_links = len(links)
            count = 0
            
            try:
                with sync_playwright() as p:
                    browser = p.chromium.launch(headless=True)
                    page = browser.new_page()

                    for index, url in enumerate(links, start=1):
                        try:
                            decoded_url = urllib.parse.unquote(url)
                            page_title = decoded_url.split("/")[-1].replace("_", " ")
                            
                            # Limpa caracteres que o Windows não aceita em nomes de arquivos
                            for char in '<>:"/\\|?*':
                                page_title = page_title.replace(char, '')
                            
                            # Garante que o nome não seja excessivamente longo
                            page_title = page_title[:100]
                            
                            file_path = os.path.join(download_folder, f"{page_title}.pdf")

                            # ATUALIZAÇÃO: Mostra o contador (ex: 1/10)
                            status_text = f"[{index}/{total_links}] Processing: {page_title[:25]}..."
                            self.status_label.configure(text=status_text, text_color="#339af0")
                            
                            page.goto(url, wait_until="networkidle")
                            page.pdf(path=file_path, format="A4", print_background=True)
                            count += 1
                        except Exception as e:
                            print(f"Error downloading {url}: {e}")

                    browser.close()
            except Exception as e:
                print(f"Playwright Error: {e}")

            # Atualiza a UI ao finalizar
            lang = "en" if self.is_english else "pt"
            self.status_label.configure(text=self.translations[lang]["status_done"].format(count), text_color="#2b8a3e")
            self.download_btn.configure(state="normal")
            messagebox.showinfo("Success", f"All files saved in:\n{download_folder}")

if __name__ == "__main__":
    app = WikiPDFDownloaderApp()
    app.mainloop()