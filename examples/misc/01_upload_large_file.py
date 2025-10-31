import time

from pdfdancer import PDFDancer


def run_example():
    start = time.time()
    with PDFDancer.open("examples/ISO 32000-2 FDIS.pdf", timeout=120) as pdf:
        end = time.time()
        print(f"Uploading time: {end - start:.3f} seconds")
        start = time.time()
        try:
            pdf.save("large-file.pdf")
        finally:
            end = time.time()
            print(f"Saving time: {end - start:.3f} seconds")


if __name__ == "__main__":
    run_example()
