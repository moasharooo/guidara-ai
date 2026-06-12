from fastapi.responses import HTMLResponse

def dashboard_page():
    return HTMLResponse("""
<!DOCTYPE html>
<html>
<head>
    <title>Guidara AI Dashboard</title>
    <style>
        body {
            margin: 0;
            font-family: Arial, sans-serif;
            background: #0f172a;
            color: #e5e7eb;
        }
        .layout {
            display: flex;
            min-height: 100vh;
        }
        .sidebar {
            width: 260px;
            background: #020617;
            padding: 24px;
            border-right: 1px solid #1f2937;
        }
        .logo {
            font-size: 26px;
            font-weight: bold;
            margin-bottom: 8px;
        }
        .tagline {
            color: #94a3b8;
            font-size: 13px;
            margin-bottom: 28px;
        }
        .nav {
            color: #cbd5e1;
            margin: 16px 0;
            font-size: 15px;
        }
        .section-title {
            font-size: 13px;
            color: #94a3b8;
            margin: 22px 0 12px;
        }
        .saved-project {
            background: #111827;
            padding: 12px;
            border-radius: 12px;
            margin-bottom: 10px;
            cursor: pointer;
            font-size: 13px;
            border: 1px solid #1f2937;
        }
        .saved-project:hover {
            border-color: #38bdf8;
            background: #0f172a;
        }
        .saved-project strong {
            display: block;
            color: #e5e7eb;
            margin-bottom: 4px;
        }
        .saved-project span {
            color: #94a3b8;
            font-size: 12px;
        }
        .main {
            flex: 1;
            padding: 32px;
        }
        .header {
            margin-bottom: 28px;
        }
        .header h1 {
            margin: 0;
            font-size: 34px;
        }
        .header p {
            color: #94a3b8;
        }
        .grid {
            display: grid;
            grid-template-columns: 1fr 1.2fr;
            gap: 24px;
        }
        .card {
            background: #111827;
            border: 1px solid #1f2937;
            border-radius: 18px;
            padding: 24px;
            box-shadow: 0 20px 40px rgba(0,0,0,0.25);
        }
        input, textarea {
            width: 100%;
            box-sizing: border-box;
            padding: 12px;
            margin-top: 8px;
            margin-bottom: 14px;
            border-radius: 10px;
            border: 1px solid #334155;
            background: #020617;
            color: white;
        }
        textarea {
            min-height: 90px;
        }
        label {
            font-size: 14px;
            color: #cbd5e1;
        }
        button {
            background: #38bdf8;
            color: #020617;
            border: none;
            padding: 14px 18px;
            border-radius: 12px;
            font-weight: bold;
            cursor: pointer;
            width: 100%;
            margin-top: 10px;
        }
        button:hover {
            background: #0ea5e9;
        }
        .result-box {
            white-space: pre-wrap;
            background: #020617;
            border-radius: 14px;
            padding: 18px;
            color: #d1fae5;
            font-size: 14px;
            max-height: 520px;
            overflow-y: auto;
            border: 1px solid #1f2937;
        }
        .metric {
            display: inline-block;
            background: #020617;
            border: 1px solid #334155;
            padding: 14px;
            border-radius: 14px;
            margin-right: 12px;
            margin-bottom: 12px;
            min-width: 130px;
        }
        .metric span {
            display: block;
            color: #94a3b8;
            font-size: 12px;
        }
        .metric strong {
            font-size: 22px;
            color: #38bdf8;
        }
        .small-note {
            color: #94a3b8;
            font-size: 13px;
            margin-top: 12px;
        }
                        

       .report-section {
    background: #020617;
    border: 1px solid #1f2937;
    border-radius: 16px;
    padding: 18px;
    margin-bottom: 18px;
}

.report-section h3 {
    color: #38bdf8;
    margin-top: 0;
}

.report-section p {
    color: #dbeafe;
    line-height: 1.7;
}

.swot-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 14px;
}

.swot-card {
    background: #0f172a;
    border: 1px solid #334155;
    border-radius: 14px;
    padding: 14px;
}

.swot-card h4 {
    color: #facc15;
    margin-top: 0;
}

.swot-card li,
.recommendations li {
    margin-bottom: 8px;
    color: #e5e7eb;
}

.final-box {
    background: linear-gradient(135deg, #0ea5e9, #6366f1);
    color: white;
    border-radius: 18px;
    padding: 22px;
    margin-top: 20px;
}

.final-box h3 {
    margin-top: 0;
}    

      .saved-project {
    position: relative;
    background: #111827;
    padding: 12px;
    border-radius: 12px;
    margin-bottom: 10px;
    border: 1px solid #1f2937;
    transition: all 0.25s ease;
}

.saved-project:hover {
    border-color: #38bdf8;
    transform: translateY(-2px);
}

.delete-btn {
    position: absolute;
    top: 10px;
    right: 10px;

    background: transparent;
    color: #ef4444;

    border: none;
    cursor: pointer;

    opacity: 0;
    transition: all 0.25s ease;

    font-size: 13px;
    width: auto;
    padding: 4px 8px;
}

.saved-project:hover .delete-btn {
    opacity: 1;
}                               
    </style>
</head>

<body>
<div class="layout">
    <aside class="sidebar">
        <div class="logo">Guidara AI</div>
        <div class="tagline">Smarter Decisions. Lower Risks.</div>

        <div class="nav">Dashboard</div>
        <div class="nav">Business Ideas</div>
        <div class="nav">AI Analysis</div>

        <hr style="border-color:#1f2937; margin:22px 0;">

        <div class="section-title">Saved Projects</div>
        <div id="saved-projects">Loading...</div>
    </aside>

    <main class="main">
        <div class="header">
            <h1>Business Idea Validator</h1>
            <p>Analyze business ideas using AI-powered market, risk, SWOT, and recommendation insights.</p>
        </div>

        <div class="grid">
            <div class="card">
                <h2>Create Business Idea</h2>

                <label>Business Name</label>
                <input id="business_name" value="FitZone Gym">

                <label>Industry</label>
                <input id="industry" value="Fitness">

                <label>Budget</label>
                <input id="budget" type="number" value="30000">

                <label>Location</label>
                <input id="location" value="Amman">

                <label>Target Audience</label>
                <input id="target_audience" value="Young professionals">

                <label>Description</label>
                <textarea id="description">A premium gym for working professionals with monthly memberships.</textarea>

                <button onclick="createAndAnalyze()">Create & Analyze</button>
                <div class="small-note">Saved projects will appear automatically in the sidebar.</div>
            </div>

            <div class="card">
                <h2 id="result-title">AI Analysis Result</h2>

                <div id="metrics"></div>

                <div class="result-box" id="result">
                    Your AI analysis will appear here...
                </div>
            </div>
        </div>
    </main>
</div>

<script>
async function loadProjects() {
    const response = await fetch("/business-ideas");
    const data = await response.json();

    let html = "";

    if (!data.data || data.data.length === 0) {
        html = "<div style='color:#94a3b8;font-size:13px;'>No saved projects yet.</div>";
    } else {
        data.data.slice().reverse().forEach(project => {
            html += `
                <div class="saved-project">

                    <div onclick="loadProject(${project.id})" style="cursor:pointer;">
                        <strong>${project.business_name}</strong>
                        <span>${project.industry} • ${project.location}</span>
                    </div>

                   <button
    class="delete-btn"
    onclick="deleteProject(event, ${project.id})">
    🗑 Delete
</button>

                </div>
            `;
        });
    }

    document.getElementById("saved-projects").innerHTML = html;
}

async function loadProject(id) {
    document.getElementById("result").innerText = "Loading saved project...";

    const response = await fetch(`/business-ideas/${id}`);
    const project = await response.json();

    document.getElementById("result-title").innerText = project.business_name;

    document.getElementById("business_name").value = project.business_name || "";
    document.getElementById("industry").value = project.industry || "";
    document.getElementById("budget").value = project.budget || "";
    document.getElementById("location").value = project.location || "";
    document.getElementById("target_audience").value = project.target_audience || "";
    document.getElementById("description").value = project.description || "";

    if (project.analysis) {
        showAnalysis(project.analysis);
    } else {
        document.getElementById("metrics").innerHTML = "";
        document.getElementById("result").innerText =
            "This project is saved, but it has not been analyzed yet.";
    }
}

function showAnalysis(analysis) {
    document.getElementById("metrics").innerHTML = `
        <div class="metric">
            <span>Risk Score</span>
            <strong>${analysis.risk_score ?? "-"}%</strong>
        </div>
        <div class="metric">
            <span>Success Probability</span>
            <strong>${analysis.success_probability ?? "-"}%</strong>
        </div>
        <div class="metric">
            <span>Competition</span>
            <strong>${analysis.competition_level ?? "-"}</strong>
        </div>
    `;

    document.getElementById("result").innerHTML = `
        <div class="report-section">
            <h3>Market Analysis</h3>
            <p>${analysis.market_analysis || "No market analysis available."}</p>
        </div>

        <div class="report-section">
            <h3>SWOT Analysis</h3>

            <div class="swot-grid">
                <div class="swot-card">
                    <h4>Strengths</h4>
                    <ul>${(analysis.swot_analysis?.strengths || []).map(item => `<li>${item}</li>`).join("")}</ul>
                </div>

                <div class="swot-card">
                    <h4>Weaknesses</h4>
                    <ul>${(analysis.swot_analysis?.weaknesses || []).map(item => `<li>${item}</li>`).join("")}</ul>
                </div>

                <div class="swot-card">
                    <h4>Opportunities</h4>
                    <ul>${(analysis.swot_analysis?.opportunities || []).map(item => `<li>${item}</li>`).join("")}</ul>
                </div>

                <div class="swot-card">
                    <h4>Threats</h4>
                    <ul>${(analysis.swot_analysis?.threats || []).map(item => `<li>${item}</li>`).join("")}</ul>
                </div>
            </div>
        </div>

        <div class="report-section">
            <h3>Recommendations</h3>
            <ul class="recommendations">
                ${(analysis.recommendations || []).map(item => `<li>${item}</li>`).join("")}
            </ul>
        </div>

        <div class="report-section">
            <h3>Financial Advice</h3>
            <p>${analysis.financial_advice || "No financial advice available."}</p>
        </div>

        <div class="report-section">
            <h3>Marketing Strategy</h3>
            <p>${analysis.marketing_strategy || "No marketing strategy available."}</p>
        </div>

        <div class="final-box">
            <h3>Final Recommendation</h3>
            <p>${analysis.final_recommendation || "No final recommendation available."}</p>
        </div>
    `;
}
async function createAndAnalyze() {
    const idea = {
        business_name: document.getElementById("business_name").value,
        industry: document.getElementById("industry").value,
        budget: parseFloat(document.getElementById("budget").value),
        location: document.getElementById("location").value,
        target_audience: document.getElementById("target_audience").value,
        description: document.getElementById("description").value
    };

    document.getElementById("result-title").innerText = "AI Analysis Result";
    document.getElementById("result").innerText = "Creating business idea...";
    document.getElementById("metrics").innerHTML = "";

    const createResponse = await fetch("/business-ideas", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(idea)
    });

    const created = await createResponse.json();
    const ideaId = created.data.id;

    document.getElementById("result").innerText = "Analyzing with AI...";

    const analyzeResponse = await fetch(`/analyze/${ideaId}`, {
        method: "POST"
    });

    const analysisData = await analyzeResponse.json();
    const analysis = analysisData.analysis;

    showAnalysis(analysis);
    await loadProjects();
}

  async function deleteProject(event, id) {

    event.stopPropagation();

    const confirmDelete =
        confirm("Are you sure you want to delete this project?");

    if (!confirmDelete) return;

    await fetch(`/business-ideas/${id}`, {
        method: "DELETE"
    });

    await loadProjects();

    document.getElementById("result-title").innerText =
        "AI Analysis Result";

    document.getElementById("metrics").innerHTML = "";

    document.getElementById("result").innerText =
        "Project deleted successfully.";
}                      

loadProjects();
</script>
</body>
</html>
    """)