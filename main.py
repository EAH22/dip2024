#! /home/frijol/Desktop/no_recollection/venv/bin python

from time import sleep

import scanner
import transcription
import receipt_printer

def main():

    # Hello World from printer to clean buffer
    receipt_printer.test_print()

    while True:
        try:
            # Try to scan
            success = scanner.scan()
            if success:
                print("Scanned a postcard")

                # ======================================================
                # Send postcard to chatGPT
                # ======================================================

                # (1) Convert scanned image to base64
                base64_image = transcription.encode_image()

                # (2) Ask GPT to extract written text
                gpt_answer = transcription.ask_gpt(base64_image)
                
                print("*************")
                print(gpt_answer)
                print("*************")

                # ======================================================

                # Print answer in receipt
                receipt_printer.print_answer(gpt_answer)    

            else:
                print("Nothing to scan")
            
            # Wait 7 seconds
            print("Pausing for 7s")
            sleep(7)

        except KeyboardInterrupt:
            print("\nKeyboard Interrupt. Exiting gracefully.")
            break

        except Exception as e:
            print("An error occured: ")
            print(e)


if __name__ == "__main__":
    main()