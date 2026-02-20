import { useState } from 'react';

const API = 'http://localhost:8000';

const defaultCampaign = {
  product_name: 'AI CRM Assistant',
  target_audience: 'SaaS sales managers',
  channel: 'LinkedIn',
  goal: 'Book demos'
};

export default function App() {
  const [campaign, setCampaign] = useState(defaultCampaign);
  const [lead, setLead] = useState({ company_size: 250, budget: 40000, engagement_level: 7, industry_fit: 8 });
  const [output, setOutput] = useState('Run a workflow to see AI + analytics output.');

  const runCampaign = async () => {
    const res = await fetch(`${API}/campaigns/generate`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(campaign)
    });
    const data = await res.json();
    setOutput(data.content || JSON.stringify(data, null, 2));
  };

  const runLeadScore = async () => {
    const res = await fetch(`${API}/leads/score`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ ...lead, company_size: Number(lead.company_size), budget: Number(lead.budget) })
    });
    const data = await res.json();
    setOutput(`Lead score: ${data.score} (${data.tier})\n${JSON.stringify(data.rationale, null, 2)}`);
  };

  return (
    <main className="container">
      <h1>MarketMind</h1>
      <p>Generative AI-powered sales and marketing intelligence platform.</p>

      <section className="card">
        <h2>Campaign Generator</h2>
        <input value={campaign.product_name} onChange={(e) => setCampaign({ ...campaign, product_name: e.target.value })} placeholder="Product" />
        <input value={campaign.target_audience} onChange={(e) => setCampaign({ ...campaign, target_audience: e.target.value })} placeholder="Audience" />
        <input value={campaign.channel} onChange={(e) => setCampaign({ ...campaign, channel: e.target.value })} placeholder="Channel" />
        <input value={campaign.goal} onChange={(e) => setCampaign({ ...campaign, goal: e.target.value })} placeholder="Goal" />
        <button onClick={runCampaign}>Generate Campaign</button>
      </section>

      <section className="card">
        <h2>Lead Scoring</h2>
        <label>Company Size</label>
        <input type="number" value={lead.company_size} onChange={(e) => setLead({ ...lead, company_size: e.target.value })} />
        <label>Budget</label>
        <input type="number" value={lead.budget} onChange={(e) => setLead({ ...lead, budget: e.target.value })} />
        <button onClick={runLeadScore}>Score Lead</button>
      </section>

      <section className="card output">
        <h2>Output</h2>
        <pre>{output}</pre>
      </section>
    </main>
  );
}
