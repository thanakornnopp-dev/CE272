# -*- coding: utf-8 -*-
import os

html_parts = []

# PART 1: Head & Setup
html_parts.append(r'''<!DOCTYPE html>
<html lang="th" class="scroll-smooth">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CE272 รวมสรุปเตรียมสอบปฏิบัติการกลศาสตร์ของไหล ครบทุกบท (ฉบับคนไม่รู้อะไรเลย)</title>
    <!-- Tailwind CSS -->
    <script src="https://cdn.tailwindcss.com"></script>
    <!-- Chart.js -->
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <!-- FontAwesome Icons -->
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
            background-color: #0b1120;
            color: #f1f5f9;
            -webkit-font-smoothing: antialiased;
        }
        h1, h2, h3, h4, .font-heading {
            font-family: 'Chakra Petch', sans-serif;
        }
        .glass-panel {
            background: rgba(30, 41, 59, 0.75);
            backdrop-filter: blur(16px);
            border: 1px solid rgba(255, 255, 255, 0.08);
        }
        .glass-panel:hover {
            border-color: rgba(56, 189, 248, 0.3);
        }
        .trap-callout {
            background: linear-gradient(135deg, rgba(239, 68, 68, 0.12), rgba(185, 28, 28, 0.05));
            border-left: 4px solid #ef4444;
        }
        .formula-box {
            background: rgba(15, 23, 42, 0.9);
            border: 1px solid rgba(255, 255, 255, 0.1);
        }
        .flow-pill {
            display: inline-flex;
            align-items: center;
            gap: 0.375rem;
            padding: 0.25rem 0.625rem;
            border-radius: 9999px;
            font-size: 0.75rem;
            font-weight: 600;
        }
        @media print {
            .no-print { display: none !important; }
            body { background: white !important; color: black !important; }
            .glass-panel { background: white !important; border: 1px solid #ccc !important; box-shadow: none !important; }
            .text-white { color: black !important; }
            .text-slate-300, .text-slate-400 { color: #333 !important; }
            .page-break { page-break-before: always; }
        }
    </style>
</head>
<body class="min-h-screen text-slate-200">

    <!-- Top Banner -->
    <div class="bg-gradient-to-r from-sky-600 via-indigo-600 to-purple-600 text-white text-xs sm:text-sm font-medium py-2 px-4 text-center shadow-md no-print">
        <span>📚 <strong>CE272 คลังสรุปเตรียมสอบปฏิบัติการกลศาสตร์ของไหล ครบทุกบท (1 ถึง 11):</strong> สรุปสูตร ทิศทางน้ำเข้า-ออก วาล์ว จุดดักคะแนน และแนวข้อสอบปรนัย</span>
    </div>

    <!-- Navigation Header -->
    <header class="sticky top-0 z-50 glass-panel border-b border-slate-800 shadow-xl px-4 sm:px-8 py-3.5 flex flex-wrap items-center justify-between gap-4">
        <div class="flex items-center gap-3">
            <div class="w-10 h-10 rounded-xl bg-gradient-to-tr from-sky-500 to-indigo-500 flex items-center justify-center text-white font-extrabold text-lg shadow-md shadow-sky-500/25">
                CE
            </div>
            <div>
                <a href="#hero" class="text-lg sm:text-xl font-bold tracking-tight text-white font-heading flex items-center gap-2">
                    CE 272 <span class="text-xs px-2.5 py-0.5 rounded-full bg-sky-500/20 text-sky-400 border border-sky-500/30 font-normal">Fluid Mechanics Lab</span>
                </a>
                <p class="text-[11px] text-slate-400">คลังติวสอบอัตโนมัติครบทุกบท (ฉบับคนไม่รู้อะไรเลย)</p>
            </div>
        </div>

        <!-- Quick Chapter Navigator Dropdown / Pills -->
        <div class="flex items-center gap-2 text-xs overflow-x-auto max-w-full pb-1 sm:pb-0 no-print">
            <a href="#ch-intro" class="px-2.5 py-1 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 whitespace-nowrap">บทนำ</a>
            <a href="#ch2" class="px-2.5 py-1 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 whitespace-nowrap">บท 2 แรงดัน</a>
            <a href="#ch3" class="px-2.5 py-1 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 whitespace-nowrap">บท 3 ลำน้ำ</a>
            <a href="#ch4" class="px-2.5 py-1 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 whitespace-nowrap">บท 4 เบอร์นูลลี่</a>
            <a href="#ch5" class="px-2.5 py-1 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 whitespace-nowrap">บท 5 แมนนิ่ง</a>
            <a href="#ch6" class="px-2.5 py-1 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 whitespace-nowrap">บท 6 ฝาย</a>
            <a href="#ch7" class="px-2.5 py-1 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 whitespace-nowrap">บท 7 ท่อ</a>
            <a href="#ch8" class="px-2.5 py-1 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 whitespace-nowrap">บท 8 รูลอด</a>
            <a href="#ch9" class="px-2.5 py-1 rounded-lg bg-sky-600/40 border border-sky-500/50 text-sky-300 font-bold whitespace-nowrap">บท 9 ปั๊ม</a>
            <a href="#ch10" class="px-2.5 py-1 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 whitespace-nowrap">บท 10 ประตูน้ำ</a>
            <a href="#ch11" class="px-2.5 py-1 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 whitespace-nowrap">บท 11 เวนจูรี่</a>
            <a href="#quiz-master" class="px-3 py-1 rounded-lg bg-indigo-600 hover:bg-indigo-500 text-white font-bold whitespace-nowrap flex items-center gap-1">
                <i class="fa-solid fa-pen-nib"></i> ข้อสอบ 12 ข้อ
            </a>
            <button onclick="window.print()" class="px-2.5 py-1 rounded-lg bg-slate-700 hover:bg-slate-600 text-white">
                <i class="fa-solid fa-print"></i>
            </button>
        </div>
    </header>
''')

# PART 2: Hero Section & Search
html_parts.append(r'''
    <!-- Hero Section -->
    <section id="hero" class="max-w-6xl mx-auto px-4 pt-10 pb-8 text-center">
        <div class="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full bg-slate-800/80 text-sky-400 text-xs font-semibold border border-slate-700 mb-4 shadow-sm">
            <i class="fa-solid fa-book-bookmark"></i> สรุปครบสมบูรณ์ทุกบทตามคู่มือแล็ป วศย. 272 (รวม 10 การทดลอง)
        </div>
        <h1 class="text-3xl sm:text-5xl font-extrabold text-white tracking-tight mb-4 font-heading leading-tight">
            คู่มือเตรียมสอบปฏิบัติการกลศาสตร์ของไหล<br>
            <span class="bg-gradient-to-r from-sky-400 via-indigo-300 to-purple-400 bg-clip-text text-transparent">CE 272 Comprehensive Exam Hub (ครบทุกบท)</span>
        </h1>
        <p class="text-sm sm:text-base text-slate-300 max-w-3xl mx-auto font-light leading-relaxed mb-6">
            ข้อสอบแล็ปอาจารย์เป็น <strong>ข้อสอบปรนัย (กากบาท) มีสูตรมาให้ครบ!</strong> สิ่งที่ต้องรู้คือ 
            <strong class="text-amber-400">"อุปกรณ์ทำงานยังไง น้ำเข้าทางไหน ออกทางไหน วาล์วไหนเปิด-ปิด และแทนค่าระวังหน่วยอะไร"</strong> 
            เว็บนี้สรุปกระชับ เจาะลึกจุดตายของข้อสอบ ครบตั้งแต่บทที่ 1 ถึงบทที่ 11 สำหรับคนไม่รู้อะไรเลย!
        </p>

        <!-- Search Bar -->
        <div class="max-w-xl mx-auto mb-8 relative no-print">
            <i class="fa-solid fa-magnifying-glass absolute left-4 top-3.5 text-slate-400"></i>
            <input type="text" id="quick-search" oninput="filterContent()" placeholder="พิมพ์ชื่อบท, ชื่ออุปกรณ์, หรือสูตร เช่น ปั๊ม, ฝาย, เบอร์นูลลี่, แมนนิ่ง, Vena Contracta..." class="w-full bg-slate-900/90 border border-slate-700 rounded-2xl py-3 pl-11 pr-4 text-sm text-white placeholder-slate-500 focus:outline-none focus:border-sky-500 shadow-inner">
        </div>

        <!-- Master Cheatsheet Matrix Quick Link -->
        <div class="grid grid-cols-2 sm:grid-cols-4 gap-3 max-w-4xl mx-auto text-left text-xs">
            <a href="#master-table" class="glass-panel p-3.5 rounded-xl border border-slate-700 hover:border-sky-500 transition-all">
                <span class="text-sky-400 font-bold block mb-1"><i class="fa-solid fa-table-list"></i> ตารางสูตรทุกบท</span>
                <span class="text-slate-400">รวมสมการและตัวแปร 10 แล็ป</span>
            </a>
            <a href="#universal-calc" class="glass-panel p-3.5 rounded-xl border border-slate-700 hover:border-emerald-500 transition-all">
                <span class="text-emerald-400 font-bold block mb-1"><i class="fa-solid fa-calculator"></i> เครื่องคิดเลขสูตร</span>
                <span class="text-slate-400">ลองแทนค่าตรวจเลขจริง</span>
            </a>
            <a href="#unit-rules" class="glass-panel p-3.5 rounded-xl border border-slate-700 hover:border-red-500 transition-all">
                <span class="text-red-400 font-bold block mb-1"><i class="fa-solid fa-triangle-exclamation"></i> รวมจุดดักคะแนน</span>
                <span class="text-slate-400">มล. $\to$ ลบ.ม. & ค่าแก้ Z</span>
            </a>
            <a href="#quiz-master" class="glass-panel p-3.5 rounded-xl border border-slate-700 hover:border-purple-500 transition-all">
                <span class="text-purple-400 font-bold block mb-1"><i class="fa-solid fa-check-to-slot"></i> ข้อสอบจำลอง 12 ข้อ</span>
                <span class="text-slate-400">กากบาทพร้อมเฉลยละเอียด</span>
            </a>
        </div>
    </section>
''')

# PART 3: Chapter 1 & Chapter 2
html_parts.append(r'''
    <!-- MAIN CHAPTERS SECTION -->
    <main class="max-w-6xl mx-auto px-4 space-y-10 py-6">

        <!-- บทที่ 1: บทนำ โต๊ะชลศาสตร์ -->
        <section id="ch-intro" class="chapter-card glass-panel rounded-3xl p-6 sm:p-8 border border-slate-700/60 shadow-xl">
            <div class="flex items-center justify-between border-b border-slate-700/60 pb-4 mb-5">
                <div class="flex items-center gap-3">
                    <span class="w-9 h-9 rounded-xl bg-slate-800 text-sky-400 border border-slate-700 flex items-center justify-center font-bold font-heading">1</span>
                    <div>
                        <span class="text-xs font-semibold text-sky-400 uppercase tracking-wider">บทที่ 1 บทนำ (หน้า 3 - 4)</span>
                        <h2 class="text-xl sm:text-2xl font-bold text-white font-heading">โต๊ะชลศาสตร์ (Hydraulic Bench) & การวัดอัตราการไหล</h2>
                    </div>
                </div>
                <span class="flow-pill bg-sky-500/20 text-sky-300 border border-sky-500/30">อุปกรณ์ฐานสำหรับทุกแล็ป</span>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-2 gap-6 text-sm">
                <div class="space-y-3">
                    <h3 class="font-bold text-white text-base flex items-center gap-2">
                        <i class="fa-solid fa-circle-info text-sky-400"></i> ส่วนประกอบและการทำงานของเครื่อง
                    </h3>
                    <ul class="space-y-2 text-slate-300 text-xs sm:text-sm list-disc list-inside leading-relaxed">
                        <li><strong>ถังเก็บน้ำด้านล่าง (Sump Tank):</strong> เป็นอ่างเก็บน้ำหลักสำหรับให้ปั๊มดูดน้ำขึ้นไปใช้งาน</li>
                        <li><strong>เครื่องสูบน้ำ (Centrifugal Pump):</strong> สูบน้ำจาก Sump Tank จ่ายไปยังชุดการทดลองด้านบน</li>
                        <li><strong>ถังวัดปริมาตร (Volumetric Tank):</strong> ถังรับน้ำที่ไหลกลับมาจากชุดทดลอง มี 2 สเต็ป (ช่องแคบด้านล่างสำหรับปริมาตรน้อย และช่องกว้างด้านบนสำหรับปริมาตรมาก)</li>
                        <li><strong>วาล์วระบายน้ำ (Dump / Drain Valve):</strong> วาล์วดัมพ์เปิด-ปิดกักน้ำเพื่อวัดระดับปริมาตร</li>
                        <li><strong>หลอดแก้ววัดระดับ (Sight Glass):</strong> หลอดอ่านปริมาตรน้ำเป็นสเกลลิตร (Litres)</li>
                    </ul>
                </div>

                <div class="space-y-3">
                    <h3 class="font-bold text-white text-base flex items-center gap-2">
                        <i class="fa-solid fa-calculator text-emerald-400"></i> สูตรการหาอัตราการไหลจริง (\(Q\))
                    </h3>
                    <div class="formula-box p-4 rounded-2xl text-xs sm:text-sm space-y-2 text-slate-200">
                        <div class="text-center font-mono text-emerald-400 text-base">
                            \[Q = \frac{\text{Volume}_2 - \text{Volume}_1}{\text{Time}_2 - \text{Time}_1} = \frac{\Delta V}{\Delta t}\]
                        </div>
                        <div class="text-xs text-slate-400">
                            • \(\text{Volume}\) มักอ่านเป็น <strong>ลิตร (L)</strong> หรือ <strong>มล. (mL)</strong><br>
                            • ต้องแปลงเป็น <strong>\(\text{m}^3/\text{s}\)</strong> โดยหาร 1,000 เสมอเมื่อนำไปคิดในสมการพลังงาน!
                        </div>
                    </div>
                    <div class="trap-callout p-3.5 rounded-xl text-xs text-red-200">
                        <strong>📌 จุดดักข้อสอบ:</strong> ในช่วงอัตราไหลต่ำ ให้วัดปริมาตรแค่ 1 ลิตร (ถ้าจับ 5 ลิตรจะช้ามาก) แต่ถ้าอัตราไหลสูง ให้เปลี่ยนเป็น 5 ลิตร เพื่อลดความคลาดเคลื่อนจากการกดนาฬิกาจับเวลา (Human error)!
                    </div>
                </div>
            </div>
        </section>

        <!-- บทที่ 2: จุดศูนย์กลางของแรงดัน -->
        <section id="ch2" class="chapter-card glass-panel rounded-3xl p-6 sm:p-8 border border-slate-700/60 shadow-xl">
            <div class="flex items-center justify-between border-b border-slate-700/60 pb-4 mb-5">
                <div class="flex items-center gap-3">
                    <span class="w-9 h-9 rounded-xl bg-slate-800 text-indigo-400 border border-slate-700 flex items-center justify-center font-bold font-heading">2</span>
                    <div>
                        <span class="text-xs font-semibold text-indigo-400 uppercase tracking-wider">บทที่ 2 (หน้า 5 - 15)</span>
                        <h2 class="text-xl sm:text-2xl font-bold text-white font-heading">จุดศูนย์กลางของแรงดัน (Center of Pressure)</h2>
                    </div>
                </div>
                <span class="flow-pill bg-indigo-500/20 text-indigo-300 border border-indigo-500/30">ทุ่นเสี้ยววงกลม Quadrant</span>
            </div>

            <!-- 1-Minute Summary -->
            <div class="p-4 rounded-2xl bg-indigo-950/30 border border-indigo-500/30 text-xs sm:text-sm text-indigo-200 mb-6">
                <strong>💡 สรุป 3 บรรทัดสำหรับคนรีบสอบ:</strong>
                <ol class="list-decimal list-inside mt-1 space-y-1 text-slate-300">
                    <li>แรงดันน้ำที่กระทำต่อ <strong>ผิวด้านโค้ง</strong> ของทุ่นเสี้ยววงกลมจะพุ่งผ่านจุดหมุน (Pivot) เสมอ ทำให้ <strong>ไม่มีโมเมนต์รอบจุดหมุน</strong></li>
                    <li>โมเมนต์ที่เกิดขึ้นจึงมาจาก <strong>แรงดันน้ำที่แผ่นสี่เหลี่ยมผืนผ้าปลายทุ่น (กว้าง B, สูง D)</strong> เพียงด้านเดียวเท่านั้น</li>
                    <li>สมดุลโมเมนต์รอบจุดหมุน: \(F \cdot h'' = W \cdot L = mgL\) โดยที่จุดศูนย์กลางแรงดัน \(y_{cp}\) จะอยู่ต่ำกว่าจุดเซนทรอยด์ (\(y_{CG}\)) เสมอ</li>
                </ol>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-2 gap-6 text-sm">
                <!-- Partially Submerged -->
                <div class="bg-slate-900/80 p-5 rounded-2xl border border-slate-700 space-y-3">
                    <div class="flex items-center justify-between">
                        <span class="font-bold text-sky-400 text-sm">กรณีที่ 1: แผ่นพื้นจมน้ำบางส่วน (\(d < D\))</span>
                        <span class="text-[11px] px-2 py-0.5 rounded bg-sky-500/20 text-sky-300">ความลึก \(d < 100\text{ mm}\)</span>
                    </div>
                    <div class="space-y-1.5 text-xs sm:text-sm font-mono text-slate-200">
                        <div>• แรงดันน้ำ: \(F = \frac{1}{2} \rho g B d^2\)</div>
                        <div>• จุดศูนย์กลางแรงดันตามทฤษฎี: \(\mathbf{y_{cp} = \frac{2}{3}d}\) <span class="text-slate-400">(วัดจากผิวน้ำ)</span></div>
                        <div>• แขนของแรงจากการทดลอง: \(h'' = \frac{mgL}{F} = \frac{2mL}{\rho B d^2}\)</div>
                        <div>• จุดศูนย์กลางแรงดันจากการทดลอง: \(\mathbf{y_{cp} = h'' - (H - d)}\)</div>
                    </div>
                    <div class="text-[11px] text-slate-400 pt-1 border-t border-slate-800">
                        \(B = 75\text{ mm}\) (กว้าง), \(D = 100\text{ mm}\) (สูง), \(H = 200\text{ mm}\), \(L = 275\text{ mm}\)
                    </div>
                </div>

                <!-- Fully Submerged -->
                <div class="bg-slate-900/80 p-5 rounded-2xl border border-slate-700 space-y-3">
                    <div class="flex items-center justify-between">
                        <span class="font-bold text-purple-400 text-sm">กรณีที่ 2: แผ่นพื้นจมน้ำทั้งหมด (\(d \ge D\))</span>
                        <span class="text-[11px] px-2 py-0.5 rounded bg-purple-500/20 text-purple-300">ความลึก \(d \ge 100\text{ mm}\)</span>
                    </div>
                    <div class="space-y-1.5 text-xs sm:text-sm font-mono text-slate-200">
                        <div>• แรงดันน้ำ: \(F = \rho g B D \left(d - \frac{D}{2}\right)\)</div>
                        <div>• จุดศูนย์กลางแรงดันตามทฤษฎี: \(y_{cp} = y_c + \frac{I_{xx}}{y_c A}\)</div>
                        <div>• แขนของแรงจากการทดลอง: \(h'' = \frac{mL}{\rho B D \left(d - \frac{D}{2}\right)}\)</div>
                        <div>• จากการทดลอง: \(\mathbf{y_{cp} = h'' - (H - d)}\)</div>
                    </div>
                    <div class="trap-callout p-2.5 rounded-lg text-xs text-red-200">
                        ⚠️ <strong>ข้อสอบชอบถาม:</strong> ระยะ \(h''\) วัดจากไหน? ตอบ: วัดจาก <strong>"จุดหมุน (Pivot)"</strong> ลงมาถึงแนวแรง ไม่ใช่ผิวน้ำ!
                    </div>
                </div>
            </div>
        </section>
''')

# PART 4: Chapter 3 & Chapter 4
html_parts.append(r'''
        <!-- บทที่ 3: แรงกระแทกของลำน้ำ -->
        <section id="ch3" class="chapter-card glass-panel rounded-3xl p-6 sm:p-8 border border-slate-700/60 shadow-xl">
            <div class="flex items-center justify-between border-b border-slate-700/60 pb-4 mb-5">
                <div class="flex items-center gap-3">
                    <span class="w-9 h-9 rounded-xl bg-slate-800 text-amber-400 border border-slate-700 flex items-center justify-center font-bold font-heading">3</span>
                    <div>
                        <span class="text-xs font-semibold text-amber-400 uppercase tracking-wider">บทที่ 3 (หน้า 16 - 19)</span>
                        <h2 class="text-xl sm:text-2xl font-bold text-white font-heading">แรงกระแทกของลำน้ำ (Impact of Jet)</h2>
                    </div>
                </div>
                <span class="flow-pill bg-amber-500/20 text-amber-300 border border-amber-500/30">Momentum Equation</span>
            </div>

            <!-- Theory Cards -->
            <div class="grid grid-cols-1 sm:grid-cols-3 gap-4 mb-6">
                <!-- Flat Plate -->
                <div class="bg-slate-900/80 p-4 rounded-2xl border border-slate-700">
                    <span class="text-xs text-slate-400 font-bold block mb-1">1. ฉากแบนราบ (Flat Plate \(\theta = 90^\circ\))</span>
                    <p class="text-xs text-slate-300 mb-2">น้ำพุ่งชนแล้วกระจายออกแนวราบ \(90^\circ\)</p>
                    <div class="font-mono text-emerald-400 font-bold text-sm bg-slate-800 p-2 rounded-lg text-center">
                        \[F = \rho Q V = \rho A V^2\]
                    </div>
                </div>

                <!-- Hemispherical Cup -->
                <div class="bg-slate-900/80 p-4 rounded-2xl border border-amber-500/40 relative">
                    <span class="absolute -top-2.5 right-3 text-[10px] bg-red-600 text-white font-bold px-2 py-0.5 rounded-full">ออกบ่อยสุด!</span>
                    <span class="text-xs text-amber-400 font-bold block mb-1">2. ฉากรูปครึ่งทรงกลม (\(\theta = 0^\circ\) หรือ \(180^\circ\))</span>
                    <p class="text-xs text-slate-300 mb-2">น้ำพุ่งชนแล้วสะท้อนย้อนกลับ \(180^\circ\)</p>
                    <div class="font-mono text-amber-300 font-extrabold text-sm bg-slate-800 p-2 rounded-lg text-center">
                        \[F = 2\rho Q V = 2\rho A V^2\]
                    </div>
                    <span class="text-[11px] text-amber-400 mt-1 block">⭐ แรงกระแทกเป็น <strong>2 เท่า</strong> ของฉากแบน!</span>
                </div>

                <!-- Conical / Angle -->
                <div class="bg-slate-900/80 p-4 rounded-2xl border border-slate-700">
                    <span class="text-xs text-purple-400 font-bold block mb-1">3. ฉากทำมุม \(\theta\) ใดๆ (Conical)</span>
                    <p class="text-xs text-slate-300 mb-2">เช่น มุม \(30^\circ, 120^\circ\)</p>
                    <div class="font-mono text-purple-300 font-bold text-xs bg-slate-800 p-2 rounded-lg text-center">
                        \[F = \rho Q V (\cos\theta + 1)\]
                    </div>
                </div>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-2 gap-4 text-xs sm:text-sm">
                <div class="p-4 rounded-2xl bg-slate-900 border border-slate-700">
                    <strong class="text-white block mb-1">⚖️ วิธีการทดลอง & สมดุลแรง:</strong>
                    เมื่อเปิดน้ำพุ่งชนฉากกั้น ก้านจานวางตุ้มน้ำหนักจะยกตัวขึ้น ผู้ทดลองต้องวางตุ้มน้ำหนัก \(m\) บนจานจนกระทั่ง Level Gauge กลับมาตรงระดับขีดอ้างอิงเดิม:
                    <div class="my-2 p-2 bg-slate-800 rounded font-mono text-sky-400 text-center">
                        \[F_{\text{actual}} = W = mg\]
                    </div>
                </div>
                <div class="p-4 rounded-2xl bg-slate-900 border border-slate-700">
                    <strong class="text-white block mb-1">📈 กราฟความสัมพันธ์:</strong>
                    เขียนกราฟระหว่าง แรงจากตุ้มน้ำหนัก (\(F = mg\)) แกน Y กับ \(V^2\) แกน X:
                    <div class="my-2 p-2 bg-slate-800 rounded font-mono text-emerald-400 text-center">
                        \[\text{Slope} = \rho A (\cos\theta + 1)\]
                    </div>
                    นำความชันไปคำนวณหามุม \(\theta\) ของฉากกั้นแต่ละชนิด
                </div>
            </div>
        </section>

        <!-- บทที่ 4: สมการเบอร์นูลลี่และการประยุกต์ใช้ -->
        <section id="ch4" class="chapter-card glass-panel rounded-3xl p-6 sm:p-8 border border-slate-700/60 shadow-xl">
            <div class="flex items-center justify-between border-b border-slate-700/60 pb-4 mb-5">
                <div class="flex items-center gap-3">
                    <span class="w-9 h-9 rounded-xl bg-slate-800 text-sky-400 border border-slate-700 flex items-center justify-center font-bold font-heading">4</span>
                    <div>
                        <span class="text-xs font-semibold text-sky-400 uppercase tracking-wider">บทที่ 4 (หน้า 20 - 24)</span>
                        <h2 class="text-xl sm:text-2xl font-bold text-white font-heading">สมการเบอร์นูลลี่และการประยุกต์ใช้ (Bernoulli & Venturi Tube)</h2>
                    </div>
                </div>
                <span class="flow-pill bg-sky-500/20 text-sky-300 border border-sky-500/30">ท่อคอด Venturi Meter</span>
            </div>

            <!-- EGL vs HGL Diagram Concept -->
            <div class="bg-slate-900/90 p-5 rounded-2xl border border-slate-700 mb-6">
                <div class="grid grid-cols-1 md:grid-cols-2 gap-4 items-center">
                    <div>
                        <h3 class="font-bold text-white text-base mb-2">⚡ หัวใจสำคัญของสมการเบอร์นูลลี่</h3>
                        <div class="font-mono text-xs sm:text-sm text-sky-300 formula-box p-3 rounded-xl mb-3">
                            \[\frac{P_1}{\gamma} + \frac{V_1^2}{2g} + Z_1 = \frac{P_2}{\gamma} + \frac{V_2^2}{2g} + Z_2 + h_f\]
                        </div>
                        <ul class="text-xs sm:text-sm text-slate-300 space-y-1 list-disc list-inside">
                            <li><strong>Hydraulic Grade Line (HGL):</strong> ระดับความดัน \(\frac{P}{\gamma} + Z\) (คือระดับน้ำที่มองเห็นในหลอดมาโนมิเตอร์)</li>
                            <li><strong>Energy Grade Line (EGL):</strong> พลังงานรวม \(\frac{P}{\gamma} + \frac{V^2}{2g} + Z\) (อยู่สูงกว่า HGL เป็นระยะ Velocity Head)</li>
                        </ul>
                    </div>

                    <div class="bg-slate-800/80 p-4 rounded-xl border border-slate-700 text-xs sm:text-sm">
                        <strong class="text-amber-400 block mb-1">🎯 เกิดอะไรขึ้นที่คอคอด (Throat)?</strong>
                        เมื่อน้ำไหลผ่านหน้าตัดแคบ (Throat):
                        <div class="my-2 p-2 bg-slate-900 rounded font-mono text-center text-slate-200">
                            หน้าตัด \(A \downarrow \implies\) ความเร็ว \(V \uparrow \implies\) ความดัน \(P \downarrow\)
                        </div>
                        ที่คอคอด ความเร็วจะสูงสุด ทำให้ระดับน้ำในหลอดมาโนมิเตอร์ <strong>ลดลงต่ำที่สุด</strong> เสมอ!
                    </div>
                </div>
            </div>

            <!-- Formulas Table -->
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 text-xs sm:text-sm">
                <div class="p-4 rounded-xl bg-slate-900 border border-slate-700">
                    <span class="text-slate-400 font-bold block mb-1">อัตราการไหลทางทฤษฎี (\(Q_{\text{theory}}\)):</span>
                    <div class="font-mono text-emerald-400 text-xs my-2">
                        \[Q_{\text{theory}} = A_1 \sqrt{\frac{2g(h_1 - h_2)}{(A_1/A_2)^2 - 1}}\]
                    </div>
                    <span class="text-slate-400 text-[11px]">\(h_1 - h_2\) คือผลต่างระดับน้ำในท่อมาโนมิเตอร์หน้าตัดกว้างกับคอคอด</span>
                </div>

                <div class="p-4 rounded-xl bg-slate-900 border border-slate-700">
                    <span class="text-slate-400 font-bold block mb-1">สัมประสิทธิ์การปรับแก้ (\(C_d\)):</span>
                    <div class="font-mono text-purple-400 text-sm my-2">
                        \[C_d = \frac{Q_{\text{actual}}}{Q_{\text{theory}}}\]
                    </div>
                    <span class="text-slate-400 text-[11px]">\(C_d < 1\) เสมอ (ประมาณ 0.95 - 0.98) เนื่องจากมีการสูญเสียพลังงานจากความเสียดทาน</span>
                </div>
            </div>
        </section>
''')

# PART 5: Chapter 5 & Chapter 6
html_parts.append(r'''
        <!-- บทที่ 5: สมการแมนนิ่ง -->
        <section id="ch5" class="chapter-card glass-panel rounded-3xl p-6 sm:p-8 border border-slate-700/60 shadow-xl">
            <div class="flex items-center justify-between border-b border-slate-700/60 pb-4 mb-5">
                <div class="flex items-center gap-3">
                    <span class="w-9 h-9 rounded-xl bg-slate-800 text-emerald-400 border border-slate-700 flex items-center justify-center font-bold font-heading">5</span>
                    <div>
                        <span class="text-xs font-semibold text-emerald-400 uppercase tracking-wider">บทที่ 5 (หน้า 25 - 26)</span>
                        <h2 class="text-xl sm:text-2xl font-bold text-white font-heading">สมการแมนนิ่ง (Manning's Equation - ทางน้ำเปิด)</h2>
                    </div>
                </div>
                <span class="flow-pill bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">Open Channel Flow</span>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-12 gap-6 items-center">
                <div class="md:col-span-7 space-y-4">
                    <div class="formula-box p-4 rounded-2xl text-center">
                        <span class="text-xs text-emerald-400 font-mono font-bold block mb-1">สมการแมนนิ่งในหน่วย SI (สมการ 5.2):</span>
                        <div class="text-lg sm:text-2xl font-extrabold text-white font-mono">
                            \[V = \frac{1}{n} R^{2/3} S^{1/2} \quad \implies \quad Q = \frac{1}{n} A R^{2/3} S^{1/2}\]
                        </div>
                    </div>

                    <div class="grid grid-cols-3 gap-2 text-xs text-center">
                        <div class="p-2.5 bg-slate-900 rounded-xl border border-slate-700">
                            <strong class="text-sky-400 block">\(n\)</strong>
                            สัมประสิทธิ์ความขรุขระ (Manning's n)
                        </div>
                        <div class="p-2.5 bg-slate-900 rounded-xl border border-slate-700">
                            <strong class="text-amber-400 block">\(R = A / P\)</strong>
                            รัศมีชลศาสตร์ (Hydraulic Radius)
                        </div>
                        <div class="p-2.5 bg-slate-900 rounded-xl border border-slate-700">
                            <strong class="text-purple-400 block">\(S = \tan\theta\)</strong>
                            ความลาดชันท้องคลอง (Slope)
                        </div>
                    </div>
                </div>

                <div class="md:col-span-5 space-y-3">
                    <div class="p-4 rounded-2xl bg-slate-900 border border-slate-700 text-xs sm:text-sm">
                        <strong class="text-white block mb-1">📊 เปรียบเทียบผลการทดลอง:</strong>
                        <ul class="space-y-1.5 text-slate-300 list-disc list-inside">
                            <li><strong>พื้นคลองเรียบ (Smooth Bed):</strong> ค่า \(n\) น้อย (\(\approx 0.010 - 0.012\)) น้ำไหลเร็ว ระดับน้ำตื้น</li>
                            <li><strong>พื้นคลองมีหญ้า (Rough Bed):</strong> ค่า \(n\) มาก (\(\approx 0.025 - 0.035\)) ต้านทานการไหล ทำให้น้ำไหลช้าและระดับน้ำเอ่อสูงขึ้น</li>
                        </ul>
                    </div>
                    <div class="trap-callout p-3 rounded-xl text-xs text-red-200">
                        ⚠️ <strong>จุดดักหน่วย:</strong> ความลาดชัน \(S\) หาจาก \(\tan(\theta)\) เช่น ถ้าโจทย์บอกเอียง \(0.125^\circ\) ให้กดเครื่องคิดเลข \(\tan(0.125^\circ)\) ไม่ใช่เอา \(0.125\) ไปคูณตรงๆ!
                    </div>
                </div>
            </div>
        </section>

        <!-- บทที่ 6: การวัดอัตราการไหลด้วยฝาย -->
        <section id="ch6" class="chapter-card glass-panel rounded-3xl p-6 sm:p-8 border border-slate-700/60 shadow-xl">
            <div class="flex items-center justify-between border-b border-slate-700/60 pb-4 mb-5">
                <div class="flex items-center gap-3">
                    <span class="w-9 h-9 rounded-xl bg-slate-800 text-rose-400 border border-slate-700 flex items-center justify-center font-bold font-heading">6</span>
                    <div>
                        <span class="text-xs font-semibold text-rose-400 uppercase tracking-wider">บทที่ 6 (หน้า 27 - 31)</span>
                        <h2 class="text-xl sm:text-2xl font-bold text-white font-heading">การวัดอัตราการไหลด้วยฝาย (Flow over Weir)</h2>
                    </div>
                </div>
                <span class="flow-pill bg-rose-500/20 text-rose-300 border border-rose-500/30">ฝายสี่เหลี่ยม vs ฝายสามเหลี่ยม V-Notch</span>
            </div>

            <!-- Comparison Grid -->
            <div class="grid grid-cols-1 md:grid-cols-2 gap-6 text-sm">
                <!-- Rectangular Weir -->
                <div class="bg-slate-900 p-5 rounded-2xl border border-slate-700 space-y-3">
                    <div class="flex items-center justify-between">
                        <span class="font-bold text-sky-400 text-base">1. ฝายรูปสี่เหลี่ยม (Rectangular Weir)</span>
                        <span class="text-xs px-2 py-0.5 rounded bg-sky-500/20 text-sky-300">แปรผันตาม \(H^{1.5}\)</span>
                    </div>
                    <div class="formula-box p-3 rounded-xl text-center font-mono text-sky-300 text-xs sm:text-sm">
                        \[Q_{\text{actual}} = C_d \frac{2}{3} B \sqrt{2g} H^{3/2}\]
                    </div>
                    <ul class="text-xs text-slate-300 space-y-1 list-disc list-inside">
                        <li>\(B\) = ความกว้างของช่องเปิดฝาย (เมตร)</li>
                        <li>\(H\) = ความสูงของระดับน้ำเหนือสันฝาย (วัดด้วย Hook Gauge)</li>
                        <li><strong>การเขียนกราฟ:</strong> พลอต \(Q_{\text{actual}}\) (แกน Y) กับ \(H^{3/2}\) (แกน X) จะได้เส้นตรงที่มีความชันเท่ากับ \(C_d \frac{2}{3} B \sqrt{2g}\)</li>
                    </ul>
                </div>

                <!-- Triangular Weir -->
                <div class="bg-slate-900 p-5 rounded-2xl border border-slate-700 space-y-3">
                    <div class="flex items-center justify-between">
                        <span class="font-bold text-rose-400 text-base">2. ฝายรูปสามเหลี่ยม (V-Notch Weir)</span>
                        <span class="text-xs px-2 py-0.5 rounded bg-rose-500/20 text-rose-300">แปรผันตาม \(H^{2.5}\)</span>
                    </div>
                    <div class="formula-box p-3 rounded-xl text-center font-mono text-rose-300 text-xs sm:text-sm">
                        \[Q_{\text{actual}} = C_d \frac{8}{15} \sqrt{2g} \tan\left(\frac{\theta}{2}\right) H^{5/2}\]
                    </div>
                    <ul class="text-xs text-slate-300 space-y-1 list-disc list-inside">
                        <li>ถ้าเป็นฝายมุมฉาก \(\theta = 90^\circ \implies \tan(45^\circ) = 1\)</li>
                        <li>สูตรย่อฝาย \(90^\circ\): \(\mathbf{Q_{\text{theory}} \approx 2.36 H^{5/2}}\)</li>
                        <li><strong>การเขียนกราฟ:</strong> พลอต \(Q_{\text{actual}}\) (แกน Y) กับ \(H^{5/2}\) (แกน X)</li>
                    </ul>
                </div>
            </div>

            <div class="mt-4 p-4 rounded-2xl bg-amber-950/30 border border-amber-500/40 text-xs sm:text-sm text-amber-200">
                ⭐ <strong>ข้อสอบถามบ่อยมาก:</strong> ทำไมฝายสามเหลี่ยมถึงวัดอัตราการไหลต่ำๆ ได้แม่นยำกว่าฝายสี่เหลี่ยม?<br>
                <span class="text-slate-300"><strong>ตอบ:</strong> เพราะที่อัตราการไหลต่ำๆ น้ำในฝายสามเหลี่ยมจะมีความสูง \(H\) ยกตัวขึ้นมามากกว่าฝายสี่เหลี่ยม ทำให้มองเห็นและใช้ Hook gauge อ่านค่าวัดได้ชัดเจน คลาดเคลื่อนน้อยกว่ามาก!</span>
            </div>
        </section>
''')

# PART 6: Chapter 7 & Chapter 8
html_parts.append(r'''
        <!-- บทที่ 7: การสูญเสียพลังงานในท่อ -->
        <section id="ch7" class="chapter-card glass-panel rounded-3xl p-6 sm:p-8 border border-slate-700/60 shadow-xl">
            <div class="flex items-center justify-between border-b border-slate-700/60 pb-4 mb-5">
                <div class="flex items-center gap-3">
                    <span class="w-9 h-9 rounded-xl bg-slate-800 text-cyan-400 border border-slate-700 flex items-center justify-center font-bold font-heading">7</span>
                    <div>
                        <span class="text-xs font-semibold text-cyan-400 uppercase tracking-wider">บทที่ 7 (หน้า 32 - 41)</span>
                        <h2 class="text-xl sm:text-2xl font-bold text-white font-heading">การสูญเสียพลังงานของการไหลในท่อ (Loss in Pipe Network)</h2>
                    </div>
                </div>
                <span class="flow-pill bg-cyan-500/20 text-cyan-300 border border-cyan-500/30">ท่อเดี่ยว vs ท่อขนาน vs ท่ออนุกรม</span>
            </div>

            <!-- Darcy Weisbach Equation -->
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4 mb-6">
                <div class="formula-box p-4 rounded-2xl text-xs sm:text-sm space-y-2">
                    <span class="text-cyan-400 font-bold block">สมการการสูญเสียหลัก (Major Loss: Darcy-Weisbach):</span>
                    <div class="font-mono text-center text-white text-base my-1">
                        \[h_f = f \frac{L}{D} \frac{V^2}{2g} = f \frac{L}{D^5} \frac{8 Q^2}{\pi^2 g}\]
                    </div>
                    <p class="text-slate-400 text-xs">• การสูญเสียเนื่องจากความเสียดทานแปรผันตาม <strong>\(Q^2\)</strong> และแปรผกผันกับ <strong>\(D^5\)</strong> (ถ้าขนาดท่อลดลงครึ่งหนึ่ง \(h_f\) จะพุ่งสูงขึ้น 32 เท่า!)</p>
                </div>

                <div class="formula-box p-4 rounded-2xl text-xs sm:text-sm space-y-2">
                    <span class="text-amber-400 font-bold block">สมการการสูญเสียรอง (Minor Loss):</span>
                    <div class="font-mono text-center text-white text-base my-1">
                        \[h_L = K_L \frac{V^2}{2g}\]
                    </div>
                    <p class="text-slate-400 text-xs">• เกิดจากข้อต่อ ข้องอ วาล์ว ทางแยก และการเปลี่ยนขนาดท่อ (\(K_L\) คือ Loss Coefficient)</p>
                </div>
            </div>

            <!-- Parallel vs Series Pipes -->
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 text-xs sm:text-sm">
                <div class="p-4 rounded-2xl bg-slate-900 border border-slate-700">
                    <strong class="text-emerald-400 block mb-1.5"><i class="fa-solid fa-code-fork"></i> ท่อต่อขนาน (Parallel Pipes):</strong>
                    <ul class="space-y-1 text-slate-300 list-disc list-inside">
                        <li><strong>Head Loss เท่ากันทุกเส้น:</strong> \(h_{f1} = h_{f2} = h_{f3}\)</li>
                        <li><strong>อัตราไหลรวมกัน:</strong> \(Q_{\text{total}} = Q_1 + Q_2 + Q_3\)</li>
                    </ul>
                </div>
                <div class="p-4 rounded-2xl bg-slate-900 border border-slate-700">
                    <strong class="text-purple-400 block mb-1.5"><i class="fa-solid fa-link"></i> ท่อต่ออนุกรม (Series Pipes):</strong>
                    <ul class="space-y-1 text-slate-300 list-disc list-inside">
                        <li><strong>อัตราไหลเท่ากันทุกเส้น:</strong> \(Q_1 = Q_2 = Q_3 = Q_{\text{total}}\)</li>
                        <li><strong>Head Loss รวมกัน:</strong> \(h_{f,\text{total}} = h_{f1} + h_{f2} + h_{f3}\)</li>
                    </ul>
                </div>
            </div>
        </section>

        <!-- บทที่ 8: การไหลผ่านรูลอด -->
        <section id="ch8" class="chapter-card glass-panel rounded-3xl p-6 sm:p-8 border border-slate-700/60 shadow-xl">
            <div class="flex items-center justify-between border-b border-slate-700/60 pb-4 mb-5">
                <div class="flex items-center gap-3">
                    <span class="w-9 h-9 rounded-xl bg-slate-800 text-teal-400 border border-slate-700 flex items-center justify-center font-bold font-heading">8</span>
                    <div>
                        <span class="text-xs font-semibold text-teal-400 uppercase tracking-wider">บทที่ 8 (หน้า 42 - 47)</span>
                        <h2 class="text-xl sm:text-2xl font-bold text-white font-heading">การไหลผ่านรูลอด (Orifice, Jet Velocity & Trajectory)</h2>
                    </div>
                </div>
                <span class="flow-pill bg-teal-500/20 text-teal-300 border border-teal-500/30">Vena Contracta & สัมประสิทธิ์ 3 ตัว</span>
            </div>

            <!-- Vena Contracta Explanation -->
            <div class="bg-slate-900/90 p-4 rounded-2xl border border-slate-700 mb-6 text-xs sm:text-sm text-slate-300 flex items-start gap-3">
                <span class="text-2xl">💧</span>
                <div>
                    <strong class="text-white text-base">ปรากฏการณ์ Vena Contracta คืออะไร?</strong><br>
                    เมื่อน้ำไหลพุ่งออกจากรูลอดขอบคม ลำน้ำจะไม่ขนานทันที แต่จะ <strong>บีบตัวคอดเล็กลงจนถึงจุดที่มีพื้นที่หน้าตัดแคบที่สุด</strong> เรียกว่าจุด <strong>Vena Contracta</strong> (ซึ่งอยู่ห่างจากรูลอดประมาณ \(d_0/2\)) จากนั้นจึงพุ่งโค้งตกลงตามแนวดิ่งแบบการเคลื่อนที่วิถีโค้ง (Projectile)
                </div>
            </div>

            <!-- 3 Coefficients Table -->
            <div class="grid grid-cols-1 sm:grid-cols-3 gap-4 text-xs sm:text-sm">
                <!-- Cv -->
                <div class="bg-slate-900 p-4 rounded-2xl border border-slate-700">
                    <span class="text-teal-400 font-bold block mb-1">1. สัมประสิทธิ์ความเร็ว (\(C_v\))</span>
                    <p class="text-[11px] text-slate-400 mb-2">หาจากวิถีโปรเจกไทล์ \(x = Vt, y = \frac{1}{2}gt^2\)</p>
                    <div class="font-mono text-white text-xs bg-slate-800 p-2.5 rounded-xl text-center">
                        \[C_v = \frac{x}{2\sqrt{yH}}\]
                    </div>
                    <span class="text-[11px] text-slate-400 mt-1 block">\(x\) = ระยะพุ่งแนวนอน, \(y\) = ระยะตกลงแนวดิ่ง</span>
                </div>

                <!-- Cc -->
                <div class="bg-slate-900 p-4 rounded-2xl border border-slate-700">
                    <span class="text-amber-400 font-bold block mb-1">2. สัมประสิทธิ์การหดตัว (\(C_c\))</span>
                    <p class="text-[11px] text-slate-400 mb-2">วัดขนาดลำน้ำที่จุด Vena Contracta</p>
                    <div class="font-mono text-white text-xs bg-slate-800 p-2.5 rounded-xl text-center">
                        \[C_c = \frac{A_c}{A_0} = \left(\frac{d_c}{d_0}\right)^2\]
                    </div>
                    <span class="text-[11px] text-slate-400 mt-1 block">\(d_c\) = ไดมิเตอร์ลำน้ำ, \(d_0\) = ไดมิเตอร์รูลอด</span>
                </div>

                <!-- Cd -->
                <div class="bg-slate-900 p-4 rounded-2xl border border-emerald-500/40">
                    <span class="text-emerald-400 font-bold block mb-1">3. สัมประสิทธิ์การไหล (\(C_d\))</span>
                    <p class="text-[11px] text-slate-400 mb-2">อัตราการไหลจริงเทียบกับทฤษฎี</p>
                    <div class="font-mono text-emerald-400 font-bold text-sm bg-slate-800 p-2.5 rounded-xl text-center">
                        \[C_d = C_v \cdot C_c = \frac{Q_{\text{actual}}}{Q_{\text{theory}}}\]
                    </div>
                    <span class="text-[11px] text-emerald-300 mt-1 block">⭐ สูตรสำคัญ: \(C_d = C_v \times C_c\)</span>
                </div>
            </div>
        </section>
''')

# PART 7: Chapter 9 (The Main Exam Focus)
html_parts.append(r'''
        <!-- บทที่ 9: การทดสอบเครื่องสูบน้ำ (MAIN FOCUS) -->
        <section id="ch9" class="chapter-card glass-panel rounded-3xl p-6 sm:p-8 border-2 border-sky-500/60 shadow-2xl relative overflow-hidden">
            <div class="absolute -top-12 -right-12 w-48 h-48 bg-sky-500/10 rounded-full blur-3xl pointer-events-none"></div>

            <div class="flex items-center justify-between border-b border-slate-700/60 pb-4 mb-5">
                <div class="flex items-center gap-3">
                    <span class="w-9 h-9 rounded-xl bg-sky-500 text-white flex items-center justify-center font-extrabold font-heading text-lg shadow-md shadow-sky-500/30">9</span>
                    <div>
                        <div class="flex items-center gap-2">
                            <span class="text-xs font-bold text-sky-400 uppercase tracking-wider">บทที่ 9 (หน้า 48 - 53)</span>
                            <span class="text-[10px] bg-red-600 text-white font-bold px-2 py-0.5 rounded-full">มีตัวอย่างข้อสอบจริง!</span>
                        </div>
                        <h2 class="text-xl sm:text-2xl font-bold text-white font-heading">การทดสอบคุณสมบัติของเครื่องสูบน้ำ (Pump Test)</h2>
                    </div>
                </div>
                <span class="flow-pill bg-sky-500/20 text-sky-300 border border-sky-500/30">Single vs Series (2H) vs Parallel (2Q)</span>
            </div>

            <!-- Notes from iPad screen -->
            <div class="bg-amber-950/40 border border-amber-500/50 rounded-2xl p-4 sm:p-5 mb-6 text-xs sm:text-sm text-amber-200">
                <strong class="text-amber-300 text-sm block mb-1 flex items-center gap-2">
                    <i class="fa-solid fa-note-sticky text-amber-400"></i> ลายมืออาจารย์หน้า 52 และ 53 (แนวข้อสอบจริง 100%):
                </strong>
                <ul class="space-y-1 list-disc list-inside text-slate-300 text-xs sm:text-sm">
                    <li><strong>ข้อสอบจะเขียนให้รูป 1-3 รูป:</strong> ถามว่า "น้ำเข้าทางไหน? ออกทางไหน? วาล์วไหนเปิด-ปิด?"</li>
                    <li><strong>ต้องปรับหน้า Z:</strong> คำนวณ Datum Head Correction (\(H_d\)) จากความต่างระดับเกจทางออกเทียบกับทางเข้า</li>
                    <li><strong>แล้วหา Power:</strong> เข้าสูตร \(W_i = \gamma Q H\) (\(\gamma = 9,810\text{ N/m}^3\))</li>
                    <li><strong>จุดดักคะแนนข้อสอบ:</strong> <strong>"มล. เป็น ลบ.ม."</strong> อย่าลืมแปลง \(Q\) เป็น \(\text{m}^3/\text{s}\) ก่อนคูณ!</li>
                </ul>
            </div>

            <!-- 3 Pump Setups Summary Cards -->
            <div class="grid grid-cols-1 sm:grid-cols-3 gap-4 mb-6">
                <!-- Single -->
                <div class="bg-slate-900/90 p-4 rounded-2xl border border-sky-500/40 space-y-2">
                    <span class="text-xs font-bold text-sky-400 block">1. ปั๊มเดี่ยว (Single Pump)</span>
                    <ul class="text-xs text-slate-300 space-y-1">
                        <li>• ดูดจาก Sump ผ่านเกจ \(h_1\) (2 cm)</li>
                        <li>• ดันออกผ่านเกจ \(h_o\) (17 cm)</li>
                        <li>• <strong>ค่าแก้ \(H_d\):</strong> \(0.17 - 0.02 = \mathbf{+0.15\text{ m}}\)</li>
                        <li>• Total Head: \(H = h_o - h_1 + 0.15\)</li>
                    </ul>
                </div>

                <!-- Series -->
                <div class="bg-slate-900/90 p-4 rounded-2xl border border-purple-500/40 space-y-2">
                    <span class="text-xs font-bold text-purple-400 block">2. ปั๊มต่ออนุกรม (Series: 2H)</span>
                    <ul class="text-xs text-slate-300 space-y-1">
                        <li>• ปั๊ม 1 ดูดจาก Sump ส่งต่อให้ปั๊ม 2</li>
                        <li>• <strong class="text-red-400">จุดดัก! \(h_1 = 0\)</strong> (เพราะดูดจากถังเปิด)</li>
                        <li>• <strong>ค่าแก้ \(H_d\):</strong> \(0.17 - 0.24 = \mathbf{-0.07\text{ m}}\) (ติดลบ!)</li>
                        <li>• <strong>Total Head เพิ่มเป็น 2 เท่า (\(2H\))!</strong></li>
                    </ul>
                </div>

                <!-- Parallel -->
                <div class="bg-slate-900/90 p-4 rounded-2xl border border-emerald-500/40 space-y-2">
                    <span class="text-xs font-bold text-emerald-400 block">3. ปั๊มต่อขนาน (Parallel: 2Q)</span>
                    <ul class="text-xs text-slate-300 space-y-1">
                        <li>• ปั๊มทั้ง 2 ตัวแยกดูดน้ำพร้อมกัน</li>
                        <li>• ส่งมารวมกันที่ Discharge Manifold (\(h_m\))</li>
                        <li>• <strong>ค่าแก้ \(H_d\):</strong> \(0.96 - 0.02 = \mathbf{+0.94\text{ m}}\)</li>
                        <li>• <strong>อัตราการไหลเพิ่มเป็น 2 เท่า (\(2Q\))!</strong></li>
                    </ul>
                </div>
            </div>

            <!-- Characteristic Curves Interactive Preview Link -->
            <div class="p-4 rounded-2xl bg-slate-900/70 border border-slate-700 flex flex-col sm:flex-row items-center justify-between gap-3 text-xs sm:text-sm">
                <div>
                    <strong class="text-white">📊 ดูรูปกราฟ H-Q ฉบับเต็มตามจอ iPad หน้า 53</strong>
                    <p class="text-slate-400 text-xs">เปรียบเทียบจุดตัด เส้นปั๊มเดี่ยว ปั๊มอนุกรม (\(2H\)) และปั๊มขนาน (\(2Q\))</p>
                </div>
                <a href="#chart-section" class="px-4 py-2 rounded-xl bg-sky-500 hover:bg-sky-400 text-white font-semibold transition-all shadow-md shadow-sky-500/20 whitespace-nowrap">
                    ดูกราฟสมรรถนะ H-Q <i class="fa-solid fa-arrow-down ml-1"></i>
                </a>
            </div>
        </section>
''')

# PART 8: Chapter 10 & Chapter 11
html_parts.append(r'''
        <!-- บทที่ 10: การไหลลอดประตูน้ำ -->
        <section id="ch10" class="chapter-card glass-panel rounded-3xl p-6 sm:p-8 border border-slate-700/60 shadow-xl">
            <div class="flex items-center justify-between border-b border-slate-700/60 pb-4 mb-5">
                <div class="flex items-center gap-3">
                    <span class="w-9 h-9 rounded-xl bg-slate-800 text-blue-400 border border-slate-700 flex items-center justify-center font-bold font-heading">10</span>
                    <div>
                        <span class="text-xs font-semibold text-blue-400 uppercase tracking-wider">บทที่ 10 (หน้า 54 - 57)</span>
                        <h2 class="text-xl sm:text-2xl font-bold text-white font-heading">การไหลลอดประตูน้ำ (Flow under Sluice Gate)</h2>
                    </div>
                </div>
                <span class="flow-pill bg-blue-500/20 text-blue-300 border border-blue-500/30">Specific Energy & Sub/Supercritical</span>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-2 gap-6 text-sm">
                <div class="space-y-3">
                    <h3 class="font-bold text-white text-base">🌊 พฤติกรรมการไหลก่อนและหลังประตูน้ำ</h3>
                    <ul class="text-xs sm:text-sm text-slate-300 space-y-2 list-disc list-inside">
                        <li><strong>ด้านต้นน้ำ (ก่อนประตูน้ำ \(y_0\)):</strong> น้ำมีความลึกมาก ไหลช้า การไหลเป็นแบบ <strong>Subcritical Flow (\(Fr < 1\))</strong></li>
                        <li><strong>ด้านท้ายน้ำ (หลังประตูน้ำ \(y_1\)):</strong> น้ำถูกบีบให้ลอดผ่านใต้บานประตู น้ำจะตื้นและไหลเชี่ยวมาก การไหลเป็นแบบ <strong>Supercritical Flow (\(Fr > 1\))</strong></li>
                        <li><strong>สัมประสิทธิ์การลดขนาดหน้าตัด:</strong> \(C_c = \frac{y_1}{y_g}\) (โดย \(y_g\) คือความสูงของช่องเปิดประตูน้ำ)</li>
                    </ul>
                </div>

                <div class="space-y-3">
                    <div class="formula-box p-4 rounded-2xl text-xs sm:text-sm space-y-2">
                        <span class="text-blue-400 font-bold block">พลังงานจำเพาะ (Specific Energy: \(E\)):</span>
                        <div class="font-mono text-center text-white text-sm my-1">
                            \[E = y + \frac{V^2}{2g} = y + \frac{Q^2}{2g B^2 y^2}\]
                        </div>
                        <p class="text-slate-400 text-xs">• ถ้าไม่มีการสูญเสียพลังงาน พลังงานจำเพาะก่อนและหลังประตูน้ำจะเท่ากัน: \(E_0 = E_1\)</p>
                    </div>
                    <div class="formula-box p-3 rounded-xl text-xs font-mono text-emerald-400 text-center">
                        \[Q_{\text{actual}} = C_d y_g B \sqrt{2g y_0}\]
                    </div>
                </div>
            </div>
        </section>

        <!-- บทที่ 11: รางน้ำแบบเวนจูรี่ -->
        <section id="ch11" class="chapter-card glass-panel rounded-3xl p-6 sm:p-8 border border-slate-700/60 shadow-xl">
            <div class="flex items-center justify-between border-b border-slate-700/60 pb-4 mb-5">
                <div class="flex items-center gap-3">
                    <span class="w-9 h-9 rounded-xl bg-slate-800 text-violet-400 border border-slate-700 flex items-center justify-center font-bold font-heading">11</span>
                    <div>
                        <span class="text-xs font-semibold text-violet-400 uppercase tracking-wider">บทที่ 11 (หน้า 58 - 62)</span>
                        <h2 class="text-xl sm:text-2xl font-bold text-white font-heading">การวัดอัตราการไหลด้วยรางน้ำแบบเวนจูรี่ (Venturi Flume)</h2>
                    </div>
                </div>
                <span class="flow-pill bg-violet-500/20 text-violet-300 border border-violet-500/30">Critical Flow Condition (Fr = 1)</span>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-2 gap-6 text-sm">
                <div class="space-y-3">
                    <h3 class="font-bold text-white text-base">📐 หลักการและข้อดีในงานชลประทาน</h3>
                    <p class="text-xs sm:text-sm text-slate-300 leading-relaxed">
                        รางน้ำแบบเวนจูรี่ใช้วิธีบีบหน้าตัดรางน้ำจากกว้าง \(B\) ให้แคบลงเป็นคอคอด \(b\) เพื่อบังคับให้เกิด <strong>การไหลวิกฤต (Critical Flow, \(Fr = 1\))</strong> ที่บริเวณคอคอด
                    </p>
                    <div class="p-3 bg-slate-900 rounded-xl border border-slate-700 text-xs text-slate-300 space-y-1">
                        <div>• <strong>ความสัมพันธ์ที่คอคอด:</strong> ความลึกวิกฤต \(y_c = \frac{2}{3} H\)</div>
                        <div>• <strong>ข้อดีเหนือฝาย:</strong> สูญเสียพลังงานน้อยกว่า และ <strong>ไม่มีตะกอนตกค้างหน้าคัน</strong> เหมือนการสร้างฝายขวางลำน้ำ เหมาะกับคลองชลประทานจริง</div>
                    </div>
                </div>

                <div class="space-y-3">
                    <div class="formula-box p-4 rounded-2xl text-xs sm:text-sm space-y-2">
                        <span class="text-violet-400 font-bold block">สูตรอัตราการไหลทฤษฎี (Free Flow Condition):</span>
                        <div class="font-mono text-center text-violet-300 text-sm my-1">
                            \[Q_{\text{theory}} = \left(\frac{2}{3}\right)^{1.5} \sqrt{g} \cdot b \cdot y_1^{1.5}\]
                        </div>
                        <p class="text-slate-400 text-xs">• \(b\) = ความกว้างคอคอด, \(y_1\) = ความลึกน้ำด้านต้นน้ำ</p>
                    </div>
                    <div class="formula-box p-3 rounded-xl text-xs font-mono text-center text-slate-300">
                        \[Q_{\text{actual}} = C_d Q_{\text{theory}}\]
                    </div>
                </div>
            </div>
        </section>

    </main>
''')

# PART 9: Master Table & Interactive Tools
html_parts.append(r'''
    <!-- MASTER CHEATSHEET TABLE (ALL 10 CHAPTERS) -->
    <section id="master-table" class="max-w-6xl mx-auto px-4 py-8 page-break">
        <div class="glass-panel rounded-3xl p-6 sm:p-8 border border-slate-700/60 shadow-2xl">
            <div class="flex items-center justify-between pb-4 mb-6 border-b border-slate-700">
                <div>
                    <h2 class="text-xl sm:text-2xl font-bold text-white font-heading flex items-center gap-2">
                        <i class="fa-solid fa-table-list text-sky-400"></i> สรุปสูตรและจุดดักคะแนนของทุกบท (Master Cheatsheet)
                    </h2>
                    <p class="text-xs sm:text-sm text-slate-400">รวมตารางสรุปสมการหลัก หน่วย และจุดที่ต้องระวังในห้องสอบ ครบทุกบทในหน้าเดียว</p>
                </div>
            </div>

            <div class="overflow-x-auto">
                <table class="w-full text-xs text-left border-collapse bg-slate-900/90 rounded-2xl overflow-hidden border border-slate-800">
                    <thead>
                        <tr class="bg-slate-800 text-slate-200 border-b border-slate-700 font-heading">
                            <th class="p-3">บทที่</th>
                            <th class="p-3">ชื่อการทดลอง</th>
                            <th class="p-3">สมการหลัก (Governing Formula)</th>
                            <th class="p-3">ตัวแปรสำคัญ</th>
                            <th class="p-3">จุดดักคะแนนในข้อสอบ (Trap)</th>
                        </tr>
                    </thead>
                    <tbody class="divide-y divide-slate-800 text-slate-300">
                        <tr>
                            <td class="p-3 font-bold text-sky-400">1</td>
                            <td class="p-3 font-semibold text-white">Hydraulic Bench</td>
                            <td class="p-3 font-mono text-emerald-400">\(Q = \Delta V / \Delta t\)</td>
                            <td class="p-3">\(V\) (ลิตร), \(t\) (วินาที)</td>
                            <td class="p-3 text-red-300">ต้องแปลง ลิตร หรือ มล. เป็น \(\text{m}^3\) เสมอ</td>
                        </tr>
                        <tr>
                            <td class="p-3 font-bold text-sky-400">2</td>
                            <td class="p-3 font-semibold text-white">Center of Pressure</td>
                            <td class="p-3 font-mono text-emerald-400">\(F = \frac{1}{2}\rho g B d^2\) (จมบางส่วน)<br>\(y_{cp} = \frac{2}{3}d\)</td>
                            <td class="p-3">\(h'' = mgL/F\)<br>\(y_{cp} = h'' - (H - d)\)</td>
                            <td class="p-3 text-red-300">แรงที่ผิวโค้งไม่เกิดโมเมนต์เพราะพุ่งผ่านจุดหมุน!</td>
                        </tr>
                        <tr>
                            <td class="p-3 font-bold text-sky-400">3</td>
                            <td class="p-3 font-semibold text-white">Impact of Jet</td>
                            <td class="p-3 font-mono text-emerald-400">\(F = \rho Q V (\cos\theta + 1)\)<br>ฉากถ้วยโค้ง: \(F = 2\rho Q V\)</td>
                            <td class="p-3">\(F = mg\) (สมดุลตุ้มน้ำหนัก)</td>
                            <td class="p-3 text-red-300">ฉากครึ่งทรงกลมแรงเป็น <strong>2 เท่า</strong> ของฉากแบน!</td>
                        </tr>
                        <tr>
                            <td class="p-3 font-bold text-sky-400">4</td>
                            <td class="p-3 font-semibold text-white">Bernoulli & Venturi</td>
                            <td class="p-3 font-mono text-emerald-400">\(P_1/\gamma + V_1^2/2g = P_2/\gamma + V_2^2/2g\)<br>\(C_d = Q_{\text{act}} / Q_{\text{the}}\)</td>
                            <td class="p-3">\(h_1 - h_2\) (ผลต่างระดับน้ำมาโนมิเตอร์)</td>
                            <td class="p-3 text-red-300">ที่คอคอด Throat: ความเร็วสูงสุด \(\to\) ความดันต่ำสุด</td>
                        </tr>
                        <tr>
                            <td class="p-3 font-bold text-sky-400">5</td>
                            <td class="p-3 font-semibold text-white">Manning Equation</td>
                            <td class="p-3 font-mono text-emerald-400">\(V = \frac{1}{n} R^{2/3} S^{1/2}\)</td>
                            <td class="p-3">\(R = A/P\), \(S = \tan\theta\)</td>
                            <td class="p-3 text-red-300">ความชัน \(S = \tan\theta\) อย่าลืมกด \(\tan\)</td>
                        </tr>
                        <tr>
                            <td class="p-3 font-bold text-sky-400">6</td>
                            <td class="p-3 font-semibold text-white">Flow over Weir</td>
                            <td class="p-3 font-mono text-emerald-400">ฝายสี่เหลี่ยม: \(Q \propto H^{1.5}\)<br>ฝายสามเหลี่ยม: \(Q \propto H^{2.5}\)</td>
                            <td class="p-3">\(H\) (ความสูงน้ำเหนือสันฝาย)</td>
                            <td class="p-3 text-red-300">ฝายสามเหลี่ยมวัดอัตราไหลต่ำได้แม่นยำกว่า</td>
                        </tr>
                        <tr>
                            <td class="p-3 font-bold text-sky-400">7</td>
                            <td class="p-3 font-semibold text-white">Pipe Network Losses</td>
                            <td class="p-3 font-mono text-emerald-400">\(h_f = f \frac{L}{D} \frac{V^2}{2g} \propto \frac{Q^2}{D^5}\)</td>
                            <td class="p-3">ท่อขนาน: \(h_L\) เท่ากัน<br>ท่ออนุกรม: \(Q\) เท่ากัน</td>
                            <td class="p-3 text-red-300">ท่อเล็กลงครึ่งหนึ่ง การสูญเสียพุ่งขึ้น \(2^5 = 32\) เท่า</td>
                        </tr>
                        <tr>
                            <td class="p-3 font-bold text-sky-400">8</td>
                            <td class="p-3 font-semibold text-white">Flow through Orifice</td>
                            <td class="p-3 font-mono text-emerald-400">\(V = \sqrt{2gH}\)<br>\(C_d = C_v \cdot C_c\)</td>
                            <td class="p-3">\(C_v = \frac{x}{2\sqrt{yH}}\)<br>\(C_c = (d_c/d_0)^2\)</td>
                            <td class="p-3 text-red-300">Vena Contracta คือจุดที่ลำน้ำคอดแคบที่สุด</td>
                        </tr>
                        <tr class="bg-sky-950/30">
                            <td class="p-3 font-bold text-sky-400">9</td>
                            <td class="p-3 font-semibold text-white">Pump Test (ออกสอบ!)</td>
                            <td class="p-3 font-mono text-sky-300">\(H = h_o - h_1 + H_d\)<br>\(W_i = \gamma Q H\)</td>
                            <td class="p-3">\(H_d\): เดี่ยว +0.15 m<br>อนุกรม -0.07 m, ขนาน +0.94 m</td>
                            <td class="p-3 text-red-300">อนุกรม \(h_1 = 0\) และได้ \(2H\), ขนานได้ \(2Q\)</td>
                        </tr>
                        <tr>
                            <td class="p-3 font-bold text-sky-400">10</td>
                            <td class="p-3 font-semibold text-white">Sluice Gate</td>
                            <td class="p-3 font-mono text-emerald-400">\(E = y + \frac{V^2}{2g}\)<br>\(Q = C_d y_g B \sqrt{2gy_0}\)</td>
                            <td class="p-3">\(y_0\) (Subcritical)<br>\(y_1\) (Supercritical)</td>
                            <td class="p-3 text-red-300">ก่อนประตูน้ำน้ำลึกไหลช้า หลังประตูน้ำน้ำตื้นไหลเชี่ยว</td>
                        </tr>
                        <tr>
                            <td class="p-3 font-bold text-sky-400">11</td>
                            <td class="p-3 font-semibold text-white">Venturi Flume</td>
                            <td class="p-3 font-mono text-emerald-400">\(Q_{\text{the}} = (2/3)^{1.5} \sqrt{g} b y_1^{1.5}\)</td>
                            <td class="p-3">\(y_c = \frac{2}{3}H\) (Critical Depth)</td>
                            <td class="p-3 text-red-300">ไม่ตกตะกอนสะสมหน้าคันเหมือนฝาย</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
    </section>

    <!-- UNIVERSAL LAB CALCULATOR -->
    <section id="universal-calc" class="max-w-6xl mx-auto px-4 py-8 no-print">
        <div class="glass-panel rounded-3xl p-6 sm:p-8 border border-emerald-500/30 shadow-xl">
            <div class="flex items-center gap-3 mb-6">
                <span class="w-9 h-9 rounded-xl bg-emerald-500/20 text-emerald-400 border border-emerald-500/30 flex items-center justify-center font-bold font-heading">
                    <i class="fa-solid fa-calculator"></i>
                </span>
                <div>
                    <h2 class="text-xl sm:text-2xl font-bold text-white font-heading">เครื่องคิดเลขจำลองสูตรชลศาสตร์ (Universal Lab Calculator)</h2>
                    <p class="text-xs sm:text-sm text-slate-400">เลือกบทที่ต้องการ แล้วกรอกตัวเลขเพื่อตรวจสอบวิธีคิดและหน่วยทันที</p>
                </div>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-12 gap-6">
                <div class="md:col-span-5 bg-slate-900 p-5 rounded-2xl border border-slate-700 space-y-4 text-xs sm:text-sm">
                    <div>
                        <label class="block text-slate-300 font-semibold mb-1">เลือกสูตรการทดลอง:</label>
                        <select id="uni-calc-mode" onchange="updateCalcFields()" class="w-full bg-slate-800 border border-slate-700 rounded-xl p-2.5 text-white font-medium focus:outline-none focus:border-emerald-500">
                            <option value="pump">บทที่ 9: ปั๊มน้ำ (Pump Power & Total Head)</option>
                            <option value="jet">บทที่ 3: แรงกระแทกลำน้ำ (Impact of Jet: Flat vs Cup)</option>
                            <option value="weir_tri">บทที่ 6: ฝายสามเหลี่ยม V-Notch (90 Degree)</option>
                            <option value="weir_rec">บทที่ 6: ฝายสี่เหลี่ยม (Rectangular Weir)</option>
                            <option value="orifice">บทที่ 8: รูลอด (Torricelli Velocity & Cv)</option>
                        </select>
                    </div>

                    <div id="dynamic-inputs" class="space-y-3">
                        <!-- Populated by JS -->
                    </div>
                </div>

                <div class="md:col-span-7 bg-slate-900 p-5 rounded-2xl border border-slate-700 flex flex-col justify-between text-xs sm:text-sm">
                    <div>
                        <span class="text-xs font-semibold text-emerald-400 uppercase tracking-wide">ขั้นตอนการคำนวณและแปลงหน่วยแบบละเอียด:</span>
                        <div id="dynamic-calc-steps" class="mt-3 space-y-2 text-slate-300 font-mono text-xs">
                            <!-- Populated by JS -->
                        </div>
                    </div>
                    <div class="mt-4 pt-3 border-t border-slate-800 flex items-center justify-between text-sm">
                        <span class="text-slate-400">ผลลัพธ์สุดท้าย:</span>
                        <span id="dynamic-calc-result" class="text-xl font-extrabold text-emerald-400 font-mono">-</span>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- MOCK EXAM QUIZ (12 ALL-CHAPTER QUESTIONS) -->
    <section id="quiz-master" class="max-w-6xl mx-auto px-4 py-8 page-break">
        <div class="glass-panel rounded-3xl p-6 sm:p-8 border border-indigo-500/40 shadow-2xl">
            <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-4 mb-6 pb-4 border-b border-slate-700">
                <div class="flex items-center gap-3">
                    <span class="w-9 h-9 rounded-xl bg-indigo-500/20 text-indigo-400 border border-indigo-500/30 flex items-center justify-center font-bold font-heading">
                        <i class="fa-solid fa-graduation-cap"></i>
                    </span>
                    <div>
                        <h2 class="text-xl sm:text-2xl font-bold text-white font-heading">แบบฝึกหัดข้อสอบปรนัยจำลอง 12 ข้อ (All-Chapters Mock Exam)</h2>
                        <p class="text-xs sm:text-sm text-slate-400">จำลองข้อสอบแล็ปจริง ครบทุกบท มีเฉลยและชี้จุดหลอกทุกข้อ</p>
                    </div>
                </div>
                <div class="flex items-center gap-3">
                    <button onclick="resetQuiz()" class="px-3 py-1.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 text-xs font-semibold border border-slate-700">
                        <i class="fa-solid fa-rotate-right mr-1"></i> ทำใหม่
                    </button>
                    <div class="px-4 py-1.5 rounded-full bg-slate-800 text-sky-400 border border-slate-700 text-xs font-bold">
                        คะแนน: <span id="quiz-score-val">0</span> / 12 ข้อ
                    </div>
                </div>
            </div>

            <!-- Quiz Items List -->
            <div id="master-quiz-container" class="space-y-6">
                <!-- Dynamically rendered via JS for 12 complete questions -->
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer class="max-w-6xl mx-auto px-4 py-12 text-center text-xs text-slate-500 border-t border-slate-800 mt-12 no-print">
        <p class="font-bold text-slate-400 text-sm">CE272 Fluid Mechanics Laboratory Master Exam Portal</p>
        <p class="mt-1">ภาควิชาวิศวกรรมโยธา คณะวิศวกรรมศาสตร์ มหาวิทยาลัยธรรมศาสตร์</p>
        <p class="mt-2 text-slate-600">จัดทำขึ้นเพื่อการทบทวนเตรียมสอบปฏิบัติการ ครอบคลุมทั้ง 11 บทอย่างสมบูรณ์แบบ 100%</p>
    </footer>

    <!-- JS LOGIC SCRIPT -->
    <script>
        // 12 Comprehensive All-Chapters Questions
        const masterQuizData = [
            {
                id: 1,
                chapter: "บทที่ 9: ปั๊มน้ำ",
                q: "ในการต่อเครื่องสูบน้ำแบบอนุกรม (Two Pumps in Series) ความดันด้านดูดของปั๊มตัวแรก (h₁) กำหนดให้มีค่าเท่าใดตามคู่มือปฏิบัติการ?",
                choices: [
                    "h₁ = 1.0 m เพราะต้องมีแรงดันบวกเสมอ",
                    "h₁ = 0 m เพราะดูดตรงจาก Sump Tank ซึ่งเปิดสัมผัสบรรยากาศ",
                    "h₁ = -2.0 m เพราะเป็นแรงดูดสุญญากาศ",
                    "h₁ = 0.24 m เท่ากับระดับความสูงของ Bench inlet"
                ],
                correct: 1,
                expl: "ตามคู่มือปฏิบัติการหน้า 51 ข้อ 6 ระบุชัดเจนว่า ความดันขาเข้าของปั๊มตัวแรกให้ถือเป็นศูนย์ (h₁ = 0) เนื่องจากดูดน้ำจาก Sump Tank ที่ผิวหน้าสัมผัสความดันบรรยากาศโดยตรง"
            },
            {
                id: 2,
                chapter: "บทที่ 9: ปั๊มน้ำ",
                q: "เครื่องสูบน้ำสองตัวต่ออนุกรมกัน (Series) และต่อขนานกัน (Parallel) มีผลต่อ Total Head (H) และ Discharge (Q) อย่างไรเมื่อเทียบกับปั๊มเดี่ยว?",
                choices: [
                    "อนุกรมได้ 2Q, ขนานได้ 2H",
                    "อนุกรมได้ 2H, ขนานได้ 2Q",
                    "ทั้งสองแบบได้ 2H และ 2Q เหมือนกัน",
                    "อนุกรมและขนานไม่มีผลต่อ H หรือ Q"
                ],
                correct: 1,
                expl: "การต่อแบบอนุกรม (Series) ช่วยเพิ่มพลังงานความดันเป็น 2 เท่า (2H) แต่อัตราไหลเท่าเดิม ส่วนการต่อแบบขนาน (Parallel) ช่วยเพิ่มอัตราการไหลเป็น 2 เท่า (2Q) แต่ Head สูงสุดเท่าเดิม"
            },
            {
                id: 3,
                chapter: "บทที่ 9: ค่าปรับหน้า Z",
                q: "ในการทดสอบเครื่องสูบน้ำแบบต่ออนุกรม (Series) กำหนดระยะ hd(outlet) = 0.17 m และระยะ hd(inlet, bench) = 0.24 m ค่าปรับแก้ระดับ Hd มีค่าเท่าใด?",
                choices: [
                    "+0.41 m",
                    "+0.07 m",
                    "-0.07 m",
                    "+0.15 m"
                ],
                correct: 2,
                expl: "Hd = hd(outlet) - hd(inlet) = 0.17 - 0.24 = -0.07 m (มีค่าติดลบ! เป็นจุดดักคะแนนที่นักศึกษามักเผลอคิดเป็นบวก)"
            },
            {
                id: 4,
                chapter: "บทที่ 3: แรงกระแทกลำน้ำ",
                q: "เมื่อปล่อยลำน้ำอัตราการไหล Q ความเร็ว V พุ่งชน 'ฉากรูปครึ่งทรงกลม' (Hemispherical Cup) แรงที่กระทำต่อฉากมีค่าเท่าใดเมื่อเทียบกับ 'ฉากแบนราบ' (Flat Plate)?",
                choices: [
                    "เท่ากัน คือ F = ρQV",
                    "ฉากครึ่งทรงกลมมีแรงเป็น 2 เท่าของฉากแบนราบ (F = 2ρQV)",
                    "ฉากครึ่งทรงกลมมีแรงเป็นครึ่งหนึ่งของฉากแบนราบ",
                    "ฉากครึ่งทรงกลมไม่มีแรงกระทำเลย"
                ],
                correct: 1,
                expl: "ฉากครึ่งทรงกลมทำให้น้ำสะท้อนย้อนกลับ 180 องศา ผลต่างความเร็วคือ (V - (-V)) = 2V ทำให้เกิดแรงโมเมนตัม F = 2ρQV หรือคิดเป็น 2 เท่าของฉากแบนราบเสมอ!"
            },
            {
                id: 5,
                chapter: "บทที่ 2: จุดศูนย์กลางแรงดัน",
                q: "ในชุดทดลองจุดศูนย์กลางแรงดัน (ทุ่นเสี้ยววงกลม Quadrant) เหตุใดแรงดันน้ำที่กระทำต่อ 'ผิวด้านโค้ง' จึงไม่ทำให้เกิดโมเมนต์รอบจุดหมุน?",
                choices: [
                    "เพราะผิวด้านโค้งไม่มีแรงดันน้ำกระทำ",
                    "เพราะแนวแรงดันของผิวด้านโค้งทุกจุดมีทิศทางพุ่งผ่านจุดหมุน (Pivot) ทำให้แขนของแรงเป็นศูนย์",
                    "เพราะน้ำหนักของทุ่นหักล้างกับแรงดันผิวด้านโค้งพอดี",
                    "เพราะผิวด้านโค้งทำจากวัสดุไร้แรงเสียดทาน"
                ],
                correct: 1,
                expl: "แรงดันน้ำที่กระทำต่อผิวโค้งทรงกระบอกจะมีทิศตั้งฉากกับผิวโค้ง ซึ่งทุกเส้นแนวแรงจะพุ่งผ่านจุดศูนย์กลางความโค้ง ซึ่งเป็นจุดหมุน (Pivot) พอดี แขนของแรงจึงเป็นศูนย์ โมเมนต์จึงไม่เกิดขึ้น!"
            },
            {
                id: 6,
                chapter: "บทที่ 4: เบอร์นูลลี่",
                q: "ในการไหลผ่านท่อเวนจูรี่ (Venturi Tube) ที่บริเวณ 'คอคอด' (Throat) ความเร็วและความดันของน้ำจะเป็นอย่างไรเมื่อเทียบกับท่อทางเข้า?",
                choices: [
                    "ความเร็วลดลง และความดันเพิ่มขึ้นสูงสุด",
                    "ความเร็วเพิ่มขึ้นสูงสุด และความดันลดลงต่ำสุด",
                    "ความเร็วเท่าเดิม แต่ความดันเพิ่มขึ้น",
                    "ความเร็วและความดันลดลงพร้อมกันทั้งคู่"
                ],
                correct: 1,
                expl: "ตามสมการความต่อเนื่อง (A1 V1 = A2 V2) เมื่อหน้าตัดแคบลง ความเร็วจะพุ่งสูงขึ้น และตามสมการเบอร์นูลลี่ พลังงานความเร็วที่สูงขึ้นจะดึงให้พลังงานความดันสถิต (P/γ) ลดลงต่ำที่สุด"
            },
            {
                id: 7,
                chapter: "บทที่ 5: แมนนิ่ง",
                q: "สมการแมนนิ่ง V = (1/n) R^(2/3) S^(1/2) ถ้าเปรียบเทียบคลองพื้นเรียบกับคลองพื้นหญ้าที่อัตราไหลเท่ากัน คลองพื้นหญ้าจะมีพฤติกรรมอย่างไร?",
                choices: [
                    "มีค่า n น้อยกว่า ทำให้น้ำไหลเร็วกว่า",
                    "มีค่า n มากกว่า ทำให้น้ำไหลช้ากว่าและระดับน้ำจะเอ่อสูงขึ้น",
                    "มีค่า n เท่ากันเสมอ",
                    "ความลึกของน้ำจะตื้นกว่าคลองพื้นเรียบ"
                ],
                correct: 1,
                expl: "พื้นหญ้ามีความขรุขระสูง ค่า n ของแมนนิ่งจึงมากกว่า ทำให้ความเร็วการไหล V ลดลง เมื่ออัตราไหล Q เท่าเดิม หน้าตัดน้ำจึงต้องขยายใหญ่ขึ้น ระดับน้ำจึงเอ่อสูงขึ้น"
            },
            {
                id: 8,
                chapter: "บทที่ 6: ฝายน้ำล้น",
                q: "อัตราการไหลของน้ำข้าม 'ฝายรูปสี่เหลี่ยม' และ 'ฝายรูปสามเหลี่ยม' แปรผันตามความสูงของน้ำเหนือสันฝาย (H) ยกกำลังเท่าใดตามลำดับ?",
                choices: [
                    "สี่เหลี่ยม H^1.0, สามเหลี่ยม H^2.0",
                    "สี่เหลี่ยม H^(3/2), สามเหลี่ยม H^(5/2)",
                    "สี่เหลี่ยม H^(5/2), สามเหลี่ยม H^(3/2)",
                    "ทั้งสองฝายแปรผันตาม H^(1/2)"
                ],
                correct: 1,
                expl: "ฝายสี่เหลี่ยม Q แปรผันตาม H^(3/2) (หรือ H^1.5) ส่วนฝายสามเหลี่ยม Q แปรผันตาม H^(5/2) (หรือ H^2.5) จำเลขชี้กำลัง 3/2 กับ 5/2 ให้แม่น!"
            },
            {
                id: 9,
                chapter: "บทที่ 7: ท่อส่งน้ำ",
                q: "ตามสมการ Darcy-Weisbach การสูญเสียพลังงานหลักจากแรงเสียดทาน (hf) แปรผันตามตัวแปรใด?",
                choices: [
                    "แปรผันตาม Q และแปรผกผันกับ D",
                    "แปรผันตาม Q² และแปรผกผันกับ D⁵",
                    "แปรผันตาม D⁵ และแปรผกผันกับ Q²",
                    "แปรผันตาม V เท่านั้น ไม่เกี่ยวกับขนาดท่อ"
                ],
                correct: 1,
                expl: "hf = f (L/D) (V²/2g) = f L 8Q² / (π² g D⁵) ดังนั้น hf จึงแปรผันตรงกับ Q² และแปรผกผันอย่างรุนแรงกับ D⁵"
            },
            {
                id: 10,
                chapter: "บทที่ 8: รูลอด Orifice",
                q: "ความสัมพันธ์ระหว่างสัมประสิทธิ์การไหล (Cd), สัมประสิทธิ์ความเร็ว (Cv) และสัมประสิทธิ์การหดตัว (Cc) คือข้อใด?",
                choices: [
                    "Cd = Cv + Cc",
                    "Cd = Cv × Cc",
                    "Cd = Cv / Cc",
                    "Cd = (Cv × Cc)²"
                ],
                correct: 1,
                expl: "สัมประสิทธิ์การไหลจริงคือผลคูณของสัมประสิทธิ์ความเร็วและสัมประสิทธิ์การลดขนาดหน้าตัด: Cd = Cv × Cc เสมอ!"
            },
            {
                id: 11,
                chapter: "บทที่ 10: ประตูน้ำ",
                q: "การไหลของน้ำที่ลอดผ่านใต้บานประตูน้ำ (Sluice Gate) ด้านท้ายน้ำ (Downstream) จะมีสภาพการไหลแบบใด?",
                choices: [
                    "Subcritical Flow (Fr < 1)",
                    "Supercritical Flow (Fr > 1)",
                    "Critical Flow (Fr = 1) เสมอ",
                    "ไม่สามารถระบุได้"
                ],
                correct: 1,
                expl: "ด้านหลังประตูน้ำ น้ำจะตื้นและมีความเร็วพุ่งสูงมาก ทำให้ Froude number มากกว่า 1 (Fr > 1) จึงเป็นการไหลแบบ Supercritical Flow"
            },
            {
                id: 12,
                chapter: "บทที่ 11: เวนจูรี่ฟลูม",
                q: "ข้อดีสำคัญของรางน้ำแบบเวนจูรี่ (Venturi Flume) เมื่อเทียบกับการใช้ฝาย (Weir) ในการวัดน้ำในคลองส่งน้ำชลประทานคืออะไร?",
                choices: [
                    "สร้างง่ายและราคาถูกกว่าฝายมาก",
                    "มีการสูญเสียพลังงานน้อยกว่า และไม่ทำให้เกิดตะกอนสะสมตกค้างเหมือนหน้าฝาย",
                    "สามารถวัดน้ำได้เฉพาะคลองทึบแสงเท่านั้น",
                    "ไม่ต้องวัดความลึกน้ำก็ทราบค่าอัตราไหลได้"
                ],
                correct: 1,
                expl: "เวนจูรี่ฟลูมไม่มีแผ่นสันฝายขวางลำน้ำ จึงไม่กักตะกอนดินทราย ทำให้ตะกอนไหลผ่านไปได้สะดวก และมีการสูญเสียพลังงาน (Head loss) ต่ำกว่าฝายมาก"
            }
        ];

        let quizScore = 0;
        let answeredQuestions = new Set();

        function renderMasterQuiz() {
            const container = document.getElementById('master-quiz-container');
            container.innerHTML = masterQuizData.map((item, idx) => `
                <div class="bg-slate-900/90 p-5 sm:p-6 rounded-2xl border border-slate-700/80 space-y-3" id="quiz-card-${item.id}">
                    <div class="flex items-center justify-between">
                        <span class="text-xs font-bold text-sky-400 uppercase tracking-wide">
                            ข้อที่ ${idx + 1} • <span class="text-slate-400">${item.chapter}</span>
                        </span>
                        <span class="text-xs px-2 py-0.5 rounded bg-slate-800 text-slate-400">1 คะแนน</span>
                    </div>
                    <p class="text-sm sm:text-base font-semibold text-white">
                        ${item.q}
                    </p>
                    <div class="space-y-2 text-xs sm:text-sm">
                        ${item.choices.map((choice, cIdx) => `
                            <label onclick="submitAnswer(${item.id}, ${cIdx})" class="flex items-start gap-3 p-3 rounded-xl bg-slate-800/80 hover:bg-slate-700/60 cursor-pointer border border-slate-700/80 transition-all">
                                <span class="font-bold text-slate-400">${['ก', 'ข', 'ค', 'ง'][cIdx]}.</span>
                                <span class="text-slate-200">${choice}</span>
                            </label>
                        `).join('')}
                    </div>
                    <div id="expl-${item.id}" class="hidden text-xs p-3.5 rounded-xl mt-2"></div>
                </div>
            `).join('');
        }

        function submitAnswer(qId, choiceIdx) {
            if (answeredQuestions.has(qId)) return;
            answeredQuestions.add(qId);

            const q = masterQuizData.find(x => x.id === qId);
            const expl = document.getElementById(`expl-${qId}`);
            expl.classList.remove('hidden');

            if (choiceIdx === q.correct) {
                quizScore++;
                document.getElementById('quiz-score-val').innerText = quizScore;
                expl.className = 'text-xs p-3.5 rounded-xl mt-2 bg-emerald-950/70 border border-emerald-500/50 text-emerald-200';
                expl.innerHTML = `<strong>✓ ถูกต้อง!</strong> ${q.expl}`;
            } else {
                expl.className = 'text-xs p-3.5 rounded-xl mt-2 bg-red-950/70 border border-red-500/50 text-red-200';
                const correctChar = ['ก', 'ข', 'ค', 'ง'][q.correct];
                expl.innerHTML = `<strong>✗ ยังไม่ถูกต้อง!</strong> คำตอบที่ถูกคือข้อ <strong>${correctChar}</strong><br>${q.expl}`;
            }
        }

        function resetQuiz() {
            quizScore = 0;
            answeredQuestions.clear();
            document.getElementById('quiz-score-val').innerText = '0';
            renderMasterQuiz();
        }

        // Search Filter
        function filterContent() {
            const query = document.getElementById('quick-search').value.toLowerCase();
            document.querySelectorAll('.chapter-card').forEach(card => {
                const text = card.innerText.toLowerCase();
                if (text.includes(query)) {
                    card.classList.remove('hidden');
                } else {
                    card.classList.add('hidden');
                }
            });
        }

        // Dynamic Calculator Setup
        function updateCalcFields() {
            const mode = document.getElementById('uni-calc-mode').value;
            const container = document.getElementById('dynamic-inputs');
            
            if (mode === 'pump') {
                container.innerHTML = `
                    <div>
                        <label class="block text-slate-300 font-semibold mb-1">เลือกประเภทปั๊ม:</label>
                        <select id="p-cfg" oninput="execUniversalCalc()" class="w-full bg-slate-800 border border-slate-700 rounded-xl p-2 text-white">
                            <option value="single">ปั๊มเดี่ยว (Hd = +0.15 m)</option>
                            <option value="series">ปั๊มอนุกรม (Hd = -0.07 m, h1 = 0)</option>
                            <option value="parallel">ปั๊มขนาน (Hd = +0.94 m)</option>
                        </select>
                    </div>
                    <div class="grid grid-cols-2 gap-2">
                        <div>
                            <label class="block text-slate-300 font-semibold mb-1">ปริมาตร (L):</label>
                            <input type="number" id="p-vol" value="1.0" step="0.5" oninput="execUniversalCalc()" class="w-full bg-slate-800 border border-slate-700 rounded-xl p-2 text-white">
                        </div>
                        <div>
                            <label class="block text-slate-300 font-semibold mb-1">เวลา (วินาที):</label>
                            <input type="number" id="p-t" value="17.71" step="0.1" oninput="execUniversalCalc()" class="w-full bg-slate-800 border border-slate-700 rounded-xl p-2 text-white">
                        </div>
                    </div>
                    <div class="grid grid-cols-2 gap-2">
                        <div>
                            <label class="block text-slate-300 font-semibold mb-1">h1 (m):</label>
                            <input type="number" id="p-h1" value="1.0" step="0.5" oninput="execUniversalCalc()" class="w-full bg-slate-800 border border-slate-700 rounded-xl p-2 text-white">
                        </div>
                        <div>
                            <label class="block text-slate-300 font-semibold mb-1">ho (m):</label>
                            <input type="number" id="p-ho" value="19.0" step="1.0" oninput="execUniversalCalc()" class="w-full bg-slate-800 border border-slate-700 rounded-xl p-2 text-white">
                        </div>
                    </div>
                `;
            } else if (mode === 'jet') {
                container.innerHTML = `
                    <div>
                        <label class="block text-slate-300 font-semibold mb-1">ชนิดของฉากกั้น:</label>
                        <select id="j-type" oninput="execUniversalCalc()" class="w-full bg-slate-800 border border-slate-700 rounded-xl p-2 text-white">
                            <option value="flat">ฉากแบนราบ (F = ρQV)</option>
                            <option value="cup">ฉากครึ่งทรงกลม (F = 2ρQV)</option>
                        </select>
                    </div>
                    <div class="grid grid-cols-2 gap-2">
                        <div>
                            <label class="block text-slate-300 font-semibold mb-1">อัตราการไหล Q (L/s):</label>
                            <input type="number" id="j-q" value="0.5" step="0.1" oninput="execUniversalCalc()" class="w-full bg-slate-800 border border-slate-700 rounded-xl p-2 text-white">
                        </div>
                        <div>
                            <label class="block text-slate-300 font-semibold mb-1">ความเร็วลำน้ำ V (m/s):</label>
                            <input type="number" id="j-v" value="5.0" step="0.5" oninput="execUniversalCalc()" class="w-full bg-slate-800 border border-slate-700 rounded-xl p-2 text-white">
                        </div>
                    </div>
                `;
            } else if (mode === 'weir_tri') {
                container.innerHTML = `
                    <div class="grid grid-cols-2 gap-2">
                        <div>
                            <label class="block text-slate-300 font-semibold mb-1">ระดับน้ำ H (cm):</label>
                            <input type="number" id="w-h" value="10.0" step="1.0" oninput="execUniversalCalc()" class="w-full bg-slate-800 border border-slate-700 rounded-xl p-2 text-white">
                        </div>
                        <div>
                            <label class="block text-slate-300 font-semibold mb-1">สัมประสิทธิ์ Cd:</label>
                            <input type="number" id="w-cd" value="0.60" step="0.01" oninput="execUniversalCalc()" class="w-full bg-slate-800 border border-slate-700 rounded-xl p-2 text-white">
                        </div>
                    </div>
                `;
            } else if (mode === 'weir_rec') {
                container.innerHTML = `
                    <div class="grid grid-cols-2 gap-2">
                        <div>
                            <label class="block text-slate-300 font-semibold mb-1">ความกว้าง B (m):</label>
                            <input type="number" id="wr-b" value="0.30" step="0.05" oninput="execUniversalCalc()" class="w-full bg-slate-800 border border-slate-700 rounded-xl p-2 text-white">
                        </div>
                        <div>
                            <label class="block text-slate-300 font-semibold mb-1">ระดับน้ำ H (cm):</label>
                            <input type="number" id="wr-h" value="8.0" step="1.0" oninput="execUniversalCalc()" class="w-full bg-slate-800 border border-slate-700 rounded-xl p-2 text-white">
                        </div>
                    </div>
                    <div>
                        <label class="block text-slate-300 font-semibold mb-1">สัมประสิทธิ์ Cd:</label>
                        <input type="number" id="wr-cd" value="0.62" step="0.01" oninput="execUniversalCalc()" class="w-full bg-slate-800 border border-slate-700 rounded-xl p-2 text-white">
                    </div>
                `;
            } else if (mode === 'orifice') {
                container.innerHTML = `
                    <div class="grid grid-cols-2 gap-2">
                        <div>
                            <label class="block text-slate-300 font-semibold mb-1">ระดับน้ำ H (m):</label>
                            <input type="number" id="or-h" value="0.40" step="0.05" oninput="execUniversalCalc()" class="w-full bg-slate-800 border border-slate-700 rounded-xl p-2 text-white">
                        </div>
                        <div>
                            <label class="block text-slate-300 font-semibold mb-1">ระยะพุ่ง X (m):</label>
                            <input type="number" id="or-x" value="0.60" step="0.05" oninput="execUniversalCalc()" class="w-full bg-slate-800 border border-slate-700 rounded-xl p-2 text-white">
                        </div>
                    </div>
                    <div>
                        <label class="block text-slate-300 font-semibold mb-1">ระยะดิ่ง Y (m):</label>
                        <input type="number" id="or-y" value="0.25" step="0.05" oninput="execUniversalCalc()" class="w-full bg-slate-800 border border-slate-700 rounded-xl p-2 text-white">
                    </div>
                `;
            }
            execUniversalCalc();
        }

        function execUniversalCalc() {
            const mode = document.getElementById('uni-calc-mode').value;
            const steps = document.getElementById('dynamic-calc-steps');
            const res = document.getElementById('dynamic-calc-result');

            if (mode === 'pump') {
                const cfg = document.getElementById('p-cfg').value;
                const vol = parseFloat(document.getElementById('p-vol').value) || 0;
                const t = parseFloat(document.getElementById('p-t').value) || 1;
                let h1 = parseFloat(document.getElementById('p-h1').value) || 0;
                const ho = parseFloat(document.getElementById('p-ho').value) || 0;

                let Hd = 0.15;
                if (cfg === 'series') { Hd = -0.07; h1 = 0; }
                if (cfg === 'parallel') { Hd = 0.94; }

                const Q_m3s = (vol / 1000) / t;
                const H = ho - h1 + Hd;
                const P = 9810 * Q_m3s * H;

                steps.innerHTML = `
                    <div>• แปลง Q: (${vol} L ÷ 1000) ÷ ${t.toFixed(2)} s = <span class="text-emerald-400 font-bold">${Q_m3s.toExponential(4)} m³/s</span></div>
                    <div>• ค่าแก้ระดับ Hd = <span class="text-sky-400 font-bold">${Hd > 0 ? '+' : ''}${Hd.toFixed(2)} m</span></div>
                    <div>• Total Head H = ${ho} - ${h1} + (${Hd}) = <span class="text-purple-400 font-bold">${H.toFixed(2)} m</span></div>
                    <div>• Power Wi = 9,810 × Q × H</div>
                `;
                res.innerText = `${P.toFixed(2)} Watts`;
            } else if (mode === 'jet') {
                const type = document.getElementById('j-type').value;
                const q_ls = parseFloat(document.getElementById('j-q').value) || 0;
                const v = parseFloat(document.getElementById('j-v').value) || 0;
                const q_m3s = q_ls / 1000;
                const factor = type === 'cup' ? 2 : 1;
                const F = factor * 1000 * q_m3s * v;

                steps.innerHTML = `
                    <div>• แปลง Q: ${q_ls} L/s = ${q_m3s} m³/s</div>
                    <div>• ตัวคูณโมเมนตัม (${type === 'cup' ? 'ถ้วยโค้ง 180° = 2 เท่า' : 'แบนราบ = 1 เท่า'}): factor = ${factor}</div>
                    <div>• F = ${factor} × 1,000 × ${q_m3s} × ${v}</div>
                `;
                res.innerText = `${F.toFixed(2)} N (น้ำหนัก m = ${(F/9.81).toFixed(3)} kg)`;
            } else if (mode === 'weir_tri') {
                const h_cm = parseFloat(document.getElementById('w-h').value) || 0;
                const cd = parseFloat(document.getElementById('w-cd').value) || 0.6;
                const h_m = h_cm / 100;
                const Q_the = 2.36 * Math.pow(h_m, 2.5);
                const Q_act = cd * Q_the;

                steps.innerHTML = `
                    <div>• แปลง H: ${h_cm} cm = ${h_m} m</div>
                    <div>• Q_the = 2.36 × (${h_m})^2.5 = ${Q_the.toFixed(5)} m³/s</div>
                    <div>• Q_act = ${cd} × Q_the = ${Q_act.toFixed(5)} m³/s (${(Q_act*1000).toFixed(3)} L/s)</div>
                `;
                res.innerText = `${(Q_act*1000).toFixed(3)} L/s (${Q_act.toFixed(5)} m³/s)`;
            } else if (mode === 'weir_rec') {
                const b = parseFloat(document.getElementById('wr-b').value) || 0.3;
                const h_cm = parseFloat(document.getElementById('wr-h').value) || 0;
                const cd = parseFloat(document.getElementById('wr-cd').value) || 0.62;
                const h_m = h_cm / 100;
                const Q_the = (2/3) * b * Math.sqrt(2 * 9.81) * Math.pow(h_m, 1.5);
                const Q_act = cd * Q_the;

                steps.innerHTML = `
                    <div>• แปลง H: ${h_cm} cm = ${h_m} m</div>
                    <div>• Q_the = (2/3) × ${b} × √19.62 × (${h_m})^1.5 = ${Q_the.toFixed(5)} m³/s</div>
                    <div>• Q_act = ${cd} × Q_the</div>
                `;
                res.innerText = `${(Q_act*1000).toFixed(3)} L/s (${Q_act.toFixed(5)} m³/s)`;
            } else if (mode === 'orifice') {
                const h = parseFloat(document.getElementById('or-h').value) || 0.4;
                const x = parseFloat(document.getElementById('or-x').value) || 0.6;
                const y = parseFloat(document.getElementById('or-y').value) || 0.25;
                const V_the = Math.sqrt(2 * 9.81 * h);
                const Cv = x / (2 * Math.sqrt(y * h));

                steps.innerHTML = `
                    <div>• V_theory = √(2 × 9.81 × ${h}) = ${V_the.toFixed(2)} m/s</div>
                    <div>• Cv = x ÷ (2 × √(y × H)) = ${x} ÷ (2 × √(${y} × ${h}))</div>
                `;
                res.innerText = `Cv = ${Cv.toFixed(3)} (V_actual = ${(Cv * V_the).toFixed(2)} m/s)`;
            }
        }

        window.addEventListener('DOMContentLoaded', () => {
            renderMasterQuiz();
            updateCalcFields();
        });
    </script>
</body>
</html>
''')

final_master_html = "".join(html_parts)

out_index = "/Users/thanaporn/.gemini/antigravity/scratch/CE272/index.html"
with open(out_index, "w", encoding="utf-8") as f:
    f.write(final_master_html)

artifact_out = "/Users/thanaporn/.gemini/antigravity/brain/0086b3cd-d8df-4e9e-86fd-d675957ab350/CE272_all_chapters.html"
with open(artifact_out, "w", encoding="utf-8") as f:
    f.write(final_master_html)

print("Generated all-chapters CE272 portal successfully!")
