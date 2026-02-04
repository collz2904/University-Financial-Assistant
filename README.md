# University Student Financial Assistant
##  Use Case & Rationale
**Use Case:** Helping university students manage limited income and plan for future savings.
**Rationale:** Students often struggle with financial literacy. A multi-agent system allows for specialized focus: one agent handles the "cold math" of forecasting, while another provides the "warm advice" of investment strategy, ensuring accuracy and personality.

## How to Run
1. **Clone the repo:** `git clone <your-url>`
2. **Install dependencies:** `pip install -r requirements.txt`
3. **Setup Environment:** Create a `.env` file and add `OPENAI_API_KEY=your_key_here`.
4. **Run the Notebook:** Open `Untitled-1.ipynb` and run all cells.

## Agent Team Structure
The team consists of three agents working in a **Sequential Process**:
1. **Budget Forecast Agent:** Analyzes raw data and predicts 3-month balances.
2. **Savings & Investment Advisor:** Takes the forecast to suggest specific financial moves.
3. **Summary & Visualization Generator:** Compiles everything into a student-friendly report.

## Key Challenges & Solutions
* **Challenge:** API Quota Limits (Error 429).
    * **Solution:** Monitored usage on the OpenAI dashboard and verified billing credits to ensure service continuity.
* **Challenge:** Hallucinations in Financial Advice.
    * **Solution:** Set `allow_delegation=False` and provided strict context from the Budget Agent to keep the Advisor grounded in real data.
* **Challenge:** Coordination Loops.
    * **Solution:** Used a `Sequential` process rather than `Hierarchical` to ensure a clear, one-way flow of information.
