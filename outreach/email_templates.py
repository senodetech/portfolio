"""
High-Converting Email Templates for Small Business Owners & Agency Leads
"""

def get_email_subject(owner_name, business_name):
    return f"A faster, zero-clutter agile workspace for {business_name} ⚡"

def get_html_email(owner_name, business_name, custom_note, pain_point):
    return f"""<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <style>
    body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; line-height: 1.6; color: #1e293b; margin: 0; padding: 0; }}
    .wrapper {{ max-width: 600px; margin: 20px auto; border: 1px solid #e2e8f0; border-radius: 12px; overflow: hidden; background: #ffffff; }}
    .header {{ background: linear-gradient(135deg, #0f172a 0%, #1e3a8a 100%); padding: 30px 25px; text-align: center; color: #ffffff; }}
    .logo-badge {{ display: inline-block; background: rgba(56, 189, 248, 0.2); border: 1px solid #38bdf8; color: #38bdf8; padding: 4px 12px; border-radius: 20px; font-size: 12px; font-weight: 700; letter-spacing: 1px; text-transform: uppercase; margin-bottom: 10px; }}
    .title {{ font-size: 22px; font-weight: 800; margin: 0; color: #ffffff; }}
    .content {{ padding: 30px 25px; }}
    .greeting {{ font-size: 16px; font-weight: 600; margin-bottom: 15px; color: #0f172a; }}
    .card {{ background: #f8fafc; border: 1px solid #e2e8f0; border-left: 4px solid #2563eb; border-radius: 8px; padding: 15px; margin: 20px 0; }}
    .card h4 {{ margin: 0 0 8px 0; color: #1e3a8a; font-size: 15px; }}
    .features {{ list-style: none; padding: 0; margin: 15px 0; }}
    .features li {{ padding: 6px 0; font-size: 14px; display: flex; align-items: center; gap: 8px; }}
    .cta-btn {{ display: inline-block; background: #2563eb; color: #ffffff !important; text-decoration: none; padding: 12px 26px; font-size: 15px; font-weight: 700; border-radius: 6px; margin: 15px 0; }}
    .footer {{ background: #f1f5f9; padding: 20px; text-align: center; font-size: 12px; color: #64748b; border-top: 1px solid #e2e8f0; }}
  </style>
</head>
<body>
  <div class="wrapper">
    <div class="header">
      <div class="logo-badge">ApexTasks Agile Workspace</div>
      <h1 class="title">Built for Fast-Moving Teams</h1>
    </div>
    <div class="content">
      <div class="greeting">Hi {owner_name},</div>
      <p>{custom_note}</p>
      <p>Managing day-to-day client deliverables and team sprints shouldn't feel like navigating slow, bloated enterprise software with endless menus.</p>
      
      <div class="card">
        <h4>⚡ Why Small Business Teams Love ApexTasks:</h4>
        <ul class="features">
          <li><strong>🚀 Instant Sub-50ms Operations:</strong> Zero lag drag-and-drop Kanban built with modern Angular Signals.</li>
          <li><strong>🛡️ Real-Time Team Control:</strong> Role-based permissions, organization boards, and security audit logs.</li>
          <li><strong>💰 No Subscription Clutter:</strong> Lightweight, clean, and instant access with zero onboarding friction.</li>
        </ul>
      </div>

      <p>I’ve made a live interactive version ready to explore immediately (no sign-up required):</p>
      <div style="text-align: center;">
        <a href="https://apextodo-omega.vercel.app/" class="cta-btn">Explore Live ApexTasks Workspace ↗</a>
      </div>

      <p style="font-size: 14px; margin-top: 25px;">
        Would you be open to a quick 5-minute chat to see how this can simplify task workflows for <strong>{business_name}</strong>?
      </p>

      <p style="margin-top: 20px; font-size: 14px;">
        Best regards,<br>
        <strong>Senapathy (Sena)</strong><br>
        <span style="color: #64748b;">Full Stack Engineer &amp; Solution Architect</span><br>
        <a href="https://senodetech.github.io/portfolio" style="color: #2563eb; text-decoration: none;">Portfolio: senodetech.github.io/portfolio</a>
      </p>
    </div>
    <div class="footer">
      Sent with ❤️ by Senapathy &bull; Bangalore, India &bull; <a href="mailto:avsentech@gmail.com?subject=Unsubscribe" style="color: #64748b;">Unsubscribe</a>
    </div>
  </div>
</body>
</html>"""

def get_text_email(owner_name, business_name, custom_note, pain_point):
    return f"""Hi {owner_name},

{custom_note}

Managing day-to-day team deliverables shouldn't feel like navigating slow, bloated enterprise software with endless menus.

I built ApexTasks (https://apextodo-omega.vercel.app/) — a lightning-fast agile workspace designed specifically for agile teams and growing businesses:

• Sub-50ms Operations: Instant drag-and-drop Kanban with zero latency.
• Real-Time Team Boards: Assign tasks, track priorities, and inspect audit logs.
• Lightweight & Simple: No subscription bloat or complex training required.

You can try the live demo immediately here:
👉 https://apextodo-omega.vercel.app/

Would you be open to a quick 5-minute chat to see how this could streamline sprint tracking for {business_name}?

Best regards,
Senapathy (Sena)
Full Stack Engineer & Solution Architect
Portfolio: https://senodetech.github.io/portfolio
"""