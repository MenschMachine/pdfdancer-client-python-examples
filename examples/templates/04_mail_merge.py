"""Working with Templates 04 — Generate multiple documents from a template (mail merge)."""

from pathlib import Path

from pdfdancer import PDFDancer, TemplateReplacement, ReflowPreset


TEMPLATE_PATH = Path("examples/templates/Template.pdf")
OUTPUT_DIR = Path("output/templates/mail_merge")

# Sample data for mail merge
RECIPIENTS = [
    {
        "name": "Alice Johnson",
        "course": "Web Development Fundamentals",
        "date": "January 5, 2026",
        "instructor": "John Smith",
    },
    {
        "name": "Bob Williams",
        "course": "Data Science Essentials",
        "date": "January 6, 2026",
        "instructor": "Sarah Chen",
    },
    {
        "name": "Carol Martinez",
        "course": "Cloud Architecture",
        "date": "January 7, 2026",
        "instructor": "Michael Brown",
    },
]


def run_example(
    pdf_path: Path = TEMPLATE_PATH,
    output_dir: Path = OUTPUT_DIR,
    recipients: list[dict[str, str]] | None = None,
) -> None:
    if not pdf_path.exists():
        raise FileNotFoundError(f"PDF file not found: {pdf_path}")

    recipients = recipients or RECIPIENTS
    output_dir.mkdir(parents=True, exist_ok=True)

    for i, recipient in enumerate(recipients, start=1):
        with PDFDancer.open(pdf_path) as pdf:
            pdf.apply_replacements(
                [
                    TemplateReplacement("{{RECIPIENT_NAME}}", recipient["name"]),
                    TemplateReplacement("{{COURSE_NAME}}", recipient["course"]),
                    TemplateReplacement("{{DATE}}", recipient["date"]),
                    TemplateReplacement("{{INSTRUCTOR}}", recipient["instructor"]),
                ],
                reflow_preset=ReflowPreset.BEST_EFFORT,
            )

            # Generate unique filename for each recipient
            safe_name = recipient["name"].lower().replace(" ", "_")
            output_path = output_dir / f"certificate_{safe_name}.pdf"
            pdf.save(output_path)
            print(f"[{i}/{len(recipients)}] Generated: {output_path}")

    print(f"\nMail merge complete. Generated {len(recipients)} certificates.")


if __name__ == "__main__":
    run_example()
