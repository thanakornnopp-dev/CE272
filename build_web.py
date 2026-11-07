import json

html_code = r'''<!DOCTYPE html>
<html lang="th" class="scroll-smooth">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CE272 สรุปเตรียมสอบวิชาปฏิบัติการกลศาสตร์ของไหล | บทที่ 9 การทดสอบเครื่องสูบน้ำ (ฉบับคนไม่รู้อะไรเลย)</title>
    <!-- Tailwind CSS -->
    <script src="https://cdn.tailwindcss.com"></script>
    <!-- Chart.js -->
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <!-- FontAwesome / Phosphor Icons -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Chakra+Petch:wght@400;500;600;700&family=Sarabun:ital,wght@0,300;0,400;0,500;0,600;0,700;1,400&display=swap" rel="stylesheet">
    <!-- MathJax 3 -->
    <script>
    window.MathJax = {
      tex: {
        inlineMath: [["\\(", "\\)"]],
        displayMath: [["$$", "$$"], ["\\[", "\\]"]],
        processEscapes: true
      },
      options: {
        skipHtmlTags: ["script", "noscript", "style", "textarea", "pre", "code"]
      }
    };
    </script>
    <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
    <style>
        body {
            font-family: 'Sarabun', sans-serif;
            background-color: #0f172a;
            color: #f1f5f9;
        }
        h1, h2, h3, h4, .font-heading {
            font-family: 'Chakra Petch', sans-serif;
        }
        .water-flow {
            stroke-dasharray: 8;
            animation: flow 1s linear infinite;
        }
        @keyframes flow {
            from { stroke-dashoffset: 16; }
            to { stroke-dashoffset: 0; }
        }
        .glass-card {
            background: rgba(30, 41, 59, 0.7);
            backdrop-filter: blur(12px);
            border: 1px solid rgba(255, 255, 255, 0.08);
        }
        .glass-card-hover:hover {
            border-color: rgba(56, 189, 248, 0.4);
            transform: translateY(-2px);
            transition: all 0.25s ease;
        }
        .trap-badge {
            background: linear-gradient(135deg, #ef4444, #b91c1c);
            color: white;
            box-shadow: 0 4px 12px rgba(239, 68, 68, 0.3);
        }
    </style>
</head>
<body class="min-h-screen text-slate-200">

    <!-- Top Announcement Bar -->
    <div class="bg-gradient-to-r from-sky-600 via-indigo-600 to-purple-600 text-white text-xs sm:text-sm font-medium py-2 px-4 text-center shadow-md">
        <span>⚡ <strong>CE272 ติวเข้มก่อนสอบ:</strong> เจาะลึกแนวข้อสอบปรนัยบทที่ 9 (เครื่องสูบน้ำ) พร้อมจุดดักคะแนน "มล. เป็น ลบ.ม." & "ปรับหน้า Z"</span>
    </div>

    <!-- Navigation Header -->
    <header class="sticky top-0 z-50 glass-card border-b border-slate-700/60 shadow-lg px-4 sm:px-8 py-4 flex items-center justify-between">
        <div class="flex items-center gap-3">
            <div class="w-10 h-10 rounded-xl bg-gradient-to-tr from-sky-500 to-indigo-500 flex items-center justify-center text-white font-bold text-lg shadow-md shadow-sky-500/20">
                CE
            </div>
            <div>
                <a href="#hero" class="text-lg sm:text-xl font-bold tracking-tight text-white font-heading flex items-center gap-2">
                    CE 272 <span class="text-xs px-2 py-0.5 rounded-full bg-sky-500/20 text-sky-400 border border-sky-500/30 font-normal">Fluid Mechanics Lab</span>
                </a>
                <p class="text-[11px] text-slate-400">บทที่ 9 การทดสอบเครื่องสูบน้ำ (Pump Test) • ฉบับคนไม่รู้อะไรเลย</p>
            </div>
        </div>
        <nav class="hidden md:flex items-center gap-5 text-sm font-medium text-slate-300">
            <a href="#concept" class="hover:text-sky-400 transition-colors">1. ปูพื้นฐาน</a>
            <a href="#flow-diagrams" class="hover:text-sky-400 transition-colors">2. เข้าทางไหนออกทางไหน</a>
            <a href="#datum-z" class="hover:text-sky-400 transition-colors">3. ปรับหน้า Z</a>
            <a href="#unit-trap" class="hover:text-sky-400 transition-colors">4. จุดดัก มล. $\to$ ลบ.ม.</a>
            <a href="#power" class="hover:text-sky-400 transition-colors">5. คำนวณ Power</a>
            <a href="#chart-section" class="hover:text-sky-400 transition-colors">6. ดูกราฟ iPad</a>
            <a href="#quiz-section" class="px-3.5 py-1.5 rounded-xl bg-sky-500 hover:bg-sky-400 text-white font-semibold transition-all shadow-md shadow-sky-500/25 flex items-center gap-1.5">
                <i class="fa-solid fa-pen-to-square"></i> ตะลุยข้อสอบจำลอง
            </a>
        </nav>
    </header>

    <!-- Hero Section -->
    <section id="hero" class="max-w-6xl mx-auto px-4 pt-10 pb-8 text-center">
        <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-slate-800 text-sky-400 text-xs font-semibold border border-slate-700 mb-4">
            <i class="fa-solid fa-graduation-cap"></i> สรุปเนื้อหาตามลายมือแนวข้อสอบของอาจารย์หน้า 52 และ 53
        </div>
        <h1 class="text-3xl sm:text-5xl font-extrabold text-white tracking-tight mb-4 font-heading leading-tight">
            เตรียมสอบปฏิบัติการกลศาสตร์ของไหล<br>
            <span class="bg-gradient-to-r from-sky-400 via-indigo-300 to-purple-400 bg-clip-text text-transparent">บทที่ 9: การทดสอบเครื่องสูบน้ำ (Pump Test)</span>
        </h1>
        <p class="text-base sm:text-lg text-slate-300 max-w-3xl mx-auto font-light leading-relaxed mb-6">
            อาจารย์ออก <strong class="text-amber-400 font-semibold">ข้อสอบปรนัย (กากบาท) 1 ข้อ</strong> ให้รูปมา 1-3 รูป มีสูตรให้ครบ! 
            แต่ดักคะแนนเรื่อง <strong class="text-red-400 underline decoration-red-500 underline-offset-4 font-semibold">ทางน้ำเข้า-ออก, การปรับหน้า Z, และการแปลงหน่วย มล. เป็น ลบ.ม.</strong> 
            เว็บนี้สรุปให้จบในหน้าเดียว อ่าน 15 นาทีพร้อมทำข้อสอบได้ทันที!
        </p>

        <!-- Key Exam Takeaway Cards -->
        <div class="grid grid-cols-1 sm:grid-cols-3 gap-4 max-w-4xl mx-auto text-left mt-6">
            <div class="glass-card p-4 rounded-2xl border-l-4 border-l-sky-500">
                <div class="text-xs text-sky-400 font-semibold mb-1 flex items-center gap-1.5">
                    <i class="fa-solid fa-arrows-split-up-and-left"></i> ถามเรื่องระบบ
                </div>
                <div class="font-bold text-white text-base">เข้าทางไหน? ออกทางไหน?</div>
                <p class="text-xs text-slate-400 mt-1">ดูว่าปั๊มเดี่ยว อนุกรม หรือขนาน วาล์วไหนเปิด-ปิด น้ำไหลผ่านเกจตัวไหน</p>
            </div>
            <div class="glass-card p-4 rounded-2xl border-l-4 border-l-amber-500">
                <div class="text-xs text-amber-400 font-semibold mb-1 flex items-center gap-1.5">
                    <i class="fa-solid fa-ruler-vertical"></i> ถามเรื่องค่าแก้ระดับ
                </div>
                <div class="font-bold text-white text-base">ต้องปรับหน้า Z อย่างไร?</div>
                <p class="text-xs text-slate-400 mt-1">เกจทางเข้ากับทางออกอยู่คนละระดับความสูง ต้องบวกหรือลบ \(H_d\)</p>
            </div>
            <div class="glass-card p-4 rounded-2xl border-l-4 border-l-red-500">
                <div class="text-xs text-red-400 font-semibold mb-1 flex items-center gap-1.5">
                    <i class="fa-solid fa-bolt"></i> คำนวณ Power & หน่วย
                </div>
                <div class="font-bold text-white text-base">มล. $\to$ ลบ.ม. & \(P = \gamma QH\)</div>
                <p class="text-xs text-slate-400 mt-1">แทนค่าสูตรกำลังชลศาสตร์ ระวังเรื่องตัวเลขหลอกจากการแปลงหน่วย</p>
            </div>
        </div>
    </section>

    <!-- SECTION 1: ปูพื้นฐานฉบับคนไม่รู้อะไรเลย -->
    <section id="concept" class="max-w-6xl mx-auto px-4 py-8">
        <div class="glass-card rounded-3xl p-6 sm:p-8 border border-slate-700/60 shadow-xl">
            <div class="flex items-center gap-3 mb-6">
                <span class="w-8 h-8 rounded-xl bg-sky-500/20 text-sky-400 border border-sky-500/30 flex items-center justify-center font-bold font-heading">1</span>
                <div>
                    <h2 class="text-xl sm:text-2xl font-bold text-white font-heading">ปูพื้นฐานแบบเข้าใจง่ายที่สุด (ฉบับคนไม่รู้อะไรเลย)</h2>
                    <p class="text-xs sm:text-sm text-slate-400">เข้าใจความหมายของตัวแปรใน 3 นาที</p>
                </div>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-2 gap-6 text-sm">
                <!-- Concept Card 1: Head -->
                <div class="bg-slate-800/80 p-5 rounded-2xl border border-slate-700">
                    <div class="flex items-center gap-2 text-sky-400 font-bold mb-2">
                        <i class="fa-solid fa-water"></i> 1. Head (ความสูงของน้ำ: \(H\)) คืออะไร?
                    </div>
                    <p class="text-slate-300 leading-relaxed text-xs sm:text-sm">
                        ในแล็ปนี้เราไม่ได้พูดถึงความดันเป็นหน่วย Pascal หรือ Bar แต่เรามองความดันในรูป <strong>"ความสูงของลำน้ำที่ปั๊มสามารถส่งน้ำขึ้นไปได้"</strong> มีหน่วยเป็น <strong>เมตรของน้ำ (m Water)</strong>
                    </p>
                    <div class="mt-3 p-3 bg-slate-900/80 rounded-xl border border-slate-700/50 text-xs text-slate-300">
                        💡 <strong>ตัวอย่าง:</strong> ถ้าปั๊มมี Total Head \(H = 18\text{ m}\) แปลว่าปั๊มตัวนี้มีแรงดันมากพอที่จะดันน้ำขึ้นตึกสูง 18 เมตรได้!
                    </div>
                </div>

                <!-- Concept Card 2: Discharge -->
                <div class="bg-slate-800/80 p-5 rounded-2xl border border-slate-700">
                    <div class="flex items-center gap-2 text-emerald-400 font-bold mb-2">
                        <i class="fa-solid fa-faucet-drip"></i> 2. Discharge (อัตราการไหล: \(Q\)) คืออะไร?
                    </div>
                    <p class="text-slate-300 leading-relaxed text-xs sm:text-sm">
                        คือ <strong>"ปริมาณน้ำที่ไหลออกมาต่อหนึ่งวินาที"</strong> คำนวณจากเอา ปริมาตร (\(\text{Volume}\)) หารด้วย เวลา (\(\text{Time}\)):
                    </p>
                    <div class="mt-3 p-3 bg-slate-900/80 rounded-xl border border-slate-700/50 text-xs text-emerald-300 font-mono">
                        \[Q = \frac{\text{Volume}}{\text{Time}} \quad \left[\text{ลิตร/วินาที}\right] \implies \text{หาร 1,000} \to \left[\text{m}^3/\text{s}\right]\]
                    </div>
                </div>

                <!-- Concept Card 3: Datum Correction -->
                <div class="bg-slate-800/80 p-5 rounded-2xl border border-slate-700">
                    <div class="flex items-center gap-2 text-amber-400 font-bold mb-2">
                        <i class="fa-solid fa-arrows-up-down"></i> 3. ทำไมต้องมี "ค่าปรับหน้า Z" (\(H_d\))?
                    </div>
                    <p class="text-slate-300 leading-relaxed text-xs sm:text-sm">
                        สมการเบอร์นูลลี่บอกว่า พลังงานรวมต้องคิดทั้งความดัน (\(P/\gamma\)) และระดับความสูง (\(Z\)) 
                        เมื่อเกจวัดความดันขาออก (\(h_o\)) ติดตั้งอยู่สูงกว่าเกจขาเข้า (\(h_1\)) เราจึงต้อง <strong>บวกชดเชยความต่างระดับ (\(Z_2 - Z_1\))</strong> เข้าไปด้วย เรียกว่า \(H_d\)
                    </p>
                    <div class="mt-3 p-3 bg-slate-900/80 rounded-xl border border-slate-700/50 text-xs text-amber-300">
                        \[H_{\text{total}} = \text{ความดันออก} - \text{ความดันเข้า} + \text{ค่าแก้ระดับ } H_d\]
                    </div>
                </div>

                <!-- Concept Card 4: Series vs Parallel -->
                <div class="bg-slate-800/80 p-5 rounded-2xl border border-slate-700">
                    <div class="flex items-center gap-2 text-purple-400 font-bold mb-2">
                        <i class="fa-solid fa-network-wired"></i> 4. ต่ออนุกรม vs ต่อขนาน ต่างกันอย่างไร?
                    </div>
                    <div class="space-y-2 text-xs sm:text-sm text-slate-300">
                        <div>• <strong class="text-purple-300">ต่ออนุกรม (Series):</strong> น้ำไหลเรียงตัว ปั๊ม 1 ส่งให้ปั๊ม 2 $\to$ <strong>Head เพิ่มเป็น 2 เท่า (\(2H\))</strong> เหมาะกับส่งน้ำขึ้นตึกสูง</div>
                        <div>• <strong class="text-emerald-300">ต่อขนาน (Parallel):</strong> ปั๊ม 2 ตัวช่วยกันสูบน้ำลงท่อรวม $\to$ <strong>อัตราไหลเพิ่มเป็น 2 เท่า (\(2Q\))</strong> เหมาะกับระบายน้ำท่วม</div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- SECTION 2: 3 รูปภาพข้อสอบจริง "เข้าทางไหน ออกทางไหน" -->
    <section id="flow-diagrams" class="max-w-6xl mx-auto px-4 py-8">
        <div class="glass-card rounded-3xl p-6 sm:p-8 border border-slate-700/60 shadow-xl">
            <div class="flex items-center gap-3 mb-6">
                <span class="w-8 h-8 rounded-xl bg-indigo-500/20 text-indigo-400 border border-indigo-500/30 flex items-center justify-center font-bold font-heading">2</span>
                <div>
                    <h2 class="text-xl sm:text-2xl font-bold text-white font-heading">เจาะลึก 3 รูปภาพข้อสอบ: "เข้าทางไหน ออกทางไหน วาล์วไหนเปิด-ปิด"</h2>
                    <p class="text-xs sm:text-sm text-slate-400">อ้างอิงรูปที่ 9.3, 9.4 และ 9.5 ในคู่มือปฏิบัติการ (หน้า 50 - 52)</p>
                </div>
            </div>

            <!-- Tab Switcher for Configurations -->
            <div class="flex flex-wrap gap-2 mb-6 border-b border-slate-700 pb-4">
                <button onclick="switchTab('single')" id="tab-btn-single" class="px-4 py-2 rounded-xl text-xs sm:text-sm font-semibold bg-sky-500 text-white shadow-md transition-all">
                    รูปที่ 1: เครื่องสูบน้ำตัวเดียว (Single)
                </button>
                <button onclick="switchTab('series')" id="tab-btn-series" class="px-4 py-2 rounded-xl text-xs sm:text-sm font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700 transition-all">
                    รูปที่ 2: สองตัวต่ออนุกรม (Series - 2H)
                </button>
                <button onclick="switchTab('parallel')" id="tab-btn-parallel" class="px-4 py-2 rounded-xl text-xs sm:text-sm font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700 transition-all">
                    รูปที่ 3: สองตัวต่อขนาน (Parallel - 2Q)
                </button>
            </div>

            <!-- CONFIG 1: SINGLE PUMP -->
            <div id="config-single" class="config-view space-y-6">
                <div class="grid grid-cols-1 lg:grid-cols-12 gap-6 items-center">
                    <!-- Diagram SVG -->
                    <div class="lg:col-span-7 bg-slate-900/90 p-4 sm:p-6 rounded-2xl border border-slate-700 text-center relative overflow-hidden">
                        <span class="absolute top-3 left-3 text-xs font-mono px-2 py-0.5 rounded bg-sky-500/20 text-sky-300 border border-sky-500/30">รูปที่ 9.3 เครื่องสูบน้ำตัวเดียว</span>
                        <!-- SVG Animation for Single Pump -->
                        <svg viewBox="0 0 500 280" class="w-full h-auto mx-auto my-2">
                            <!-- Sump Tank -->
                            <rect x="40" y="160" width="120" height="90" fill="#1e293b" stroke="#475569" stroke-width="2" rx="6" />
                            <text x="100" y="210" fill="#94a3b8" font-size="11" text-anchor="middle">Sump Tank</text>
                            <text x="100" y="225" fill="#64748b" font-size="9" text-anchor="middle">(ถังพักน้ำด้านล่าง)</text>

                            <!-- Pipe: Sump to Pump -->
                            <path d="M 160 210 L 220 210" fill="none" stroke="#38bdf8" stroke-width="6" class="water-flow" />
                            <!-- Inlet Gauge (h1) -->
                            <line x1="200" y1="210" x2="200" y2="160" stroke="#f59e0b" stroke-width="2" />
                            <circle cx="200" cy="150" r="14" fill="#f59e0b" stroke="#ffffff" stroke-width="1.5" />
                            <text x="200" y="154" fill="#000" font-size="10" font-weight="bold" text-anchor="middle">h₁</text>
                            <text x="200" y="130" fill="#f59e0b" font-size="10" text-anchor="middle">Inlet Gauge (2 cm)</text>

                            <!-- Pump 1 -->
                            <circle cx="250" cy="210" r="30" fill="#0284c7" stroke="#38bdf8" stroke-width="3" />
                            <text x="250" y="215" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle">ปั๊มเดี่ยว</text>

                            <!-- Pipe: Pump to Outlet Valve -->
                            <path d="M 250 180 L 250 90 L 370 90" fill="none" stroke="#38bdf8" stroke-width="6" class="water-flow" />
                            <!-- Outlet Gauge (ho) -->
                            <line x1="250" y1="130" x2="290" y2="130" stroke="#f43f5e" stroke-width="2" />
                            <circle cx="305" cy="130" r="14" fill="#f43f5e" stroke="#ffffff" stroke-width="1.5" />
                            <text x="305" y="134" fill="#ffffff" font-size="10" font-weight="bold" text-anchor="middle">hₒ</text>
                            <text x="310" y="110" fill="#f43f5e" font-size="10" text-anchor="middle">Outlet Gauge (17 cm)</text>

                            <!-- Discharge Valve -->
                            <polygon points="370,80 390,90 370,100" fill="#10b981" />
                            <polygon points="410,80 390,90 410,100" fill="#10b981" />
                            <circle cx="390" cy="90" r="3" fill="#ffffff" />
                            <text x="390" y="70" fill="#10b981" font-size="10" font-weight="bold" text-anchor="middle">วาล์วเปิด (Discharge Valve)</text>

                            <!-- Flow Out to Volumetric Tank -->
                            <path d="M 410 90 L 460 90 L 460 140" fill="none" stroke="#38bdf8" stroke-width="6" class="water-flow" />
                            <rect x="420" y="140" width="70" height="70" fill="#334155" stroke="#64748b" stroke-width="1.5" rx="4" />
                            <text x="455" y="175" fill="#cbd5e1" font-size="10" text-anchor="middle">ถังวัดน้ำ</text>
                            <text x="455" y="190" fill="#94a3b8" font-size="8" text-anchor="middle">(Volumetric Tank)</text>

                            <!-- Flow Direction Arrow Indicators -->
                            <marker id="arrow" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
                                <path d="M 0 0 L 10 5 L 0 10 z" fill="#38bdf8"/>
                            </marker>
                        </svg>
                    </div>

                    <!-- Explanation -->
                    <div class="lg:col-span-5 space-y-4">
                        <div class="p-4 rounded-2xl bg-sky-950/40 border border-sky-800/60">
                            <h3 class="font-bold text-sky-400 text-base mb-2 flex items-center gap-2">
                                <i class="fa-solid fa-circle-check"></i> ทางเดินน้ำของเครื่องสูบน้ำตัวเดียว
                            </h3>
                            <ul class="text-xs sm:text-sm text-slate-300 space-y-2 list-disc list-inside">
                                <li><strong>ทางเข้า (Inlet):</strong> น้ำถูกดูดจาก <strong>Sump Tank</strong> ผ่านท่อทางดูด และวัดความดันที่ <strong>Pressure Gauge Inlet (\(h_1\))</strong></li>
                                <li><strong>ทางออก (Outlet):</strong> ปั๊มดันน้ำขึ้นด้านบน ผ่าน <strong>Pressure Gauge Outlet (\(h_o\))</strong> ออกทาง <strong>Discharge Control Valve</strong> ไปลงถังวัดปริมาตร</li>
                                <li><strong>วาล์วที่ต้องเปิด:</strong> เปิด Hydraulic Bench Sump Drain Valve และเปิด Discharge Control Valve</li>
                            </ul>
                        </div>
                        <div class="p-4 rounded-2xl bg-slate-800 border border-slate-700 text-xs text-slate-300">
                            <strong class="text-amber-400 block mb-1">📐 สรุปค่าแก้ระดับ Z (คู่มือหน้า 49):</strong>
                            \(h_d(\text{inlet}) = 0.02\text{ m}\) (2 cm), \(h_d(\text{outlet}) = 0.17\text{ m}\) (17 cm)<br>
                            $$\mathbf{H_d = 0.17 - 0.02 = +0.15\text{ m}}$$
                        </div>
                    </div>
                </div>
            </div>

            <!-- CONFIG 2: SERIES PUMPS -->
            <div id="config-series" class="config-view hidden space-y-6">
                <div class="grid grid-cols-1 lg:grid-cols-12 gap-6 items-center">
                    <!-- Diagram SVG -->
                    <div class="lg:col-span-7 bg-slate-900/90 p-4 sm:p-6 rounded-2xl border border-slate-700 text-center relative overflow-hidden">
                        <span class="absolute top-3 left-3 text-xs font-mono px-2 py-0.5 rounded bg-purple-500/20 text-purple-300 border border-purple-500/30">รูปที่ 9.4 เครื่องสูบน้ำต่ออนุกรม</span>
                        <!-- SVG Animation for Series Pumps -->
                        <svg viewBox="0 0 500 280" class="w-full h-auto mx-auto my-2">
                            <!-- Sump Tank -->
                            <rect x="20" y="160" width="90" height="90" fill="#1e293b" stroke="#475569" stroke-width="2" rx="6" />
                            <text x="65" y="210" fill="#94a3b8" font-size="10" text-anchor="middle">Sump Tank</text>

                            <!-- Pipe to Pump 1 -->
                            <path d="M 110 210 L 150 210" fill="none" stroke="#a855f7" stroke-width="6" class="water-flow" />
                            <!-- Pump 1 (Bench Pump) -->
                            <circle cx="180" cy="210" r="26" fill="#7e22ce" stroke="#c084fc" stroke-width="2.5" />
                            <text x="180" y="214" fill="#ffffff" font-size="9" font-weight="bold" text-anchor="middle">ปั๊มตัวที่ 1</text>
                            <text x="180" y="170" fill="#c084fc" font-size="9" text-anchor="middle">Bench Inlet (24 cm)</text>

                            <!-- Pipe: Pump 1 to Pump 2 -->
                            <path d="M 206 210 L 260 210" fill="none" stroke="#a855f7" stroke-width="6" class="water-flow" />
                            <text x="233" y="200" fill="#e9d5ff" font-size="8" text-anchor="middle">ส่งต่อแรงดัน</text>

                            <!-- Pump 2 (Second Pump) -->
                            <circle cx="290" cy="210" r="26" fill="#7e22ce" stroke="#c084fc" stroke-width="2.5" />
                            <text x="290" y="214" fill="#ffffff" font-size="9" font-weight="bold" text-anchor="middle">ปั๊มตัวที่ 2</text>

                            <!-- Pipe: Pump 2 to Top Outlet -->
                            <path d="M 290 184 L 290 80 L 390 80" fill="none" stroke="#a855f7" stroke-width="6" class="water-flow" />
                            <!-- Outlet Gauge ho -->
                            <circle cx="330" cy="80" r="13" fill="#f43f5e" stroke="#ffffff" stroke-width="1.5" />
                            <text x="330" y="84" fill="#ffffff" font-size="9" font-weight="bold" text-anchor="middle">hₒ</text>
                            <text x="330" y="60" fill="#f43f5e" font-size="9" text-anchor="middle">Outlet Gauge (17 cm)</text>

                            <!-- Discharge Valve -->
                            <polygon points="390,70 410,80 390,90" fill="#10b981" />
                            <polygon points="430,70 410,80 430,90" fill="#10b981" />
                            <text x="410" y="55" fill="#10b981" font-size="10" font-weight="bold" text-anchor="middle">Discharge Valve</text>

                            <!-- To Weigh Tank -->
                            <path d="M 430 80 L 460 80 L 460 140" fill="none" stroke="#a855f7" stroke-width="6" class="water-flow" />
                            <rect x="425" y="140" width="65" height="70" fill="#334155" stroke="#64748b" stroke-width="1.5" rx="4" />
                            <text x="457" y="180" fill="#cbd5e1" font-size="9" text-anchor="middle">ถังวัดน้ำ</text>
                        </svg>
                    </div>

                    <!-- Explanation -->
                    <div class="lg:col-span-5 space-y-4">
                        <div class="p-4 rounded-2xl bg-purple-950/40 border border-purple-800/60">
                            <h3 class="font-bold text-purple-400 text-base mb-2 flex items-center gap-2">
                                <i class="fa-solid fa-bolt"></i> ความลับข้อสอบ: ปั๊มต่ออนุกรม (Series)
                            </h3>
                            <ul class="text-xs sm:text-sm text-slate-300 space-y-2 list-disc list-inside">
                                <li><strong>น้ำเข้าทางไหน:</strong> ปั๊มตัวที่ 1 ดูดน้ำตรงจาก Sump Tank (ความดันบรรยากาศ) แล้ว<strong>ส่งน้ำเข้าไปอัดเข้าทางดูดของปั๊มตัวที่ 2</strong></li>
                                <li><strong>น้ำออกทางไหน:</strong> น้ำออกจากปั๊มตัวที่ 2 ด้วยพลังงานที่เพิ่มขึ้น 2 เท่า ขึ้นไปผ่านเกจวัดทางออก \(h_o\)</li>
                                <li><strong class="text-amber-400">จุดดักข้อสอบ! \(h_1 = 0\):</strong> ทางเข้าปั๊มตัวแรกดูดจากถังเปิดสู่บรรยากาศ จึงถือว่า <strong>\(h_1 = 0\)</strong> เสมอ! (คู่มือหน้า 51 ข้อ 6)</li>
                                <li><strong>ผลลัพธ์:</strong> Head เพิ่มขึ้น 2 เท่า (\(\mathbf{2H}\)), แต่อัตราไหล \(Q\) เท่าเดิม!</li>
                            </ul>
                        </div>
                        <div class="p-4 rounded-2xl bg-slate-800 border border-slate-700 text-xs text-slate-300">
                            <strong class="text-red-400 block mb-1">⚠️ จุดดักคะแนน: ค่า \(H_d\) ติดลบ!</strong>
                            \(h_d(\text{inlet}) = 0.24\text{ m}\) (Bench pump inlet), \(h_d(\text{outlet}) = 0.17\text{ m}\)<br>
                            $$\mathbf{H_d = 0.17 - 0.24 = -0.07\text{ m}}$$
                            $$H = h_o - 0 + (-0.07) = \mathbf{h_o - 0.07\text{ m}}$$
                        </div>
                    </div>
                </div>
            </div>

            <!-- CONFIG 3: PARALLEL PUMPS -->
            <div id="config-parallel" class="config-view hidden space-y-6">
                <div class="grid grid-cols-1 lg:grid-cols-12 gap-6 items-center">
                    <!-- Diagram SVG -->
                    <div class="lg:col-span-7 bg-slate-900/90 p-4 sm:p-6 rounded-2xl border border-slate-700 text-center relative overflow-hidden">
                        <span class="absolute top-3 left-3 text-xs font-mono px-2 py-0.5 rounded bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">รูปที่ 9.5 เครื่องสูบน้ำต่อขนาน</span>
                        <!-- SVG Animation for Parallel Pumps -->
                        <svg viewBox="0 0 500 280" class="w-full h-auto mx-auto my-2">
                            <!-- Sump Tank -->
                            <rect x="20" y="140" width="80" height="110" fill="#1e293b" stroke="#475569" stroke-width="2" rx="6" />
                            <text x="60" y="200" fill="#94a3b8" font-size="10" text-anchor="middle">Sump Tank</text>

                            <!-- Branch 1 to Pump A -->
                            <path d="M 100 170 L 150 170 L 150 140 L 190 140" fill="none" stroke="#10b981" stroke-width="5" class="water-flow" />
                            <circle cx="215" cy="140" r="22" fill="#047857" stroke="#34d399" stroke-width="2" />
                            <text x="215" y="144" fill="#ffffff" font-size="9" font-weight="bold" text-anchor="middle">ปั๊ม A</text>

                            <!-- Branch 2 to Pump B -->
                            <path d="M 100 220 L 190 220" fill="none" stroke="#10b981" stroke-width="5" class="water-flow" />
                            <circle cx="215" cy="220" r="22" fill="#047857" stroke="#34d399" stroke-width="2" />
                            <text x="215" y="224" fill="#ffffff" font-size="9" font-weight="bold" text-anchor="middle">ปั๊ม B</text>

                            <!-- Pipes Merging into Discharge Manifold -->
                            <path d="M 237 140 L 290 140 L 290 80 L 370 80" fill="none" stroke="#10b981" stroke-width="5" class="water-flow" />
                            <path d="M 237 220 L 290 220 L 290 140" fill="none" stroke="#10b981" stroke-width="5" class="water-flow" />

                            <!-- Manifold Gauge hm -->
                            <line x1="330" y1="80" x2="330" y2="45" stroke="#f59e0b" stroke-width="2" />
                            <circle cx="330" cy="35" r="13" fill="#f59e0b" stroke="#ffffff" stroke-width="1.5" />
                            <text x="330" y="39" fill="#000000" font-size="9" font-weight="bold" text-anchor="middle">hₘ</text>
                            <text x="330" y="18" fill="#f59e0b" font-size="9" text-anchor="middle">Manifold Gauge (96 cm)</text>

                            <!-- Discharge Valve -->
                            <polygon points="370,70 390,80 370,90" fill="#10b981" />
                            <polygon points="410,70 390,80 410,90" fill="#10b981" />
                            <text x="390" y="105" fill="#10b981" font-size="9" font-weight="bold" text-anchor="middle">Discharge Valve</text>

                            <!-- To Weigh Tank -->
                            <path d="M 410 80 L 450 80 L 450 140" fill="none" stroke="#10b981" stroke-width="6" class="water-flow" />
                            <rect x="420" y="140" width="60" height="70" fill="#334155" stroke="#64748b" stroke-width="1.5" rx="4" />
                            <text x="450" y="180" fill="#cbd5e1" font-size="9" text-anchor="middle">ถังวัดน้ำ</text>
                        </svg>
                    </div>

                    <!-- Explanation -->
                    <div class="lg:col-span-5 space-y-4">
                        <div class="p-4 rounded-2xl bg-emerald-950/40 border border-emerald-800/60">
                            <h3 class="font-bold text-emerald-400 text-base mb-2 flex items-center gap-2">
                                <i class="fa-solid fa-water"></i> ความลับข้อสอบ: ปั๊มต่อขนาน (Parallel)
                            </h3>
                            <ul class="text-xs sm:text-sm text-slate-300 space-y-2 list-disc list-inside">
                                <li><strong>น้ำเข้าทางไหน:</strong> น้ำถูกแบ่งดูดพร้อมกัน 2 สายเข้าปั๊ม A และ ปั๊ม B</li>
                                <li><strong>น้ำออกทางไหน:</strong> น้ำออกจากปั๊มทั้ง 2 มารวมกันที่ท่อ <strong>Discharge Manifold</strong> และวัดความดันที่ <strong>Manifold Gauge (\(h_m\))</strong></li>
                                <li><strong>ผลลัพธ์:</strong> อัตราการไหลเพิ่มขึ้น 2 เท่า (\(\mathbf{2Q}\)), แต่ Head สูงสุดเท่าเดิม!</li>
                            </ul>
                        </div>
                        <div class="p-4 rounded-2xl bg-slate-800 border border-slate-700 text-xs text-slate-300">
                            <strong class="text-emerald-400 block mb-1">📐 สรุปค่าแก้ระดับ Z ของปั๊มต่อขนาน:</strong>
                            \(h_d(\text{inlet}) = 0.02\text{ m}\) (2 cm), \(h_d(\text{outlet}) = 0.96\text{ m}\) (96 cm บน Manifold)<br>
                            $$\mathbf{H_d = 0.96 - 0.02 = +0.94\text{ m}}$$
                            $$H = h_m - h_1 + 0.94\text{ m}$$
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- SECTION 3: จุดตายที่ 1 "ปรับหน้า Z" (Datum Head Correction) -->
    <section id="datum-z" class="max-w-6xl mx-auto px-4 py-8">
        <div class="glass-card rounded-3xl p-6 sm:p-8 border border-slate-700/60 shadow-xl">
            <div class="flex items-center gap-3 mb-6">
                <span class="w-8 h-8 rounded-xl bg-amber-500/20 text-amber-400 border border-amber-500/30 flex items-center justify-center font-bold font-heading">3</span>
                <div>
                    <h2 class="text-xl sm:text-2xl font-bold text-white font-heading">จุดตายข้อสอบที่ 1: "ต้องปรับหน้า Z" (Datum Head Correction)</h2>
                    <p class="text-xs sm:text-sm text-slate-400">ลายมือหน้า 52: "ต้องปรับหน้า z" คืออะไรและจำตัวเลขไหนไปสอบ?</p>
                </div>
            </div>

            <div class="bg-amber-950/30 border border-amber-500/40 rounded-2xl p-5 mb-6 text-sm text-amber-200">
                <div class="flex items-start gap-3">
                    <span class="text-2xl">⚠️</span>
                    <div>
                        <strong>ทำไมถึงต้อง "ปรับหน้า Z"?</strong><br>
                        เพราะเวลาอาจารย์ให้สมการพลังงาน \(H = (h_2 - h_1) + (Z_2 - Z_1)\) แต่ในการทดลองจริง 
                        เกจวัดความดันขาเข้ากับขาออกตั้งอยู่บนแท่นคนละความสูงกัน! 
                        ระยะ \(Z_2 - Z_1\) จึงถูกแปลงเป็น <strong>Head Correction Factor (\(H_d\))</strong> ตามสมการ (9.5):
                        <div class="my-2 p-2 bg-slate-900 rounded-lg font-mono text-center text-amber-400 text-sm sm:text-base">
                            \[H_d = h_d(\text{outlet}) - h_d(\text{inlet})\]
                        </div>
                    </div>
                </div>
            </div>

            <!-- Table of 4 Distances in Manual -->
            <div class="overflow-x-auto mb-6">
                <table class="w-full text-xs sm:text-sm border-collapse bg-slate-800/80 rounded-xl overflow-hidden border border-slate-700">
                    <thead>
                        <tr class="bg-slate-700/80 text-slate-200">
                            <th class="p-3 text-left">ตำแหน่งจุดวัดความดัน</th>
                            <th class="p-3 text-center">สัญลักษณ์</th>
                            <th class="p-3 text-center">ระยะจากจุดอ้างอิง (m)</th>
                            <th class="p-3 text-center">ระยะเป็นเซนติเมตร (cm)</th>
                            <th class="p-3 text-left">ใช้ในการทดลองไหน?</th>
                        </tr>
                    </thead>
                    <tbody class="divide-y divide-slate-700 text-slate-300">
                        <tr>
                            <td class="p-3 font-semibold text-white">Manifold Gauge</td>
                            <td class="p-3 text-center font-mono text-sky-400">h_d(outlet, parallel)</td>
                            <td class="p-3 text-center font-bold text-emerald-400">0.96 m</td>
                            <td class="p-3 text-center">96 cm</td>
                            <td class="p-3">ปั๊มสองตัวต่อขนานกัน (รูป 9.5)</td>
                        </tr>
                        <tr>
                            <td class="p-3 font-semibold text-white">Outlet Gauge (ท่อออกเดี่ยว)</td>
                            <td class="p-3 text-center font-mono text-sky-400">h_d(outlet, single)</td>
                            <td class="p-3 text-center font-bold text-sky-400">0.17 m</td>
                            <td class="p-3 text-center">17 cm</td>
                            <td class="p-3">ปั๊มเดี่ยว (รูป 9.3) และปั๊มอนุกรม (รูป 9.4)</td>
                        </tr>
                        <tr>
                            <td class="p-3 font-semibold text-white">Inlet Gauge (ท่อเข้าเดี่ยว)</td>
                            <td class="p-3 text-center font-mono text-sky-400">h_d(inlet)</td>
                            <td class="p-3 text-center font-bold text-amber-400">0.02 m</td>
                            <td class="p-3 text-center">2 cm</td>
                            <td class="p-3">ปั๊มเดี่ยว (รูป 9.3) และปั๊มขนาน (รูป 9.5)</td>
                        </tr>
                        <tr>
                            <td class="p-3 font-semibold text-white">Bench Pump Inlet (ท่อดูดจากถัง)</td>
                            <td class="p-3 text-center font-mono text-sky-400">h_d(inlet, series)</td>
                            <td class="p-3 text-center font-bold text-purple-400">0.24 m</td>
                            <td class="p-3 text-center">24 cm</td>
                            <td class="p-3">ปั๊มสองตัวต่ออนุกรมกัน (รูป 9.4)</td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <!-- Summary Table for 3 Cases -->
            <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
                <div class="bg-slate-900 p-4 rounded-xl border border-sky-500/40 text-center">
                    <span class="text-xs text-sky-400 font-bold block mb-1">1. เครื่องสูบน้ำตัวเดียว</span>
                    <div class="text-lg font-bold text-white font-mono">\(H_d = 0.17 - 0.02\)</div>
                    <div class="text-xl font-extrabold text-sky-400 font-mono mt-1">+0.15 m</div>
                </div>
                <div class="bg-slate-900 p-4 rounded-xl border border-purple-500/40 text-center">
                    <span class="text-xs text-purple-400 font-bold block mb-1">2. สองตัวต่ออนุกรม (ระวังติดลบ!)</span>
                    <div class="text-lg font-bold text-white font-mono">\(H_d = 0.17 - 0.24\)</div>
                    <div class="text-xl font-extrabold text-red-400 font-mono mt-1">-0.07 m</div>
                </div>
                <div class="bg-slate-900 p-4 rounded-xl border border-emerald-500/40 text-center">
                    <span class="text-xs text-emerald-400 font-bold block mb-1">3. สองตัวต่อขนานกัน</span>
                    <div class="text-lg font-bold text-white font-mono">\(H_d = 0.96 - 0.02\)</div>
                    <div class="text-xl font-extrabold text-emerald-400 font-mono mt-1">+0.94 m</div>
                </div>
            </div>
        </div>
    </section>

    <!-- SECTION 4: จุดตายที่ 2 กับดัก "มล. เป็น ลบ.ม." -->
    <section id="unit-trap" class="max-w-6xl mx-auto px-4 py-8">
        <div class="glass-card rounded-3xl p-6 sm:p-8 border border-red-500/40 shadow-xl relative overflow-hidden">
            <div class="absolute -top-10 -right-10 w-40 h-40 bg-red-500/10 rounded-full blur-2xl pointer-events-none"></div>
            
            <div class="flex items-center gap-3 mb-6">
                <span class="w-8 h-8 rounded-xl bg-red-500/20 text-red-400 border border-red-500/30 flex items-center justify-center font-bold font-heading">4</span>
                <div>
                    <h2 class="text-xl sm:text-2xl font-bold text-white font-heading">จุดตายข้อสอบที่ 2: ลายมือหน้า 53 "มล. เป็น ลบ.ม" (กับดักการแปลงหน่วย)</h2>
                    <p class="text-xs sm:text-sm text-red-300">จุดที่นักศึกษา 80% กากบาทช้อยส์ผิดเพราะลืมคูณหารเลขชี้กำลัง!</p>
                </div>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-2 gap-6 text-sm">
                <!-- Trap 1: Volume conversion -->
                <div class="bg-slate-900 p-5 rounded-2xl border border-red-500/30 space-y-3">
                    <h3 class="font-bold text-red-400 text-base flex items-center gap-2">
                        <i class="fa-solid fa-triangle-exclamation"></i> 1. การแปลงปริมาตร (\(\text{Volume}\))
                    </h3>
                    <p class="text-slate-300 text-xs sm:text-sm">
                        ในโจทย์ข้อสอบ อาจารย์อาจให้ปริมาตรมาเป็น <strong>ลิตร (L)</strong> หรือ <strong>มิลลิลิตร (mL)</strong> ห้ามนำไปคูณในสูตร Power ตรงๆ เด็ดขาด! ต้องแปลงเป็น <strong>ลูกบาศก์เมตร (\(\text{m}^3\))</strong> ก่อนเสมอ:
                    </p>
                    <div class="space-y-2 text-xs font-mono">
                        <div class="p-2.5 bg-slate-800 rounded-lg text-emerald-400 border border-slate-700">
                            • จาก <strong>ลิตร (L)</strong> $\to$ <strong>ลบ.ม. (\(\text{m}^3\))</strong>: \(\div 1,000\) หรือ \(\times 10^{-3}\)<br>
                            <span class="text-slate-400">เช่น \(1\text{ L} = 1 \times 10^{-3}\text{ m}^3 = 0.001\text{ m}^3\)</span>
                        </div>
                        <div class="p-2.5 bg-slate-800 rounded-lg text-amber-400 border border-slate-700">
                            • จาก <strong>มิลลิลิตร (mL)</strong> $\to$ <strong>ลบ.ม. (\(\text{m}^3\))</strong>: \(\div 1,000,000\) หรือ \(\times 10^{-6}\)<br>
                            <span class="text-slate-400">เช่น \(500\text{ mL} = 500 \times 10^{-6}\text{ m}^3 = 0.0005\text{ m}^3\)</span>
                        </div>
                    </div>
                </div>

                <!-- Trap 2: Flow rate conversion -->
                <div class="bg-slate-900 p-5 rounded-2xl border border-red-500/30 space-y-3">
                    <h3 class="font-bold text-red-400 text-base flex items-center gap-2">
                        <i class="fa-solid fa-calculator"></i> 2. การหาอัตราการไหล (\(Q\)) เข้าสูตร Power
                    </h3>
                    <p class="text-slate-300 text-xs sm:text-sm">
                        เมื่อจับเวลาได้ \(t\) วินาที:
                    </p>
                    <div class="p-3 bg-slate-800 rounded-lg font-mono text-xs sm:text-sm text-sky-300 border border-slate-700">
                        \[Q\text{ [m}^3/\text{s]} = \frac{\text{Volume [L]}}{1,000 \times \text{Time [s]}}\]
                    </div>
                    <div class="text-xs text-red-300 bg-red-950/40 p-3 rounded-lg border border-red-800/40">
                        💣 <strong>ข้อควรระวังในช้อยส์ข้อสอบ:</strong> อาจารย์จะสร้างช้อยส์หลอก เช่น คำตอบที่ไม่ได้หาร 1,000 (ค่าจะโตเป็น 10,000 Watts) ดักคนลืมแปลงหน่วย!
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- SECTION 5: การคำนวณหากำลัง Power (Wi) -->
    <section id="power" class="max-w-6xl mx-auto px-4 py-8">
        <div class="glass-card rounded-3xl p-6 sm:p-8 border border-slate-700/60 shadow-xl">
            <div class="flex items-center gap-3 mb-6">
                <span class="w-8 h-8 rounded-xl bg-purple-500/20 text-purple-400 border border-purple-500/30 flex items-center justify-center font-bold font-heading">5</span>
                <div>
                    <h2 class="text-xl sm:text-2xl font-bold text-white font-heading">การคำนวณกำลังงานชลศาสตร์ของเครื่องสูบน้ำ (Power: \(W_i\))</h2>
                    <p class="text-xs sm:text-sm text-slate-400">ลายมือหน้า 52: "แล้วหา power" ตามสมการที่ (9.7)</p>
                </div>
            </div>

            <div class="bg-slate-900 p-6 rounded-2xl border border-slate-700 space-y-4">
                <div class="text-center">
                    <span class="text-xs font-semibold uppercase tracking-wider text-purple-400">สมการที่ (9.7) ในคู่มือปฏิบัติการ</span>
                    <div class="text-2xl sm:text-3xl font-extrabold text-white font-mono my-2">
                        \[W_i = P = \gamma \cdot Q \cdot H = \rho \cdot g \cdot Q \cdot H\]
                    </div>
                </div>

                <div class="grid grid-cols-1 sm:grid-cols-3 gap-4 pt-2 text-xs sm:text-sm">
                    <div class="bg-slate-800 p-3.5 rounded-xl border border-slate-700">
                        <strong class="text-sky-400 block mb-1">1. \(\gamma\) (Unit Weight น้ำ)</strong>
                        \(9,810\text{ N/m}^3\)<br>
                        <span class="text-slate-400">(\(1,000\text{ kg/m}^3 \times 9.81\text{ m/s}^2\))</span>
                    </div>
                    <div class="bg-slate-800 p-3.5 rounded-xl border border-slate-700">
                        <strong class="text-emerald-400 block mb-1">2. \(Q\) (Discharge)</strong>
                        ต้องมีหน่วยเป็น <strong>\(\text{m}^3/\text{s}\)</strong> เท่านั้น!
                    </div>
                    <div class="bg-slate-800 p-3.5 rounded-xl border border-slate-700">
                        <strong class="text-amber-400 block mb-1">3. \(H\) (Total Head)</strong>
                        ต้องรวมค่าแก้ระดับ \(H_d\):<br>
                        \(H = h_o - h_1 + H_d\) (m)
                    </div>
                </div>

                <!-- Example Calculation Box -->
                <div class="mt-4 p-4 rounded-xl bg-purple-950/30 border border-purple-500/40 text-xs sm:text-sm text-purple-200">
                    <strong class="text-purple-300 block mb-1 font-semibold">📌 ตัวอย่างแทนค่าในห้องสอบ (Single Pump จุดที่ 1):</strong>
                    กำหนด \(V = 1\text{ L}\), \(t = 17.71\text{ s}\), \(h_1 = 1.0\text{ m}\), \(h_o = 19.0\text{ m}\), \(H_d = 0.15\text{ m}\)<br>
                    • \(Q = \frac{1}{1,000 \times 17.71} = 5.6475 \times 10^{-5}\text{ m}^3\text{/s}\)<br>
                    • \(H = 19.0 - 1.0 + 0.15 = 18.15\text{ m}\)<br>
                    • \(W_i = 9,810 \times (5.6475 \times 10^{-5}) \times 18.15 = \mathbf{10.06\text{ Watts}}\)
                </div>
            </div>
        </div>
    </section>

    <!-- SECTION 6: กราฟ iPad หน้า 53 (Interactive Chart) -->
    <section id="chart-section" class="max-w-6xl mx-auto px-4 py-8">
        <div class="glass-card rounded-3xl p-6 sm:p-8 border border-slate-700/60 shadow-xl">
            <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-4 mb-6">
                <div class="flex items-center gap-3">
                    <span class="w-8 h-8 rounded-xl bg-sky-500/20 text-sky-400 border border-sky-500/30 flex items-center justify-center font-bold font-heading">6</span>
                    <div>
                        <h2 class="text-xl sm:text-2xl font-bold text-white font-heading">กราฟความสัมพันธ์ H-Q (ตามจอ iPad หน้า 53)</h2>
                        <p class="text-xs sm:text-sm text-slate-400">เปรียบเทียบ Single vs Series (\(2H\)) vs Parallel (\(2Q\))</p>
                    </div>
                </div>
                <div class="flex items-center gap-2">
                    <span class="text-xs text-slate-400">สลับหน่วยแกน X:</span>
                    <button id="chart-btn-ls" onclick="updateChartUnit('ls')" class="px-3 py-1 rounded-lg text-xs font-semibold bg-sky-500 text-white shadow-md">L/s</button>
                    <button id="chart-btn-m3s" onclick="updateChartUnit('m3s')" class="px-3 py-1 rounded-lg text-xs font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700">m³/s</button>
                </div>
            </div>

            <!-- Chart Container -->
            <div class="bg-slate-900/90 p-4 sm:p-6 rounded-2xl border border-slate-700 relative" style="height: 480px;">
                <canvas id="examPumpChart"></canvas>
            </div>

            <!-- Key Graph Insights for Exam -->
            <div class="grid grid-cols-1 md:grid-cols-3 gap-4 mt-6 text-xs sm:text-sm">
                <div class="p-4 rounded-xl bg-slate-800 border-t-2 border-sky-500">
                    <strong class="text-sky-400 block mb-1">1. เครื่องสูบน้ำตัวเดียว (Single)</strong>
                    Shutoff Head อยู่ที่ \(\approx 18.15\text{ m}\) และอัตราไหลสูงสุด \(Q_{\max} \approx 1.63\text{ L/s}\) เป็นเส้นฐานอ้างอิง
                </div>
                <div class="p-4 rounded-xl bg-slate-800 border-t-2 border-purple-500">
                    <strong class="text-purple-400 block mb-1">2. สองตัวต่ออนุกรม (Series: 2H)</strong>
                    Shutoff Head พุ่งขึ้นเป็น <strong>2 เท่า (\(\approx 37.93\text{ m}\))</strong> แต่อัตราไหลสูงสุดไม่เพิ่ม (\(Q_{\max} \approx 1.60\text{ L/s}\))
                </div>
                <div class="p-4 rounded-xl bg-slate-800 border-t-2 border-emerald-500">
                    <strong class="text-emerald-400 block mb-1">3. สองตัวต่อขนาน (Parallel: 2Q)</strong>
                    Shutoff Head เท่ากับปั๊มเดี่ยว (\(\approx 19.94\text{ m}\)) แต่อัตราไหลสูงสุดพุ่งเป็น <strong>2 เท่า (\(Q_{\max} \approx 2.96\text{ L/s}\))</strong>
                </div>
            </div>
        </div>
    </section>

    <!-- SECTION 7: INTERACTIVE FORMULA CALCULATOR -->
    <section id="calculator" class="max-w-6xl mx-auto px-4 py-8">
        <div class="glass-card rounded-3xl p-6 sm:p-8 border border-sky-500/30 shadow-xl">
            <div class="flex items-center gap-3 mb-6">
                <span class="w-8 h-8 rounded-xl bg-sky-500/20 text-sky-400 border border-sky-500/30 flex items-center justify-center font-bold font-heading">7</span>
                <div>
                    <h2 class="text-xl sm:text-2xl font-bold text-white font-heading">เครื่องคิดเลขจำลองข้อสอบ (Exam Simulator Calculator)</h2>
                    <p class="text-xs sm:text-sm text-slate-400">ลองกรอกตัวเลขแล้วดูขั้นตอนการแทนค่าทีละสเต็ป ป้องกันการคำนวณพลาดในห้องสอบ</p>
                </div>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                <!-- Input Controls -->
                <div class="bg-slate-900 p-5 rounded-2xl border border-slate-700 space-y-4 text-xs sm:text-sm">
                    <div>
                        <label class="block text-slate-300 font-semibold mb-1">1. เลือกรูปแบบการต่อเครื่องสูบน้ำ:</label>
                        <select id="calc-config" onchange="runCalculator()" class="w-full bg-slate-800 border border-slate-700 rounded-xl p-2.5 text-white font-medium focus:outline-none focus:border-sky-500">
                            <option value="single">เครื่องสูบน้ำตัวเดียว (Single Pump) - [Hd = +0.15 m]</option>
                            <option value="series">เครื่องสูบน้ำสองตัวต่ออนุกรม (Series) - [Hd = -0.07 m, h1 = 0]</option>
                            <option value="parallel">เครื่องสูบน้ำสองตัวต่อขนาน (Parallel) - [Hd = +0.94 m]</option>
                        </select>
                    </div>

                    <div class="grid grid-cols-2 gap-3">
                        <div>
                            <label class="block text-slate-300 font-semibold mb-1">ปริมาตรน้ำ:</label>
                            <div class="flex gap-1">
                                <input type="number" id="calc-vol" value="1" step="0.5" oninput="runCalculator()" class="w-2/3 bg-slate-800 border border-slate-700 rounded-xl p-2 text-white">
                                <select id="calc-vol-unit" onchange="runCalculator()" class="w-1/3 bg-slate-800 border border-slate-700 rounded-xl p-2 text-white text-xs">
                                    <option value="L">L</option>
                                    <option value="mL">mL</option>
                                </select>
                            </div>
                        </div>
                        <div>
                            <label class="block text-slate-300 font-semibold mb-1">เวลาที่จับได้ (วินาที):</label>
                            <input type="number" id="calc-time" value="17.71" step="0.01" oninput="runCalculator()" class="w-full bg-slate-800 border border-slate-700 rounded-xl p-2 text-white">
                        </div>
                    </div>

                    <div class="grid grid-cols-2 gap-3">
                        <div>
                            <label class="block text-slate-300 font-semibold mb-1">Inlet Head \(h_1\) (m):</label>
                            <input type="number" id="calc-h1" value="1.0" step="0.1" oninput="runCalculator()" class="w-full bg-slate-800 border border-slate-700 rounded-xl p-2 text-white">
                        </div>
                        <div>
                            <label class="block text-slate-300 font-semibold mb-1">Outlet Head \(h_o\) (m):</label>
                            <input type="number" id="calc-ho" value="19.0" step="0.5" oninput="runCalculator()" class="w-full bg-slate-800 border border-slate-700 rounded-xl p-2 text-white">
                        </div>
                    </div>
                </div>

                <!-- Result Live Display -->
                <div class="bg-slate-900 p-5 rounded-2xl border border-slate-700 flex flex-col justify-between text-xs sm:text-sm">
                    <div>
                        <span class="text-xs font-semibold text-emerald-400 uppercase tracking-wide">ผลการคำนวณแบบ Step-by-Step</span>
                        <div id="calc-steps" class="mt-3 space-y-2 text-slate-300 font-mono">
                            <!-- Populated by JS -->
                        </div>
                    </div>
                    <div class="mt-4 pt-3 border-t border-slate-800 flex items-center justify-between text-sm">
                        <span class="text-slate-400">กำลังชลศาสตร์สุดท้าย (\(W_i\)):</span>
                        <span id="calc-power-result" class="text-xl font-extrabold text-sky-400 font-mono">10.06 W</span>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- SECTION 8: คลังข้อสอบปรนัยจำลอง (MOCK EXAM QUIZ) -->
    <section id="quiz-section" class="max-w-6xl mx-auto px-4 py-8">
        <div class="glass-card rounded-3xl p-6 sm:p-8 border border-indigo-500/40 shadow-2xl">
            <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-4 mb-6 pb-4 border-b border-slate-700">
                <div class="flex items-center gap-3">
                    <span class="w-8 h-8 rounded-xl bg-indigo-500/20 text-indigo-400 border border-indigo-500/30 flex items-center justify-center font-bold font-heading">8</span>
                    <div>
                        <h2 class="text-xl sm:text-2xl font-bold text-white font-heading">แบบฝึกหัดข้อสอบจำลองเสมือนจริง 5 ข้อ (Mock Exam)</h2>
                        <p class="text-xs sm:text-sm text-slate-400">ทดสอบความพร้อมก่อนเข้าห้องสอบจริง มีช้อยส์หลอกตามเกณฑ์อาจารย์ 100%</p>
                    </div>
                </div>
                <div id="quiz-score-badge" class="px-4 py-1.5 rounded-full bg-slate-800 text-sky-400 border border-slate-700 text-xs font-bold">
                    คะแนน: <span id="current-score">0</span> / 5 ข้อ
                </div>
            </div>

            <!-- Quiz Questions Container -->
            <div id="quiz-container" class="space-y-6">
                <!-- Question 1 -->
                <div class="bg-slate-900/90 p-5 sm:p-6 rounded-2xl border border-slate-700 space-y-3" id="q1-box">
                    <div class="flex items-center justify-between">
                        <span class="text-xs font-bold text-sky-400 uppercase tracking-wide">ข้อที่ 1 • วิเคราะห์ภาพและทิศทางน้ำ</span>
                        <span class="text-xs px-2 py-0.5 rounded bg-slate-800 text-slate-400">1 คะแนน</span>
                    </div>
                    <p class="text-sm sm:text-base font-semibold text-white">
                        ในการต่อเครื่องสูบน้ำแบบอนุกรม (Two Pumps in Series ตามรูปที่ 9.4) ข้อใดอธิบายทิศทางการไหลของน้ำและความดันขาเข้า (\(h_1\)) ได้ถูกต้องที่สุด?
                    </p>
                    <div class="space-y-2 text-xs sm:text-sm">
                        <label onclick="checkAnswer(1, 'A')" class="quiz-option flex items-start gap-3 p-3 rounded-xl bg-slate-800 hover:bg-slate-700/60 cursor-pointer border border-slate-700">
                            <span class="font-bold text-slate-400">ก.</span>
                            <span>น้ำถูกดูดจาก Sump tank เข้าปั๊มตัวที่ 1 แล้วส่งออกทาง Discharge Manifold ทันที โดย \(h_1 = 1.0\text{ m}\)</span>
                        </label>
                        <label onclick="checkAnswer(1, 'B')" class="quiz-option flex items-start gap-3 p-3 rounded-xl bg-slate-800 hover:bg-slate-700/60 cursor-pointer border border-slate-700">
                            <span class="font-bold text-slate-400">ข.</span>
                            <span>น้ำจาก Sump tank ถูกดูดเข้าปั๊มตัวที่ 1 แล้วส่งต่อไปยังทางดูดของปั๊มตัวที่ 2 โดยถือว่า \(h_1 = 0\text{ m}\) เนื่องจากดูดจากถังเปิดสู่บรรยากาศ</span>
                        </label>
                        <label onclick="checkAnswer(1, 'C')" class="quiz-option flex items-start gap-3 p-3 rounded-xl bg-slate-800 hover:bg-slate-700/60 cursor-pointer border border-slate-700">
                            <span class="font-bold text-slate-400">ค.</span>
                            <span>น้ำแยกไหลเข้าปั๊มทั้งสองตัวพร้อมกัน ทำให้ Total Head เพิ่มขึ้นเป็น 2 เท่า</span>
                        </label>
                        <label onclick="checkAnswer(1, 'D')" class="quiz-option flex items-start gap-3 p-3 rounded-xl bg-slate-800 hover:bg-slate-700/60 cursor-pointer border border-slate-700">
                            <span class="font-bold text-slate-400">ง.</span>
                            <span>ปั๊มตัวที่ 2 ดูดน้ำตรงจาก Sump tank ส่วนปั๊มตัวที่ 1 ไม่ได้เปิดทำงาน</span>
                        </label>
                    </div>
                    <div id="q1-explanation" class="hidden text-xs p-3.5 rounded-xl mt-2"></div>
                </div>

                <!-- Question 2 -->
                <div class="bg-slate-900/90 p-5 sm:p-6 rounded-2xl border border-slate-700 space-y-3" id="q2-box">
                    <div class="flex items-center justify-between">
                        <span class="text-xs font-bold text-sky-400 uppercase tracking-wide">ข้อที่ 2 • ค่าปรับหน้า Z (Datum Correction)</span>
                        <span class="text-xs px-2 py-0.5 rounded bg-slate-800 text-slate-400">1 คะแนน</span>
                    </div>
                    <p class="text-sm sm:text-base font-semibold text-white">
                        ในการทดสอบเครื่องสูบน้ำแบบสองตัวต่ออนุกรมกัน (Two Pumps in Series) กำหนดให้ระยะจากจุดอ้างอิงถึง Outlet Gauge เท่ากับ \(0.17\text{ m}\) และระยะถึง Bench Pump Inlet เท่ากับ \(0.24\text{ m}\) ค่าปรับแก้ระดับ Datum Head Correction (\(H_d\)) มีค่าเท่าใด?
                    </p>
                    <div class="space-y-2 text-xs sm:text-sm">
                        <label onclick="checkAnswer(2, 'A')" class="quiz-option flex items-start gap-3 p-3 rounded-xl bg-slate-800 hover:bg-slate-700/60 cursor-pointer border border-slate-700">
                            <span class="font-bold text-slate-400">ก.</span>
                            <span>\(+0.41\text{ m}\)</span>
                        </label>
                        <label onclick="checkAnswer(2, 'B')" class="quiz-option flex items-start gap-3 p-3 rounded-xl bg-slate-800 hover:bg-slate-700/60 cursor-pointer border border-slate-700">
                            <span class="font-bold text-slate-400">ข.</span>
                            <span>\(+0.07\text{ m}\)</span>
                        </label>
                        <label onclick="checkAnswer(2, 'C')" class="quiz-option flex items-start gap-3 p-3 rounded-xl bg-slate-800 hover:bg-slate-700/60 cursor-pointer border border-slate-700">
                            <span class="font-bold text-slate-400">ค.</span>
                            <span>\(-0.07\text{ m}\)</span>
                        </label>
                        <label onclick="checkAnswer(2, 'D')" class="quiz-option flex items-start gap-3 p-3 rounded-xl bg-slate-800 hover:bg-slate-700/60 cursor-pointer border border-slate-700">
                            <span class="font-bold text-slate-400">ง.</span>
                            <span>\(+0.15\text{ m}\)</span>
                        </label>
                    </div>
                    <div id="q2-explanation" class="hidden text-xs p-3.5 rounded-xl mt-2"></div>
                </div>

                <!-- Question 3 -->
                <div class="bg-slate-900/90 p-5 sm:p-6 rounded-2xl border border-slate-700 space-y-3" id="q3-box">
                    <div class="flex items-center justify-between">
                        <span class="text-xs font-bold text-sky-400 uppercase tracking-wide">ข้อที่ 3 • กับดักการแปลงหน่วย (มล. $\to$ ลบ.ม.)</span>
                        <span class="text-xs px-2 py-0.5 rounded bg-slate-800 text-slate-400">1 คะแนน</span>
                    </div>
                    <p class="text-sm sm:text-base font-semibold text-white">
                        ในการวัดอัตราการไหล ได้ปริมาตรน้ำ \(V = 5,000\text{ mL}\) ในเวลา \(t = 4.0\text{ วินาที}\) อัตราการไหลจริง (\(Q\)) ในหน่วยลูกบาศก์เมตรต่อวินาที (\(\text{m}^3/\text{s}\)) มีค่าเท่ากับเท่าใด?
                    </p>
                    <div class="space-y-2 text-xs sm:text-sm">
                        <label onclick="checkAnswer(3, 'A')" class="quiz-option flex items-start gap-3 p-3 rounded-xl bg-slate-800 hover:bg-slate-700/60 cursor-pointer border border-slate-700">
                            <span class="font-bold text-slate-400">ก.</span>
                            <span>\(1,250\text{ m}^3/\text{s}\)</span>
                        </label>
                        <label onclick="checkAnswer(3, 'B')" class="quiz-option flex items-start gap-3 p-3 rounded-xl bg-slate-800 hover:bg-slate-700/60 cursor-pointer border border-slate-700">
                            <span class="font-bold text-slate-400">ข.</span>
                            <span>\(1.25\text{ m}^3/\text{s}\)</span>
                        </label>
                        <label onclick="checkAnswer(3, 'C')" class="quiz-option flex items-start gap-3 p-3 rounded-xl bg-slate-800 hover:bg-slate-700/60 cursor-pointer border border-slate-700">
                            <span class="font-bold text-slate-400">ค.</span>
                            <span>\(0.00125\text{ m}^3/\text{s}\) (\(1.25 \times 10^{-3}\text{ m}^3/\text{s}\))</span>
                        </label>
                        <label onclick="checkAnswer(3, 'D')" class="quiz-option flex items-start gap-3 p-3 rounded-xl bg-slate-800 hover:bg-slate-700/60 cursor-pointer border border-slate-700">
                            <span class="font-bold text-slate-400">ง.</span>
                            <span>\(0.00000125\text{ m}^3/\text{s}\)</span>
                        </label>
                    </div>
                    <div id="q3-explanation" class="hidden text-xs p-3.5 rounded-xl mt-2"></div>
                </div>

                <!-- Question 4 -->
                <div class="bg-slate-900/90 p-5 sm:p-6 rounded-2xl border border-slate-700 space-y-3" id="q4-box">
                    <div class="flex items-center justify-between">
                        <span class="text-xs font-bold text-sky-400 uppercase tracking-wide">ข้อที่ 4 • คำนวณหากำลังชลศาสตร์ (Power)</span>
                        <span class="text-xs px-2 py-0.5 rounded bg-slate-800 text-slate-400">1 คะแนน</span>
                    </div>
                    <p class="text-sm sm:text-base font-semibold text-white">
                        เครื่องสูบน้ำตัวหนึ่งมี Total Head \(H = 20.0\text{ m}\) และสูบน้ำได้อัตราการไหล \(Q = 2.0\text{ L/s}\) กำหนดหน่วยน้ำหนักของน้ำ \(\gamma = 9,810\text{ N/m}^3\) กำลังงานชลศาสตร์ของเครื่องสูบน้ำ (\(W_i\)) มีค่าเท่าใด?
                    </p>
                    <div class="space-y-2 text-xs sm:text-sm">
                        <label onclick="checkAnswer(4, 'A')" class="quiz-option flex items-start gap-3 p-3 rounded-xl bg-slate-800 hover:bg-slate-700/60 cursor-pointer border border-slate-700">
                            <span class="font-bold text-slate-400">ก.</span>
                            <span>\(392.4\text{ Watts}\)</span>
                        </label>
                        <label onclick="checkAnswer(4, 'B')" class="quiz-option flex items-start gap-3 p-3 rounded-xl bg-slate-800 hover:bg-slate-700/60 cursor-pointer border border-slate-700">
                            <span class="font-bold text-slate-400">ข.</span>
                            <span>\(392,400\text{ Watts}\)</span>
                        </label>
                        <label onclick="checkAnswer(4, 'C')" class="quiz-option flex items-start gap-3 p-3 rounded-xl bg-slate-800 hover:bg-slate-700/60 cursor-pointer border border-slate-700">
                            <span class="font-bold text-slate-400">ค.</span>
                            <span>\(40.0\text{ Watts}\)</span>
                        </label>
                        <label onclick="checkAnswer(4, 'D')" class="quiz-option flex items-start gap-3 p-3 rounded-xl bg-slate-800 hover:bg-slate-700/60 cursor-pointer border border-slate-700">
                            <span class="font-bold text-slate-400">ง.</span>
                            <span>\(19.62\text{ Watts}\)</span>
                        </label>
                    </div>
                    <div id="q4-explanation" class="hidden text-xs p-3.5 rounded-xl mt-2"></div>
                </div>

                <!-- Question 5 -->
                <div class="bg-slate-900/90 p-5 sm:p-6 rounded-2xl border border-slate-700 space-y-3" id="q5-box">
                    <div class="flex items-center justify-between">
                        <span class="text-xs font-bold text-sky-400 uppercase tracking-wide">ข้อที่ 5 • วิเคราะห์กราฟและงานวิศวกรรมโยธา</span>
                        <span class="text-xs px-2 py-0.5 rounded bg-slate-800 text-slate-400">1 คะแนน</span>
                    </div>
                    <p class="text-sm sm:text-base font-semibold text-white">
                        วิศวกรโยธาต้องการออกแบบระบบสูบระบายน้ำเพื่อแก้ไขปัญหาน้ำท่วมขังในคลอง โดยระดับความสูงที่ต้องยกน้ำขึ้น (Head) มีค่าไม่สูงมาก แต่ต้องการระบายน้ำปริมาณมหาศาลอย่างรวดเร็ว ควรกำหนดให้ติดตั้งเครื่องสูบน้ำแบบใด และเพราะเหตุใด?
                    </p>
                    <div class="space-y-2 text-xs sm:text-sm">
                        <label onclick="checkAnswer(5, 'A')" class="quiz-option flex items-start gap-3 p-3 rounded-xl bg-slate-800 hover:bg-slate-700/60 cursor-pointer border border-slate-700">
                            <span class="font-bold text-slate-400">ก.</span>
                            <span>ต่อแบบอนุกรม (Series) เพราะให้ Total Head สูงที่สุด</span>
                        </label>
                        <label onclick="checkAnswer(5, 'B')" class="quiz-option flex items-start gap-3 p-3 rounded-xl bg-slate-800 hover:bg-slate-700/60 cursor-pointer border border-slate-700">
                            <span class="font-bold text-slate-400">ข.</span>
                            <span>ต่อแบบขนาน (Parallel) เพราะให้อัตราการไหลรวมเพิ่มขึ้นเป็น 2 เท่า (\(2Q\)) เหมาะกับงานระบายน้ำปริมาณมาก</span>
                        </label>
                        <label onclick="checkAnswer(5, 'C')" class="quiz-option flex items-start gap-3 p-3 rounded-xl bg-slate-800 hover:bg-slate-700/60 cursor-pointer border border-slate-700">
                            <span class="font-bold text-slate-400">ค.</span>
                            <span>ใช้เครื่องสูบน้ำตัวเดียวขนาดเล็กก็เพียงพอ</span>
                        </label>
                        <label onclick="checkAnswer(5, 'D')" class="quiz-option flex items-start gap-3 p-3 rounded-xl bg-slate-800 hover:bg-slate-700/60 cursor-pointer border border-slate-700">
                            <span class="font-bold text-slate-400">ง.</span>
                            <span>ต่อแบบใดก็ได้ เพราะให้ปริมาณน้ำและแรงดันเท่ากันเสมอ</span>
                        </label>
                    </div>
                    <div id="q5-explanation" class="hidden text-xs p-3.5 rounded-xl mt-2"></div>
                </div>
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer class="max-w-6xl mx-auto px-4 py-12 text-center text-xs text-slate-500 border-t border-slate-800 mt-12">
        <p class="font-medium text-slate-400">CE272 Fluid Mechanics Laboratory Exam Preparation Hub</p>
        <p class="mt-1">ภาควิชาวิศวกรรมโยธา คณะวิศวกรรมศาสตร์ มหาวิทยาลัยธรรมศาสตร์ • รหัสวิชา วศย. 272</p>
        <p class="mt-2 text-slate-600">จัดทำเพื่อสรุปเตรียมความพร้อมสอบปฏิบัติการ สำหรับนักศึกษาทุกคน</p>
    </footer>

    <!-- Scripts Logic -->
    <script>
        // Tab Switcher for Configurations
        function switchTab(config) {
            document.querySelectorAll('.config-view').forEach(el => el.classList.add('hidden'));
            document.getElementById('config-' + config).classList.remove('hidden');

            const btnSingle = document.getElementById('tab-btn-single');
            const btnSeries = document.getElementById('tab-btn-series');
            const btnParallel = document.getElementById('tab-btn-parallel');

            const inactiveClass = 'px-4 py-2 rounded-xl text-xs sm:text-sm font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700 transition-all';
            const activeClass = 'px-4 py-2 rounded-xl text-xs sm:text-sm font-semibold text-white shadow-md transition-all ';

            btnSingle.className = inactiveClass;
            btnSeries.className = inactiveClass;
            btnParallel.className = inactiveClass;

            if (config === 'single') btnSingle.className = activeClass + 'bg-sky-500';
            if (config === 'series') btnSeries.className = activeClass + 'bg-purple-600';
            if (config === 'parallel') btnParallel.className = activeClass + 'bg-emerald-600';
        }

        // Live Calculator Logic
        function runCalculator() {
            const config = document.getElementById('calc-config').value;
            let vol = parseFloat(document.getElementById('calc-vol').value) || 0;
            const volUnit = document.getElementById('calc-vol-unit').value;
            const t = parseFloat(document.getElementById('calc-time').value) || 1;
            let h1 = parseFloat(document.getElementById('calc-h1').value) || 0;
            const ho = parseFloat(document.getElementById('calc-ho').value) || 0;

            if (config === 'series') {
                h1 = 0.0;
                document.getElementById('calc-h1').value = "0.0";
            }

            // Convert to m^3
            let vol_m3 = (volUnit === 'mL') ? vol * 1e-6 : vol * 1e-3;
            let Q_m3s = vol_m3 / t;
            let Q_ls = (volUnit === 'mL') ? (vol / 1000) / t : vol / t;

            // Datum correction
            let Hd = 0.15;
            if (config === 'series') Hd = -0.07;
            if (config === 'parallel') Hd = 0.94;

            let H = ho - h1 + Hd;
            let Wi = 9810 * Q_m3s * H;

            const stepsHtml = `
                <div>1. ปริมาตรแปลงเป็น ลบ.ม.: ${vol} ${volUnit} = <span class="text-amber-400 font-bold">${vol_m3.toExponential(4)} m³</span></div>
                <div>2. อัตราไหล Q: (${vol_m3.toExponential(4)}) ÷ ${t.toFixed(2)} s = <span class="text-emerald-400 font-bold">${Q_m3s.toExponential(4)} m³/s</span> (${Q_ls.toFixed(4)} L/s)</div>
                <div>3. Datum Head Corr. (Hd): <span class="text-sky-400 font-bold">${Hd > 0 ? '+' : ''}${Hd.toFixed(2)} m</span></div>
                <div>4. Total Head H: ${ho.toFixed(2)} - ${h1.toFixed(2)} + (${Hd.toFixed(2)}) = <span class="text-purple-400 font-bold">${H.toFixed(2)} m</span></div>
                <div>5. Wi = 9,810 × (${Q_m3s.toExponential(4)}) × ${H.toFixed(2)}</div>
            `;
            document.getElementById('calc-steps').innerHTML = stepsHtml;
            document.getElementById('calc-power-result').innerText = `${Wi.toFixed(2)} Watts`;
        }

        // Quiz Logic
        const quizAnswers = {
            1: { correct: 'B', expl: 'ถูกต้อง! ในระบบอนุกรม ปั๊ม 1 ดูดน้ำจาก Sump tank ซึ่งเป็นถังเปิดผิวสัมผัสบรรยากาศ จึงถือว่า h1 = 0 m เสมอ แล้วส่งต่อให้ปั๊มตัวที่ 2 ช่วยอัดพลังงาน Head เพิ่มเป็น 2 เท่า' },
            2: { correct: 'C', expl: 'ถูกต้อง! สมการคือ Hd = hd(outlet) - hd(inlet) = 0.17 - 0.24 = -0.07 m (มีค่าติดลบ! เป็นจุดดักข้อสอบยอดฮิต)' },
            3: { correct: 'C', expl: 'ถูกต้อง! 5,000 mL = 5 L = 0.005 m³ จากนั้น Q = 0.005 ÷ 4.0 = 0.00125 m³/s (ถ้าตอบ ก. คือลืมแปลงหน่วยมิลลิลิตรเป็นลูกบาศก์เมตร)' },
            4: { correct: 'A', expl: 'ถูกต้อง! แปลง Q = 2.0 L/s = 0.002 m³/s จากนั้น Wi = 9,810 × 0.002 × 20.0 = 392.4 Watts (ช้อยส์ ข. ดักคนลืมแปลงลิตรเป็นลูกบาศก์เมตร)' },
            5: { correct: 'B', expl: 'ถูกต้อง! การต่อแบบขนานทำให้สายน้ำแยกสูบพร้อมกัน อัตราไหลจึงรวมกัน (Q_total = Q1 + Q2 = 2Q) เหมาะที่สุดกับงานสูบระบายน้ำท่วมที่ต้องการปริมาณน้ำมาก' }
        };

        let answeredCount = 0;
        let score = 0;

        function checkAnswer(qNum, choice) {
            const q = quizAnswers[qNum];
            const explBox = document.getElementById(`q${qNum}-explanation`);
            const qBox = document.getElementById(`q${qNum}-box`);
            
            if (explBox.classList.contains('active-answered')) return; // already answered
            explBox.classList.add('active-answered');

            explBox.classList.remove('hidden');
            if (choice === q.correct) {
                score++;
                document.getElementById('current-score').innerText = score;
                explBox.className = 'text-xs p-3.5 rounded-xl mt-2 bg-emerald-950/70 border border-emerald-500/50 text-emerald-200';
                explBox.innerHTML = `<strong>✓ ถูกต้อง!</strong> ${q.expl}`;
            } else {
                explBox.className = 'text-xs p-3.5 rounded-xl mt-2 bg-red-950/70 border border-red-500/50 text-red-200';
                explBox.innerHTML = `<strong>✗ ยังไม่ถูกต้อง!</strong> คำตอบที่ถูกคือข้อ <strong>${q.correct}</strong><br>${q.expl}`;
            }
        }

        // Chart.js Setup for iPad Reference Curve
        let chartUnit = 'ls';
        let examChart = null;

        const singleData = [
            { x: 0.0565, y: 18.15 }, { x: 0.1789, y: 17.15 }, { x: 0.3650, y: 15.65 },
            { x: 0.6466, y: 14.15 }, { x: 0.9464, y: 12.65 }, { x: 1.0760, y: 11.15 },
            { x: 1.1646, y: 9.15 }, { x: 1.3345, y: 7.65 }, { x: 1.4577, y: 6.15 }, { x: 1.6322, y: 4.15 }
        ];

        const parallelData = [
            { x: 0.1575, y: 19.94 }, { x: 0.4184, y: 17.94 }, { x: 1.3417, y: 16.44 },
            { x: 0.7407, y: 14.94 }, { x: 1.9036, y: 13.94 }, { x: 2.4116, y: 11.94 },
            { x: 2.4351, y: 9.94 }, { x: 2.7778, y: 8.44 }, { x: 2.6455, y: 7.44 }, { x: 2.9644, y: 6.44 }
        ].sort((a,b) => a.x - b.x);

        const seriesData = [
            { x: 0.0401, y: 37.93 }, { x: 0.2708, y: 35.93 }, { x: 0.4724, y: 31.93 },
            { x: 0.6772, y: 27.93 }, { x: 0.8174, y: 23.93 }, { x: 0.9091, y: 19.93 },
            { x: 1.3078, y: 15.93 }, { x: 1.3979, y: 11.93 }, { x: 1.4925, y: 7.93 }, { x: 1.6026, y: 3.93 }
        ];

        function getPoints(data, unit) {
            return data.map(pt => ({
                x: unit === 'ls' ? pt.x : pt.x / 1000,
                y: pt.y
            }));
        }

        function initExamChart() {
            if (examChart) examChart.destroy();
            const ctx = document.getElementById('examPumpChart').getContext('2d');
            const xLabel = chartUnit === 'ls' ? 'Discharge Q (L/s)' : 'Discharge Q (m³/s)';

            examChart = new Chart(ctx, {
                type: 'line',
                data: {
                    datasets: [
                        {
                            label: 'ปั๊มเดี่ยว (Single Pump Baseline)',
                            data: getPoints(singleData, chartUnit),
                            borderColor: '#38bdf8',
                            backgroundColor: '#38bdf8',
                            borderWidth: 3,
                            pointRadius: 5,
                            tension: 0.35
                        },
                        {
                            label: 'ต่ออนุกรม (Series: 2H เพิ่มแรงดัน 2 เท่า)',
                            data: getPoints(seriesData, chartUnit),
                            borderColor: '#c084fc',
                            backgroundColor: '#c084fc',
                            borderWidth: 3,
                            pointRadius: 5,
                            tension: 0.35
                        },
                        {
                            label: 'ต่อขนาน (Parallel: 2Q เพิ่มปริมาณน้ำ 2 เท่า)',
                            data: getPoints(parallelData, chartUnit),
                            borderColor: '#34d399',
                            backgroundColor: '#34d399',
                            borderWidth: 3,
                            pointRadius: 5,
                            tension: 0.35
                        }
                    ]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    devicePixelRatio: Math.max(window.devicePixelRatio || 1, 2),
                    plugins: {
                        legend: {
                            position: 'bottom',
                            labels: {
                                font: { family: 'Sarabun', size: 12 },
                                color: '#cbd5e1',
                                padding: 15
                            }
                        },
                        tooltip: {
                            callbacks: {
                                label: ctx => `${ctx.dataset.label}: H = ${ctx.parsed.y.toFixed(2)} m, Q = ${ctx.parsed.x.toFixed(chartUnit === 'ls' ? 3 : 5)}`
                            }
                        }
                    },
                    scales: {
                        x: {
                            type: 'linear',
                            title: {
                                display: true,
                                text: xLabel,
                                color: '#94a3b8',
                                font: { family: 'Chakra Petch', size: 13, weight: 'bold' }
                            },
                            ticks: { color: '#64748b' },
                            grid: { color: 'rgba(255,255,255,0.06)' }
                        },
                        y: {
                            title: {
                                display: true,
                                text: 'Total Head H (m Water)',
                                color: '#94a3b8',
                                font: { family: 'Chakra Petch', size: 13, weight: 'bold' }
                            },
                            min: 0,
                            suggestedMax: 42,
                            ticks: { color: '#64748b' },
                            grid: { color: 'rgba(255,255,255,0.06)' }
                        }
                    }
                }
            });
        }

        function updateChartUnit(unit) {
            chartUnit = unit;
            const btnLs = document.getElementById('chart-btn-ls');
            const btnM3s = document.getElementById('chart-btn-m3s');
            if (unit === 'ls') {
                btnLs.className = 'px-3 py-1 rounded-lg text-xs font-semibold bg-sky-500 text-white shadow-md';
                btnM3s.className = 'px-3 py-1 rounded-lg text-xs font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700';
            } else {
                btnM3s.className = 'px-3 py-1 rounded-lg text-xs font-semibold bg-sky-500 text-white shadow-md';
                btnLs.className = 'px-3 py-1 rounded-lg text-xs font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700';
            }
            initExamChart();
        }

        window.addEventListener('DOMContentLoaded', () => {
            initExamChart();
            runCalculator();
        });
    </script>
</body>
</html>
'''

with open("/Users/thanaporn/.gemini/antigravity/scratch/CE272/index.html", "w", encoding="utf-8") as f:
    f.write(html_code)

print("Generated CE272/index.html successfully.")
