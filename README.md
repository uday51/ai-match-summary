# 🏏 Automated Cricket Match Report Generator using Groq & AWS

This project generates engaging cricket match reports using AI. It reads structured match data from **AWS S3**, builds a prompt, and sends it to **Groq's Mistral-SABA-24B** language model to produce a professional report in a journalistic style.

---

## 📸 Sample Output

> 📰 **"Dhoni's Magic at Wankhede: CSK Outclass MI in Tight Thriller"**  
>  
> In a pulsating encounter at Wankhede Stadium, CSK overcame MI in the final overs of IPL 2025. With 25 needed off 12, Dhoni turned back the clock, smashing 3 sixes to seal the game.  
>  
> 🔹 **Ruturaj Gaikwad**: 68(45)  
> 🔹 **Jasprit Bumrah**: 3/26  
> 🔹 **MS Dhoni**: 34*(12)  
>  
> 🧠 *“We backed ourselves. The crowd lifted us in those final moments,”* said CSK coach.

---

## 🚀 Features

- ✅ Fetches match data from an AWS S3 bucket
- ✅ Automatically constructs AI prompts
- ✅ Generates:
  - Catchy headlines
  - 3-paragraph match summaries
  - Bullet points of key performances
  - Tactical insights
  - Imaginary player/coach quotes
- ✅ Uses `Groq` API with `mistral-saba-24b` for fast LLM responses
- ✅ Written in pure Python

---

## 🧠 Technologies Used

| Component       | Technology                     |
|----------------|---------------------------------|
| Programming     | Python                         |
| Cloud Storage   | AWS S3 (via `boto3`)           |
| LLM Inference   | Groq API (`mistral-saba-24b`)  |
| Data Format     | JSON                           |

---


