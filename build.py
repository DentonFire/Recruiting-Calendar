import html, json
from content import MONTHS, FLEX_TOPICS, TOOLS, FLEX_STANDING, ARCHIVE

def esc(s): return html.escape(s, quote=True)

# ---------- CSS ----------
CSS = r"""
* { box-sizing: border-box; margin: 0; padding: 0; }
html { scroll-behavior: smooth; }
:root {
  --navy: #152a40; --navy-light: #1e3a5c; --red: #bf2726; --yellow: #f9c031; --green: #28a745;
  --gray-50: #f9fafb; --gray-100: #f3f4f6; --gray-200: #e5e7eb; --gray-500: #6b7280; --gray-700: #374151; --gray-900: #111827;
  --fb: #1877f2; --li: #0a66c2; --x: #111827;
}
body { font-family: 'Inter', Arial, sans-serif; background-color: var(--gray-100); color: var(--gray-700); line-height: 1.6; }
.container { max-width: 1100px; margin: 32px auto; background-color: #fff; border-radius: 1rem; overflow: hidden; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1); }

/* HERO */
.hero { background-color: var(--navy); background-image: url('https://www.transparenttextures.com/patterns/cubes.png'); background-repeat: repeat; color: #fff; text-align: center; padding: 64px 32px; }
.hero-logo { height: 140px; width: auto; margin: 0 auto 24px; display: block; filter: drop-shadow(0 10px 8px rgba(0,0,0,0.2)); }
.hero-kicker { font-size: .85rem; font-weight: 600; letter-spacing: 3px; text-transform: uppercase; color: var(--yellow); margin-bottom: 8px; }
.hero-title { font-size: 3rem; font-weight: 900; line-height: 1.05; color: #fff; margin-bottom: 4px; }
.hero-subtitle { font-size: 1rem; color: var(--yellow); font-weight: 700; margin-bottom: 24px; }
.hero-pill { display: inline-block; background-color: var(--yellow); border-radius: 6px; padding: 10px 24px; }
.hero-pill p { margin: 0; font-size: .95rem; font-weight: 700; color: var(--navy); }

/* BANNER */
.banner { background-color: var(--red); padding: 16px 32px; text-align: center; }
.banner p { margin: 0; font-size: .95rem; font-weight: 700; color: #fff; }

/* INTRO */
.intro { padding: 48px 32px 24px; }
.intro-title { font-size: 1.75rem; font-weight: 900; color: var(--navy); margin-bottom: 16px; }
.intro p { font-size: 1.1rem; line-height: 1.7; color: var(--gray-700); margin-bottom: 16px; }
.intro p:last-child { margin-bottom: 0; }

/* CYCLE STRIP */
.cycle { padding: 8px 32px 40px; }
.cycle-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 12px; }
.cycle-card { background: var(--gray-50); border: 1px solid var(--gray-200); border-top: 4px solid var(--yellow); border-radius: 10px; padding: 16px 18px; }
.cycle-card.red { border-top-color: var(--red); }
.cycle-label { font-size: .7rem; font-weight: 700; letter-spacing: 1.5px; text-transform: uppercase; color: var(--red); margin-bottom: 4px; }
.cycle-value { font-size: 1.15rem; font-weight: 900; color: var(--navy); line-height: 1.2; }
.cycle-note { font-size: .82rem; color: var(--gray-500); margin-top: 4px; }
.update-flag { display: inline-block; font-size: .65rem; font-weight: 800; letter-spacing: 1px; text-transform: uppercase; color: var(--navy); background: var(--yellow); border-radius: 4px; padding: 2px 8px; margin-left: 8px; vertical-align: middle; }

/* SCHEDULE + PLATFORM GUIDELINES */
.schedule { padding: 0 32px 40px; }
.section-kicker { font-size: .85rem; font-weight: 700; letter-spacing: 2px; text-transform: uppercase; color: var(--red); margin-bottom: 20px; }
.sched-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 12px; margin-bottom: 20px; }
.sched-card { border-radius: 10px; padding: 18px; color: #fff; background: var(--navy); }
.sched-card.news { background: var(--navy); }
.sched-card.fb { background: var(--fb); }
.sched-card.li { background: var(--li); }
.sched-card.x { background: var(--x); }
.sched-day { font-size: .7rem; font-weight: 800; letter-spacing: 1.5px; text-transform: uppercase; opacity: .85; }
.sched-name { font-size: 1.15rem; font-weight: 900; margin: 2px 0 6px; }
.sched-desc { font-size: .85rem; line-height: 1.5; opacity: .92; }
.guide-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 12px; }
.guide-card { border: 1px solid var(--gray-200); border-radius: 10px; padding: 18px 20px; background: #fff; }
.guide-head { display: flex; align-items: center; gap: 10px; margin-bottom: 8px; }
.guide-name { font-size: 1rem; font-weight: 800; color: var(--navy); }
.guide-card p { font-size: .88rem; line-height: 1.55; margin-bottom: 6px; }
.guide-card p:last-child { margin-bottom: 0; }
.guide-card strong { color: var(--navy); }

/* YEAR GRID */
.year-overview { padding: 0 32px 48px; }
.overview-title { font-size: .85rem; font-weight: 700; letter-spacing: 2px; text-transform: uppercase; color: var(--red); margin-bottom: 20px; }
.month-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 12px; }
.month-card { background-color: var(--navy); color: #fff; padding: 20px 16px; border-radius: 10px; text-decoration: none; transition: transform .2s cubic-bezier(.2,.8,.2,1), box-shadow .2s cubic-bezier(.2,.8,.2,1), border-color .2s ease; cursor: pointer; border: 2px solid transparent; position: relative; overflow: hidden; }
.month-card:hover { transform: translateY(-3px) scale(1.01); box-shadow: 0 10px 20px rgba(21,42,64,.25); border-color: var(--yellow); }
.month-card.current { border-color: var(--yellow); box-shadow: 0 0 0 2px var(--yellow); }
.month-card.current::after { content: "THIS MONTH"; position: absolute; top: 10px; right: -28px; background-color: var(--red); color: #fff; font-size: .6rem; font-weight: 800; letter-spacing: 1px; padding: 3px 32px; transform: rotate(35deg); box-shadow: 0 2px 4px rgba(0,0,0,.2); }
.month-num { font-size: .75rem; font-weight: 700; letter-spacing: 2px; color: var(--yellow); }
.month-name { font-size: 1.2rem; font-weight: 800; color: #fff; margin: 4px 0 8px; }
.month-theme { font-size: .85rem; color: #c7d2dd; line-height: 1.4; }
.month-card.winter { border-left: 4px solid #60a5fa; }
.month-card.spring { border-left: 4px solid #86efac; }
.month-card.summer { border-left: 4px solid var(--red); }
.month-card.fall { border-left: 4px solid var(--yellow); }

/* MONTH SECTIONS */
.month-section { padding: 40px 32px 32px; border-top: 1px solid var(--gray-200); }
.month-header { display: flex; align-items: center; gap: 20px; margin-bottom: 24px; }
.month-number-badge { background-color: var(--navy); color: var(--yellow); font-size: 1.75rem; font-weight: 900; width: 64px; height: 64px; border-radius: 12px; display: flex; align-items: center; justify-content: center; flex-shrink: 0; }
.month-header-content { flex: 1; }
.month-title-small { font-size: .8rem; font-weight: 700; letter-spacing: 2px; text-transform: uppercase; color: var(--red); }
.month-title { font-size: 1.75rem; font-weight: 900; color: var(--navy); line-height: 1.2; margin-top: 2px; }
.month-focus { font-size: .9rem; color: var(--gray-500); margin-top: 4px; }
.month-actions { display: flex; gap: 8px; flex-shrink: 0; }
.hazard-basis { background-color: var(--gray-50); border-left: 4px solid var(--yellow); padding: 20px 24px; border-radius: 6px; margin-bottom: 24px; }
.hazard-basis-label { font-size: .75rem; font-weight: 700; letter-spacing: 2px; text-transform: uppercase; color: var(--navy); margin-bottom: 6px; }
.hazard-basis p { font-size: .95rem; line-height: 1.6; color: var(--gray-700); margin: 0; }

.week-grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 14px; margin-bottom: 20px; }
.week-card { background-color: #fff; border: 1px solid var(--gray-200); border-radius: 10px; padding: 20px; transition: border-color .15s ease; display: flex; flex-direction: column; }
.week-card:hover { border-color: var(--navy); }
.week-header { display: flex; align-items: center; gap: 10px; margin-bottom: 10px; }
.week-number { background-color: var(--yellow); color: var(--navy); font-size: .7rem; font-weight: 800; letter-spacing: 1px; text-transform: uppercase; padding: 4px 10px; border-radius: 4px; white-space: nowrap; }
.week-focus { font-size: 1rem; font-weight: 700; color: var(--navy); flex: 1; }
.week-angle { font-size: .9rem; line-height: 1.5; color: var(--gray-700); }

/* POSTS */
.posts { margin-top: 14px; border-top: 1px dashed var(--gray-200); padding-top: 12px; display: flex; flex-direction: column; gap: 10px; }
.post { display: grid; grid-template-columns: 74px 1fr auto; gap: 10px; align-items: start; }
.post-tag { font-size: .65rem; font-weight: 800; letter-spacing: 1px; text-transform: uppercase; color: #fff; border-radius: 4px; padding: 4px 0; text-align: center; margin-top: 2px; }
.post-tag.fb { background: var(--fb); } .post-tag.li { background: var(--li); } .post-tag.x { background: var(--x); }
.post-day { display: block; font-size: .55rem; font-weight: 700; opacity: .85; letter-spacing: .5px; }
.post-text { font-size: .86rem; line-height: 1.5; color: var(--gray-700); }
.post-meta { font-size: .68rem; color: var(--gray-500); margin-top: 2px; }
.post-meta.over { color: var(--red); font-weight: 700; }
.copy-btn { border: 1px solid var(--gray-200); background: #fff; color: var(--navy); font-family: inherit; font-size: .68rem; font-weight: 800; letter-spacing: 1px; text-transform: uppercase; padding: 6px 10px; border-radius: 6px; cursor: pointer; transition: background .15s, color .15s, border-color .15s; white-space: nowrap; }
.copy-btn:hover { background: var(--navy); color: var(--yellow); border-color: var(--navy); }
.copy-btn.done { background: var(--green); color: #fff; border-color: var(--green); }
.copy-btn.ghost { background: transparent; border-color: rgba(255,255,255,.4); color: #fff; }
.copy-btn.ghost:hover { background: var(--yellow); color: var(--navy); border-color: var(--yellow); }
.copy-btn.month { border-color: var(--navy); }

/* TOOL CONNECTION */
.tool-connection { background-color: #EFF6FF; border: 1px solid #BFDBFE; border-radius: 10px; padding: 16px 20px; display: flex; align-items: center; gap: 12px; }
.tool-connection-icon { background-color: var(--navy); color: var(--yellow); width: 40px; height: 40px; border-radius: 8px; display: flex; align-items: center; justify-content: center; font-size: 1.1rem; flex-shrink: 0; }
.tool-connection-content { flex: 1; }
.tool-connection-label { font-size: .7rem; font-weight: 700; letter-spacing: 1.5px; text-transform: uppercase; color: var(--navy); margin-bottom: 2px; }
.tool-connection-text { font-size: .9rem; color: var(--gray-700); margin: 0; }
.tool-connection-text a { color: var(--red); font-weight: 700; text-decoration: none; border-bottom: 2px solid transparent; transition: border-color .15s ease; }
.tool-connection-text a:hover { border-color: var(--red); }

/* FLEX BANK */
.flex-bank { padding: 40px 32px 48px; border-top: 1px solid var(--gray-200); }
.flex-intro { font-size: 1rem; line-height: 1.7; margin-bottom: 20px; }
.flex-table { width: 100%; border-collapse: collapse; font-size: .9rem; }
.flex-table th { background: var(--navy); color: #fff; text-align: left; font-size: .72rem; letter-spacing: 1.5px; text-transform: uppercase; padding: 10px 14px; }
.flex-table td { padding: 12px 14px; border-bottom: 1px solid var(--gray-200); vertical-align: top; }
.flex-table tr:nth-child(even) td { background: var(--gray-50); }
.flex-table td:first-child { font-weight: 800; color: var(--navy); white-space: nowrap; }

/* ARCHIVE */
.archive { padding: 40px 32px 48px; border-top: 1px solid var(--gray-200); }
.archive-intro { font-size: 1rem; line-height: 1.7; margin-bottom: 20px; }
.archive-list { display: flex; flex-direction: column; gap: 12px; }
.archive-item { display: grid; grid-template-columns: 130px 1fr auto; gap: 16px; align-items: start; border: 1px solid var(--gray-200); border-radius: 10px; padding: 16px 18px; background: #fff; }
.archive-when { font-size: .72rem; font-weight: 800; letter-spacing: 1px; text-transform: uppercase; color: var(--red); padding-top: 3px; }
.archive-title { font-size: 1rem; font-weight: 800; color: var(--navy); margin-bottom: 4px; }
.archive-take { font-size: .88rem; line-height: 1.55; color: var(--gray-700); }
.archive-link { font-size: .7rem; font-weight: 800; letter-spacing: 1.5px; text-transform: uppercase; color: var(--red); text-decoration: none; white-space: nowrap; padding-top: 4px; }
.archive-link:hover { text-decoration: underline; }
.status { display: inline-block; font-size: .62rem; font-weight: 800; letter-spacing: 1px; text-transform: uppercase; border-radius: 4px; padding: 2px 8px; margin-left: 8px; vertical-align: middle; }
.status.evergreen { background: #dcfce7; color: #166534; }
.status.dated { background: var(--gray-200); color: var(--gray-700); }
.status.partly { background: #fef3c7; color: #92400e; }
.standing-head { font-size: .8rem; font-weight: 800; letter-spacing: 1.5px; text-transform: uppercase; color: var(--navy); margin: 28px 0 12px; }

/* NOTES */
.notes { padding: 40px 32px 48px; border-top: 1px solid var(--gray-200); }
.notes ol { padding-left: 22px; }
.notes li { font-size: .95rem; line-height: 1.6; margin-bottom: 8px; }

/* TOOLS SECTION */
.tools-section { background-color: var(--navy); background-image: url('https://www.transparenttextures.com/patterns/cubes.png'); background-repeat: repeat; padding: 56px 32px; color: #fff; }
.tools-section-kicker { font-size: .85rem; font-weight: 700; letter-spacing: 3px; text-transform: uppercase; color: var(--yellow); text-align: center; margin-bottom: 8px; }
.tools-section-title { font-size: 2.2rem; font-weight: 900; text-align: center; margin-bottom: 12px; color: #fff; }
.tools-section-subtitle { font-size: 1rem; text-align: center; color: #c7d2dd; margin-bottom: 36px; max-width: 640px; margin-left: auto; margin-right: auto; }
.tools-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 14px; max-width: 1000px; margin: 0 auto; }
.tool-card { background-color: #fff; border-radius: 12px; padding: 22px 18px; text-decoration: none; display: flex; flex-direction: column; transition: transform .2s ease, box-shadow .2s ease; border-top: 4px solid var(--yellow); }
.tool-card:hover { transform: translateY(-4px); box-shadow: 0 12px 24px rgba(0,0,0,.25); }
.tool-card-icon { font-size: 2rem; margin-bottom: 10px; line-height: 1; }
.tool-card-name { font-size: 1.05rem; font-weight: 800; color: var(--navy); margin-bottom: 6px; line-height: 1.25; }
.tool-card-desc { font-size: .82rem; color: var(--gray-700); line-height: 1.5; margin-bottom: 14px; flex: 1; }
.tool-card-link { font-size: .7rem; font-weight: 800; letter-spacing: 1.5px; text-transform: uppercase; color: var(--red); display: inline-flex; align-items: center; gap: 4px; }

/* FOOTER */
.footer { background-color: var(--navy); padding: 48px 32px; text-align: center; border-top: 1px solid rgba(255,255,255,.08); }
.footer-tagline { font-size: 1.25rem; font-weight: 900; color: var(--red); letter-spacing: 4px; text-transform: uppercase; margin-bottom: 20px; }
.footer-label { font-size: .85rem; font-weight: 600; letter-spacing: 2px; text-transform: uppercase; color: var(--yellow); margin-bottom: 8px; }
.footer-text { font-size: .85rem; color: #9CA3AF; margin-bottom: 4px; }

/* STICKY CONTROLS */
.controls { position: sticky; top: 0; z-index: 50; background: rgba(255,255,255,.96); backdrop-filter: blur(6px); border-bottom: 1px solid var(--gray-200); padding: 10px 32px; display: flex; align-items: center; gap: 10px; flex-wrap: wrap; justify-content: flex-end; }
.jump { font-family: inherit; font-size: .8rem; font-weight: 700; padding: 8px 10px; border-radius: 6px; border: 1px solid var(--gray-200); color: var(--navy); background: #fff; }

/* BACK TO TOP */
.back-to-top { position: fixed; bottom: 24px; right: 24px; width: 48px; height: 48px; background-color: var(--navy); color: var(--yellow); border: 2px solid var(--yellow); border-radius: 50%; font-size: 1.3rem; font-weight: 800; cursor: pointer; opacity: 0; pointer-events: none; transition: opacity .25s ease, transform .2s cubic-bezier(.2,.8,.2,1); z-index: 100; display: flex; align-items: center; justify-content: center; box-shadow: 0 4px 12px rgba(0,0,0,.25); }
.back-to-top.visible { opacity: 1; pointer-events: auto; }
.back-to-top:hover, .back-to-top:focus { transform: translateY(-2px); outline: 3px solid var(--yellow); outline-offset: 2px; }
.skip-link { position: absolute; top: -40px; left: 0; background-color: var(--navy); color: var(--yellow); padding: 8px 16px; font-weight: 700; text-decoration: none; z-index: 200; }
.skip-link:focus { top: 0; }
a:focus-visible, button:focus-visible { outline: 3px solid var(--yellow); outline-offset: 2px; border-radius: 4px; }
.toast { position: fixed; bottom: 84px; right: 24px; background: var(--navy); color: #fff; font-size: .8rem; font-weight: 700; padding: 10px 14px; border-radius: 8px; opacity: 0; transform: translateY(8px); transition: opacity .2s, transform .2s; z-index: 120; pointer-events: none; }
.toast.show { opacity: 1; transform: translateY(0); }

@media screen and (max-width: 900px) {
  .cycle-grid, .sched-grid { grid-template-columns: repeat(2, 1fr); }
  .guide-grid { grid-template-columns: 1fr; }
}
@media screen and (max-width: 768px) {
  .container { margin: 16px; border-radius: 12px; }
  .hero-title { font-size: 2rem; }
  .hero { padding: 40px 20px; }
  .intro, .cycle, .schedule, .year-overview, .month-section, .flex-bank, .notes, .footer, .controls { padding-left: 20px; padding-right: 20px; }
  .month-grid { grid-template-columns: repeat(2, 1fr); }
  .week-grid { grid-template-columns: 1fr; }
  .month-header { gap: 14px; flex-wrap: wrap; }
  .month-number-badge { width: 52px; height: 52px; font-size: 1.4rem; }
  .month-title { font-size: 1.4rem; }
  .month-card.current::after { content: "NOW"; top: 6px; right: 6px; padding: 2px 8px; font-size: .55rem; letter-spacing: 1px; transform: none; border-radius: 3px; }
  .post { grid-template-columns: 70px 1fr; }
  .post-tag { font-size: .58rem; letter-spacing: .5px; }
  .post .copy-btn { grid-column: 2; justify-self: start; }
  .tools-section { padding: 40px 20px; }
  .tools-section-title { font-size: 1.6rem; }
  .tools-grid { grid-template-columns: repeat(2, 1fr); }
  .archive-item { grid-template-columns: 1fr; gap: 6px; }
  .archive { padding-left: 20px; padding-right: 20px; }
}
@media print {
  .controls, .back-to-top, .toast, .copy-btn { display: none !important; }
  .container { box-shadow: none; margin: 0; border-radius: 0; }
  .month-section { break-inside: avoid; }
}
"""

# ---------- HTML pieces ----------
def post_row(tag, day, text):
    n = len(text)
    meta = f'<div class="post-meta{" over" if tag=="x" and n>280 else ""}">{n} characters</div>' if tag == "x" else ""
    label = {"fb":"Facebook","li":"LinkedIn","x":"X"}[tag]
    return f'''
        <div class="post">
          <span class="post-tag {tag}">{label}<span class="post-day">{day}</span></span>
          <div><p class="post-text">{esc(text)}</p>{meta}</div>
          <button class="copy-btn" type="button" data-copy="{esc(text)}" aria-label="Copy {label} post">Copy</button>
        </div>'''

def week_card(i, w):
    return f'''
      <article class="week-card">
        <div class="week-header">
          <span class="week-number">Week {i}</span>
          <span class="week-focus">{esc(w["focus"])}</span>
        </div>
        <p class="week-angle">{esc(w["angle"])}</p>
        <div class="posts">
          {post_row("fb","Mon",w["fb"])}
          {post_row("li","Wed",w["li"])}
          {post_row("x","Fri",w["x"])}
        </div>
      </article>'''

def month_section(m):
    tool = TOOLS[m["tool"]]
    weeks = "".join(week_card(i+1, w) for i, w in enumerate(m["weeks"]))
    # month-level copy: all 12 posts as plain text
    lines = [f'{m["name"]}: {m["theme"]}', '']
    for i, w in enumerate(m["weeks"]):
        lines += [f'WEEK {i+1}: {w["focus"]}', f'Facebook (Mon): {w["fb"]}', f'LinkedIn (Wed): {w["li"]}', f'X (Fri): {w["x"]}', '']
    month_copy = "\n".join(lines).strip()
    return f'''
    <section class="month-section" id="{m["id"]}" aria-labelledby="{m["id"]}-title">
      <div class="month-header">
        <div class="month-number-badge">{m["num"]}</div>
        <div class="month-header-content">
          <div class="month-title-small">{m["name"]} &bull; Newsletter first Tuesday</div>
          <h3 class="month-title" id="{m["id"]}-title">{esc(m["theme"])}</h3>
          <div class="month-focus">{esc(m["focus"])}</div>
        </div>
        <div class="month-actions">
          <button class="copy-btn month" type="button" data-copy="{esc(month_copy)}" aria-label="Copy all {m["name"]} posts">Copy month</button>
        </div>
      </div>
      <div class="hazard-basis">
        <div class="hazard-basis-label">Why This Month</div>
        <p>{esc(m["why"])}</p>
      </div>
      <div class="week-grid">{weeks}
      </div>
      <div class="tool-connection">
        <div class="tool-connection-icon">{tool["icon"]}</div>
        <div class="tool-connection-content">
          <div class="tool-connection-label">Recruiting Tool Connection</div>
          <p class="tool-connection-text"><a href="#" data-link="{m["tool"]}" target="_blank" rel="noopener">{esc(tool["name"])}</a>. {esc(m["tool_text"])}</p>
        </div>
      </div>
    </section>'''

def month_cards():
    return "".join(f'''
        <a class="month-card {m["season"]}" href="#{m["id"]}">
          <div class="month-num">{m["num"]}</div>
          <div class="month-name">{m["name"]}</div>
          <div class="month-theme">{esc(m["theme"])}</div>
        </a>''' for m in MONTHS)

def flex_rows():
    return "".join(f'<tr><td>{esc(t)}</td><td>{esc(u)}</td></tr>' for t, u in FLEX_TOPICS)

def archive_items():
    out = []
    for a in ARCHIVE:
        cls = {"evergreen":"evergreen","dated":"dated"}.get(a["status"], "partly")
        out.append(f'''
        <div class="archive-item">
          <div class="archive-when">{esc(a["when"])}</div>
          <div><div class="archive-title">{esc(a["title"])}<span class="status {cls}">{esc(a["status"])}</span></div><p class="archive-take">{esc(a["takeaway"])}</p></div>
          <a class="archive-link" href="{a["url"]}" target="_blank" rel="noopener">Read edition &rarr;</a>
        </div>''')
    return "".join(out)

def standing_set():
    return "".join(week_card(i+1, w) for i, w in enumerate(FLEX_STANDING["weeks"]))

def tool_cards():
    order = ["neogov","careers","ridealong","pat","newsletter","archive","frontline"]
    return "".join(f'''
        <a class="tool-card" href="#" data-link="{k}" target="_blank" rel="noopener">
          <div class="tool-card-icon">{TOOLS[k]["icon"]}</div>
          <div class="tool-card-name">{esc(TOOLS[k]["name"])}</div>
          <p class="tool-card-desc">{esc(TOOLS[k]["desc"])}</p>
          <span class="tool-card-link">{esc(TOOLS[k]["cta"])} &rarr;</span>
        </a>''' for k in order)

themes_js = json.dumps([m["theme"] for m in MONTHS])
jump_opts = "".join(f'<option value="#{m["id"]}">{m["num"]} {m["name"]}: {esc(m["theme"])}</option>' for m in MONTHS)

HTML = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Ready to Serve: Recruiting Content Calendar | Denton Fire Department</title>
<link rel="icon" type="image/png" href="https://files.constantcontact.com/3720c3fd901/10017eb4-f7d2-424d-92ed-c1b5424b9869.png">
<link rel="apple-touch-icon" href="https://files.constantcontact.com/3720c3fd901/10017eb4-f7d2-424d-92ed-c1b5424b9869.png">
<meta name="description" content="Denton Fire Department Ready to Serve recruiting content calendar. Twelve monthly themes aligned to the Civil Service hiring cycle, with weekly Facebook, LinkedIn, and X posts.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@600;700;800;900&display=swap" rel="stylesheet">
<style>{CSS}</style>
</head>
<body>
<a href="#main" class="skip-link">Skip to main content</a>
<div class="container">

  <header class="hero">
    <img src="https://files.constantcontact.com/3720c3fd901/10017eb4-f7d2-424d-92ed-c1b5424b9869.png" alt="Denton Fire Department" class="hero-logo">
    <p class="hero-kicker">Denton Fire Department</p>
    <h1 class="hero-title">READY TO SERVE</h1>
    <p class="hero-subtitle">Recruiting Content Calendar</p>
    <div class="hero-pill"><p>Annual Publishing Plan &bull; Aligned to the Civil Service Hiring Cycle</p></div>
  </header>

  <div class="banner" role="doc-subtitle">
    <p id="monthBannerText">Every month. Every step of the process. Every future Denton firefighter.</p>
  </div>

  <div class="controls" aria-label="Page controls">
    <label class="visually-hidden" for="jumpTo" style="position:absolute;left:-9999px;">Jump to month</label>
    <select class="jump" id="jumpTo"><option value="">Jump to month&hellip;</option>{jump_opts}<option value="#flex">Flex Month Topic Bank</option><option value="#archive">Edition Archive</option></select>
  </div>

  <main id="main">

    <section class="intro">
      <h2 class="intro-title">One candidate. Every channel. Every month.</h2>
      <p>This is the annual publishing plan for the Ready to Serve recruiting newsletter and its supporting social media content. It is written for the DFD recruiting team and the City of Denton Marketing and Communications team, the people who put recruiting messages in front of candidates across email, Facebook, LinkedIn, and X.</p>
      <p>The twelve themes follow the Civil Service hiring cycle from start to finish. The year opens with the January exam, resets in February with a full career overview, walks candidates through the academy, EMS certification, station life, and the rookie year, then turns toward the next cycle: fitness in September, PAT prep in October, registration in November, and interviews in December. Each month's "Why This Month" box explains the placement. The four weekly cards carry the core message for that week, and beneath each one sits the ready-to-post copy for all three platforms, tuned to each audience and sized for each channel.</p>
      <p>The newsletter goes out the first Tuesday of the month and sets the theme. Facebook posts on Monday, LinkedIn on Wednesday, X on Friday. Every month points candidates to one specific recruiting resource. Adjustments to the plan route through the CRR Officer. Use the copy as written or adapt it to the current cycle's dates.</p>
    </section>

    <section class="cycle" aria-labelledby="cycle-title">
      <h2 class="section-kicker" id="cycle-title">Current Cycle Key Dates <span class="update-flag">Update annually</span></h2>
      <div class="cycle-grid">
        <div class="cycle-card"><div class="cycle-label">Registration opens</div><div class="cycle-value" id="dateRegOpen">October 2026</div><div class="cycle-note">NEOGOV, City of Denton</div></div>
        <div class="cycle-card red"><div class="cycle-label">Civil Service Exam</div><div class="cycle-value" id="dateExam">January 2027</div><div class="cycle-note">Confirm exact date and location</div></div>
        <div class="cycle-card"><div class="cycle-label">PAT and Background</div><div class="cycle-value" id="datePat">February to March 2027</div><div class="cycle-note">Passing score 84 or higher</div></div>
        <div class="cycle-card"><div class="cycle-label">Academy start</div><div class="cycle-value" id="dateAcademy">July 2027</div><div class="cycle-note">Conditional offers May to June</div></div>
      </div>
    </section>

    <section class="schedule" aria-labelledby="sched-title">
      <h2 class="section-kicker" id="sched-title">Publishing Schedule</h2>
      <div class="sched-grid">
        <div class="sched-card news"><div class="sched-day">First Tuesday</div><div class="sched-name">Newsletter</div><div class="sched-desc">Ready to Serve via Constant Contact. Establishes the month's theme and carries the long-form version.</div></div>
        <div class="sched-card fb"><div class="sched-day">Every Monday</div><div class="sched-name">Facebook</div><div class="sched-desc">Conversational and direct. Speak to candidates as individuals. 2 to 4 sentences, end with a clear call to action.</div></div>
        <div class="sched-card li"><div class="sched-day">Every Wednesday</div><div class="sched-name">LinkedIn</div><div class="sched-desc">Professional but not corporate. Career-minded candidates. 2 to 3 polished sentences on growth and institutional values.</div></div>
        <div class="sched-card x"><div class="sched-day">Every Friday</div><div class="sched-name">X</div><div class="sched-desc">Punchy and direct. Under 280 characters. Short declarative sentences. No hashtags unless campaign-specific. End with impact.</div></div>
      </div>
      <h2 class="section-kicker">Platform Guidelines</h2>
      <div class="guide-grid">
        <div class="guide-card"><div class="guide-head"><span class="post-tag fb" style="width:74px">Facebook</span><span class="guide-name">Conversational and direct</span></div><p><strong>Tone:</strong> Speak to candidates as individuals. Complete sentences, accessible language, no jargon.</p><p><strong>Format:</strong> 2 to 4 sentences. End with a clear call to action when appropriate.</p></div>
        <div class="guide-card"><div class="guide-head"><span class="post-tag li" style="width:74px">LinkedIn</span><span class="guide-name">Professional, not corporate</span></div><p><strong>Tone:</strong> Speak to career-minded candidates. Reference career development, professional growth, and institutional values.</p><p><strong>Format:</strong> 2 to 3 sentences with polished phrasing.</p></div>
        <div class="guide-card"><div class="guide-head"><span class="post-tag x" style="width:74px">X</span><span class="guide-name">Punchy and direct</span></div><p><strong>Tone:</strong> Every word earns its place. Short declarative sentences. No hashtags unless campaign-specific.</p><p><strong>Format:</strong> Under 280 characters. End with impact, not trailing thoughts. Character counts are shown on every X post below.</p></div>
      </div>
    </section>

    <section class="year-overview" aria-labelledby="overview-title">
      <h2 class="overview-title" id="overview-title">Year at a Glance</h2>
      <div class="month-grid">{month_cards()}
      </div>
    </section>
{"".join(month_section(m) for m in MONTHS)}

    <section class="flex-bank" id="flex" aria-labelledby="flex-title">
      <h2 class="section-kicker" id="flex-title">Flex Month Topic Bank (August)</h2>
      <p class="flex-intro">August is designated as a flex month. Select from the following topics based on department priorities, diversity initiatives, or emerging recruitment needs. In 2026 the flex slot carries the Ready to Serve reveal and catch-up (see August above). The standing set below (second careers, women in fire, veterans, education) is ready for any year without a reveal, and any week can be swapped for a topic from this table when the pipeline calls for it.</p>
      <table class="flex-table">
        <thead><tr><th>Topic</th><th>Best use case</th></tr></thead>
        <tbody>{flex_rows()}</tbody>
      </table>
      <div class="standing-head">Standing August set (second careers, women in fire, veterans, education). Ready to run in any year without a reveal.</div>
      <div class="week-grid">{standing_set()}
      </div>
    </section>

    <section class="archive" id="archive" aria-labelledby="archive-title">
      <h2 class="section-kicker" id="archive-title">Ready to Serve Edition Archive</h2>
      <p class="archive-intro">Every edition sent to date, with the takeaways that still hold. New subscribers should be pointed here, and the August catch-up edition links to the evergreen ones directly. Add each new edition to this list when it goes out.</p>
      <div class="archive-list">{archive_items()}
      </div>
    </section>

    <section class="notes" aria-labelledby="notes-title">
      <h2 class="section-kicker" id="notes-title">Implementation Notes</h2>
      <ol>
        <li>Update all date references (exam dates, registration deadlines, academy start dates) at the beginning of each fiscal year. The Key Dates strip at the top of this page and the LINKS block in the page source are the two places to edit.</li>
        <li>January edition content should be finalized in December and scheduled in advance to ensure timely delivery before the exam.</li>
        <li>Social media posts can be scheduled using Constant Contact's social media scheduler or a third-party tool such as Buffer or Hootsuite. Use the Copy buttons here to move text into the scheduler.</li>
        <li>Monitor engagement metrics monthly. If a particular topic or format consistently outperforms others, adjust the calendar accordingly.</li>
        <li>Cross-promote content: link newsletter signup in social posts, and include social follow buttons in newsletters.</li>
        <li>All content should align with DFD branding standards: professional tone, no em dashes, no AI writing tells, active voice, and concrete language.</li>
        <li>Coordinate with the Frontline Report (CRR calendar) so recruiting and community safety posts do not land on the same channel on the same day during high-priority weeks such as Fire Prevention Week or registration deadlines.</li>
      </ol>
    </section>

    <section class="tools-section" aria-labelledby="tools-title">
      <p class="tools-section-kicker">Department Resources</p>
      <h2 class="tools-section-title" id="tools-title">Recruiting Tools Reference</h2>
      <p class="tools-section-subtitle">The resources every recruiting message should point to. Link to these from every relevant newsletter and social post.</p>
      <div class="tools-grid">{tool_cards()}
      </div>
    </section>

  </main>

  <footer class="footer">
    <p class="footer-tagline">Ready to Serve.</p>
    <p class="footer-label">Denton Fire Department</p>
    <p class="footer-text">Recruiting &bull; Community Risk Reduction</p>
    <p class="footer-text">(940) 349-8848 &bull; <a href="mailto:FireRecruiter@cityofdenton.com" style="color: inherit; text-decoration: underline;">FireRecruiter@cityofdenton.com</a> &bull; <a href="https://dentonfire.com" style="color: inherit; text-decoration: underline;">dentonfire.com</a></p>
  </footer>
</div>

<button class="back-to-top" id="backToTop" aria-label="Back to top" title="Back to top">&uarr;</button>
<div class="toast" id="toast" role="status" aria-live="polite">Copied</div>

<script>
// ---------------------------------------------------------------
// LINKS: update these once and every reference on the page follows.
// ---------------------------------------------------------------
var LINKS = {{
  neogov:     'https://www.governmentjobs.com/careers/dentontx',
  careers:    'https://www.cityofdenton.com/582/Fire-Department-Careers',
  ridealong:  'https://www.cityofdenton.com/582/Fire-Department-Careers',   // replace with ride-along request page
  pat:        'https://www.cityofdenton.com/582/Fire-Department-Careers',   // replace with PAT prep guide
  newsletter: 'https://www.cityofdenton.com/582/Fire-Department-Careers',   // replace with Constant Contact signup
  archive:    '#archive',
  frontline:  'https://dentonfire.github.io/Calendar/'
}};
document.querySelectorAll('[data-link]').forEach(function(a) {{
  var k = a.getAttribute('data-link');
  if (LINKS[k]) {{
    a.setAttribute('href', LINKS[k]);
    if (LINKS[k].charAt(0) === '#') {{ a.removeAttribute('target'); a.removeAttribute('rel'); }}
  }}
}});

// Highlight the current month card and populate the banner
(function() {{
  var monthIds = ['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec'];
  var themes = {themes_js};
  var now = new Date();
  var idx = now.getMonth();
  var monthName = now.toLocaleDateString('en-US', {{ month: 'long' }});
  var card = document.querySelector('a.month-card[href="#' + monthIds[idx] + '"]');
  if (card) {{ card.classList.add('current'); card.setAttribute('aria-current', 'date'); }}
  var b = document.getElementById('monthBannerText');
  if (b) b.textContent = 'THIS MONTH \\u2022 ' + monthName.toUpperCase() + ' ' + now.getFullYear() + ' \\u2022 THEME: ' + themes[idx].toUpperCase();
}})();

// Jump to month
(function() {{
  var sel = document.getElementById('jumpTo');
  if (!sel) return;
  sel.addEventListener('change', function() {{
    if (sel.value) {{ window.location.hash = sel.value; sel.value = ''; }}
  }});
}})();

// Copy buttons
(function() {{
  var toast = document.getElementById('toast');
  function showToast(msg) {{
    toast.textContent = msg; toast.classList.add('show');
    clearTimeout(toast._t); toast._t = setTimeout(function() {{ toast.classList.remove('show'); }}, 1400);
  }}
  function copyText(text) {{
    if (navigator.clipboard && window.isSecureContext) return navigator.clipboard.writeText(text);
    return new Promise(function(res, rej) {{
      var ta = document.createElement('textarea'); ta.value = text; ta.style.position = 'fixed'; ta.style.opacity = '0';
      document.body.appendChild(ta); ta.select();
      try {{ document.execCommand('copy'); res(); }} catch (e) {{ rej(e); }} finally {{ document.body.removeChild(ta); }}
    }});
  }}
  document.querySelectorAll('.copy-btn[data-copy]').forEach(function(btn) {{
    btn.addEventListener('click', function() {{
      var text = btn.getAttribute('data-copy');
      var orig = btn.textContent;
      copyText(text).then(function() {{
        btn.classList.add('done'); btn.textContent = 'Copied';
        showToast('Copied to clipboard');
        setTimeout(function() {{ btn.classList.remove('done'); btn.textContent = orig; }}, 1500);
      }}).catch(function() {{ showToast('Copy failed. Select the text manually.'); }});
    }});
  }});
}})();

// Back-to-top
(function() {{
  var btn = document.getElementById('backToTop');
  if (!btn) return;
  function onScroll() {{ btn.classList.toggle('visible', window.scrollY > 400); }}
  window.addEventListener('scroll', onScroll, {{ passive: true }});
  btn.addEventListener('click', function() {{ window.scrollTo({{ top: 0, behavior: 'smooth' }}); }});
  onScroll();
}})();
</script>
</body>
</html>
'''

with open("index.html", "w", encoding="utf-8") as f:
    f.write(HTML)
print("wrote index.html", len(HTML), "bytes")
