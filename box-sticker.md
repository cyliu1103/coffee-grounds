# Box sticker

Print-and-stick sheet for the coffee grounds collection box.

## Print

```bash
python3 -m http.server 8000
```

Open <http://localhost:8000/box-sticker.html>, then **Print → Save as PDF**.

The page is already sized to 100 × 100 mm with no margins, so it should come out
at exactly 100 mm square. Print **Actual size** (not "Fit to page") and make sure
**Scale** is 100% with margins set to *None*.

Sticker stock: matte, non-glossy, tear-resistant vinyl — a laminated sheet or a
sticker printer if the box gets wiped down regularly.

## Copy on the sticker

> **Coffee Grounds**
>
> If the coffee knock box is full, please empty it here.
>
> *Scan to learn more*
>
> Chen will collect it and feed his worm farm.
> Grounds only, please — no lids, pods or stirrers.

The wording is deliberately short: it's read from a metre or two away, often
while holding a coffee. The instruction comes first, the reason for collecting
second, and the detail that people get wrong (plastics) sits last in the
smallest type.

## Why 100 mm

- Fits an A4 sheet 4-up without wasting paper
- QR stays above ~25 mm wide, which scans reliably from about 40 cm
- Small enough to sit on the front of a bin lid without dominating it

The QR encodes **https://cyliu1103.github.io/coffee-grounds/** at error
correction **H** (~30% recoverable), so it still scans if the sticker gets
scratched, dusty or partly covered.

## Regenerating the QR

`assets/box-qr.png` is checked in. To rebuild it after the URL changes:

```bash
curl -sS -o assets/box-qr.png \
  "https://api.qrserver.com/v1/create-qr-code/?data=https%3A%2F%2Fcyliu1103.github.io%2Fcoffee-grounds%2F&size=600x600&margin=8&ecc=H"
```

Verify it decodes to the right address before printing:

```bash
curl -sS -F "file=@assets/box-qr.png" "https://api.qrserver.com/v1/read-qr-code/"
```

Keep the white border around the code — that's the quiet zone. Without it most
cameras fail to lock on. The page gives it 6 mm of white on every side.

## A/B test it

Tape the sticker up, then scan it with three different phones before committing
to a full print run. Scanner quality varies more than you'd expect, and a QR that
works on your phone can still fail on someone else's.