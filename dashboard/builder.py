import re

# Read the original file to extract the script tag at the bottom
with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Extract script text precisely to avoid breaking JS
script_match = re.search(r'(<script type="module">.*?</script>)', text, re.DOTALL)
js_code = script_match.group(1) if script_match else ''

# Replace JS dynamic render templates with Light Theme / Orange
js_code = js_code.replace('hover:bg-white/[0.01]', 'hover:bg-slate-50')
js_code = js_code.replace('bg-indigo-500/10 text-indigo-400', 'bg-orange-50 text-orange-600')
js_code = js_code.replace('border-indigo-500/10', 'border-orange-500/20')
js_code = js_code.replace('border-indigo-500/20', 'border-orange-500/20')
js_code = js_code.replace('text-white group-hover:text-indigo-400', 'text-slate-900 group-hover:text-orange-500')
js_code = js_code.replace('text-slate-400', 'text-slate-500') # Lighten up some midtones
js_code = js_code.replace('text-slate-500 font-mono', 'text-slate-400 font-mono')
js_code = js_code.replace('text-white', 'text-slate-800')
js_code = js_code.replace('text-indigo-400 font-bold', 'text-orange-500 font-bold')
js_code = js_code.replace('text-emerald-400 outfit', 'text-emerald-600 outfit')
js_code = js_code.replace('bg-white/5 text-slate-300', 'bg-slate-100 text-slate-600')
js_code = js_code.replace('border-white/5', 'border-slate-200')
js_code = js_code.replace('group-hover:bg-emerald-500 group-hover:text-black', 'group-hover:bg-emerald-100 group-hover:text-emerald-700')

# Modal updates
js_code = js_code.replace('glass p-8 rounded-[2.5rem]', 'glass-card p-8 rounded-[2.5rem]')
js_code = js_code.replace('bg-indigo-600 text-white text-[10px] font-black rounded-2xl hover:bg-indigo-500', 'bg-orange-500 text-white text-[10px] font-black rounded-2xl hover:bg-orange-400 shadow shadow-orange-500/30')
js_code = js_code.replace('bg-white text-black font-black text-[10px] rounded-2xl hover:bg-slate-200', 'bg-slate-900 text-white font-black text-[10px] rounded-2xl hover:bg-slate-800')
js_code = js_code.replace('bg-white/5 p-4 rounded-2xl border border-white/5', 'bg-slate-50 p-4 rounded-2xl border border-slate-200')
js_code = js_code.replace('text-slate-300 truncate', 'text-slate-700 truncate')

html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>JobAgent AI | Intelligence Dashboard</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Outfit:wght@600;700;800&display=swap" rel="stylesheet">
    <style>
        :root {{ --bg: #f8fafc; --sidebar: #ffffff; --accent: #ea580c; --accent-hover: #f97316; --glass: rgba(255, 255, 255, 0.85); --border: rgba(0, 0, 0, 0.06); }}
        body {{ font-family: 'Inter', sans-serif; background: var(--bg); color: #334155; margin: 0; display: flex; height: 100vh; overflow: hidden; }}
        .outfit {{ font-family: 'Outfit', sans-serif; }}
        
        /* Layout Structure */
        aside {{ width: 260px; background: var(--sidebar); border-right: 1px solid var(--border); display: flex; flex-direction: column; overflow-y: auto; z-index: 20; box-shadow: 4px 0 24px rgba(0,0,0,0.03); }}
        main {{ flex: 1; overflow-y: auto; display: flex; flex-direction: column; scroll-behavior: smooth; }}
        
        /* Glass Components & Animations */
        .glass {{ background: var(--glass); backdrop-filter: blur(24px); -webkit-backdrop-filter: blur(24px); border-bottom: 1px solid var(--border); }}
        .glass-card {{ background: #ffffff; border: 1px solid var(--border); transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1); box-shadow: 0 4px 20px rgba(0, 0, 0, 0.04); }}
        .glass-card:hover {{ border-color: var(--accent-hover); box-shadow: 0 10px 40px rgba(234, 88, 12, 0.12); transform: translateY(-3px); }}
        
        /* Input Styles */
        .f-input {{ background: #ffffff; border: 1px solid #e2e8f0; border-radius: 12px; padding: 12px 14px; font-size: 12px; color: #0f172a; width: 100%; transition: all 0.3s ease; box-shadow: inset 0 2px 4px rgba(0,0,0,0.02); }}
        .f-input:focus {{ outline: none; border-color: var(--accent); background: #ffffff; box-shadow: 0 0 0 4px rgba(234, 88, 12, 0.1); }}
        .f-input::placeholder {{ color: #94a3b8; }}
        select.f-input {{ cursor: pointer; appearance: none; background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' fill='none' viewBox='0 0 24 24' stroke='%2394a3b8'%3E%3Cpath stroke-linecap='round' stroke-linejoin='round' stroke-width='2' d='M19 9l-7 7-7-7'%3E%3C/path%3E%3C/svg%3E"); background-repeat: no-repeat; background-position: right 12px center; background-size: 16px; padding-right: 36px; }}

        /* Custom Scrollbar */
        ::-webkit-scrollbar {{ width: 8px; height: 8px; }}
        ::-webkit-scrollbar-track {{ background: transparent; }}
        ::-webkit-scrollbar-thumb {{ background: #cbd5e1; border-radius: 10px; border: 2px solid var(--bg); }}
        ::-webkit-scrollbar-thumb:hover {{ background: #94a3b8; }}
        
        .grad-text {{ background: linear-gradient(135deg, #ea580c 0%, #f97316 50%, #facc15 100%); background-size: 200% auto; -webkit-background-clip: text; -webkit-text-fill-color: transparent; animation: shine 4s linear infinite; }}
        .sticky-col {{ position: sticky; left: 0; background: inherit; z-index: 10; }}
        
        /* Keyframe Animations */
        @keyframes shine {{ to {{ background-position: 200% center; }} }}
        @keyframes fadeInUp {{
            from {{ opacity: 0; transform: translateY(20px); }}
            to {{ opacity: 1; transform: translateY(0); }}
        }}
        @keyframes slideInLeft {{
            from {{ opacity: 0; transform: translateX(-20px); }}
            to {{ opacity: 1; transform: translateX(0); }}
        }}
        @keyframes pulse-glow {{
            0%, 100% {{ box-shadow: 0 0 15px rgba(234, 88, 12, 0.2); }}
            50% {{ box-shadow: 0 0 25px rgba(234, 88, 12, 0.5); border-color: rgba(234, 88, 12, 0.5); }}
        }}
        
        .animate-fade-in {{ animation: fadeInUp 0.6s cubic-bezier(0.16, 1, 0.3, 1) forwards; opacity: 0; }}
        .animate-slide-left {{ animation: slideInLeft 0.5s cubic-bezier(0.16, 1, 0.3, 1) forwards; opacity: 0; }}
        .delay-100 {{ animation-delay: 100ms; }}
        .delay-200 {{ animation-delay: 200ms; }}
        .delay-300 {{ animation-delay: 300ms; }}
        .glow-node {{ animation: pulse-glow 3s infinite; }}
    </style>
</head>
<body>

    <!-- Sidebar Navigation -->
    <aside class="p-6">
        <div class="flex items-center gap-3 mb-10 px-2 animate-slide-left">
            <div class="w-9 h-9 bg-orange-600 rounded-xl flex items-center justify-center font-black text-lg italic text-white shadow-lg shadow-orange-500/30">J</div>
            <h2 class="outfit text-lg font-bold tracking-tight text-slate-800">JobAgent<span class="text-orange-500">AI</span></h2>
        </div>

        <nav class="flex-1 space-y-1 animate-slide-left delay-100">
            <div class="text-[9px] text-slate-400 font-bold uppercase tracking-widest px-4 mb-4">Operations</div>
            <a href="#" class="flex items-center gap-3 px-4 py-3 bg-orange-50 text-orange-600 rounded-xl font-semibold border border-orange-500/10">
                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6"></path></svg>
                Dashboard
            </a>
            <a href="#" class="flex items-center gap-3 px-4 py-3 text-slate-500 hover:bg-slate-100 hover:text-slate-800 rounded-xl transition-all">
                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"></path></svg>
                Insights
            </a>
        </nav>

        <div class="mt-auto pt-6 border-t border-slate-200 animate-slide-left delay-200">
             <div class="flex items-center gap-3 px-2">
                <div class="w-8 h-8 bg-slate-200 rounded-full border border-slate-300"></div>
                <div class="flex-1 min-w-0">
                    <p class="text-[10px] font-bold text-slate-800 truncate">Cloud Engine</p>
                    <p class="text-[9px] text-slate-500 truncate">joyboy-b6f27</p>
                </div>
            </div>
        </div>
    </aside>

    <!-- Main Content Area -->
    <main class="animate-fade-in delay-100">
        <!-- Header -->
        <header class="p-10 pb-4 flex justify-between items-center h-24 border-b border-slate-200 relative z-10 transition-all hover:bg-slate-50/50">
            <div>
                <h1 class="text-3xl font-black outfit grad-text">Intelligence Command</h1>
                <p class="text-[10px] text-slate-500 font-bold uppercase tracking-widest mt-1">Total Assets: <span id="appCount" class="text-orange-500">0</span></p>
            </div>
            <div class="flex items-center gap-4">
                 <div class="glow-node bg-emerald-50 px-4 py-2 rounded-full border border-emerald-200 text-[10px] font-bold text-emerald-600 transition-all">
                    REAL-TIME NODE ACTIVE
                </div>
            </div>
        </header>

        <!-- Dynamic Filter Bar (Sticky) -->
        <div class="sticky top-0 z-50 glass px-10 py-5 animate-fade-in delay-200">
            <div class="grid grid-cols-2 lg:grid-cols-7 gap-4">
                <div class="space-y-1.5">
                    <label class="text-[9px] text-slate-400 font-bold uppercase tracking-widest pl-1">Search Role / Co.</label>
                    <input id="f-role" type="text" placeholder="AI Engineer, Google..." class="f-input">
                </div>
                <div class="space-y-1.5">
                    <label class="text-[9px] text-slate-400 font-bold uppercase tracking-widest pl-1">Platform</label>
                    <select id="f-platform" class="f-input">
                        <option value="">All Platforms</option>
                        <option value="LinkedIn">LinkedIn</option>
                        <option value="Naukri">Naukri</option>
                        <option value="Indeed">Indeed</option>
                        <option value="Wellfound">Wellfound</option>
                        <option value="Direct">Direct Company</option>
                    </select>
                </div>
                <div class="space-y-1.5">
                    <label class="text-[9px] text-slate-400 font-bold uppercase tracking-widest pl-1">Status</label>
                    <select id="f-status" class="f-input">
                        <option value="">All Statuses</option>
                        <option value="Applied">Applied</option>
                        <option value="Interviewing">Interviewing</option>
                        <option value="Offer">Offer</option>
                        <option value="Rejected">Rejected</option>
                    </select>
                </div>
                <div class="space-y-1.5">
                    <label class="text-[9px] text-slate-400 font-bold uppercase tracking-widest pl-1">Location</label>
                    <input id="f-location" type="text" placeholder="Remote, India..." class="f-input">
                </div>
                 <div class="space-y-1.5">
                    <label class="text-[9px] text-slate-400 font-bold uppercase tracking-widest pl-1">Date Applied</label>
                    <select id="f-date" class="f-input">
                        <option value="">All Time</option>
                        <option value="today">Applied Today</option>
                        <option value="week">Past 7 Days</option>
                        <option value="month">This Month</option>
                    </select>
                </div>
                <div class="space-y-1.5">
                    <label class="text-[9px] text-slate-400 font-bold uppercase tracking-widest pl-1">Financial</label>
                    <input id="f-salary" type="text" placeholder="LPA, $k..." class="f-input">
                </div>
                <div class="flex items-end">
                    <button id="resetFilters" class="w-full h-[40px] bg-slate-900 border border-slate-700 text-[10px] text-white font-bold uppercase tracking-widest hover:bg-slate-800 transition-all rounded-xl shadow-[0_4px_12px_rgba(0,0,0,0.1)] hover:shadow-[0_4px_20px_rgba(0,0,0,0.2)]">Reset</button>
                </div>
            </div>
        </div>

        <!-- Main Intelligence Table -->
        <div class="p-10 flex-1 overflow-x-auto min-h-0 animate-fade-in delay-300">
            <div class="glass-card rounded-[2rem] overflow-hidden min-w-[1200px]">
                <table class="w-full text-left border-collapse">
                    <thead>
                        <tr class="bg-slate-50 text-[9px] font-black uppercase text-slate-400 tracking-widest border-b border-slate-200">
                            <th class="px-6 py-5">Platform</th>
                            <th class="px-6 py-5">Date</th>
                            <th class="px-6 py-5">Role & Intelligence</th>
                            <th class="px-6 py-5">Company</th>
                            <th class="px-6 py-5 group relative tool cursor-help" data-tip="Contact person detected by AI.">
                                HR Intelligence ⓘ
                            </th>
                            <th class="px-6 py-5">Location</th>
                            <th class="px-6 py-5">Financials</th>
                            <th class="px-6 py-5">Status</th>
                        </tr>
                    </thead>
                    <tbody id="jobList" class="divide-y divide-slate-100 border-b border-slate-200">
                        <!-- Populated via JS -->
                    </tbody>
                </table>
            </div>

            <div id="noData" class="hidden py-40 text-center text-slate-500 glass-card rounded-[2rem] mt-6 transition-all border-dashed border-2">
                <div class="mb-6 w-16 h-16 bg-slate-50 rounded-2xl mx-auto flex items-center justify-center border border-slate-200 shadow-sm">
                    <svg class="w-8 h-8 text-slate-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
                </div>
                <p class="text-xl outfit font-bold text-slate-800">No results matching your filters.</p>
                <p class="text-sm mt-2 font-medium text-slate-500">Adjust your parameters or reset to see all telemetry.</p>
            </div>
        </div>
    </main>

    <!-- Deep Intelligence Portal (Modal) -->
    <div id="detailModal" class="hidden fixed inset-0 bg-slate-900/60 backdrop-blur-md z-50 flex items-center justify-center p-8 animate-fade-in">
        <div class="glass-card max-w-5xl w-full max-h-[90vh] overflow-hidden rounded-[3rem] relative flex flex-col shadow-2xl">
            <button onclick="closeModal()" class="absolute top-10 right-10 w-12 h-12 rounded-full bg-slate-100 flex items-center justify-center text-slate-500 hover:text-slate-900 hover:bg-slate-200 transition-all hover:rotate-90 z-20">
                <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path></svg>
            </button>
            <div id="modalContent" class="overflow-y-auto p-16 custom-scrollbar"></div>
        </div>
    </div>

    <!-- Tooltip Simple Helper -->
    <style>
        .tool {{ position: relative; }}
        .tool:hover::after {{
            content: attr(data-tip); position: absolute; bottom: 100%; left: 0;
            padding: 8px 12px; background: #0f172a; color: #fff; font-size: 10px; border-radius: 8px; width: 220px;
            box-shadow: 0 10px 25px -3px rgba(0,0,0,0.2); z-index: 100; border: 1px solid rgba(255,255,255,0.1);
        }}
    </style>

    {js_code}
</body>
</html>
"""

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated successfully")
