from kivymd.uix.snackbar import Snackbar

class QRCodeModel:
    def handle_symbols(self, instance, symbols):
        if not symbols == "":
            for symbol in symbols:
                data = symbol.data.decode()

                print("Your QR is:", data)

                Snackbar(
                    text="Your QR is: {}".format(data),
                    md_bg_color="green",
                    font_size=25
                ).open()
