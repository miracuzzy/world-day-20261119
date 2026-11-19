"""Draw the 19 November 2026 world-news collage shipped as entry.png."""
from PIL import Image, ImageDraw, ImageFont
import os

W, H = 1024, 1024

def font(size, bold=False):
    candidates = [
        '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf' if bold else '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',
        '/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf' if bold else '/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf',
    ]
    for p in candidates:
        if os.path.exists(p):
            return ImageFont.truetype(p, size)
    return ImageFont.load_default()

def main():
    img = Image.new('RGB', (W, H), '#0b1220')
    d = ImageDraw.Draw(img)
    f_mast, f_date = font(42, True), font(22, True)
    f_hed, f_sub = font(28, True), font(16, True)
    f_body, f_small, f_label = font(14, False), font(12, False), font(11, True)

    d.rectangle([0, 0, W, 118], fill='#9f1239')
    d.text((24, 18), 'WORLD DAY', font=f_mast, fill='#fff7ed')
    d.text((24, 68), 'Thursday 19 November 2026  ·  one-day world news', font=f_date, fill='#fecdd3')
    d.text((720, 28), 'make.fun', font=f_sub, fill='#fecdd3')
    d.text((720, 52), 'edition', font=f_small, fill='#fda4af')

    d.rectangle([16, 134, 1008, 360], fill='#111827', outline='#334155', width=2)
    d.rectangle([16, 134, 28, 360], fill='#ef4444')
    d.text((44, 148), 'LEAD  ·  SHENZHEN', font=f_label, fill='#f87171')
    d.text((44, 172), 'Trump, Xi and Putin hold historic\ntrilateral on APEC sidelines', font=f_hed, fill='#f8fafc')
    d.text((44, 250),
           'Nuclear arms control and ending the wars in Ukraine and Iran top the agenda.\n'
           'Trump meets Putin first: “Wonderful things can come out of this — or at least start.”\n'
           'Xi greets Trump at the airport ahead of talks; expectations for breakthroughs stay low.',
           font=f_body, fill='#cbd5e1')
    d.text((44, 320),
           'Meanwhile: Crimean Bridge hit again — third attack this week as Ukraine aims to\n'
           'embarrass Putin on the world stage ahead of the summit.',
           font=f_body, fill='#94a3b8')

    stories = [
        ('#b45309', 'GULF', 'Iran drones hit U.S. base in Kuwait',
         'Iran’s army says combat drones struck Ali Al-Salem Air Base after a U.S. raid on Qeshm. Kuwait air defences intercept; CENTCOM: no U.S. personnel wounded. Army chief vows a “more crushing” reply if attacked again.'),
        ('#0369a1', 'MARKETS', 'Anthropic prices record $1.5T IPO',
         'AI giant prices at $83 a share — biggest Wall Street debut on record — as investors still chase AI despite bubble talk and Nvidia leadership drama.'),
        ('#15803d', 'AFRICA', 'DRC Ebola past 6 months, uncontrolled',
         'WHO: outbreak exceeds 11,000 infections and 5,400 deaths. Haiti OHCHR counts 4,595 armed-violence deaths Jan–Oct 2026.'),
        ('#6d28d9', 'U.S.', 'Peltola flips Alaska; Dems 56–44 Senate',
         'Mary Peltola defeats Dan Sullivan, sealing a Democratic Senate majority. Separately: U.S.–Venezuela reestablish military ties in Caracas.'),
        ('#0f766e', 'SPACE', 'Voyager 1 reaches one light-day',
         'NASA: first human-made object one light-day from Earth (~26 billion km) at 05:16 ET Wednesday — reported into Thursday’s news cycle.'),
        ('#be123c', 'MIDDLE EAST', 'Israel rare ground push past Yellow Line',
         'IDF launches rare ground operation in Gaza beyond the Yellow Line; Hamas calls it a ceasefire violation. Myanmar faces genocide verdict at UN court.'),
    ]
    cols, x0, y0, gw, gh, gap = 2, 16, 376, 488, 190, 16
    for i, (color, label, title, body) in enumerate(stories):
        c, r = i % cols, i // cols
        x = x0 + c * (gw + gap)
        y = y0 + r * (gh + gap)
        d.rectangle([x, y, x + gw, y + gh], fill='#0f172a', outline='#1e293b', width=2)
        d.rectangle([x, y, x + 8, y + gh], fill=color)
        d.text((x + 20, y + 12), label, font=f_label, fill=color)
        d.text((x + 20, y + 32), title, font=f_sub, fill='#f1f5f9')
        words, lines, cur = body.split(), [], ''
        for w in words:
            t = (cur + ' ' + w).strip()
            if d.textlength(t, font=f_body) > gw - 40:
                lines.append(cur); cur = w
            else:
                cur = t
        if cur:
            lines.append(cur)
        d.text((x + 20, y + 62), '\n'.join(lines[:5]), font=f_body, fill='#94a3b8')

    d.rectangle([0, 980, W, H], fill='#020617')
    d.text((24, 992),
           '19 November 2026 world news collage  ·  events of / first reported on this day  ·  for make.fun news-image-20261119',
           font=f_small, fill='#64748b')
    out = os.path.join(os.path.dirname(__file__), 'entry.png')
    img.save(out, 'PNG', optimize=True)
    print(out, os.path.getsize(out))

if __name__ == '__main__':
    main()
