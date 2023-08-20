from kivymd.uix.snackbar import Snackbar

class QRCodeModel:
    """Handles QR code data and related logic."""

    def handle_symbols(self, instance, symbols):
        """
        Handle QR code symbols and display related information using a Snackbar.

        Parameters:
            instance: The instance of the QR code widget that triggered the event.
            symbols (list): List of QR code symbols detected.
        """
        if not symbols == "":
            for symbol in symbols:
                data = symbol.data.decode()

                print("Your QR is:", data)

                Snackbar(
                    text="Your QR is: {}".format(data),
                    md_bg_color="green",
                    font_size=25
                ).open()
