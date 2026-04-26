# 🇵🇰 Hunar — Talent Mapper

> **You built it. You know it. Now the world can see it.**

**[🚀 Live Demo](https://hunar-talent-mapper-p3jrurcstdm2az2gff5m4v.streamlit.app/)** — Try it now, no account needed.

Built for **HackNation 5th Global AI Hackathon** in collaboration with MIT — Challenge 5: Unmapped.

---

## The Problem

Most job platforms assume you have a CV. They assume a degree, internships, a LinkedIn profile built over years.

For millions of young people across Pakistan, West Africa, and Southeast Asia — that assumption just doesn't hold.

A self-taught coder in Mardan who built a machine learning system has no way to show that to an employer. A mobile repair technician who has fixed 500 phones has no credential for that. A designer in Lagos who built apps for local shops is invisible to every hiring algorithm.

The skills exist. The infrastructure to surface them doesn't. Hunar fixes that.

---

## What It Does

You open Hunar, describe what you can do in whatever language feels natural — English, Urdu, or Roman Urdu — and hit generate.

The platform pulls out your skills automatically and organizes them into three tiers: Primary Expertise, Additional Strengths, and Professional Qualities. It builds a structured profile from plain text. No form. No template. No degree field.

Every profile gets a unique shareable URL you can send on WhatsApp right now. The opportunity matching section shows you real platforms — Upwork, Fiverr, Kaggle, Google Summer of Code, Rozee.pk, KPITB — ranked by how well your skills line up with what they need.

### Try it yourself

Type something like:

```
main Python mein machine learning karta hun, YOLOv8 se object detection banaya hai
```

Or:

```
I build websites and mobile apps. I taught myself React and Flutter.
```

Or just:

```
me mobile repair karska hu, screen aur battery replace kar sakta hun
```

All three work.

---

## Features

- **Multilingual NLP** — English, Urdu script, and Roman Urdu in one pipeline
- **Automatic language detection** — detects which language you wrote in and shows a badge
- **Three-tier skill extraction** — Primary Expertise, Additional Strengths, Professional Qualities
- **Shareable profile URL** — every profile gets a unique UUID-based link
- **WhatsApp share button** — one tap to share your profile
- **Real opportunity matching** — matched to 50+ platforms with actual match scores
- **Skill gap guidance** — shows what to learn next to increase your match score
- **No account required** — works instantly, no sign-up

---

## Tech Stack

| Layer | Technology |
|---|---|
| Frontend & Backend | Python, Streamlit |
| NLP Engine | Custom multilingual keyword extraction |
| Language Detection | langdetect |
| Profile Storage | UUID + Streamlit session state |
| Opportunity Matching | Skill overlap scoring algorithm |
| Deployment | Streamlit Cloud |

---

## Project Structure

```
hunar-talent-mapper/
├── app.py               # Main Streamlit application
├── processor.py         # NLP skill extraction engine
├── styles.py            # Custom CSS and UI components
├── requirements.txt     # Python dependencies
└── .devcontainer/       # Dev container configuration
```

---

## Run Locally

```bash
# Clone the repo
git clone https://github.com/TheAhmadYousaf/hunar-talent-mapper.git
cd hunar-talent-mapper

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

App will open at `http://localhost:8501`

---

## How the Matching Works

When you submit your skill description, the NLP engine extracts structured skills from your text. Each skill gets assigned to a category — programming, AI/ML, design, mobile, hardware etc.

The opportunity catalog has 50+ entries. Each entry has a list of required skill keywords. The match score is:

```
match_score = (user skills overlapping with opportunity keywords) 
              / (total required skills for that opportunity) 
              × 100
```

Opportunities are sorted by match score. Green badge means strong match. Orange means partial. Gray means low overlap.

---

## Why Hunar?

Hunar means skill in Urdu.

A 22-year-old in Mardan builds an AI system in his spare time. He has no LinkedIn. No degree yet. No formal work history. By every traditional measure — invisible. By every real measure — talented, driven, and ready.

Hunar changes that.

---

## Builder

**Muhammad Ahmad Yousaf Mubarak**
BS Artificial Intelligence — Abdul Wali Khan University Mardan (AWKUM)

[GitHub](https://github.com/TheAhmadYousaf) · [LinkedIn](https://linkedin.com/in/ahmad-yousaf-ai)

---

## Hackathon

Built at **HackNation 5th Global AI Hackathon** in collaboration with MIT Sloan AI Club.
Challenge 5 — Unmapped: Map informal talent to real economic opportunity.

*Powered by Hunar AI — Mardan Region Talent Hub*
