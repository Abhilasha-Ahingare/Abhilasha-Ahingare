# Abhilasha · Violet Signal / Design 29

This package is for **Abhilasha-Ahingare**, with email **abhilashaahingare.02@gmail.com**.
It follows the supplied Violet Signal reference: charcoal panels, violet light,
fine borders, a central name, orbital detail, and two project cards.

## Sabse aasaan upload

1. ZIP par right-click → **Extract All**.
2. Extracted `violet-signal-29` folder kholo. Andar `README.md`, `assets`,
   `scripts`, `data`, `tests` aur `.github` dikhne chahiye.
3. Abhilasha ke account se [profile repository](https://github.com/Abhilasha-Ahingare/Abhilasha-Ahingare) kholo.
4. **Add file → Upload files** select karo.
5. File Explorer aur browser ko side by side rakho. Extracted folder ke **andar
   ki files aur folders** select karke upload box par drag karo.
6. Upload list mein `assets/hero.svg`, `assets/badges/react.svg`,
   `scripts/update_metrics.py` aur `.github/workflows/refresh-profile.yml` jaise
   **poore paths** check karo. Folder icon na dikhna apne aap mein failure nahi hai.
7. Default branch par **Commit changes** karo. Profile refresh karo.

**Outer folder ya ZIP upload mat karo.** Repository ke root par `README.md`
aur `assets` ek hi level par hone chahiye. Sirf README paste karne se local images
load nahi hongi. Purani README ko replace karo; unrelated repository files ko
delete karne ki zaroorat nahi hai.

**Agar purana Violet Signal package pehle se laga hua hai:** is ZIP ke andar
ka `README.md`, poora `assets` folder aur `scripts/build_theme.py` zaroor replace
karo. Naam, role, projects aur stack ka visible text SVG images mein hai;
sirf README ke `alt` text ko badalne se images nahi badlengi. Naya generator
upload karne se daily refresh bhi updated details ko hi banayega.

The profile repository must be public and its name must match the username.
See [GitHub's profile README requirements](https://docs.github.com/en/account-and-profile/how-tos/profile-customization/managing-your-profile-readme)
and [upload instructions](https://docs.github.com/en/repositories/working-with-files/managing-files/adding-a-file-to-a-repository).

## Agar browser se folders upload na hon

VS Code + Git ka option use karo. Windows PowerShell mein:

```powershell
git clone https://github.com/Abhilasha-Ahingare/Abhilasha-Ahingare.git
cd Abhilasha-Ahingare
```

Ab File Explorer se extracted package ke **andar ki saari files/folders** is
cloned folder mein copy karo. Existing README replace karne par **Replace** chuno.
Phir usi PowerShell window mein:

```powershell
git status --short
git add -- README.md assets scripts data tests .github .gitignore SETUP.md METRICS.md VALIDATION.md
git commit -m "Update profile with Violet Signal theme"
git push
```

Git sign-in aaye to Abhilasha ke GitHub account se sign in karo. Paths ko check
karo: `assets/hero.svg` hona chahiye, `violet-signal-29/assets/hero.svg` nahi.
If the clone destination already exists, open that existing clone instead.

## Daily stats update

The package already includes a real, dated snapshot, so cards can display
immediately after upload. To turn on refresh:

1. Repository → **Actions**.
2. If GitHub asks to enable workflows, enable them for this repository.
3. Select **Refresh Violet Signal profile** → **Run workflow** on the default branch.
4. Wait for the green check. The workflow commits updated SVG cards and data.

The schedule requests a daily run at **02:23 UTC / 07:53 IST**. GitHub can delay
scheduled jobs; this is not an exact-time promise. The workflow uses the default
`GITHUB_TOKEN`; a separate personal access token is not required. It runs only in
`Abhilasha-Ahingare/Abhilasha-Ahingare` on its default branch.

If the job reports a write-permission error, check **Settings → Actions →
General → Workflow permissions** and repository or organization restrictions.
Protected branches can prevent automatic pushes. No additional approval or token
is needed for viewing the included snapshot.

GitHub can disable scheduled workflows in public repositories after 60 days
without repository activity; re-enable the workflow if that happens.
See [scheduled workflow behavior](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows#schedule)
and [workflow token permissions](https://docs.github.com/en/actions/tutorials/authenticate-with-github_token).

## Editing the profile later

- Normal README text and links: edit `README.md` directly. The daily workflow
  **preserves your README edits**.
- Colors: edit `scripts/theme.py`.
- Hero name, role, project visuals, tech labels and illustrations: edit
  `scripts/build_theme.py`; the workflow regenerates those assets.
- Quote text: edit `DEV_NOTES` in `scripts/update_metrics.py`. Seven original,
  unattributed development notes rotate daily.
- To rebuild everything locally with Python 3.10 or newer:

```powershell
python scripts/build_theme.py --assets-only
python scripts/update_metrics.py
python -m unittest discover -s tests -v
```

`python scripts/build_theme.py` without `--assets-only` intentionally regenerates
the original README template and will overwrite manual README edits. Use that
only when you want to rebuild the template.

## What the package includes

- Hero, project illustrations, two-column desktop projects, stacked mobile cards.
- 21 technology badges, with PostgreSQL and Express.js in Backend & data,
  plus an explicitly labelled **System Design · learning** badge.
- MERN Stack Developer role in both hero sizes and the About section.
- About section, email and repository links; no invented LinkedIn or portfolio URL.
- Real overview, streaks, language composition, violet contribution grid and
  top contributed repository ranking.
- A readable daily contribution table at `data/ACTIVITY.md`.
- Daily development quote and a matching optional profile-view counter.
- Local SVG files and a standard-library Python refresh workflow.

The featured projects are **ProjectHub** (`project-management-system`) and
**Event Ticket Management System** (`Event-Management-Ticketing-System`).
ProjectHub's branding was verified in its public frontend source; both repository
links and their public source trees were checked on 2026-09-17. Their illustrations
are decorative artwork, not screenshots. Application functionality and deployment
health have not been audited.

## GitHub styling limits

This themes the content **inside the profile README**. GitHub controls the outer
sidebar, avatar, native repository pins, achievements, native contribution grid,
activity timeline and surrounding page colors. A README cannot globally recolor
those elements. The violet contribution grid supplied here is an additional
README card. Native text links also follow the viewer's GitHub theme.

These cards intentionally retain their dark Violet Signal palette in both GitHub
light and dark mode. Custom CSS and JavaScript are not used in the README because
[GitHub sanitizes them](https://github.com/github/markup#github-markup).

Preview PNGs show the locally rendered assets and representative Markdown layout;
they are not screenshots of a deployed GitHub profile. GitHub's renderer may
differ in spacing and font details. Read `VALIDATION.md` for the checks performed.
